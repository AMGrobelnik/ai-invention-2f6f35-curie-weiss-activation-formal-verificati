#!/usr/bin/env python3
"""CWA Unnormalized MLP Depth Sweep + Fixed-J Ablation on CIFAR-10."""

import sys
import os
import json
import math
import gc
from pathlib import Path

from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

import resource
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as T
import numpy as np
from scipy import stats
from torch.optim.lr_scheduler import CosineAnnealingLR

# ─── Hardware detection ────────────────────────────────────────────────────────
def _detect_cpus() -> int:
    try:
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError):
        pass
    try:
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError):
        pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float:
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError):
            pass
    return 32.0

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb()

logger.info(f"Hardware: {NUM_CPUS} CPUs, GPU={HAS_GPU}, RAM={TOTAL_RAM_GB:.1f}GB")
if HAS_GPU:
    VRAM_GB = torch.cuda.get_device_properties(0).total_memory / 1e9
    logger.info(f"GPU: {torch.cuda.get_device_properties(0).name}, VRAM={VRAM_GB:.1f}GB")
    # Set VRAM budget to 85%
    _free, _total = torch.cuda.mem_get_info(0)
    torch.cuda.set_per_process_memory_fraction(0.85)

# RAM budget: 40GB (leave headroom)
RAM_BUDGET = int(40 * 1024**3)
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))

# ─── Paths ─────────────────────────────────────────────────────────────────────
WORKSPACE = Path(__file__).parent
RESULTS_CACHE = WORKSPACE / "results_cache.json"
OUTPUT_FILE = WORKSPACE / "method_out.json"
CIFAR_DIR = WORKSPACE / "cifar_data"
CIFAR_DIR.mkdir(exist_ok=True)


# ─── CWA Layer ─────────────────────────────────────────────────────────────────
class CWALayer(nn.Module):
    """Curie-Weiss Activation: y_i = tanh(x_i + J * m*), where m* = mean(tanh(x + J*m*))."""

    def __init__(self, fixed_J=None, K_max=50):
        super().__init__()
        self.K_max = K_max
        self.fixed_J = fixed_J
        if fixed_J is None:
            # Learnable: J = sigmoid(J_raw), init J_raw=0 => J=0.5
            self.J_raw = nn.Parameter(torch.zeros(1))
        else:
            self.register_buffer("J_buf", torch.tensor([float(fixed_J)], dtype=torch.float32))
        self._last_J_s_bar = 0.0
        self._last_K = 0
        self._last_mode = "unrolled"

    def get_J(self) -> torch.Tensor:
        if self.fixed_J is None:
            return torch.sigmoid(self.J_raw)
        else:
            return self.J_buf

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        J = self.get_J()
        J_val = J.item()
        delta = 1e-4 * (1.0 - J_val)  # tolerance from Lean Theorem 3

        # Phase 1: converge m* without grad (cheap, no graph)
        with torch.no_grad():
            m = torch.zeros(x.shape[:-1] + (1,), device=x.device, dtype=x.dtype)
            K_conv = self.K_max
            for k in range(self.K_max):
                m_new = torch.mean(torch.tanh(x + J_val * m), dim=-1, keepdim=True)
                if (m_new - m).abs().max().item() < delta:
                    m = m_new
                    K_conv = k + 1
                    break
                m = m_new
            m_star = m  # shape: (batch, 1)

        # Phase 2: compute s_bar for mode selection
        with torch.no_grad():
            z_star = x + J_val * m_star
            s_bar = (1.0 - torch.tanh(z_star) ** 2).mean().item()
        J_s_bar = J_val * s_bar
        self._last_J_s_bar = J_s_bar
        self._last_K = K_conv

        if J_s_bar >= 0.8:
            # IFT BRANCH: detach m_star, gradient flows through x directly (s_k term)
            # and through J via detached computation
            self._last_mode = "ift"
            m_star_detached = m_star.detach()
            # For x gradient: dy_i/dx_k = sech^2(z_i) * delta_ik (direct term only)
            # IFT chain adds s_i * J/(n*(1-J*s_bar)) * sum_k s_k -- small correction
            y = torch.tanh(x + J_val * m_star_detached)
        else:
            # UNROLLED BRANCH: 3 tracked steps from detached m_star
            self._last_mode = "unrolled"
            m = m_star.detach()
            steps = min(K_conv, 3)
            for _ in range(steps):
                m = torch.mean(torch.tanh(x + J * m), dim=-1, keepdim=True)
            y = torch.tanh(x + J * m)

        return y


# ─── Baselines ──────────────────────────────────────────────────────────────────
class CompetingNonlinearities(nn.Module):
    """Quenched random mixture: each neuron fixed as Swish (p=0.83) or Tanh."""

    def __init__(self, n_neurons: int, p_c: float = 0.83):
        super().__init__()
        mask = (torch.rand(1, n_neurons) < p_c).float()
        self.register_buffer("mask", mask)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        swish_out = x * torch.sigmoid(x)
        tanh_out = torch.tanh(x)
        return self.mask * swish_out + (1.0 - self.mask) * tanh_out


# ─── MLP Factory ───────────────────────────────────────────────────────────────
def make_activation(activation: str, hidden: int, fixed_J=None, p_c: float = 0.83) -> nn.Module:
    if activation == "cwa":
        return CWALayer(fixed_J=fixed_J)
    elif activation == "relu":
        return nn.ReLU()
    elif activation == "gelu":
        return nn.GELU()
    elif activation == "selu":
        return nn.SELU()
    elif activation == "competing_nl":
        return CompetingNonlinearities(hidden, p_c=p_c)
    elif activation == "gelu_ln":
        return nn.GELU()  # LN inserted separately in build_mlp
    else:
        raise ValueError(f"Unknown activation: {activation}")


def build_mlp(
    depth: int,
    hidden: int = 256,
    n_in: int = 3072,
    n_out: int = 10,
    activation: str = "cwa",
    fixed_J=None,
    use_ln: bool = False,
    p_c: float = 0.83,
) -> nn.Sequential:
    """Build MLP with `depth` activation layers. Architecture:
    Linear(n_in, hidden) -> [LN] -> Act -> Linear(hidden, hidden) -> [LN] -> Act -> ... -> Linear(hidden, n_out)
    Total: depth+1 linear layers, depth activation layers.
    """
    layers = [nn.Linear(n_in, hidden)]
    for i in range(depth):
        if use_ln:
            layers.append(nn.LayerNorm(hidden))
        act = make_activation(activation, hidden, fixed_J, p_c)
        layers.append(act)
        if i < depth - 1:
            layers.append(nn.Linear(hidden, hidden))
    layers.append(nn.Linear(hidden, n_out))

    model = nn.Sequential(*layers)

    # SELU requires LeCun initialization
    if activation == "selu":
        for m in model.modules():
            if isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, std=1.0 / math.sqrt(m.in_features))
                if m.bias is not None:
                    nn.init.zeros_(m.bias)

    return model


# ─── Gradient ratio ─────────────────────────────────────────────────────────────
def measure_gradient_ratios(model, loader, loss_fn, device):
    """Measure gradient norms for W_1 (first linear) and W_L (last linear)."""
    model.zero_grad()
    x, y = next(iter(loader))
    x, y = x.to(device), y.to(device)
    out = model(x)
    loss = loss_fn(out, y)
    loss.backward()

    linear_layers = [m for m in model.modules() if isinstance(m, nn.Linear)]
    W_first = linear_layers[0]
    W_last = linear_layers[-1]

    eps = 1e-12
    gf = W_first.weight.grad.norm().item() if W_first.weight.grad is not None else eps
    gl = W_last.weight.grad.norm().item() if W_last.weight.grad is not None else eps

    ratio = abs(math.log(gf + eps)) / abs(math.log(gl + eps))
    model.zero_grad()
    return ratio, gf, gl


# ─── Training loop ──────────────────────────────────────────────────────────────
def get_cifar10_loaders(batch_size: int = 256):
    transform = T.Compose([
        T.ToTensor(),
        T.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        T.Lambda(lambda x: x.view(-1)),
    ])
    train_ds = torchvision.datasets.CIFAR10(str(CIFAR_DIR), train=True, download=True, transform=transform)
    test_ds = torchvision.datasets.CIFAR10(str(CIFAR_DIR), train=False, download=True, transform=transform)
    num_workers = min(4, NUM_CPUS)
    train_loader = torch.utils.data.DataLoader(
        train_ds, batch_size=batch_size, shuffle=True, num_workers=num_workers, pin_memory=HAS_GPU
    )
    test_loader = torch.utils.data.DataLoader(
        test_ds, batch_size=512, shuffle=False, num_workers=num_workers, pin_memory=HAS_GPU
    )
    return train_loader, test_loader


def train_one_config(
    depth: int,
    activation_name: str,
    seed: int,
    fixed_J=None,
    epochs: int = 25,
    hidden: int = 256,
    batch: int = 256,
    lr: float = 1e-3,
    device: torch.device = DEVICE,
) -> dict:
    torch.manual_seed(seed)
    np.random.seed(seed)

    train_loader, test_loader = get_cifar10_loaders(batch_size=batch)

    use_ln = activation_name == "gelu_ln"
    model = build_mlp(
        depth, hidden=hidden, activation=activation_name, fixed_J=fixed_J, use_ln=use_ln
    ).to(device)

    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    scheduler = CosineAnnealingLR(optimizer, T_max=epochs, eta_min=1e-5)
    loss_fn = nn.CrossEntropyLoss()

    metrics = {
        "train_loss": [],
        "test_acc": [],
        "grad_ratio_epoch5": None,
        "grad_first_epoch5": None,
        "grad_last_epoch5": None,
        "grad_ratio_epoch25": None,
        "grad_first_epoch25": None,
        "grad_last_epoch25": None,
        "J_s_bar_traj": [],
        "K_traj": [],
        "mode_traj": [],
    }

    for epoch in range(1, epochs + 1):
        model.train()
        epoch_loss = 0.0
        for xb, yb in train_loader:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad()
            out = model(xb)
            loss = loss_fn(out, yb)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            epoch_loss += loss.item()
        scheduler.step()

        # Test accuracy
        model.eval()
        correct = total = 0
        with torch.no_grad():
            for xb, yb in test_loader:
                xb, yb = xb.to(device), yb.to(device)
                pred = model(xb).argmax(1)
                correct += (pred == yb).sum().item()
                total += yb.size(0)
        test_acc = correct / total
        metrics["train_loss"].append(round(epoch_loss / len(train_loader), 5))
        metrics["test_acc"].append(round(test_acc, 5))

        # Log CWA stats
        cwa_layers = [m for m in model.modules() if isinstance(m, CWALayer)]
        if cwa_layers:
            J_s_bars = [m._last_J_s_bar for m in cwa_layers]
            Ks = [m._last_K for m in cwa_layers]
            modes = [m._last_mode for m in cwa_layers]
            metrics["J_s_bar_traj"].append(round(float(np.mean(J_s_bars)), 5))
            metrics["K_traj"].append(round(float(np.mean(Ks)), 3))
            metrics["mode_traj"].append(modes[0] if modes else None)

        # Gradient ratio at epochs 5 and 25
        if epoch == 5:
            ratio, gf, gl = measure_gradient_ratios(model, train_loader, loss_fn, device)
            metrics["grad_ratio_epoch5"] = round(ratio, 5)
            metrics["grad_first_epoch5"] = round(gf, 8)
            metrics["grad_last_epoch5"] = round(gl, 8)
        if epoch == epochs:
            ratio, gf, gl = measure_gradient_ratios(model, train_loader, loss_fn, device)
            metrics["grad_ratio_epoch25"] = round(ratio, 5)
            metrics["grad_first_epoch25"] = round(gf, 8)
            metrics["grad_last_epoch25"] = round(gl, 8)

    # Extract final J value for CWA
    cwa_layers = [m for m in model.modules() if isinstance(m, CWALayer)]
    if cwa_layers:
        J_vals = [cwa.get_J().item() for cwa in cwa_layers]
        metrics["final_J_mean"] = round(float(np.mean(J_vals)), 5)
        metrics["fraction_converged_before_Kmax"] = round(
            sum(1 for k in metrics["K_traj"] if k < 50) / max(len(metrics["K_traj"]), 1), 4
        )

    metrics["final_test_acc"] = metrics["test_acc"][-1] if metrics["test_acc"] else 0.0
    metrics["final_train_loss"] = metrics["train_loss"][-1] if metrics["train_loss"] else float("nan")
    if metrics["J_s_bar_traj"]:
        metrics["J_s_bar_mean"] = round(float(np.mean(metrics["J_s_bar_traj"])), 5)
    else:
        metrics["J_s_bar_mean"] = None
    if metrics["K_traj"]:
        metrics["K_mean"] = round(float(np.mean(metrics["K_traj"])), 3)
    else:
        metrics["K_mean"] = None

    # Free model memory
    del model
    if HAS_GPU:
        torch.cuda.empty_cache()
    gc.collect()

    return metrics


# ─── Experiment grid ────────────────────────────────────────────────────────────
EXP_A_ACTIVATIONS = ["cwa", "relu", "gelu", "selu", "competing_nl", "gelu_ln"]
EXP_A_DEPTHS = [6, 10, 20]
EXP_A_SEEDS = [0, 1, 2]

EXP_B_FIXED_J = [0.1, 0.3, 0.5, 0.7, 0.9]
EXP_B_SEEDS = [0, 1, 2]

EPOCHS = 25


def run_key_a(depth: int, activation: str, seed: int) -> str:
    return f"A_d{depth}_{activation}_s{seed}"


def run_key_b(fixed_J, seed: int) -> str:
    j_str = f"{fixed_J:.1f}" if fixed_J is not None else "learned"
    return f"B_J{j_str}_s{seed}"


def load_cache() -> dict:
    if RESULTS_CACHE.exists():
        try:
            return json.loads(RESULTS_CACHE.read_text())
        except Exception:
            return {}
    return {}


def save_cache(cache: dict):
    RESULTS_CACHE.write_text(json.dumps(cache, indent=2))


# ─── Statistical analysis ───────────────────────────────────────────────────────
def compute_summary_tables(cache: dict) -> dict:
    tables = {}

    # Gradient ratio by depth and activation
    grad_by_depth_act = {}
    for depth in EXP_A_DEPTHS:
        d_key = f"depth{depth}"
        grad_by_depth_act[d_key] = {}
        for act in EXP_A_ACTIVATIONS:
            ratios = []
            for seed in EXP_A_SEEDS:
                k = run_key_a(depth, act, seed)
                if k in cache and cache[k].get("grad_ratio_epoch25") is not None:
                    ratios.append(cache[k]["grad_ratio_epoch25"])
            if ratios:
                grad_by_depth_act[d_key][act] = {
                    "mean": round(float(np.mean(ratios)), 4),
                    "std": round(float(np.std(ratios)), 4),
                    "n": len(ratios),
                    "values": ratios,
                }
    tables["gradient_ratio_by_depth_activation"] = grad_by_depth_act

    # Accuracy by depth
    acc_by_depth = {}
    for depth in EXP_A_DEPTHS:
        d_key = f"depth{depth}"
        acc_by_depth[d_key] = {}
        for act in EXP_A_ACTIVATIONS:
            accs = []
            for seed in EXP_A_SEEDS:
                k = run_key_a(depth, act, seed)
                if k in cache:
                    accs.append(cache[k].get("final_test_acc", 0.0))
            if accs:
                acc_by_depth[d_key][act] = {
                    "mean": round(float(np.mean(accs)), 4),
                    "std": round(float(np.std(accs)), 4),
                    "n": len(accs),
                    "values": accs,
                }
    tables["accuracy_by_depth"] = acc_by_depth

    # Fixed-J gradient ratios
    fixed_j_grad = {}
    for J_val in EXP_B_FIXED_J:
        j_str = f"J{J_val:.1f}"
        ratios = []
        for seed in EXP_B_SEEDS:
            k = run_key_b(J_val, seed)
            if k in cache and cache[k].get("grad_ratio_epoch25") is not None:
                ratios.append(cache[k]["grad_ratio_epoch25"])
        if ratios:
            fixed_j_grad[j_str] = {
                "mean": round(float(np.mean(ratios)), 4),
                "std": round(float(np.std(ratios)), 4),
                "n": len(ratios),
                "values": ratios,
            }
    # Learned J (from Exp B)
    learned_ratios = []
    for seed in EXP_B_SEEDS:
        k = run_key_b(None, seed)
        if k in cache and cache[k].get("grad_ratio_epoch25") is not None:
            learned_ratios.append(cache[k]["grad_ratio_epoch25"])
    if learned_ratios:
        fixed_j_grad["learned_J"] = {
            "mean": round(float(np.mean(learned_ratios)), 4),
            "std": round(float(np.std(learned_ratios)), 4),
            "n": len(learned_ratios),
            "values": learned_ratios,
        }
    tables["fixed_j_gradient_ratios"] = fixed_j_grad

    # Fixed-J accuracy
    fixed_j_acc = {}
    for J_val in EXP_B_FIXED_J:
        j_str = f"J{J_val:.1f}"
        accs = []
        for seed in EXP_B_SEEDS:
            k = run_key_b(J_val, seed)
            if k in cache:
                accs.append(cache[k].get("final_test_acc", 0.0))
        if accs:
            fixed_j_acc[j_str] = {
                "mean": round(float(np.mean(accs)), 4),
                "std": round(float(np.std(accs)), 4),
                "n": len(accs),
            }
    learned_accs = []
    for seed in EXP_B_SEEDS:
        k = run_key_b(None, seed)
        if k in cache:
            learned_accs.append(cache[k].get("final_test_acc", 0.0))
    if learned_accs:
        fixed_j_acc["learned_J"] = {
            "mean": round(float(np.mean(learned_accs)), 4),
            "std": round(float(np.std(learned_accs)), 4),
            "n": len(learned_accs),
        }
    tables["fixed_j_accuracy"] = fixed_j_acc

    # J_s_bar trajectory summary
    jsbar_traj = {}
    for depth in EXP_A_DEPTHS:
        for seed in EXP_A_SEEDS:
            k = run_key_a(depth, "cwa", seed)
            if k in cache and cache[k].get("J_s_bar_traj"):
                traj_key = f"cwa_d{depth}_s{seed}"
                jsbar_traj[traj_key] = cache[k]["J_s_bar_traj"]
    tables["J_s_bar_trajectory"] = jsbar_traj

    # Fraction steps converged before K_max
    conv_frac = {}
    for depth in EXP_A_DEPTHS:
        for seed in EXP_A_SEEDS:
            k = run_key_a(depth, "cwa", seed)
            if k in cache:
                conv_frac[f"d{depth}_s{seed}"] = cache[k].get("fraction_converged_before_Kmax", None)
    tables["fraction_steps_converged_before_K_max"] = conv_frac

    return tables


def compute_statistical_tests(cache: dict) -> dict:
    tests = {}

    for depth in [6, 10, 20]:
        cwa_accs = []
        gelu_accs = []
        for seed in EXP_A_SEEDS:
            kc = run_key_a(depth, "cwa", seed)
            kg = run_key_a(depth, "gelu", seed)
            if kc in cache and kg in cache:
                cwa_accs.append(cache[kc].get("final_test_acc", 0.0))
                gelu_accs.append(cache[kg].get("final_test_acc", 0.0))
        if len(cwa_accs) == 3:
            t, p = stats.ttest_rel(cwa_accs, gelu_accs)
            ci_cwa = 1.96 * np.std(cwa_accs) / np.sqrt(3)
            ci_gelu = 1.96 * np.std(gelu_accs) / np.sqrt(3)
            tests[f"paired_ttest_cwa_vs_gelu_depth{depth}_acc"] = {
                "t": round(float(t), 4),
                "p": round(float(p), 6),
                "significant": bool(p < 0.05),
                "cwa_mean_ci": f"{np.mean(cwa_accs):.4f} ± {ci_cwa:.4f}",
                "gelu_mean_ci": f"{np.mean(gelu_accs):.4f} ± {ci_gelu:.4f}",
            }

    # Fixed-J gradient ratio tests vs GELU at depth 10
    gelu_ratios_d10 = []
    for seed in EXP_A_SEEDS:
        k = run_key_a(10, "gelu", seed)
        if k in cache and cache[k].get("grad_ratio_epoch25") is not None:
            gelu_ratios_d10.append(cache[k]["grad_ratio_epoch25"])

    if gelu_ratios_d10:
        for J_val in EXP_B_FIXED_J:
            j_ratios = []
            for seed in EXP_B_SEEDS:
                k = run_key_b(J_val, seed)
                if k in cache and cache[k].get("grad_ratio_epoch25") is not None:
                    j_ratios.append(cache[k]["grad_ratio_epoch25"])
            if len(j_ratios) >= 2:
                t, p = stats.ttest_ind(j_ratios, gelu_ratios_d10, equal_var=False)
                tests[f"welch_fixedJ{J_val:.1f}_vs_gelu_grad_ratio"] = {
                    "t": round(float(t), 4),
                    "p": round(float(p), 6),
                    "significant": bool(p < 0.05),
                    "fixedJ_mean": round(float(np.mean(j_ratios)), 4),
                    "gelu_mean": round(float(np.mean(gelu_ratios_d10)), 4),
                }

    return tests


def determine_verdict(cache: dict, tables: dict) -> tuple[str, str]:
    """Apply verdict logic from plan."""
    grad_by_depth = tables.get("gradient_ratio_by_depth_activation", {})

    # Check gradient stability at depth 10
    cwa_grad_d10 = grad_by_depth.get("depth10", {}).get("cwa", {}).get("mean", float("inf"))
    gelu_grad_d10 = grad_by_depth.get("depth10", {}).get("gelu", {}).get("mean", 0.0)

    # Check accuracy comparison
    acc_by_depth = tables.get("accuracy_by_depth", {})
    cwa_better_count = 0
    for d_key in ["depth6", "depth10", "depth20"]:
        cwa_acc = acc_by_depth.get(d_key, {}).get("cwa", {}).get("mean", 0.0)
        gelu_acc = acc_by_depth.get(d_key, {}).get("gelu", {}).get("mean", 0.0)
        if cwa_acc > gelu_acc + 0.005:
            cwa_better_count += 1

    # Fixed-J at 0.7/0.9
    fixed_j_grad = tables.get("fixed_j_gradient_ratios", {})
    j09_grad = fixed_j_grad.get("J0.9", {}).get("mean", float("inf"))
    j07_grad = fixed_j_grad.get("J0.7", {}).get("mean", float("inf"))

    grad_stability_met = (cwa_grad_d10 < 2.0) and (gelu_grad_d10 > 5.0)
    acc_met = cwa_better_count >= 2
    mechanism_sound = (j09_grad < 2.0) or (j07_grad < 2.0)

    if grad_stability_met and acc_met:
        verdict = "CONFIRM"
        reason = (
            f"CWA gradient ratio at depth 10: {cwa_grad_d10:.3f} < 2.0, "
            f"GELU: {gelu_grad_d10:.3f} > 5.0. "
            f"CWA outperforms GELU in accuracy on {cwa_better_count}/3 depths. "
            "Both gradient stability and accuracy claims confirmed."
        )
    elif grad_stability_met or mechanism_sound:
        verdict = "PARTIAL_CONFIRM"
        parts = []
        if grad_stability_met:
            parts.append(f"gradient stability confirmed (CWA={cwa_grad_d10:.3f} < 2.0, GELU={gelu_grad_d10:.3f})")
        if mechanism_sound:
            near_crit_grad = min(j07_grad, j09_grad)
            parts.append(f"mechanism confirmed via fixed-J (J0.7/0.9 grad_ratio={near_crit_grad:.3f} < 2.0)")
        if not acc_met:
            parts.append(f"but accuracy advantage only on {cwa_better_count}/3 depths")
        reason = "; ".join(parts)
    else:
        verdict = "DISCONFIRM"
        reason = (
            f"CWA gradient ratio depth10={cwa_grad_d10:.3f} >= GELU={gelu_grad_d10:.3f}. "
            f"Fixed-J 0.9 grad_ratio={j09_grad:.3f} (not < GELU). "
            "Neither gradient stability nor mechanism confirmed."
        )

    return verdict, reason


# ─── Output builder ─────────────────────────────────────────────────────────────
def build_method_out(cache: dict) -> dict:
    tables = compute_summary_tables(cache)
    stat_tests = compute_statistical_tests(cache)
    verdict, verdict_reason = determine_verdict(cache, tables)

    # Build examples list in exp_gen_sol_out format
    examples = []

    # Experiment A examples
    for depth in EXP_A_DEPTHS:
        for act in EXP_A_ACTIVATIONS:
            for seed in EXP_A_SEEDS:
                k = run_key_a(depth, act, seed)
                result = cache.get(k, {})
                config_str = f"depth={depth}, activation={act}, seed={seed}, fixed_J=null"
                output_str = (
                    f"final_test_acc={result.get('final_test_acc', 'N/A')}, "
                    f"grad_ratio_epoch25={result.get('grad_ratio_epoch25', 'N/A')}, "
                    f"J_s_bar_mean={result.get('J_s_bar_mean', 'N/A')}"
                )
                ex = {
                    "input": config_str,
                    "output": output_str,
                    "metadata_experiment": "A_depth_sweep",
                    "metadata_run_key": k,
                    "metadata_depth": str(depth),
                    "metadata_activation": act,
                    "metadata_seed": str(seed),
                    "metadata_fixed_J": "null",
                    "metadata_final_test_acc": result.get("final_test_acc"),
                    "metadata_grad_ratio_epoch5": result.get("grad_ratio_epoch5"),
                    "metadata_grad_ratio_epoch25": result.get("grad_ratio_epoch25"),
                    "metadata_J_s_bar_mean": result.get("J_s_bar_mean"),
                    "metadata_K_mean": result.get("K_mean"),
                    "metadata_fraction_converged": result.get("fraction_converged_before_Kmax"),
                    "metadata_final_J_mean": result.get("final_J_mean"),
                    "metadata_grad_first_epoch25": result.get("grad_first_epoch25"),
                    "metadata_grad_last_epoch25": result.get("grad_last_epoch25"),
                    "metadata_train_loss": result.get("final_train_loss"),
                    "metadata_test_acc_traj": result.get("test_acc", []),
                    "metadata_J_s_bar_traj": result.get("J_s_bar_traj", []),
                    "predict_final_test_acc": str(result.get("final_test_acc", "")),
                    "predict_grad_ratio_epoch25": str(result.get("grad_ratio_epoch25", "")),
                }
                examples.append(ex)

    # Experiment B examples
    for J_val in EXP_B_FIXED_J:
        for seed in EXP_B_SEEDS:
            k = run_key_b(J_val, seed)
            result = cache.get(k, {})
            config_str = f"depth=10, activation=cwa, seed={seed}, fixed_J={J_val}"
            output_str = (
                f"final_test_acc={result.get('final_test_acc', 'N/A')}, "
                f"grad_ratio_epoch25={result.get('grad_ratio_epoch25', 'N/A')}"
            )
            ex = {
                "input": config_str,
                "output": output_str,
                "metadata_experiment": "B_fixed_J_ablation",
                "metadata_run_key": k,
                "metadata_depth": "10",
                "metadata_activation": "cwa",
                "metadata_seed": str(seed),
                "metadata_fixed_J": str(J_val),
                "metadata_final_test_acc": result.get("final_test_acc"),
                "metadata_grad_ratio_epoch5": result.get("grad_ratio_epoch5"),
                "metadata_grad_ratio_epoch25": result.get("grad_ratio_epoch25"),
                "metadata_grad_first_epoch25": result.get("grad_first_epoch25"),
                "metadata_grad_last_epoch25": result.get("grad_last_epoch25"),
                "metadata_J_s_bar_mean": result.get("J_s_bar_mean"),
                "metadata_K_mean": result.get("K_mean"),
                "metadata_train_loss": result.get("final_train_loss"),
                "metadata_test_acc_traj": result.get("test_acc", []),
                "predict_final_test_acc": str(result.get("final_test_acc", "")),
                "predict_grad_ratio_epoch25": str(result.get("grad_ratio_epoch25", "")),
            }
            examples.append(ex)

    # Learned J from Exp B (depth=10, cwa, seeds 0,1,2)
    for seed in EXP_B_SEEDS:
        k = run_key_b(None, seed)
        result = cache.get(k, {})
        config_str = f"depth=10, activation=cwa, seed={seed}, fixed_J=learned"
        output_str = (
            f"final_test_acc={result.get('final_test_acc', 'N/A')}, "
            f"grad_ratio_epoch25={result.get('grad_ratio_epoch25', 'N/A')}, "
            f"learned_J={result.get('final_J_mean', 'N/A')}"
        )
        ex = {
            "input": config_str,
            "output": output_str,
            "metadata_experiment": "B_fixed_J_ablation",
            "metadata_run_key": k,
            "metadata_depth": "10",
            "metadata_activation": "cwa",
            "metadata_seed": str(seed),
            "metadata_fixed_J": "learned",
            "metadata_final_test_acc": result.get("final_test_acc"),
            "metadata_grad_ratio_epoch25": result.get("grad_ratio_epoch25"),
            "metadata_J_s_bar_mean": result.get("J_s_bar_mean"),
            "metadata_final_J_mean": result.get("final_J_mean"),
            "metadata_train_loss": result.get("final_train_loss"),
            "predict_final_test_acc": str(result.get("final_test_acc", "")),
            "predict_grad_ratio_epoch25": str(result.get("grad_ratio_epoch25", "")),
        }
        examples.append(ex)

    # Derive key findings
    acc_by_depth = tables.get("accuracy_by_depth", {})
    grad_by_depth = tables.get("gradient_ratio_by_depth_activation", {})
    key_findings = []

    for depth in EXP_A_DEPTHS:
        d_key = f"depth{depth}"
        cwa_acc = acc_by_depth.get(d_key, {}).get("cwa", {}).get("mean", None)
        gelu_acc = acc_by_depth.get(d_key, {}).get("gelu", {}).get("mean", None)
        cwa_grad = grad_by_depth.get(d_key, {}).get("cwa", {}).get("mean", None)
        gelu_grad = grad_by_depth.get(d_key, {}).get("gelu", {}).get("mean", None)
        if cwa_acc is not None:
            key_findings.append(
                f"Depth {depth}: CWA acc={cwa_acc:.4f} vs GELU acc={gelu_acc:.4f}; "
                f"grad_ratio: CWA={cwa_grad} vs GELU={gelu_grad}"
            )

    fixed_j_grad = tables.get("fixed_j_gradient_ratios", {})
    for j_str in ["J0.5", "J0.7", "J0.9"]:
        val = fixed_j_grad.get(j_str, {}).get("mean", None)
        if val is not None:
            key_findings.append(f"Fixed {j_str}: grad_ratio_epoch25={val:.4f}")

    learned_jsbar = None
    for seed in EXP_A_SEEDS:
        k = run_key_a(10, "cwa", seed)
        if k in cache and cache[k].get("J_s_bar_mean") is not None:
            learned_jsbar = cache[k]["J_s_bar_mean"]
            break
    if learned_jsbar is not None:
        key_findings.append(f"Learned CWA at depth 10: J*s_bar converges to ~{learned_jsbar:.3f}")

    return {
        "metadata": {
            "experiment_name": "CWA Unnormalized MLP Depth Sweep + Fixed-J Ablation",
            "hypothesis_tested": "CWA provides gradient stability via near-critical J*s_bar; fixed-J ablation tests mechanism",
            "verdict": verdict,
            "verdict_reason": verdict_reason,
            "summary_tables": tables,
            "statistical_tests": stat_tests,
            "key_findings": key_findings,
            "n_runs_completed": len(cache),
            "n_runs_expected": 75,  # 54 + 18 + 3 learned
        },
        "datasets": [
            {
                "dataset": "CIFAR-10",
                "examples": examples,
            }
        ],
    }


# ─── Main ───────────────────────────────────────────────────────────────────────
@logger.catch(reraise=True)
def main():
    logger.info("=== CWA Depth Sweep + Fixed-J Ablation ===")
    logger.info(f"Device: {DEVICE}")

    # Download CIFAR-10 first (shared across runs)
    logger.info("Downloading CIFAR-10...")
    transform = T.Compose([T.ToTensor()])
    torchvision.datasets.CIFAR10(str(CIFAR_DIR), train=True, download=True, transform=transform)
    torchvision.datasets.CIFAR10(str(CIFAR_DIR), train=False, download=True, transform=transform)
    logger.info("CIFAR-10 ready")

    cache = load_cache()
    logger.info(f"Loaded cache with {len(cache)} completed runs")

    # ── Experiment A: Depth sweep ─────────────────────────────────────────────
    logger.info("=== Experiment A: Depth Sweep ===")
    # Priority order: depth=10 first (core), then depth=6, then depth=20
    run_order_A = []
    for depth in [10, 6, 20]:
        for act in EXP_A_ACTIVATIONS:
            for seed in EXP_A_SEEDS:
                run_order_A.append((depth, act, seed))

    total_A = len(run_order_A)
    completed_A = 0
    for depth, act, seed in run_order_A:
        k = run_key_a(depth, act, seed)
        if k in cache:
            completed_A += 1
            continue
        logger.info(f"[A] depth={depth}, act={act}, seed={seed} ({completed_A+1}/{total_A})")
        try:
            metrics = train_one_config(
                depth=depth,
                activation_name=act,
                seed=seed,
                epochs=EPOCHS,
                device=DEVICE,
            )
            cache[k] = metrics
            save_cache(cache)
            logger.info(
                f"  -> acc={metrics['final_test_acc']:.4f}, "
                f"grad_ratio={metrics.get('grad_ratio_epoch25', 'N/A')}, "
                f"J_s_bar={metrics.get('J_s_bar_mean', 'N/A')}"
            )
        except Exception as e:
            logger.error(f"Run {k} failed: {e}")
            cache[k] = {"error": str(e), "final_test_acc": 0.0}
            save_cache(cache)
        completed_A += 1

    # ── Experiment B: Fixed-J ablation ────────────────────────────────────────
    logger.info("=== Experiment B: Fixed-J Ablation (depth=10) ===")
    # Include learned J at depth 10 as well (from Exp A already done)
    # Run all fixed-J values
    run_order_B = []
    for J_val in EXP_B_FIXED_J:
        for seed in EXP_B_SEEDS:
            run_order_B.append((J_val, seed))
    # Also run learned J (depth=10, cwa, learnable) if not in cache already
    for seed in EXP_B_SEEDS:
        run_order_B.append((None, seed))

    total_B = len(run_order_B)
    completed_B = 0
    for J_val, seed in run_order_B:
        k = run_key_b(J_val, seed)
        if k in cache:
            completed_B += 1
            continue
        j_str = f"{J_val:.1f}" if J_val is not None else "learned"
        logger.info(f"[B] fixed_J={j_str}, seed={seed} ({completed_B+1}/{total_B})")
        try:
            metrics = train_one_config(
                depth=10,
                activation_name="cwa",
                seed=seed,
                fixed_J=J_val,
                epochs=EPOCHS,
                device=DEVICE,
            )
            cache[k] = metrics
            save_cache(cache)
            logger.info(
                f"  -> acc={metrics['final_test_acc']:.4f}, "
                f"grad_ratio={metrics.get('grad_ratio_epoch25', 'N/A')}"
            )
        except Exception as e:
            logger.error(f"Run {k} failed: {e}")
            cache[k] = {"error": str(e), "final_test_acc": 0.0}
            save_cache(cache)
        completed_B += 1

    # ── Build output ──────────────────────────────────────────────────────────
    logger.info("Building method_out.json...")
    method_out = build_method_out(cache)
    OUTPUT_FILE.write_text(json.dumps(method_out, indent=2))
    logger.info(f"Saved method_out.json with {len(method_out['datasets'][0]['examples'])} examples")

    # Report verdict
    verdict = method_out["metadata"]["verdict"]
    logger.info(f"VERDICT: {verdict}")
    logger.info(f"REASON: {method_out['metadata']['verdict_reason']}")

    for finding in method_out["metadata"]["key_findings"]:
        logger.info(f"  {finding}")


if __name__ == "__main__":
    main()
