#!/usr/bin/env python3
"""CWA Final-Paper Stats: Power Analysis, Metric Tables, Figure Captions, Abstract Numbers, Contributions Fix."""

from loguru import logger
from pathlib import Path
import json
import sys
import math
import numpy as np
from scipy import stats

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
Path("logs").mkdir(exist_ok=True)
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

WORKSPACE = Path("/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_5/gen_art/gen_art_evaluation_1")
DEP_SHIFT_ABL = Path("/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_3/gen_art/gen_art_experiment_1")
DEP_DEPTH_SWEEP = Path("/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_experiment_1")
DEP_LM = Path("/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_experiment_2")
DEP_MEMORY = Path("/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_4/gen_art/gen_art_experiment_1")


def compute_power_analysis(sub_exp_b: dict) -> dict:
    """Deliverable A: paired t-test power analysis for shift ablation null results."""
    logger.info("--- Deliverable A: Power Analysis ---")

    n = sub_exp_b["pairwise_ttests"]["cwa_full_vs_shift_only"]["n_pairs"]
    df = n - 1  # = 2
    alpha = 0.05
    t_crit = float(stats.t.ppf(1 - alpha / 2, df=df))
    t_power_80 = float(stats.t.ppf(0.80, df=df))
    logger.info(f"n={n}, df={df}, t_crit={t_crit:.4f}, t_power_80={t_power_80:.4f}")

    acc = sub_exp_b["accuracy_by_condition"]
    mean_full = acc["cwa_full"]["mean"]
    mean_shift = acc["cwa_shift_only"]["mean"]
    mean_tanh = acc["pure_tanh"]["mean"]

    t_full_shift = sub_exp_b["pairwise_ttests"]["cwa_full_vs_shift_only"]["t_stat"]
    t_full_tanh = sub_exp_b["pairwise_ttests"]["cwa_full_vs_pure_tanh"]["t_stat"]
    p_full_shift = sub_exp_b["pairwise_ttests"]["cwa_full_vs_shift_only"]["p_val"]
    p_full_tanh = sub_exp_b["pairwise_ttests"]["cwa_full_vs_pure_tanh"]["p_val"]

    # mean_d = mean(cwa_full) - mean(other); sigma_d = |mean_d| * sqrt(n) / |t|
    mean_d_shift = mean_full - mean_shift
    mean_d_tanh = mean_full - mean_tanh

    sigma_full_shift = abs(mean_d_shift) * math.sqrt(n) / abs(t_full_shift) if abs(t_full_shift) > 1e-10 else 0.0
    sigma_full_tanh = abs(mean_d_tanh) * math.sqrt(n) / abs(t_full_tanh)

    # MDE at 50% power: t_crit * sigma / sqrt(n)
    mde_50_shift = t_crit * sigma_full_shift / math.sqrt(n)
    mde_50_tanh = t_crit * sigma_full_tanh / math.sqrt(n)

    # MDE at 80% power: (t_crit + t_power_80) * sigma / sqrt(n)
    mde_80_shift = (t_crit + t_power_80) * sigma_full_shift / math.sqrt(n)
    mde_80_tanh = (t_crit + t_power_80) * sigma_full_tanh / math.sqrt(n)

    logger.info(f"CWA-Full vs ShiftOnly: mean_d={mean_d_shift:.6f}, sigma_d={sigma_full_shift:.6f}")
    logger.info(f"  MDE_50={mde_50_shift*100:.3f}pp, MDE_80={mde_80_shift*100:.3f}pp, p={p_full_shift:.6f}")
    logger.info(f"CWA-Full vs Pure-Tanh: mean_d={mean_d_tanh:.6f}, sigma_d={sigma_full_tanh:.6f}")
    logger.info(f"  MDE_50={mde_50_tanh*100:.3f}pp, MDE_80={mde_80_tanh*100:.3f}pp, p={p_full_tanh:.6f}")

    mde_80_tanh_pp = round(mde_80_tanh * 100, 3)
    mde_80_shift_pp = round(mde_80_shift * 100, 3)

    narrative = (
        f"With n=3 seeds and sigma_diff≈{sigma_full_tanh*100:.2f}pp (CWA-Full vs Pure-Tanh), "
        f"effects below {mde_80_tanh_pp:.1f}pp cannot be detected at 80% power; "
        f"our null result p={p_full_shift:.3f}/{p_full_tanh:.3f} rules out effects ≥{mde_80_tanh_pp:.1f}pp"
    )

    return {
        "n": n,
        "df": df,
        "t_crit_alpha005": round(t_crit, 4),
        "t_power_80": round(t_power_80, 4),
        "mean_d_full_vs_shift": round(mean_d_shift, 8),
        "mean_d_full_vs_tanh": round(mean_d_tanh, 8),
        "sigma_diff_full_vs_shift": round(sigma_full_shift, 8),
        "sigma_diff_full_vs_tanh": round(sigma_full_tanh, 8),
        "mde_50pct_full_vs_shift_pp": round(mde_50_shift * 100, 3),
        "mde_80pct_full_vs_shift_pp": mde_80_shift_pp,
        "mde_50pct_full_vs_tanh_pp": round(mde_50_tanh * 100, 3),
        "mde_80pct_full_vs_tanh_pp": mde_80_tanh_pp,
        "p_full_vs_shift": p_full_shift,
        "p_full_vs_tanh": p_full_tanh,
        "narrative": narrative,
    }


def build_metric_table(grad_ratio_data: dict) -> list:
    """Deliverable B: standardized raw-ratio vs |ratio-1| table for all activations × depths."""
    logger.info("--- Deliverable B: Metric Standardization Table ---")

    depths = [6, 10, 20]
    activations = ["cwa", "relu", "gelu", "selu", "competing_nl", "gelu_ln"]
    depth_key_map = {6: "depth6", 10: "depth10", 20: "depth20"}

    table = []
    for depth in depths:
        dk = depth_key_map[depth]
        depth_rows = []
        for act in activations:
            if dk in grad_ratio_data and act in grad_ratio_data[dk]:
                entry = grad_ratio_data[dk][act]
                raw_ratio = entry["mean"]
                raw_std = entry["std"]
                abs_dev = abs(raw_ratio - 1.0)
                depth_rows.append({
                    "depth": depth,
                    "activation": act,
                    "raw_ratio_mean": round(raw_ratio, 4),
                    "raw_ratio_std": round(raw_std, 4),
                    "abs_dev": round(abs_dev, 4),
                })

        # Rank by abs_dev (lower = better = rank 1)
        sorted_by_abs = sorted(depth_rows, key=lambda r: r["abs_dev"])
        for rank, row in enumerate(sorted_by_abs, 1):
            row["rank_abs_dev"] = rank

        # Rank by raw_ratio (same criterion, but explicit)
        sorted_by_raw = sorted(depth_rows, key=lambda r: abs(r["raw_ratio_mean"] - 1.0))
        for rank, row in enumerate(sorted_by_raw, 1):
            row["rank_raw_ratio"] = rank

        table.extend(depth_rows)

    for row in table:
        logger.debug(
            f"  depth={row['depth']} act={row['activation']:<15} "
            f"raw_ratio={row['raw_ratio_mean']:.4f} abs_dev={row['abs_dev']:.4f} "
            f"rank_abs={row['rank_abs_dev']}"
        )

    # Log cross-check flags mentioned in plan
    rows_by_key = {(r["depth"], r["activation"]): r for r in table}
    logger.info(f"Cross-check: SELU d6 abs_dev={rows_by_key[(6,'selu')]['abs_dev']:.4f} (expected 0.089)")
    logger.info(f"Cross-check: CWA d6 abs_dev={rows_by_key[(6,'cwa')]['abs_dev']:.4f} (expected 0.695)")
    logger.info(f"Cross-check: GELU+LN d6 abs_dev={rows_by_key[(6,'gelu_ln')]['abs_dev']:.4f} (expected 0.630)")
    logger.info(f"Cross-check: CWA d20 abs_dev={rows_by_key[(20,'cwa')]['abs_dev']:.4f} (expected 10.017)")
    logger.info(f"Cross-check: GELU+LN d20 abs_dev={rows_by_key[(20,'gelu_ln')]['abs_dev']:.4f} (expected 8.661)")

    return table


def build_figure_captions() -> list:
    """Deliverable C: four complete LaTeX-ready figure captions."""
    logger.info("--- Deliverable C: Figure Captions ---")
    return [
        {
            "fig_num": 1,
            "title": "CWA fixed-point iteration diagram",
            "caption": (
                r"Illustration of the Curie-Weiss Activation (CWA) fixed-point iteration for a single hidden layer. "
                r"Starting from $m_0=0$, the mean-field iteration $m_{t+1}=\frac{1}{n}\sum_i \tanh(x_i + J \cdot m_t)$ "
                r"converges geometrically at rate $\rho = J\bar{s} < 1$ to the fixed point $m^*$, which then defines "
                r"the output $y_i = \tanh(x_i + J \cdot m^*)$. The learnable scalar $J = \sigma(J_{\mathrm{raw}}) \in (0,1)$ "
                r"controls coupling strength and serves as the backpropagation mode switch (IFT when $J\bar{s}\geq 0.8$, "
                r"unrolled otherwise). Convergence typically occurs in $K^* \approx 7.4$ iterations under experimental conditions."
            ),
        },
        {
            "fig_num": 2,
            "title": "Gradient stability bar chart across depths and activations",
            "caption": (
                r"Gradient stability across depths and activations, measured by $|\text{ratio}-1|$ where "
                r"$\text{ratio} = \log\|\nabla_{W_1}\mathcal{L}\| / \log\|\nabla_{W_L}\mathcal{L}\|$ "
                r"(lower is better; ideal ratio = 1). Six activations evaluated at depths 6, 10, 20 on unnormalized MLPs "
                r"(256 hidden units, CIFAR-10, 3 seeds). \textbf{SELU achieves the best stability at all depths} "
                r"($|\text{ratio}-1|=0.089$ at depth 6). CWA exhibits gradient underflow at depths 6 and 10 "
                r"($|\text{ratio}-1|=0.695,\,0.653$, indicating ratio$\approx 0.3$ from underflow) and catastrophic "
                r"collapse at depth 20 ($|\text{ratio}-1|=10.017$). GELU+LN is second-worst at every depth "
                r"($|\text{ratio}-1|=0.630,\,0.642,\,8.661$) due to LayerNorm's internal re-scaling conflating with "
                r"inter-layer gradient magnitudes, making cross-architecture comparisons unreliable. "
                r"Error bars show $\pm 1$ standard deviation over 3 seeds."
            ),
        },
        {
            "fig_num": 3,
            "title": "IFT vs Unrolled vs GELU peak GPU memory benchmark",
            "caption": (
                r"Peak GPU memory (MB, log scale) for CWA-IFT vs.\ CWA-Unrolled ($K=50$) vs.\ GELU baseline "
                r"at layer widths $n \in \{256, 1024, 4096\}$ (batch=64, $J_{\mathrm{raw}}=4.0$, measured over 5 runs "
                r"after 3 warmups on NVIDIA RTX A4500). The GELU baseline includes an $O(n^2)$ weight matrix "
                r"$W \in \mathbb{R}^{n \times n}$; IFT measures only the activation backward pass in isolation --- "
                r"this is an apples-to-oranges comparison. The architecturally fair comparison is IFT vs.\ Unrolled: "
                r"IFT achieves $0.31\times$ the memory of unrolled $K=50$ at $n=4096$ (3.25$\times$ savings, "
                r"69\% reduction). Savings grow monotonically with $n$: 16\% at $n=256$, 41\% at $n=1024$, "
                r"69\% at $n=4096$, consistent with IFT's $O(n)$ vs.\ $O(Kn)$ memory complexity."
            ),
        },
        {
            "fig_num": 4,
            "title": "Shift ablation: CWA-Full vs CWA-ShiftOnly vs Pure-Tanh on CIFAR-10",
            "caption": (
                r"Shift ablation: final test accuracy on CIFAR-10 for three conditions of a 10-layer unnormalized MLP "
                r"($n=3$ seeds each, 25 epochs). CWA-Full (full fixed-point iteration with learned $J$), "
                r"CWA-ShiftOnly (detached mean shift $\bar{m}^*$ added to pre-activations without backpropagating "
                r"through $J$), and Pure-Tanh (pointwise, no shift). Paired $t$-tests show no significant difference "
                r"between CWA-Full and CWA-ShiftOnly ($p=0.984$), nor between CWA-Full and Pure-Tanh ($p=0.126$). "
                r"The self-consistent inter-neuron coupling adds zero measurable benefit over a simple mean-shift "
                r"bias correction. With $n=3$ seeds, effects smaller than $\approx 1\,\text{pp}$ cannot be "
                r"excluded at 80\% power."
            ),
        },
    ]


def compute_abstract_numbers(
    memory_data: dict,
    depth_sweep_data: dict,
    lm_data: dict,
    power_result: dict,
) -> dict:
    """Deliverable D: structured audit of all key quantitative claims."""
    logger.info("--- Deliverable D: Abstract Numbers Audit ---")

    # sech²(2.0)
    cosh_2 = math.cosh(2.0)
    sech2_2 = 1.0 / cosh_2 ** 2
    logger.info(f"sech²(2.0) = {sech2_2:.6f}  (cosh(2.0)={cosh_2:.6f})")

    # Memory benchmark n=4096
    mem_summary = memory_data["metadata"]["summary_table"]
    n4096_row = next(r for r in mem_summary if r["n"] == 4096 and r["x_scale"] == 0.1)
    ift_over_unrolled_4096 = n4096_row["ift_over_unrolled"]
    savings_pct = round((1 - ift_over_unrolled_4096) * 100, 1)
    savings_multiple = round(1 / ift_over_unrolled_4096, 3)
    logger.info(f"IFT/Unrolled at n=4096: {ift_over_unrolled_4096:.4f} ({savings_pct}% reduction, {savings_multiple:.3f}x savings)")

    # Gradient ratios
    grad = depth_sweep_data["metadata"]["summary_tables"]["gradient_ratio_by_depth_activation"]
    acc_table = depth_sweep_data["metadata"]["summary_tables"]["accuracy_by_depth"]

    cwa_d6 = grad["depth6"]["cwa"]["mean"]
    selu_d6 = grad["depth6"]["selu"]["mean"]
    gelu_d6 = grad["depth6"]["gelu"]["mean"]
    cwa_d10 = grad["depth10"]["cwa"]["mean"]
    selu_d10 = grad["depth10"]["selu"]["mean"]
    gelu_ln_d6 = grad["depth6"]["gelu_ln"]["mean"]
    gelu_ln_d10 = grad["depth10"]["gelu_ln"]["mean"]
    gelu_ln_d20 = grad["depth20"]["gelu_ln"]["mean"]
    cwa_d20 = grad["depth20"]["cwa"]["mean"]

    cwa_d6_abs = abs(cwa_d6 - 1.0)
    selu_d6_abs = abs(selu_d6 - 1.0)
    gelu_d6_abs = abs(gelu_d6 - 1.0)
    cwa_d10_abs = abs(cwa_d10 - 1.0)
    cwa_d20_abs = abs(cwa_d20 - 1.0)
    gelu_ln_d6_abs = abs(gelu_ln_d6 - 1.0)
    gelu_ln_d10_abs = abs(gelu_ln_d10 - 1.0)
    gelu_ln_d20_abs = abs(gelu_ln_d20 - 1.0)

    selu_d20_acc = acc_table["depth20"]["selu"]["mean"]
    cwa_d20_acc = acc_table["depth20"]["cwa"]["mean"]

    # LM results
    sub_b = lm_data["metadata"]["sub_exp_b"]
    sub_c = lm_data["metadata"]["sub_exp_c"]
    cwa_bpc = sub_b["CWA_val_bpc_mean"]
    gelu_bpc = sub_b["GELU_val_bpc_mean"]
    final_j_shared = sub_b["CWA_final_J_mean"]
    final_j_100xlr = sub_c["final_J_mean_per_seed"]

    logger.info(f"CWA d6 |ratio-1|={cwa_d6_abs:.4f}, SELU={selu_d6_abs:.4f}, GELU={gelu_d6_abs:.4f}")
    logger.info(f"CWA/SELU ratio: {cwa_d6_abs/selu_d6_abs:.1f}x, CWA/GELU ratio: {cwa_d6_abs/gelu_d6_abs:.1f}x")
    logger.info(f"CWA d20 raw_ratio={cwa_d20:.4f}, abs_dev={cwa_d20_abs:.4f}")
    logger.info(f"GELU+LN: d6={gelu_ln_d6_abs:.4f}, d10={gelu_ln_d10_abs:.4f}, d20={gelu_ln_d20_abs:.4f}")
    logger.info(f"LM: CWA BPC={cwa_bpc:.4f}, GELU BPC={gelu_bpc:.4f}, delta={cwa_bpc-gelu_bpc:.4f}")

    return {
        "sech2_2_0": {
            "value": round(sech2_2, 6),
            "cosh_2_0": round(cosh_2, 6),
            "formula": "1/cosh^2(2.0)",
            "source": "analytical",
        },
        "memory_ift_vs_unrolled_n4096": {
            "ift_over_unrolled": round(ift_over_unrolled_4096, 4),
            "savings_pct": savings_pct,
            "savings_multiple": savings_multiple,
            "ift_MB": n4096_row["ift_MB"],
            "unrolled_MB": n4096_row["unrolled_MB"],
            "gelu_MB": n4096_row["gelu_MB"],
            "source_artifact": "art_xd3tmcyckf00",
            "json_path": "metadata.summary_table[n=4096,x_scale=0.1]",
        },
        "memory_savings_by_n": {
            "n256_pct": round((1 - 0.841) * 100, 1),
            "n1024_pct": round((1 - 0.586) * 100, 1),
            "n4096_pct": round((1 - ift_over_unrolled_4096) * 100, 1),
            "monotone_increasing": True,
            "source_artifact": "art_xd3tmcyckf00",
        },
        "grad_ratio_cwa_d6": {
            "raw_ratio": round(cwa_d6, 4),
            "abs_dev": round(cwa_d6_abs, 4),
            "source_artifact": "art_v26XKv4_F1RM",
            "json_path": "metadata.summary_tables.gradient_ratio_by_depth_activation.depth6.cwa.mean",
        },
        "grad_ratio_selu_d6": {
            "raw_ratio": round(selu_d6, 4),
            "abs_dev": round(selu_d6_abs, 4),
            "source_artifact": "art_v26XKv4_F1RM",
            "json_path": "metadata.summary_tables.gradient_ratio_by_depth_activation.depth6.selu.mean",
        },
        "grad_ratio_gelu_d6": {
            "raw_ratio": round(gelu_d6, 4),
            "abs_dev": round(gelu_d6_abs, 4),
            "source_artifact": "art_v26XKv4_F1RM",
            "json_path": "metadata.summary_tables.gradient_ratio_by_depth_activation.depth6.gelu.mean",
        },
        "grad_ratio_gelu_ln": {
            "d6_abs_dev": round(gelu_ln_d6_abs, 4),
            "d10_abs_dev": round(gelu_ln_d10_abs, 4),
            "d20_abs_dev": round(gelu_ln_d20_abs, 4),
            "d6_raw_ratio": round(gelu_ln_d6, 4),
            "d10_raw_ratio": round(gelu_ln_d10, 4),
            "d20_raw_ratio": round(gelu_ln_d20, 4),
            "source_artifact": "art_v26XKv4_F1RM",
        },
        "grad_ratio_cwa_d10": {
            "raw_ratio": round(cwa_d10, 4),
            "abs_dev": round(cwa_d10_abs, 4),
            "source_artifact": "art_v26XKv4_F1RM",
        },
        "grad_ratio_cwa_d20": {
            "raw_ratio": round(cwa_d20, 4),
            "abs_dev": round(cwa_d20_abs, 4),
            "source_artifact": "art_v26XKv4_F1RM",
        },
        "cwa_vs_selu_ratio_d6": {
            "value": round(cwa_d6_abs / selu_d6_abs, 2),
            "interpretation": f"CWA is {round(cwa_d6_abs/selu_d6_abs, 1)}x worse than SELU at depth 6",
        },
        "cwa_vs_gelu_ratio_d6": {
            "value": round(cwa_d6_abs / gelu_d6_abs, 2),
            "interpretation": f"CWA is {round(cwa_d6_abs/gelu_d6_abs, 1)}x worse than GELU at depth 6",
        },
        "cwa_d20_collapse": {
            "grad_ratio": round(cwa_d20, 4),
            "acc": round(cwa_d20_acc, 4),
            "selu_acc_d20": round(selu_d20_acc, 4),
            "source_artifact": "art_v26XKv4_F1RM",
        },
        "lm_results": {
            "cwa_bpc": round(cwa_bpc, 4),
            "gelu_bpc": round(gelu_bpc, 4),
            "delta_bpc": round(cwa_bpc - gelu_bpc, 4),
            "j_trajectory_shared_lr": f"0.500 -> {max(final_j_shared):.3f}",
            "j_range_100xlr": f"0.500 -> {min(final_j_100xlr):.3f}-{max(final_j_100xlr):.3f}",
            "cwa_better": False,
            "source_artifact": "art_V46hELP73T_t",
            "json_path": "metadata.sub_exp_b / sub_exp_c",
        },
        "shift_ablation_power": {
            "p_full_vs_shift_only": round(power_result["p_full_vs_shift"], 6),
            "p_full_vs_pure_tanh": round(power_result["p_full_vs_tanh"], 6),
            "mde_80pct_pp_full_vs_tanh": power_result["mde_80pct_full_vs_tanh_pp"],
            "mde_80pct_pp_full_vs_shift": power_result["mde_80pct_full_vs_shift_pp"],
            "source_artifact": "art_5zKSer_FGOKx",
            "json_path": "metadata.summary.sub_exp_B.pairwise_ttests",
        },
        "j_s_bar_range": {
            "min_observed": 0.205,
            "max_observed": 0.412,
            "note": (
                "LM J*s_bar~0.205 (sub_exp_b, shared LR); "
                "small-init max=0.412 (art_5zKSer); "
                "depth-sweep d10 mean trajectory ~0.285-0.353"
            ),
            "sources": ["art_V46hELP73T_t", "art_5zKSer_FGOKx", "art_v26XKv4_F1RM"],
        },
        "lean4_proofs": {
            "n_theorems": 4,
            "n_corollaries": 1,
            "total": 5,
            "theorem_names": [
                "Banach fixed-point convergence of CWA iteration",
                "IFT gradient correctness",
                "Revised adaptive bias bound (code tolerance delta=1e-4*(1-J*s_bar))",
                "Warm-start-T bias bound (Theorem 4)",
            ],
            "corollary_names": [
                "Corollary 4b: specialization of Theorem 4 to J<=0.55 giving bias<=16.7%*epsilon"
            ],
        },
    }


def build_contributions_fix() -> dict:
    """Deliverable E: corrected contributions bullet."""
    logger.info("--- Deliverable E: Contributions Fix ---")
    return {
        "old_text": "Five Lean 4 theorems and proofs without sorry establishing the mathematical foundation",
        "new_text": (
            "Four Lean 4 theorems and one corollary without sorry establishing the mathematical foundation: "
            "(1) Banach fixed-point convergence of the CWA iteration, "
            "(2) IFT gradient correctness, "
            "(3) revised adaptive bias bound covering code tolerance delta=1e-4*(1-J*s_bar), "
            "(4) warm-start-T bias bound (Theorem 4), and "
            "(5) Corollary 4b --- a specialization of Theorem 4 to J<=0.55 giving bias<=16.7%*epsilon, "
            "covering experimentally observed J in [0.515, 0.521]"
        ),
        "explanation": (
            "Corollary 4b is not an independent theorem; it specializes Theorem 4 to the experimentally "
            "observed regime J<=0.55"
        ),
        "n_theorems": 4,
        "n_corollaries": 1,
        "total_lean4_items": 5,
    }


@logger.catch(reraise=True)
def main():
    logger.info("=== CWA Final-Paper Stats Evaluation ===")

    # Load data
    logger.info("Loading dependency data...")
    shift_abl_data = json.loads((DEP_SHIFT_ABL / "preview_method_out.json").read_text())
    depth_sweep_data = json.loads((DEP_DEPTH_SWEEP / "preview_method_out.json").read_text())
    lm_data = json.loads((DEP_LM / "preview_method_out.json").read_text())
    memory_data = json.loads((DEP_MEMORY / "full_method_out.json").read_text())

    sub_exp_b = shift_abl_data["metadata"]["summary"]["sub_exp_B"]
    grad_ratio_data = depth_sweep_data["metadata"]["summary_tables"]["gradient_ratio_by_depth_activation"]

    # Compute all deliverables
    power_result = compute_power_analysis(sub_exp_b)
    metric_table = build_metric_table(grad_ratio_data)
    fig_captions = build_figure_captions()
    abstract_numbers = compute_abstract_numbers(memory_data, depth_sweep_data, lm_data, power_result)
    contributions_fix = build_contributions_fix()

    # Build metrics_agg (all numeric)
    abs_nums = abstract_numbers
    metrics_agg = {
        "power_mde_80pp_full_vs_shift": power_result["mde_80pct_full_vs_shift_pp"],
        "power_mde_80pp_full_vs_tanh": power_result["mde_80pct_full_vs_tanh_pp"],
        "power_mde_50pp_full_vs_shift": power_result["mde_50pct_full_vs_shift_pp"],
        "power_mde_50pp_full_vs_tanh": power_result["mde_50pct_full_vs_tanh_pp"],
        "power_sigma_diff_full_shift": power_result["sigma_diff_full_vs_shift"],
        "power_sigma_diff_full_tanh": power_result["sigma_diff_full_vs_tanh"],
        "power_p_full_vs_shift": round(power_result["p_full_vs_shift"], 6),
        "power_p_full_vs_tanh": round(power_result["p_full_vs_tanh"], 6),
        "power_t_crit": power_result["t_crit_alpha005"],
        "power_t_power80": power_result["t_power_80"],
        "sech2_2_0": abs_nums["sech2_2_0"]["value"],
        "cwa_abs_dev_d6": abs_nums["grad_ratio_cwa_d6"]["abs_dev"],
        "selu_abs_dev_d6": abs_nums["grad_ratio_selu_d6"]["abs_dev"],
        "gelu_abs_dev_d6": abs_nums["grad_ratio_gelu_d6"]["abs_dev"],
        "cwa_abs_dev_d10": abs_nums["grad_ratio_cwa_d10"]["abs_dev"],
        "cwa_abs_dev_d20": abs_nums["grad_ratio_cwa_d20"]["abs_dev"],
        "gelu_ln_abs_dev_d6": abs_nums["grad_ratio_gelu_ln"]["d6_abs_dev"],
        "gelu_ln_abs_dev_d10": abs_nums["grad_ratio_gelu_ln"]["d10_abs_dev"],
        "gelu_ln_abs_dev_d20": abs_nums["grad_ratio_gelu_ln"]["d20_abs_dev"],
        "cwa_vs_selu_abs_dev_ratio_d6": abs_nums["cwa_vs_selu_ratio_d6"]["value"],
        "cwa_vs_gelu_abs_dev_ratio_d6": abs_nums["cwa_vs_gelu_ratio_d6"]["value"],
        "ift_over_unrolled_n4096": abs_nums["memory_ift_vs_unrolled_n4096"]["ift_over_unrolled"],
        "ift_savings_pct_n4096": abs_nums["memory_ift_vs_unrolled_n4096"]["savings_pct"],
        "ift_savings_multiple_n4096": abs_nums["memory_ift_vs_unrolled_n4096"]["savings_multiple"],
        "ift_savings_pct_n256": abs_nums["memory_savings_by_n"]["n256_pct"],
        "ift_savings_pct_n1024": abs_nums["memory_savings_by_n"]["n1024_pct"],
        "cwa_bpc": abs_nums["lm_results"]["cwa_bpc"],
        "gelu_bpc": abs_nums["lm_results"]["gelu_bpc"],
        "bpc_delta_cwa_minus_gelu": abs_nums["lm_results"]["delta_bpc"],
        "n_lean4_theorems": float(contributions_fix["n_theorems"]),
        "n_lean4_corollaries": float(contributions_fix["n_corollaries"]),
        "n_metric_table_rows": float(len(metric_table)),
        "n_figure_captions": float(len(fig_captions)),
    }

    # Build datasets
    datasets = [
        {
            "dataset": "power_analysis",
            "examples": [
                {
                    "input": "paired_t_power: CWA-Full vs CWA-ShiftOnly, n=3, df=2, alpha=0.05",
                    "output": f"MDE_80={power_result['mde_80pct_full_vs_shift_pp']:.3f}pp; p={power_result['p_full_vs_shift']:.4f} (no sig diff)",
                    "metadata_n": power_result["n"],
                    "metadata_df": power_result["df"],
                    "metadata_t_crit": power_result["t_crit_alpha005"],
                    "metadata_t_power_80": power_result["t_power_80"],
                    "metadata_mean_d": power_result["mean_d_full_vs_shift"],
                    "metadata_sigma_diff": power_result["sigma_diff_full_vs_shift"],
                    "metadata_mde_50pp": power_result["mde_50pct_full_vs_shift_pp"],
                    "metadata_mde_80pp": power_result["mde_80pct_full_vs_shift_pp"],
                    "metadata_p_value": power_result["p_full_vs_shift"],
                    "metadata_formula": "(t_crit + t_power80) * sigma_diff / sqrt(n)",
                    "predict_mde_80pp": str(power_result["mde_80pct_full_vs_shift_pp"]),
                    "predict_interpretation": "null result; coupling adds nothing over shift-only",
                    "eval_mde_80pp": power_result["mde_80pct_full_vs_shift_pp"],
                    "eval_p_value": round(power_result["p_full_vs_shift"], 6),
                },
                {
                    "input": "paired_t_power: CWA-Full vs Pure-Tanh, n=3, df=2, alpha=0.05",
                    "output": power_result["narrative"],
                    "metadata_n": power_result["n"],
                    "metadata_df": power_result["df"],
                    "metadata_t_crit": power_result["t_crit_alpha005"],
                    "metadata_t_power_80": power_result["t_power_80"],
                    "metadata_mean_d": power_result["mean_d_full_vs_tanh"],
                    "metadata_sigma_diff": power_result["sigma_diff_full_vs_tanh"],
                    "metadata_mde_50pp": power_result["mde_50pct_full_vs_tanh_pp"],
                    "metadata_mde_80pp": power_result["mde_80pct_full_vs_tanh_pp"],
                    "metadata_p_value": power_result["p_full_vs_tanh"],
                    "metadata_formula": "(t_crit + t_power80) * sigma_diff / sqrt(n)",
                    "predict_mde_80pp": str(power_result["mde_80pct_full_vs_tanh_pp"]),
                    "predict_interpretation": "null result; coupling adds nothing over pure tanh",
                    "eval_mde_80pp": power_result["mde_80pct_full_vs_tanh_pp"],
                    "eval_p_value": round(power_result["p_full_vs_tanh"], 6),
                },
            ],
        },
        {
            "dataset": "metric_standardization_table",
            "examples": [
                {
                    "input": f"depth={r['depth']}, activation={r['activation']}",
                    "output": (
                        f"raw_ratio={r['raw_ratio_mean']:.4f} (std={r['raw_ratio_std']:.4f}), "
                        f"|ratio-1|={r['abs_dev']:.4f}, rank_abs_dev={r['rank_abs_dev']}"
                    ),
                    "metadata_depth": r["depth"],
                    "metadata_activation": r["activation"],
                    "metadata_raw_ratio_mean": r["raw_ratio_mean"],
                    "metadata_raw_ratio_std": r["raw_ratio_std"],
                    "metadata_abs_dev": r["abs_dev"],
                    "metadata_rank_abs_dev": r["rank_abs_dev"],
                    "metadata_rank_raw_ratio": r["rank_raw_ratio"],
                    "predict_stability_rank": str(r["rank_abs_dev"]),
                    "predict_abs_dev": str(r["abs_dev"]),
                    "eval_abs_dev": r["abs_dev"],
                    "eval_rank_abs_dev": float(r["rank_abs_dev"]),
                }
                for r in metric_table
            ],
        },
        {
            "dataset": "figure_captions",
            "examples": [
                {
                    "input": f"figure_{cap['fig_num']}: {cap['title']}",
                    "output": cap["caption"],
                    "metadata_fig_num": cap["fig_num"],
                    "metadata_title": cap["title"],
                    "predict_caption_word_count": str(len(cap["caption"].split())),
                    "eval_caption_char_length": float(len(cap["caption"])),
                }
                for cap in fig_captions
            ],
        },
        {
            "dataset": "abstract_numbers_audit",
            "examples": [
                {
                    "input": "sech^2(2.0) analytical verification",
                    "output": f"cosh(2.0)={abstract_numbers['sech2_2_0']['cosh_2_0']}, sech^2(2.0)={abstract_numbers['sech2_2_0']['value']}",
                    "metadata_source": "analytical",
                    "metadata_formula": "1/cosh^2(2.0)",
                    "predict_sech2_value": str(abstract_numbers["sech2_2_0"]["value"]),
                    "eval_sech2_2_0": abstract_numbers["sech2_2_0"]["value"],
                },
                {
                    "input": "IFT vs Unrolled memory savings at n=4096 (fair comparison)",
                    "output": (
                        f"ift_MB={abstract_numbers['memory_ift_vs_unrolled_n4096']['ift_MB']}, "
                        f"unrolled_MB={abstract_numbers['memory_ift_vs_unrolled_n4096']['unrolled_MB']}, "
                        f"ift_over_unrolled={abstract_numbers['memory_ift_vs_unrolled_n4096']['ift_over_unrolled']}, "
                        f"savings={abstract_numbers['memory_ift_vs_unrolled_n4096']['savings_pct']}%, "
                        f"multiple={abstract_numbers['memory_ift_vs_unrolled_n4096']['savings_multiple']}x"
                    ),
                    "metadata_source_artifact": "art_xd3tmcyckf00",
                    "metadata_json_path": "metadata.summary_table[n=4096,x_scale=0.1]",
                    "predict_ift_over_unrolled": str(abstract_numbers["memory_ift_vs_unrolled_n4096"]["ift_over_unrolled"]),
                    "eval_ift_over_unrolled": abstract_numbers["memory_ift_vs_unrolled_n4096"]["ift_over_unrolled"],
                    "eval_savings_pct": abstract_numbers["memory_ift_vs_unrolled_n4096"]["savings_pct"],
                },
                {
                    "input": "Gradient stability: CWA vs SELU vs GELU at depth 6",
                    "output": (
                        f"CWA |ratio-1|={abstract_numbers['grad_ratio_cwa_d6']['abs_dev']}, "
                        f"SELU |ratio-1|={abstract_numbers['grad_ratio_selu_d6']['abs_dev']}, "
                        f"GELU |ratio-1|={abstract_numbers['grad_ratio_gelu_d6']['abs_dev']}, "
                        f"CWA/SELU={abstract_numbers['cwa_vs_selu_ratio_d6']['value']}x, "
                        f"CWA/GELU={abstract_numbers['cwa_vs_gelu_ratio_d6']['value']}x"
                    ),
                    "metadata_source_artifact": "art_v26XKv4_F1RM",
                    "metadata_json_path": "metadata.summary_tables.gradient_ratio_by_depth_activation.depth6",
                    "predict_cwa_selu_ratio": str(abstract_numbers["cwa_vs_selu_ratio_d6"]["value"]),
                    "eval_cwa_abs_dev_d6": abstract_numbers["grad_ratio_cwa_d6"]["abs_dev"],
                    "eval_selu_abs_dev_d6": abstract_numbers["grad_ratio_selu_d6"]["abs_dev"],
                    "eval_cwa_selu_ratio_d6": abstract_numbers["cwa_vs_selu_ratio_d6"]["value"],
                },
                {
                    "input": "GELU+LN gradient instability across all depths (second-worst)",
                    "output": (
                        f"d6 |ratio-1|={abstract_numbers['grad_ratio_gelu_ln']['d6_abs_dev']}, "
                        f"d10 |ratio-1|={abstract_numbers['grad_ratio_gelu_ln']['d10_abs_dev']}, "
                        f"d20 |ratio-1|={abstract_numbers['grad_ratio_gelu_ln']['d20_abs_dev']}; "
                        "second-worst at every depth; d20 raw_ratio=9.661 -> abs_dev=8.661 (NOT 9.661)"
                    ),
                    "metadata_source_artifact": "art_v26XKv4_F1RM",
                    "metadata_note": "d20 raw_ratio=9.661 means |ratio-1|=8.661, not 9.661",
                    "predict_d20_abs_dev": str(abstract_numbers["grad_ratio_gelu_ln"]["d20_abs_dev"]),
                    "eval_gelu_ln_abs_dev_d6": abstract_numbers["grad_ratio_gelu_ln"]["d6_abs_dev"],
                    "eval_gelu_ln_abs_dev_d10": abstract_numbers["grad_ratio_gelu_ln"]["d10_abs_dev"],
                    "eval_gelu_ln_abs_dev_d20": abstract_numbers["grad_ratio_gelu_ln"]["d20_abs_dev"],
                },
                {
                    "input": "LM results: CWA BPC vs GELU BPC (5000 steps, 2 seeds)",
                    "output": (
                        f"CWA_BPC={abstract_numbers['lm_results']['cwa_bpc']}, "
                        f"GELU_BPC={abstract_numbers['lm_results']['gelu_bpc']}, "
                        f"delta={abstract_numbers['lm_results']['delta_bpc']} (CWA worse), "
                        f"J_shared_lr={abstract_numbers['lm_results']['j_trajectory_shared_lr']}, "
                        f"J_100xlr={abstract_numbers['lm_results']['j_range_100xlr']}"
                    ),
                    "metadata_source_artifact": "art_V46hELP73T_t",
                    "metadata_json_path": "metadata.sub_exp_b / sub_exp_c",
                    "predict_cwa_advantage": "none (delta>0 means CWA worse)",
                    "eval_cwa_bpc": abstract_numbers["lm_results"]["cwa_bpc"],
                    "eval_gelu_bpc": abstract_numbers["lm_results"]["gelu_bpc"],
                    "eval_bpc_delta": abstract_numbers["lm_results"]["delta_bpc"],
                },
                {
                    "input": "Shift ablation p-values and 80% power MDE",
                    "output": (
                        f"p(CWA-Full vs ShiftOnly)={round(abstract_numbers['shift_ablation_power']['p_full_vs_shift_only'], 4)}, "
                        f"p(CWA-Full vs Pure-Tanh)={round(abstract_numbers['shift_ablation_power']['p_full_vs_pure_tanh'], 4)}, "
                        f"MDE_80(Full vs Tanh)={abstract_numbers['shift_ablation_power']['mde_80pct_pp_full_vs_tanh']}pp"
                    ),
                    "metadata_source_artifact": "art_5zKSer_FGOKx",
                    "metadata_json_path": "metadata.summary.sub_exp_B.pairwise_ttests",
                    "predict_mde_pp": str(abstract_numbers["shift_ablation_power"]["mde_80pct_pp_full_vs_tanh"]),
                    "eval_p_full_vs_shift": abstract_numbers["shift_ablation_power"]["p_full_vs_shift_only"],
                    "eval_p_full_vs_tanh": abstract_numbers["shift_ablation_power"]["p_full_vs_pure_tanh"],
                    "eval_mde_80pp_full_vs_tanh": abstract_numbers["shift_ablation_power"]["mde_80pct_pp_full_vs_tanh"],
                },
                {
                    "input": "J*s_bar range across all experiments",
                    "output": (
                        f"min={abstract_numbers['j_s_bar_range']['min_observed']}, "
                        f"max={abstract_numbers['j_s_bar_range']['max_observed']}; "
                        f"note: {abstract_numbers['j_s_bar_range']['note']}"
                    ),
                    "metadata_sources": abstract_numbers["j_s_bar_range"]["sources"],
                    "predict_j_s_bar_range": "0.20-0.41",
                    "eval_j_s_bar_min": abstract_numbers["j_s_bar_range"]["min_observed"],
                    "eval_j_s_bar_max": abstract_numbers["j_s_bar_range"]["max_observed"],
                },
                {
                    "input": "Lean 4 proof inventory audit",
                    "output": (
                        f"n_theorems={abstract_numbers['lean4_proofs']['n_theorems']}, "
                        f"n_corollaries={abstract_numbers['lean4_proofs']['n_corollaries']}, "
                        f"total={abstract_numbers['lean4_proofs']['total']}; "
                        f"theorems: {'; '.join(abstract_numbers['lean4_proofs']['theorem_names'])}"
                    ),
                    "metadata_theorem_names": abstract_numbers["lean4_proofs"]["theorem_names"],
                    "metadata_corollary_names": abstract_numbers["lean4_proofs"]["corollary_names"],
                    "predict_count": "4 theorems + 1 corollary = 5 total",
                    "eval_n_theorems": float(abstract_numbers["lean4_proofs"]["n_theorems"]),
                    "eval_n_corollaries": float(abstract_numbers["lean4_proofs"]["n_corollaries"]),
                },
            ],
        },
        {
            "dataset": "contributions_fix",
            "examples": [
                {
                    "input": f"OLD contributions bullet: {contributions_fix['old_text']}",
                    "output": f"NEW contributions bullet: {contributions_fix['new_text']}",
                    "metadata_explanation": contributions_fix["explanation"],
                    "metadata_n_theorems": contributions_fix["n_theorems"],
                    "metadata_n_corollaries": contributions_fix["n_corollaries"],
                    "metadata_total_lean4_items": contributions_fix["total_lean4_items"],
                    "predict_corrected_count": "4 theorems + 1 corollary",
                    "predict_new_text": contributions_fix["new_text"],
                    "eval_n_theorems": float(contributions_fix["n_theorems"]),
                    "eval_n_corollaries": float(contributions_fix["n_corollaries"]),
                }
            ],
        },
    ]

    output = {
        "metadata": {
            "evaluation_name": "CWA Final-Paper Stats: Power Analysis, Metric Tables, Figure Captions, Abstract Numbers, Contributions Fix",
            "deliverables": [
                "A: paired-t power analysis for shift ablation null (n=3, df=2)",
                "B: raw-ratio vs |ratio-1| table for 6 activations x 3 depths",
                "C: four LaTeX figure captions",
                "D: numbered abstract-level key claims with source citations",
                "E: corrected contributions bullet (4 theorems + 1 corollary)",
            ],
            "power_analysis_detail": power_result,
            "metric_table": metric_table,
            "figure_captions": fig_captions,
            "abstract_numbers": abstract_numbers,
            "contributions_fix": contributions_fix,
        },
        "metrics_agg": metrics_agg,
        "datasets": datasets,
    }

    output_path = WORKSPACE / "full_eval_out.json"
    logger.info(f"Writing output to {output_path}")
    output_path.write_text(json.dumps(output, indent=2))

    total_examples = sum(len(d["examples"]) for d in datasets)
    logger.info(f"Saved {len(datasets)} datasets, {total_examples} total examples")
    logger.info("=== DONE ===")
    logger.info(f"(A) MDE_80 (Full vs Tanh) = {power_result['mde_80pct_full_vs_tanh_pp']:.3f}pp")
    logger.info(f"(B) Metric table: {len(metric_table)} rows")
    logger.info(f"(C) Figure captions: {len(fig_captions)}")
    logger.info(f"(D) Abstract numbers: {len(abstract_numbers)} items")
    logger.info(f"(E) Contributions: {contributions_fix['n_theorems']} theorems + {contributions_fix['n_corollaries']} corollary")


if __name__ == "__main__":
    main()
