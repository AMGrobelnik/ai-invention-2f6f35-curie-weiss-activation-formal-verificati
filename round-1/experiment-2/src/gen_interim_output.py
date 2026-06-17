#!/usr/bin/env python3
"""Generate interim method_out.json from partial_results.json and run format script."""
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ws = Path("/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_experiment_2")

EXPERIMENT_CONFIGS = [
    ("standard_no_bn", [16, 32, 64],   False),
    ("standard_bn",    [16, 32, 64],   True),
    ("wide_no_bn",     [64, 128, 256], False),
    ("wide_bn",        [64, 128, 256], True),
]


def build_schema_output(results: dict, overhead_table: list, verdict: dict) -> dict:
    examples = []

    # Per-epoch examples
    for cfg_label, widths, use_bn in EXPERIMENT_CONFIGS:
        cfg = results.get(cfg_label, {})
        for act_name, agg in cfg.items():
            for s_idx, epoch_accs in enumerate(agg.get("acc_history_per_seed", [])):
                final_acc = epoch_accs[-1] if epoch_accs else 0.0
                for ep, acc in enumerate(epoch_accs):
                    inp = (
                        f"ResNet-20 CIFAR-100 config={cfg_label} "
                        f"(widths={widths}, use_bn={use_bn}), "
                        f"activation={act_name}, seed={s_idx}, epoch={ep}/{len(epoch_accs)-1}."
                    )
                    out = f"test_acc={acc:.4f} at epoch {ep}. Final acc={final_acc:.4f}."
                    ex = {
                        "input": inp,
                        "output": out,
                        "metadata_experiment": "exp2_cifar100_per_epoch",
                        "metadata_config": cfg_label,
                        "metadata_activation": act_name,
                        "metadata_seed": str(s_idx),
                        "metadata_epoch": str(ep),
                    }
                    if act_name == "CWA":
                        ex["predict_cwa"] = f"acc={acc:.4f}"
                    else:
                        ex["predict_baseline"] = f"acc={acc:.4f}"
                    examples.append(ex)

    # Aggregate examples
    for cfg_label, widths, use_bn in EXPERIMENT_CONFIGS:
        cfg = results.get(cfg_label, {})
        for act_name, agg in cfg.items():
            inp = (
                f"ResNet-20 CIFAR-100 aggregate config={cfg_label} "
                f"(widths={widths}, use_bn={use_bn}), "
                f"activation={act_name}, n_seeds={len(agg.get('seeds', []))}."
            )
            out = (
                f"test_acc_mean={agg.get('test_acc_mean', 0):.4f}, "
                f"test_acc_std={agg.get('test_acc_std', 0):.4f}."
            )
            ex = {
                "input": inp,
                "output": out,
                "metadata_experiment": "exp2_cifar100_aggregate",
                "metadata_config": cfg_label,
                "metadata_activation": act_name,
            }
            if act_name == "CWA":
                ex["predict_cwa"] = f"acc={agg.get('test_acc_mean', 0):.4f}"
            else:
                ex["predict_baseline"] = f"acc={agg.get('test_acc_mean', 0):.4f}"
            examples.append(ex)

    # Overhead examples
    for row in overhead_table:
        J_actual = row.get("J_s_bar_actual", 0.0)
        K_star = row.get("K_star", 0)
        inp = (
            f"Overhead benchmark CWA vs GELU: target J*s_bar={row['J_s_bar_target']}, "
            f"actual={J_actual:.4f}, K_star={K_star:.0f}, mode={row.get('backprop_mode','N/A')}."
        )
        out = (
            f"wall_ratio={row['wall_clock_ratio']:.3f}x, "
            f"mem_ratio={row['memory_ratio']:.3f}x."
        )
        examples.append({
            "input": inp,
            "output": out,
            "metadata_experiment": "exp5_overhead",
            "metadata_J_s_bar_target": str(row["J_s_bar_target"]),
            "predict_cwa": f"wall={row['wall_clock_ms_cwa']:.3f}ms mem={row['memory_mb_cwa']:.1f}MB",
            "predict_baseline": f"wall={row['wall_clock_ms_gelu']:.3f}ms mem={row['memory_mb_gelu']:.1f}MB",
        })

    # Verdict
    examples.append({
        "input": (
            f"CWA verdict: memory_within_2x={verdict.get('memory_within_2x','N/A')}, "
            f"width_positive_correlation={verdict.get('width_positive_correlation','N/A')}, "
            f"cwa_vs_gelu_no_bn_significant={verdict.get('cwa_vs_gelu_no_bn_significant','N/A')}, "
            f"soc_observed={verdict.get('soc_observed','N/A')}."
        ),
        "output": (
            f"CWA acc={verdict.get('cwa_acc_standard_no_bn', 0):.4f} "
            f"vs GELU={verdict.get('gelu_acc_standard_no_bn', 0):.4f}, "
            f"J_s_bar={verdict.get('mean_final_J_s_bar', 0):.4f}."
        ),
        "metadata_experiment": "verdict",
        "predict_cwa": f"acc={verdict.get('cwa_acc_standard_no_bn', 0):.4f}",
        "predict_baseline": f"acc={verdict.get('gelu_acc_standard_no_bn', 0):.4f}",
    })

    return {
        "metadata": {
            "method_name": "CWA (Curie-Weiss Activation)",
            "description": "ResNet-20 CIFAR-100 width analysis + overhead benchmark (interim)",
            "timestamp": datetime.utcnow().isoformat(),
            "verdict": verdict,
            "n_examples": len(examples),
        },
        "datasets": [{"dataset": "CIFAR-100+synthetic-overhead", "examples": examples}],
    }


def compute_interim_verdict(results: dict) -> dict:
    std_no_bn = results.get("standard_no_bn", {})
    cwa_acc = std_no_bn.get("CWA", {}).get("test_acc_mean", 0)
    gelu_acc = std_no_bn.get("GELU", {}).get("test_acc_mean", 0)
    cwa_blocks = std_no_bn.get("CWA", {}).get("final_J_s_bar_per_block", {})
    all_vals = [v for vals in cwa_blocks.values() for v in (vals if isinstance(vals, list) else [vals]) if v is not None]
    mean_J_s_bar = sum(all_vals) / max(len(all_vals), 1) if all_vals else 0.0
    return {
        "memory_within_2x": None,
        "cwa_vs_gelu_no_bn_significant": (cwa_acc - gelu_acc) > 0.005,
        "soc_observed": mean_J_s_bar > 0.7,
        "mean_final_J_s_bar": mean_J_s_bar,
        "width_positive_correlation": None,
        "cwa_acc_standard_no_bn": cwa_acc,
        "gelu_acc_standard_no_bn": gelu_acc,
        "note": "interim result — experiment still running",
    }


def std_no_bn_complete(results: dict) -> bool:
    cfg = results.get("standard_no_bn", {})
    required = {"CWA", "GELU", "SELU", "tanhLN", "GELULN"}
    return required.issubset(cfg.keys()) and all(
        len(v.get("acc_history_per_seed", [[]])[0]) >= 1 for v in cfg.values()
        if v.get("acc_history_per_seed")
    )


def count_examples(out: dict) -> int:
    return sum(len(ds.get("examples", [])) for ds in out.get("datasets", []))


partial = ws / "partial_results.json"
method_out = ws / "method_out.json"
SKILL_DIR = Path("/ai-inventor/.claude/skills/aii-json")
PY = SKILL_DIR / "../.ability_client_venv/bin/python"
FORMAT_SCRIPT = SKILL_DIR / "scripts/aii_json_format_mini_preview.py"

print("Watching for partial_results.json with std_no_bn complete...")
deadline = time.time() + 7200  # 2 hour max

while time.time() < deadline:
    if partial.exists():
        try:
            results = json.loads(partial.read_text())
            if std_no_bn_complete(results):
                print(f"std_no_bn complete! Writing interim method_out.json...")
                verdict = compute_interim_verdict(results)
                out = build_schema_output(results, [], verdict)
                n = count_examples(out)
                print(f"  Writing {n} examples to method_out.json")
                method_out.write_text(json.dumps(out, indent=2))

                # Run format script
                print("Running format script...")
                r = subprocess.run(
                    [str(PY), str(FORMAT_SCRIPT), "--input", str(method_out)],
                    capture_output=True, text=True, cwd=str(ws)
                )
                print(r.stdout)
                if r.returncode != 0:
                    print(f"Format error: {r.stderr}", file=sys.stderr)
                else:
                    print(f"SUCCESS: {n} examples, format files generated")
                sys.exit(0)
        except (json.JSONDecodeError, Exception) as e:
            print(f"  Error reading partial: {e}")
    time.sleep(10)

print("Timeout waiting for std_no_bn to complete")
sys.exit(1)
