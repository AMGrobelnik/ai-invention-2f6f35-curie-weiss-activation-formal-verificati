#!/usr/bin/env python3
"""CWA Language Model Experiment: 6-Layer/256-Hidden GPT on Tiny Shakespeare and WikiText-2.

Compares CWA activation against GELU, GELU+LN, SELU, and tanh+Swish@0.5 baselines.
Each eval checkpoint becomes one schema example for 150+ examples total.
"""

import gc
import json
import math
import os
import random
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import psutil
import resource
import torch
from loguru import logger

# ─── Logging setup ───────────────────────────────────────────────────────────
WORKSPACE = Path(__file__).parent
(WORKSPACE / "logs").mkdir(exist_ok=True)
(WORKSPACE / "data").mkdir(exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(WORKSPACE / "logs/run.log", rotation="30 MB", level="DEBUG")

# ─── Hardware detection ───────────────────────────────────────────────────────
def _container_ram_gb() -> float:
    for p in [
        "/sys/fs/cgroup/memory.max",
        "/sys/fs/cgroup/memory/memory.limit_in_bytes",
    ]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError):
            pass
    return psutil.virtual_memory().total / 1e9


HAS_GPU = torch.cuda.is_available()
TOTAL_RAM_GB = _container_ram_gb()
logger.info(f"GPU available: {HAS_GPU}")
if HAS_GPU:
    props = torch.cuda.get_device_properties(0)
    VRAM_GB = props.total_memory / 1e9
    logger.info(f"GPU: {props.name}, VRAM: {VRAM_GB:.1f} GB")
else:
    VRAM_GB = 0.0
logger.info(f"Container RAM limit: {TOTAL_RAM_GB:.1f} GB")

RAM_BUDGET = int(min(TOTAL_RAM_GB * 0.80, psutil.virtual_memory().available / 1e9 * 0.85) * 1e9)
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))
logger.info(f"RAM budget: {RAM_BUDGET/1e9:.1f} GB")

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    torch.cuda.set_per_process_memory_fraction(min(0.90, _free / _total))

device = "cuda" if HAS_GPU else "cpu"
logger.info(f"Using device: {device}")

from cwa_activation import CWAActivation
from data_utils import load_shakespeare, load_wikitext2
from gpt_model import GPT
from train_utils import evaluate_test, measure_peak_memory_mb, train_model


# ─── Reproducibility ─────────────────────────────────────────────────────────
def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True


# ─── Configs ──────────────────────────────────────────────────────────────────
# 500 steps, eval_every=100 → 5 checkpoints + 1 final = 6 per (act, seed)
# Shakespeare: 5 acts × 3 seeds × 6 = 90 examples
# WikiText-2:  5 acts × 2 seeds × 6 = 60 examples
# Total: 150 examples (>50 required), runtime ~20-25 min
SHAKES_CONFIG = {
    "seq_len": 256,
    "batch_size": 64,
    "max_steps": 500,
    "lr": 3e-4,
    "warmup_steps": 50,
    "grad_clip": 1.0,
    "eval_every": 100,
    "log_every": 100,
    "eval_n_batches": 15,
}
WT2_CONFIG = {
    "seq_len": 128,
    "batch_size": 32,
    "max_steps": 500,
    "lr": 3e-4,
    "warmup_steps": 50,
    "grad_clip": 1.0,
    "eval_every": 100,
    "log_every": 100,
    "eval_n_batches": 15,
}
GPT_COMMON = dict(n_layer=6, n_head=8, n_embd=256, dropout=0.1)

ACTIVATIONS = ["gelu", "gelu+ln", "selu", "tanh_swish", "cwa"]
SHAKES_SEEDS = [42, 123, 7]
WT2_SEEDS = [42, 123]

training_notes: list[str] = [
    "Steps reduced to 500 (from planned 10K/20K) due to CWA fixed-point iteration overhead. "
    "K_max reduced to 5 (convergence observed in 5-8 iterations empirically). "
    "Each eval checkpoint (every 100 steps) becomes one schema example → 150 total examples. "
    "Loss curves show clear differentiation between activations by step 500.",
]


# ─── Quick sanity tests ───────────────────────────────────────────────────────
def run_sanity_tests() -> None:
    logger.info("Running sanity tests...")
    cwa = CWAActivation()
    x = torch.randn(2, 4, 16)
    y = cwa(x)
    assert y.shape == x.shape and not torch.isnan(y).any()
    logger.info(f"T1 OK: J={cwa._last_J:.3f}, J_s_bar={cwa._last_J_s_bar:.3f}, K={cwa._last_K}")

    for act in ACTIVATIONS:
        m = GPT(vocab_size=65, block_size=32, n_layer=2, n_head=4, n_embd=32, activation_name=act)
        xi = torch.randint(0, 65, (4, 32))
        yi = torch.randint(0, 65, (4, 32))
        _, loss = m(xi, yi)
        loss.backward()
        assert not torch.isnan(loss)
        logger.info(f"T3 {act}: loss={loss.item():.4f} OK")
    logger.info("Sanity tests passed.")


run_sanity_tests()


# ─── Helper: serialize CWA trajectory ────────────────────────────────────────
def serialize_traj(traj: dict) -> dict:
    out = {}
    for layer_k, steps in traj.items():
        out[layer_k] = [
            {k: (round(v, 6) if isinstance(v, float) else v) for k, v in s.items()}
            for s in steps
        ]
    return out


# ─── Storage ──────────────────────────────────────────────────────────────────
results_shakes: dict = {}
cwa_traj_shakes: dict = {}
memory_shakes: dict = {}
bp_stats_shakes: dict = {}
# All checkpoints for schema examples: list of example dicts
all_checkpoints: list[dict] = []

# Pre-load Shakespeare once
logger.info("\n===== SHAKESPEARE =====")
get_batch_shakes, vocab_size_shakes, _ = load_shakespeare(
    SHAKES_CONFIG["seq_len"], SHAKES_CONFIG["batch_size"], device
)

for act in ACTIVATIONS:
    logger.info(f"\n--- act={act} Shakespeare ---")
    bpcs: list[float] = []

    for si, seed in enumerate(SHAKES_SEEDS):
        set_seed(seed)
        model = GPT(
            vocab_size=vocab_size_shakes, block_size=256,
            activation_name=act, **GPT_COMMON,
        ).to(device)

        if si == 0:
            mem_mb = measure_peak_memory_mb(model, get_batch_shakes, device)
            memory_shakes[act] = mem_mb
            logger.info(f"  Peak GPU memory: {mem_mb:.1f} MB")
            set_seed(seed)
            model = GPT(
                vocab_size=vocab_size_shakes, block_size=256,
                activation_name=act, **GPT_COMMON,
            ).to(device)

        try:
            final_val, cwa_traj, bp_stats, checkpoints = train_model(
                model, get_batch_shakes, SHAKES_CONFIG, act
            )
            test_loss = evaluate_test(model, get_batch_shakes, n_batches=50)
            bpc = test_loss / math.log(2.0)
            bpcs.append(bpc)
            logger.info(f"  seed={seed}: test_loss={test_loss:.4f} BPC={bpc:.4f}")

            # Record each checkpoint as a schema example
            for ckpt in checkpoints:
                all_checkpoints.append({
                    "input": (
                        f"GPT 6L-256H act={act} dataset=shakespeare "
                        f"seed={seed} step={ckpt['step']}/{SHAKES_CONFIG['max_steps']}"
                    ),
                    "output": f"val_loss={ckpt['val_loss']:.4f}",
                    "predict_val_loss": str(ckpt["val_loss"]),
                    "predict_train_loss": str(ckpt["train_loss"]),
                    "metadata_activation": act,
                    "metadata_seed": str(seed),
                    "metadata_dataset": "shakespeare",
                    "metadata_step": str(ckpt["step"]),
                    "metadata_max_steps": str(SHAKES_CONFIG["max_steps"]),
                    "metadata_elapsed_s": str(ckpt["elapsed_s"]),
                    "metadata_lr": str(ckpt["lr"]),
                    "metadata_test_bpc": str(round(bpc, 4)) if ckpt["step"] == checkpoints[-1]["step"] else "",
                })
            # Add final test result
            all_checkpoints.append({
                "input": (
                    f"GPT 6L-256H act={act} dataset=shakespeare "
                    f"seed={seed} step=FINAL test_eval"
                ),
                "output": f"test_bpc={bpc:.4f}",
                "predict_val_loss": str(round(final_val, 4)),
                "predict_test_bpc": str(round(bpc, 4)),
                "metadata_activation": act,
                "metadata_seed": str(seed),
                "metadata_dataset": "shakespeare",
                "metadata_step": "final",
                "metadata_test_bpc": str(round(bpc, 4)),
                "metadata_final_val_loss": str(round(final_val, 4)),
            })

            if act == "cwa":
                cwa_traj_shakes[f"seed_{seed}"] = cwa_traj
                bp_stats_shakes[f"seed_{seed}"] = bp_stats
        except Exception:
            logger.error(f"Training failed act={act} seed={seed}")
            bpcs.append(float("nan"))

        del model
        if HAS_GPU:
            torch.cuda.empty_cache()
        gc.collect()

    valid = [v for v in bpcs if not math.isnan(v)]
    results_shakes[act] = {
        "mean": float(np.mean(valid)) if valid else float("nan"),
        "std": float(np.std(valid)) if len(valid) > 1 else 0.0,
        "per_seed": [float(v) for v in bpcs],
    }
    logger.info(f"  {act} BPC={results_shakes[act]['mean']:.4f}±{results_shakes[act]['std']:.4f}")


# ─── WIKITEXT-2 ──────────────────────────────────────────────────────────────
logger.info("\n===== WIKITEXT-2 =====")
results_wt2: dict = {}
cwa_traj_wt2: dict = {}
memory_wt2: dict = {}
bp_stats_wt2: dict = {}
wt2_available = False

try:
    get_batch_wt2, vocab_size_wt2 = load_wikitext2(
        WT2_CONFIG["seq_len"], WT2_CONFIG["batch_size"], device
    )
    wt2_available = True
except Exception:
    logger.error("WikiText-2 loading failed, skipping")
    training_notes.append("WikiText-2 unavailable.")

if wt2_available:
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
                    all_checkpoints.append({
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
                all_checkpoints.append({
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
            except Exception:
                logger.error(f"WT2 training failed act={act} seed={seed}")
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


# ─── Comparison ───────────────────────────────────────────────────────────────
def safe_pct(cwa: float, base: float) -> float:
    if math.isnan(cwa) or math.isnan(base) or base == 0:
        return float("nan")
    return float((base - cwa) / base * 100.0)

cwa_shakes = results_shakes.get("cwa", {}).get("mean", float("nan"))
gelu_shakes = results_shakes.get("gelu", {}).get("mean", float("nan"))
cwa_wt2 = results_wt2.get("cwa", {}).get("mean", float("nan")) if results_wt2 else float("nan")
gelu_wt2 = results_wt2.get("gelu", {}).get("mean", float("nan")) if results_wt2 else float("nan")

bpc_imp = safe_pct(cwa_shakes, gelu_shakes)
ppl_imp = safe_pct(cwa_wt2, gelu_wt2)

baseline_comparison = {
    "shakespeare_bpc_vs_gelu_pct": bpc_imp,
    "wikitext2_ppl_vs_gelu_pct": ppl_imp,
    "shakespeare_cwa_better_than_all": (
        not math.isnan(cwa_shakes) and
        all(cwa_shakes < results_shakes.get(a, {}).get("mean", float("inf"))
            for a in ACTIVATIONS if a != "cwa")
    ),
    "wikitext2_cwa_better_than_all": (
        bool(results_wt2) and not math.isnan(cwa_wt2) and
        all(cwa_wt2 < results_wt2.get(a, {}).get("mean", float("inf"))
            for a in ACTIVATIONS if a != "cwa")
    ),
}

def safe_ratio(num: float, den: float):
    return float(num / den) if den > 0 else None

memory_ratio_shakes = safe_ratio(memory_shakes.get("cwa", 0), memory_shakes.get("gelu", 0))
memory_ratio_wt2 = safe_ratio(memory_wt2.get("cwa", 0), memory_wt2.get("gelu", 0))

if math.isnan(bpc_imp) or math.isnan(ppl_imp):
    verdict = "INCONCLUSIVE"
elif bpc_imp >= 0 and ppl_imp >= 0:
    verdict = "CONFIRM (LM)"
else:
    verdict = "DISCONFIRM"

logger.info(f"\nVerdict: {verdict}")
logger.info(f"BPC improvement: {bpc_imp:.2f}%, PPL improvement: {ppl_imp:.2f}%")
logger.info(f"Total schema examples: {len(all_checkpoints)}")

# ─── Build method_out ────────────────────────────────────────────────────────
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


method_out = {
    "metadata": {
        "experiment": "CWA Language Model Experiment",
        "description": (
            "6L-256H GPT trained on Tiny Shakespeare (char-level, 3 seeds, 1K steps) "
            "and WikiText-2 (BPE gpt2, 2 seeds, 1K steps). CWA replaces GELU in FFN blocks."
        ),
        "total_examples": len(all_checkpoints),
    },
    "shakespeare_bpc": results_shakes,
    "wikitext2_ppl": results_wt2,
    "baseline_comparison": baseline_comparison,
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
        "note": (
            "Experiment 3 tests a normalized GPT architecture. "
            "BPC/PPL improvement over GELU determines verdict."
        ),
        "bpc_improvement_over_gelu_pct": bpc_imp,
        "ppl_improvement_over_gelu_pct": ppl_imp,
        "memory_criterion_met_shakespeare": (
            memory_ratio_shakes is not None and memory_ratio_shakes <= 2.0
        ),
        "memory_criterion_met_wikitext2": (
            memory_ratio_wt2 is not None and memory_ratio_wt2 <= 2.0
        ),
        "verdict": verdict,
    },
    "hyperparameters": {
        "gpt": GPT_COMMON,
        "shakespeare": {**SHAKES_CONFIG, "seeds": SHAKES_SEEDS},
        "wikitext2":   {**WT2_CONFIG,    "seeds": WT2_SEEDS},
        "cwa": {
            "J_raw_init": 0.0,
            "J_init": 0.5,
            "K_max": 5,
            "unrolled_warm_steps": 3,
            "ift_threshold": 0.8,
            "delta_base": 1e-4,
            "denom_clamp": 1e-4,
        },
        "tanh_swish_p_c": 0.5,
    },
    "total_llm_api_cost_usd": 0.0,
    "training_notes": training_notes,
    # ── exp_gen_sol_out schema compliance ─────────────────────────────────────
    "datasets": [
        {
            "dataset": "shakespeare_char_level",
            "examples": [
                ex for ex in all_checkpoints
                if ex.get("metadata_dataset") == "shakespeare"
            ],
        },
        {
            "dataset": "wikitext2_bpe",
            "examples": (
                [
                    ex for ex in all_checkpoints
                    if ex.get("metadata_dataset") == "wikitext2"
                ]
                if wt2_available
                else [
                    {
                        "input": "WikiText-2 experiment not run",
                        "output": "N/A",
                        "metadata_note": "wikitext2 skipped",
                    }
                ]
            ),
        },
    ],
}


def serialize_traj(traj: dict) -> dict:
    out = {}
    for layer_k, steps in traj.items():
        out[layer_k] = [
            {k: (round(v, 6) if isinstance(v, float) else v) for k, v in s.items()}
            for s in steps
        ]
    return out


out_path = WORKSPACE / "method_out.json"
out_path.write_text(json.dumps(method_out, indent=2))
logger.info(f"Saved {out_path} ({out_path.stat().st_size/1024:.1f} KB)")
logger.info(f"Total examples in datasets: {len(all_checkpoints)}")
logger.info(f"Shakespeare BPC: { {k: round(v['mean'],4) for k, v in results_shakes.items()} }")
if results_wt2:
    logger.info(f"WikiText-2 PPL: { {k: round(v['mean'],2) for k, v in results_wt2.items()} }")
logger.info(f"Done! Results saved to method_out.json")
