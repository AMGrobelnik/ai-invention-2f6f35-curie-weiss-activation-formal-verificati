#!/usr/bin/env python3
"""Run only WikiText-2 portion and merge with existing Shakespeare results."""

import gc
import json
import math
import os
import random
import sys
import time
from pathlib import Path

import numpy as np
import psutil
import resource
import torch
from loguru import logger

WORKSPACE = Path(__file__).parent
(WORKSPACE / "logs").mkdir(exist_ok=True)
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(WORKSPACE / "logs/run_wt2.log", rotation="30 MB", level="DEBUG")

HAS_GPU = torch.cuda.is_available()
if HAS_GPU:
    props = torch.cuda.get_device_properties(0)
    logger.info(f"GPU: {props.name}, VRAM: {props.total_memory/1e9:.1f} GB")

device = "cuda" if HAS_GPU else "cpu"
logger.info(f"Device: {device}")

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    torch.cuda.set_per_process_memory_fraction(min(0.90, _free / _total))

from cwa_activation import CWAActivation
from data_utils import load_wikitext2
from gpt_model import GPT
from train_utils import evaluate_test, measure_peak_memory_mb, train_model

def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True

WT2_CONFIG = {
    "seq_len": 128, "batch_size": 32, "max_steps": 500,
    "lr": 3e-4, "warmup_steps": 50, "grad_clip": 1.0,
    "eval_every": 100, "log_every": 100, "eval_n_batches": 15,
}
GPT_COMMON = dict(n_layer=6, n_head=8, n_embd=256, dropout=0.1)
ACTIVATIONS = ["gelu", "gelu+ln", "selu", "tanh_swish", "cwa"]
WT2_SEEDS = [42, 123]

def serialize_traj(traj: dict) -> dict:
    out = {}
    for layer_k, steps in traj.items():
        out[layer_k] = [
            {k: (round(v, 6) if isinstance(v, float) else v) for k, v in s.items()}
            for s in steps
        ]
    return out

logger.info("Loading WikiText-2...")
get_batch_wt2, vocab_size_wt2 = load_wikitext2(
    WT2_CONFIG["seq_len"], WT2_CONFIG["batch_size"], device
)
logger.info(f"WikiText-2 loaded, vocab={vocab_size_wt2}")

results_wt2: dict = {}
cwa_traj_wt2: dict = {}
memory_wt2: dict = {}
bp_stats_wt2: dict = {}
wt2_checkpoints: list[dict] = []

for act in ACTIVATIONS:
    logger.info(f"\n--- act={act} WikiText-2 ---")
    ppls: list[float] = []

    for si, seed in enumerate(WT2_SEEDS):
        set_seed(seed)
        model = GPT(
            vocab_size=vocab_size_wt2, block_size=128,
            activation_name=act, **GPT_COMMON,
        ).to(device)

        if si == 0:
            mem_mb = measure_peak_memory_mb(model, get_batch_wt2, device)
            memory_wt2[act] = mem_mb
            logger.info(f"  Peak GPU memory: {mem_mb:.1f} MB")
            set_seed(seed)
            model = GPT(
                vocab_size=vocab_size_wt2, block_size=128,
                activation_name=act, **GPT_COMMON,
            ).to(device)

        try:
            final_val, cwa_traj, bp_stats, checkpoints = train_model(
                model, get_batch_wt2, WT2_CONFIG, act
            )
            test_loss = evaluate_test(model, get_batch_wt2, n_batches=50)
            ppl = math.exp(min(test_loss, 20.0))
            ppls.append(ppl)
            logger.info(f"  seed={seed}: test_loss={test_loss:.4f} PPL={ppl:.2f}")

            for ckpt in checkpoints:
                wt2_checkpoints.append({
                    "input": (
                        f"GPT 6L-256H act={act} dataset=wikitext2 "
                        f"seed={seed} step={ckpt['step']}/{WT2_CONFIG['max_steps']}"
                    ),
                    "output": f"val_loss={ckpt['val_loss']:.4f}",
                    "predict_val_loss": str(ckpt["val_loss"]),
                    "predict_train_loss": str(ckpt["train_loss"]),
                    "metadata_activation": act,
                    "metadata_seed": str(seed),
                    "metadata_dataset": "wikitext2",
                    "metadata_step": str(ckpt["step"]),
                    "metadata_max_steps": str(WT2_CONFIG["max_steps"]),
                    "metadata_elapsed_s": str(ckpt["elapsed_s"]),
                    "metadata_lr": str(ckpt["lr"]),
                    "metadata_test_ppl": str(round(ppl, 2)) if ckpt["step"] == checkpoints[-1]["step"] else "",
                })
            wt2_checkpoints.append({
                "input": (
                    f"GPT 6L-256H act={act} dataset=wikitext2 "
                    f"seed={seed} step=FINAL test_eval"
                ),
                "output": f"test_ppl={ppl:.2f}",
                "predict_val_loss": str(round(final_val, 4)),
                "predict_test_ppl": str(round(ppl, 2)),
                "metadata_activation": act,
                "metadata_seed": str(seed),
                "metadata_dataset": "wikitext2",
                "metadata_step": "final",
                "metadata_test_ppl": str(round(ppl, 2)),
                "metadata_final_val_loss": str(round(final_val, 4)),
            })

            if act == "cwa":
                cwa_traj_wt2[f"seed_{seed}"] = cwa_traj
                bp_stats_wt2[f"seed_{seed}"] = bp_stats
        except Exception as e:
            logger.error(f"WT2 training failed act={act} seed={seed}: {e}")
            ppls.append(float("nan"))

        del model
        if HAS_GPU:
            torch.cuda.empty_cache()
        gc.collect()

    valid = [v for v in ppls if not math.isnan(v)]
    results_wt2[act] = {
        "mean": float(np.mean(valid)) if valid else float("nan"),
        "std": float(np.std(valid)) if len(valid) > 1 else 0.0,
        "per_seed": [float(v) for v in ppls],
    }
    logger.info(f"  {act} PPL={results_wt2[act]['mean']:.2f}±{results_wt2[act]['std']:.2f}")

def _k_stats(traj: dict, seeds: list[int]) -> dict:
    out = {}
    for s in [f"seed_{sd}" for sd in seeds]:
        seed_traj = traj.get(s, {})
        if not seed_traj:
            out[s] = {}
            continue
        out[s] = {
            lk: {
                "mean_K": float(np.mean([x["K"] for x in steps])),
                "max_K": int(max(x["K"] for x in steps)),
            }
            for lk, steps in seed_traj.items() if steps
        }
    return out

def _j_conv(traj: dict, seeds: list[int]) -> dict:
    out = {}
    for s in [f"seed_{sd}" for sd in seeds]:
        seed_traj = traj.get(s, {})
        if not seed_traj:
            out[s] = {}
            continue
        out[s] = {
            lk: {
                "final_J": round(steps[-1]["J"], 6) if steps else None,
                "final_J_s_bar": round(steps[-1]["J_s_bar"], 6) if steps else None,
            }
            for lk, steps in seed_traj.items() if steps
        }
    return out

# Load existing Shakespeare results
existing = json.loads((WORKSPACE / "method_out.json").read_text())
shakes_examples = [
    ex for ex in existing["datasets"][0]["examples"]
    if ex.get("metadata_dataset") == "shakespeare"
]

logger.info(f"\nMerging: {len(shakes_examples)} shakespeare + {len(wt2_checkpoints)} wt2 examples")

def safe_pct(cwa: float, base: float) -> float:
    if math.isnan(cwa) or math.isnan(base) or base == 0:
        return float("nan")
    return float((base - cwa) / base * 100.0)

results_shakes = existing["shakespeare_bpc"]
SHAKES_SEEDS = [42, 123, 7]

cwa_shakes = results_shakes.get("cwa", {}).get("mean", float("nan"))
gelu_shakes = results_shakes.get("gelu", {}).get("mean", float("nan"))
cwa_wt2 = results_wt2.get("cwa", {}).get("mean", float("nan"))
gelu_wt2 = results_wt2.get("gelu", {}).get("mean", float("nan"))
bpc_imp = safe_pct(cwa_shakes, gelu_shakes)
ppl_imp = safe_pct(cwa_wt2, gelu_wt2)

if math.isnan(bpc_imp) or math.isnan(ppl_imp):
    verdict = "INCONCLUSIVE"
elif bpc_imp >= 0 and ppl_imp >= 0:
    verdict = "CONFIRM (LM)"
else:
    verdict = "DISCONFIRM"

logger.info(f"Verdict: {verdict}  BPC_imp={bpc_imp:.2f}%  PPL_imp={ppl_imp:.2f}%")

def safe_ratio(num: float, den: float):
    return float(num / den) if den > 0 else None

memory_shakes = existing["peak_gpu_memory_mb"]["shakespeare"]
memory_ratio_shakes = safe_ratio(memory_shakes.get("cwa", 0), memory_shakes.get("gelu", 0))
memory_ratio_wt2 = safe_ratio(memory_wt2.get("cwa", 0), memory_wt2.get("gelu", 0))

cwa_traj_shakes = {
    k: {lk: v for lk, v in sv.items()}
    for k, sv in existing["J_s_bar_trajectory_per_layer"]["shakespeare"].items()
}
bp_stats_shakes = existing["backprop_mode_statistics"]["shakespeare"]

all_examples = shakes_examples + wt2_checkpoints

method_out = {
    "metadata": {
        "experiment": "CWA Language Model Experiment",
        "description": (
            "6L-256H GPT trained on Tiny Shakespeare (char-level, 3 seeds, 500 steps) "
            "and WikiText-2 (BPE gpt2, 2 seeds, 500 steps). CWA replaces GELU in FFN blocks."
        ),
        "total_examples": len(all_examples),
    },
    "shakespeare_bpc": results_shakes,
    "wikitext2_ppl": results_wt2,
    "baseline_comparison": {
        "shakespeare_bpc_vs_gelu_pct": bpc_imp,
        "wikitext2_ppl_vs_gelu_pct": ppl_imp,
        "shakespeare_cwa_better_than_all": (
            not math.isnan(cwa_shakes) and
            all(cwa_shakes < results_shakes.get(a, {}).get("mean", float("inf"))
                for a in ACTIVATIONS if a != "cwa")
        ),
        "wikitext2_cwa_better_than_all": (
            not math.isnan(cwa_wt2) and
            all(cwa_wt2 < results_wt2.get(a, {}).get("mean", float("inf"))
                for a in ACTIVATIONS if a != "cwa")
        ),
    },
    "J_s_bar_trajectory_per_layer": {
        "shakespeare": {s: serialize_traj(t) for s, t in cwa_traj_shakes.items()},
        "wikitext2":   {s: serialize_traj(t) for s, t in cwa_traj_wt2.items()},
    },
    "K_per_layer": {
        "shakespeare": _k_stats(cwa_traj_shakes, SHAKES_SEEDS),
        "wikitext2":   _k_stats(cwa_traj_wt2, WT2_SEEDS),
    },
    "backprop_mode_statistics": {
        "shakespeare": bp_stats_shakes,
        "wikitext2":   bp_stats_wt2,
    },
    "peak_gpu_memory_mb": {
        "shakespeare": memory_shakes,
        "wikitext2":   memory_wt2,
        "ratio_cwa_over_gelu": {
            "shakespeare": memory_ratio_shakes,
            "wikitext2":   memory_ratio_wt2,
        },
    },
    "J_per_layer_at_convergence": {
        "shakespeare": _j_conv(cwa_traj_shakes, SHAKES_SEEDS),
        "wikitext2":   _j_conv(cwa_traj_wt2, WT2_SEEDS),
    },
    "success_criteria_evaluation": {
        "note": "BPC/PPL improvement over GELU determines verdict.",
        "bpc_improvement_over_gelu_pct": bpc_imp,
        "ppl_improvement_over_gelu_pct": ppl_imp,
        "memory_criterion_met_shakespeare": memory_ratio_shakes is not None and memory_ratio_shakes <= 2.0,
        "memory_criterion_met_wikitext2": memory_ratio_wt2 is not None and memory_ratio_wt2 <= 2.0,
        "verdict": verdict,
    },
    "hyperparameters": {
        "gpt": GPT_COMMON,
        "shakespeare": {"seeds": SHAKES_SEEDS},
        "wikitext2": {**WT2_CONFIG, "seeds": WT2_SEEDS},
        "cwa": {
            "J_raw_init": 0.0, "J_init": 0.5, "K_max": 5,
            "unrolled_warm_steps": 3, "ift_threshold": 0.8,
        },
    },
    "total_llm_api_cost_usd": 0.0,
    "training_notes": [
        "Steps=500 (K_max=5 for CWA speed). Each eval checkpoint=one schema example.",
        f"Shakespeare: {len(shakes_examples)} examples from 5 acts × 3 seeds × 6 checkpoints.",
        f"WikiText-2: {len(wt2_checkpoints)} examples from 5 acts × 2 seeds × 6 checkpoints.",
    ],
    "datasets": [
        {"dataset": "shakespeare_char_level", "examples": shakes_examples},
        {"dataset": "wikitext2_bpe", "examples": wt2_checkpoints},
    ],
}

out_path = WORKSPACE / "method_out.json"
out_path.write_text(json.dumps(method_out, indent=2))
logger.info(f"Saved {out_path} ({out_path.stat().st_size/1024:.1f} KB)")
logger.info(f"Total examples: {len(all_examples)}")
logger.info("WT2 run complete!")
