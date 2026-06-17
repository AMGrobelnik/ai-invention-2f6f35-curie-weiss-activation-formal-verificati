#!/usr/bin/env python3
"""CWA Mechanistic Sub-Experiments: Small-Weight Init (J*sbar Saturation) and Constant-Shift Ablation."""

import sys
import math
import json
import time
import gc
import resource
import multiprocessing as mp
from pathlib import Path
from collections import defaultdict

from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
Path("logs").mkdir(exist_ok=True)
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

import numpy as np
from scipy import stats
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as T
from torch.utils.data import DataLoader


# ──────────────────────────────────────────────────────────────────────────────
# Hardware detection & limits
# ──────────────────────────────────────────────────────────────────────────────

def _container_ram_gb() -> float:
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError):
            pass
    import psutil
    return psutil.virtual_memory().total / 1e9

TOTAL_RAM_GB = _container_ram_gb()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_memory / 1e9 if HAS_GPU else 0.0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")

logger.info(f"RAM: {TOTAL_RAM_GB:.1f} GB | GPU: {HAS_GPU} | VRAM: {VRAM_GB:.1f} GB | device={DEVICE}")

# Set conservative RAM limit
try:
    RAM_BUDGET = int(min(40, TOTAL_RAM_GB * 0.45) * 1024**3)
    resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))
except (ValueError, resource.error) as e:
    logger.warning(f"Could not set RLIMIT_AS: {e}")

# Verify CUDA actually works (RTX 5090 / sm_120 requires PyTorch >= 2.7)
_CUDA_OK = False
if HAS_GPU:
    try:
        _test = torch.randn(4, 4, device="cuda")
        _ = (_test @ _test)
        _CUDA_OK = True
        logger.info("CUDA verified working")
        _free, _total = torch.cuda.mem_get_info(0)
        VRAM_BUDGET = min(_free * 0.80, _total * 0.85)
        torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.85))
        logger.info(f"VRAM budget: {VRAM_BUDGET/1e9:.1f} GB / {_total/1e9:.1f} GB")
    except Exception as e:
        logger.warning(f"CUDA not functional (sm_120 incompatibility?): {e} — falling back to CPU")
        _CUDA_OK = False

DEVICE = torch.device("cuda" if _CUDA_OK else "cpu")
logger.info(f"Effective device: {DEVICE}")


# ──────────────────────────────────────────────────────────────────────────────
# Dataset
# ──────────────────────────────────────────────────────────────────────────────

def get_cifar10_loaders(batch_size: int = 256, root: str = "/tmp/cifar10"):
    tf = T.Compose([
        T.ToTensor(),
        T.Normalize((0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616)),
        T.Lambda(lambda x: x.view(-1)),  # flatten to 3072
    ])
    train_ds = torchvision.datasets.CIFAR10(root, train=True,  download=True, transform=tf)
    test_ds  = torchvision.datasets.CIFAR10(root, train=False, download=True, transform=tf)
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True,  num_workers=4, pin_memory=HAS_GPU, persistent_workers=True)
    test_loader  = DataLoader(test_ds,  batch_size=batch_size, shuffle=False, num_workers=4, pin_memory=HAS_GPU, persistent_workers=True)
    return train_loader, test_loader


# ──────────────────────────────────────────────────────────────────────────────
# CWA Module — IFT backward (always IFT, closed-form)
# ──────────────────────────────────────────────────────────────────────────────

class CWAFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x: torch.Tensor, J_raw: torch.Tensor, K_max: int = 50):
        J = torch.sigmoid(J_raw)  # scalar in (0,1)
        n = x.shape[-1]

        m = torch.zeros(*x.shape[:-1], 1, device=x.device, dtype=x.dtype)

        for k in range(K_max):
            h     = x + J * m
            m_new = torch.tanh(h).mean(dim=-1, keepdim=True)
            s_bar = (1.0 / torch.cosh(h)).pow(2).mean(dim=-1, keepdim=True)
            j_s_bar = J * s_bar
            delta = (1e-4 * (1.0 - j_s_bar.clamp(max=0.9999))).clamp(min=1e-8)
            if (m_new - m).abs().max() < delta.max():
                m = m_new
                break
            m = m_new

        m_star  = m.detach()
        h_star  = x + J * m_star
        s_k     = (1.0 / torch.cosh(h_star)).pow(2)  # (batch, n)
        s_bar   = s_k.mean(dim=-1, keepdim=True)       # (batch, 1)
        j_s_bar = (J * s_bar).squeeze(-1)              # (batch,)
        y       = torch.tanh(h_star)

        ift_triggered = (j_s_bar >= 0.8).sum().item()

        ctx.save_for_backward(x, J_raw, m_star, s_k, s_bar)
        ctx.K_max = K_max
        ctx.ift_triggered = ift_triggered
        ctx.j_s_bar_mean  = j_s_bar.mean().item()
        return y, j_s_bar.mean().detach(), torch.tensor(float(ift_triggered))

    @staticmethod
    def backward(ctx, grad_y, grad_jsbar, grad_ift):
        x, J_raw, m_star, s_k, s_bar = ctx.saved_tensors
        J       = torch.sigmoid(J_raw)
        n       = x.shape[-1]
        j_s_bar = J * s_bar  # (batch, 1)
        denom   = (1.0 - j_s_bar).clamp(min=1e-6)

        # Σ_gs = Σ_k g_k * s_k  per sample
        sum_gs = (grad_y * s_k).sum(dim=-1, keepdim=True)  # (batch, 1)

        # ∂L/∂x_k = s_k * [g_k + J * sum_gs / (n * denom)]
        grad_x = s_k * (grad_y + J * sum_gs / (n * denom))

        # ∂L/∂J = m* * s̄ * sum_gs / denom  (summed over batch)
        grad_J_sum = (m_star * s_bar * sum_gs / denom).sum()
        # chain rule: J = sigmoid(J_raw)
        grad_J_raw = grad_J_sum * J * (1.0 - J)

        return grad_x, grad_J_raw, None


class CWALayer(nn.Module):
    """Curie-Weiss Activation with IFT backward."""

    def __init__(self, K_max: int = 50):
        super().__init__()
        self.J_raw  = nn.Parameter(torch.zeros(1))
        self.K_max  = K_max
        self.last_j_s_bar       = 0.0
        self.last_ift_triggered = 0
        self.last_iters         = 0

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        y, j_s_bar, ift_trig = CWAFunction.apply(x, self.J_raw, self.K_max)
        self.last_j_s_bar        = j_s_bar.item()
        self.last_ift_triggered += int(ift_trig.item())
        return y


# ──────────────────────────────────────────────────────────────────────────────
# CWA-ShiftOnly (Sub-Exp B ablation)
# ──────────────────────────────────────────────────────────────────────────────

class CWAShiftOnlyLayer(nn.Module):
    """Constant-shift ablation: y_i = tanh(x_i + c), c = J_frozen * mean(tanh(x)). No backprop through c."""

    def __init__(self, J_frozen: float = 0.5):
        super().__init__()
        self.J_frozen = J_frozen

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        with torch.no_grad():
            c = self.J_frozen * torch.tanh(x).mean(dim=-1, keepdim=True)
        return torch.tanh(x + c.detach())


# ──────────────────────────────────────────────────────────────────────────────
# MLP Architecture
# ──────────────────────────────────────────────────────────────────────────────

def build_mlp(
    depth: int = 10,
    hidden: int = 256,
    in_dim: int = 3072,
    out_dim: int = 10,
    act: str = "cwa",
    weight_init: str = "kaiming",
    K_max: int = 50,
) -> nn.Sequential:
    """Build unnormalized MLP (no BatchNorm, LayerNorm, Dropout)."""
    def make_act():
        if act == "cwa":         return CWALayer(K_max=K_max)
        elif act == "shift_only": return CWAShiftOnlyLayer(J_frozen=0.5)
        elif act == "tanh":       return nn.Tanh()
        elif act == "gelu":       return nn.GELU()
        else: raise ValueError(f"Unknown act: {act}")

    dims   = [in_dim] + [hidden] * (depth - 1) + [out_dim]
    layers = []
    for i in range(len(dims) - 1):
        linear = nn.Linear(dims[i], dims[i + 1])
        if weight_init == "small":
            nn.init.normal_(linear.weight, mean=0.0, std=0.01)
            nn.init.zeros_(linear.bias)
        else:  # kaiming
            nn.init.kaiming_uniform_(linear.weight, a=math.sqrt(5))
            fan_in, _ = nn.init._calculate_fan_in_and_fan_out(linear.weight)
            bound = 1 / math.sqrt(fan_in) if fan_in > 0 else 0
            nn.init.uniform_(linear.bias, -bound, bound)
        layers.append(linear)
        if i < len(dims) - 2:
            layers.append(make_act())
    return nn.Sequential(*layers)


# ──────────────────────────────────────────────────────────────────────────────
# Gradient Ratio & Evaluation
# ──────────────────────────────────────────────────────────────────────────────

def _get_linear_layers(model: nn.Module):
    return [m for m in model.modules() if isinstance(m, nn.Linear)]


def _grad_norm(layer: nn.Linear) -> float:
    if layer.weight.grad is None:
        return 1e-12
    return layer.weight.grad.norm().item() + 1e-12


def measure_grad_ratio(model: nn.Module, loader: DataLoader, criterion: nn.Module, device: torch.device) -> float:
    """Compute |∇W_first_linear| / |∇W_last_hidden_linear| on one batch."""
    model.train()
    model.zero_grad()
    xb, yb = next(iter(loader))
    xb, yb = xb.to(device), yb.to(device)
    loss = criterion(model(xb), yb)
    loss.backward()
    linears = _get_linear_layers(model)
    if len(linears) < 2:
        model.zero_grad()
        return 1.0
    ratio = _grad_norm(linears[0]) / _grad_norm(linears[-2])
    model.zero_grad()
    return ratio


def evaluate(model: nn.Module, loader: DataLoader, device: torch.device) -> float:
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for xb, yb in loader:
            xb, yb = xb.to(device), yb.to(device)
            preds   = model(xb).argmax(dim=-1)
            correct += (preds == yb).sum().item()
            total   += len(yb)
    return correct / total


def measure_activation_magnitudes(model: nn.Module, loader: DataLoader, device: torch.device):
    """Record mean absolute activation after each Linear layer (one batch)."""
    model.eval()
    mags = []
    hooks = []

    def _hook(mod, inp, out, container=mags):
        container.append(out.detach().abs().mean().item())

    for m in model.modules():
        if isinstance(m, nn.Linear):
            hooks.append(m.register_forward_hook(_hook))

    xb, yb = next(iter(loader))
    with torch.no_grad():
        model(xb.to(device))
    for h in hooks:
        h.remove()
    return mags


# ──────────────────────────────────────────────────────────────────────────────
# Training Loop
# ──────────────────────────────────────────────────────────────────────────────

def train_model(
    model: nn.Module,
    train_loader: DataLoader,
    test_loader:  DataLoader,
    n_epochs: int  = 25,
    lr: float      = 1e-3,
    grad_clip: float = 1.0,
    device: torch.device = DEVICE,
    label: str = "",
) -> dict:
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=n_epochs)
    criterion = nn.CrossEntropyLoss()

    model.to(device)

    results = dict(
        test_acc_per_epoch=[],
        grad_ratio_per_epoch=[],
        j_s_bar_per_epoch=[],
        ift_triggered_total=0,
        activation_magnitudes_epoch1=None,
        activation_magnitudes_epoch25=None,
    )

    cwa_layers = [m for m in model.modules() if isinstance(m, CWALayer)]

    t0 = time.time()
    for epoch in range(n_epochs):
        model.train()
        for xb, yb in train_loader:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad()
            out = model(xb)
            if isinstance(out, (list, tuple)):
                logits = out[0]
            else:
                logits = out
            loss = criterion(logits, yb)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), grad_clip)
            optimizer.step()
        scheduler.step()

        # Activation magnitudes on epoch 1 and epoch 25
        if epoch == 0:
            results["activation_magnitudes_epoch1"] = measure_activation_magnitudes(model, train_loader, device)
        if epoch == n_epochs - 1:
            results["activation_magnitudes_epoch25"] = measure_activation_magnitudes(model, train_loader, device)

        # Gradient ratio
        grad_ratio = measure_grad_ratio(model, train_loader, criterion, device)

        # CWA stats
        j_s_bar_epoch = float(np.mean([c.last_j_s_bar for c in cwa_layers])) if cwa_layers else 0.0
        ift_total_epoch = sum(c.last_ift_triggered for c in cwa_layers)
        results["ift_triggered_total"] += ift_total_epoch
        for c in cwa_layers:
            c.last_ift_triggered = 0

        # Test accuracy
        acc = evaluate(model, test_loader, device)

        results["test_acc_per_epoch"].append(acc)
        results["grad_ratio_per_epoch"].append(grad_ratio)
        results["j_s_bar_per_epoch"].append(j_s_bar_epoch)

        elapsed = time.time() - t0
        logger.info(
            f"[{label}] epoch {epoch+1}/{n_epochs}: acc={acc:.4f} "
            f"grad_ratio={grad_ratio:.3f} j_s_bar={j_s_bar_epoch:.4f} "
            f"ift={ift_total_epoch} elapsed={elapsed:.0f}s"
        )

    results["final_test_acc"] = results["test_acc_per_epoch"][-1]
    results["max_j_s_bar_achieved"] = max(results["j_s_bar_per_epoch"]) if results["j_s_bar_per_epoch"] else 0.0
    return results


# ──────────────────────────────────────────────────────────────────────────────
# Sub-Exp A: Small-Weight Init
# ──────────────────────────────────────────────────────────────────────────────

SEEDS = [42, 123, 777]


def run_sub_exp_A(train_loader, test_loader, device, n_epochs=25) -> list:
    logger.info("=== SUB-EXP A: Small-weight initialization ===")
    results_A = []

    conditions_A = [
        ("cwa_small_init",   "cwa",  "small"),
        ("gelu_small_init",  "gelu", "small"),
        ("cwa_kaiming_init", "cwa",  "kaiming"),
    ]

    for seed in SEEDS:
        for cond_name, act, w_init in conditions_A:
            logger.info(f"Sub-Exp A | seed={seed} | cond={cond_name}")
            torch.manual_seed(seed)
            np.random.seed(seed)

            model = build_mlp(depth=10, hidden=256, act=act, weight_init=w_init, K_max=50)
            res = train_model(
                model, train_loader, test_loader,
                n_epochs=n_epochs, lr=1e-3, grad_clip=1.0,
                device=device,
                label=f"A/{cond_name}/s{seed}",
            )
            del model
            torch.cuda.empty_cache() if HAS_GPU else None
            gc.collect()

            results_A.append({
                "sub_exp": "A_small_weight_init",
                "condition": cond_name,
                "seed": seed,
                "final_test_acc": res["final_test_acc"],
                "j_s_bar_trajectory": res["j_s_bar_per_epoch"],
                "max_j_s_bar_achieved": res["max_j_s_bar_achieved"],
                "ift_triggered_total": res["ift_triggered_total"],
                "grad_ratio_trajectory": res["grad_ratio_per_epoch"],
                "test_acc_trajectory": res["test_acc_per_epoch"],
                "activation_magnitudes_epoch1":  res["activation_magnitudes_epoch1"],
                "activation_magnitudes_epoch25": res["activation_magnitudes_epoch25"],
            })

    return results_A


# ──────────────────────────────────────────────────────────────────────────────
# Sub-Exp B: Constant-Shift Ablation
# ──────────────────────────────────────────────────────────────────────────────

def run_sub_exp_B(train_loader, test_loader, device, n_epochs=25) -> list:
    logger.info("=== SUB-EXP B: Constant-shift ablation ===")
    results_B = []

    conditions_B = [
        ("cwa_full",       "cwa"),
        ("cwa_shift_only", "shift_only"),
        ("pure_tanh",      "tanh"),
    ]

    for seed in SEEDS:
        for cond_name, act in conditions_B:
            logger.info(f"Sub-Exp B | seed={seed} | cond={cond_name}")
            torch.manual_seed(seed)
            np.random.seed(seed)

            model = build_mlp(depth=10, hidden=256, act=act, weight_init="kaiming", K_max=50)
            res = train_model(
                model, train_loader, test_loader,
                n_epochs=n_epochs, lr=1e-3, grad_clip=1.0,
                device=device,
                label=f"B/{cond_name}/s{seed}",
            )
            del model
            torch.cuda.empty_cache() if HAS_GPU else None
            gc.collect()

            final_grad_ratio = res["grad_ratio_per_epoch"][-1]
            results_B.append({
                "sub_exp": "B_shift_ablation",
                "condition": cond_name,
                "seed": seed,
                "final_test_acc": res["final_test_acc"],
                "grad_ratio_abs_deviation": abs(final_grad_ratio - 1.0),
                "grad_ratio_trajectory": res["grad_ratio_per_epoch"],
                "test_acc_trajectory": res["test_acc_per_epoch"],
                "j_s_bar_trajectory": res.get("j_s_bar_per_epoch", [0.0] * n_epochs),
                "ift_triggered_total": res.get("ift_triggered_total", 0),
                "activation_magnitudes_epoch1":  res["activation_magnitudes_epoch1"],
                "activation_magnitudes_epoch25": res["activation_magnitudes_epoch25"],
            })

    return results_B


# ──────────────────────────────────────────────────────────────────────────────
# Statistical Analysis
# ──────────────────────────────────────────────────────────────────────────────

def aggregate_results(records: list, sub_exp_name: str, metric: str = "final_test_acc") -> dict:
    by_cond = defaultdict(list)
    for r in records:
        if r["sub_exp"] == sub_exp_name:
            by_cond[r["condition"]].append(r[metric])

    out = {}
    for cond, vals in by_cond.items():
        vals_arr = np.array(vals)
        n    = len(vals_arr)
        mean = float(np.mean(vals_arr))
        std  = float(np.std(vals_arr, ddof=1)) if n > 1 else 0.0
        if n > 1:
            se     = std / math.sqrt(n)
            t_crit = stats.t.ppf(0.975, df=n - 1)
            ci     = (mean - t_crit * se, mean + t_crit * se)
        else:
            ci = (mean, mean)
        out[cond] = {"mean": mean, "std": std, "ci_95": list(ci), "n": n, "values": list(vals_arr)}
    return out


def paired_ttest(records: list, sub_exp: str, cond_a: str, cond_b: str, metric: str = "final_test_acc") -> dict:
    a = [r[metric] for r in records if r["sub_exp"] == sub_exp and r["condition"] == cond_a]
    b = [r[metric] for r in records if r["sub_exp"] == sub_exp and r["condition"] == cond_b]
    if len(a) == len(b) and len(a) >= 2:
        t_stat, p_val = stats.ttest_rel(a, b)
        return {"t_stat": float(t_stat), "p_val": float(p_val), "n_pairs": len(a)}
    return {"t_stat": None, "p_val": None, "n_pairs": len(a)}


def determine_mechanistic_verdict(agg_B: dict, agg_A: dict) -> dict:
    cwa_full_acc   = agg_B.get("cwa_full",       {}).get("mean", 0.0)
    shift_only_acc = agg_B.get("cwa_shift_only", {}).get("mean", 0.0)
    tanh_acc       = agg_B.get("pure_tanh",       {}).get("mean", 0.0)

    THRESH = 0.005
    if abs(shift_only_acc - cwa_full_acc) <= THRESH:
        verdict_B = "bias_dominant"
    elif shift_only_acc > cwa_full_acc + THRESH:
        verdict_B = "coupling_harmful"
    elif abs(shift_only_acc - tanh_acc) <= THRESH:
        verdict_B = "capacity_only"
    else:
        verdict_B = "ambiguous"

    descriptions = {
        "bias_dominant":     "Coupling loss is entirely from mean shift; fixed-point adds no value.",
        "coupling_harmful":  "Iterative feedback actively hurts; one-shot shift is better.",
        "capacity_only":     "Shift has no effect; accuracy gap is pure capacity/optimization.",
        "ambiguous":         "No clear verdict; intermediate regime.",
    }

    # Sub-Exp A: check small-init criticality
    cwa_small_jsbar = agg_A.get("cwa_small_init", {}).get("mean", 0.0)
    if cwa_small_jsbar > 0.7:
        verdict_A = "init_unlocks_criticality"
    else:
        verdict_A = "init_does_not_help"

    return {
        "sub_exp_B_verdict":     verdict_B,
        "sub_exp_B_description": descriptions.get(verdict_B, ""),
        "sub_exp_A_verdict":     verdict_A,
    }


# ──────────────────────────────────────────────────────────────────────────────
# Smoke Test
# ──────────────────────────────────────────────────────────────────────────────

def smoke_test(device):
    logger.info("--- Smoke Test ---")

    # 1. CWA forward
    layer = CWALayer(K_max=50).to(device)
    x = torch.randn(4, 32, device=device)
    y, j_s_bar, ift = CWAFunction.apply(x, layer.J_raw, 50)
    assert y.shape == (4, 32), f"Expected (4,32), got {y.shape}"
    assert 0.0 < j_s_bar.item() < 1.0, f"j_s_bar={j_s_bar.item()} out of range"
    y.sum().backward()
    assert layer.J_raw.grad is not None and layer.J_raw.grad.abs().item() > 0, "J_raw.grad is zero"
    logger.info(f"  CWA forward OK — j_s_bar={j_s_bar.item():.4f}")

    # 2. CWA-ShiftOnly no-param check
    shift_layer = CWAShiftOnlyLayer().to(device)
    x2 = torch.randn(4, 32, device=device, requires_grad=True)
    y2 = shift_layer(x2)
    assert list(shift_layer.parameters()) == [], "CWAShiftOnly should have no parameters"
    y2.sum().backward()
    assert x2.grad is not None, "Input x2 should still receive gradient"
    logger.info("  CWAShiftOnly no-param OK")

    # 3. MLP build checks
    m_cwa   = build_mlp(depth=10, hidden=32, act="cwa")
    m_shift = build_mlp(depth=10, hidden=32, act="shift_only")
    m_tanh  = build_mlp(depth=10, hidden=32, act="tanh")
    n_cwa   = sum(1 for m in m_cwa.modules()   if isinstance(m, CWALayer))
    n_shift = sum(1 for m in m_shift.modules() if isinstance(m, CWAShiftOnlyLayer))
    n_tanh  = sum(1 for m in m_tanh.modules()  if isinstance(m, nn.Tanh))
    assert n_cwa   == 9, f"Expected 9 CWA layers, got {n_cwa}"
    assert n_shift == 9, f"Expected 9 ShiftOnly layers, got {n_shift}"
    assert n_tanh  == 9, f"Expected 9 Tanh layers, got {n_tanh}"
    logger.info(f"  MLP build OK — cwa:{n_cwa} shift:{n_shift} tanh:{n_tanh}")

    # 4. Small-init weight std
    m_small = build_mlp(depth=10, hidden=32, act="cwa", weight_init="small")
    linears = [m for m in m_small.modules() if isinstance(m, nn.Linear)]
    std_val = linears[0].weight.std().item()
    assert abs(std_val - 0.01) < 0.005, f"small init std={std_val:.4f} expected ~0.01"
    logger.info(f"  Small init std={std_val:.5f} OK")

    logger.info("--- Smoke Test PASSED ---")


# ──────────────────────────────────────────────────────────────────────────────
# Output
# ──────────────────────────────────────────────────────────────────────────────

def write_method_out(results_A: list, results_B: list, out_path: str = "method_out.json"):
    all_records = results_A + results_B

    agg_B      = aggregate_results(all_records, "B_shift_ablation",    "final_test_acc")
    agg_A_acc  = aggregate_results(all_records, "A_small_weight_init", "final_test_acc")
    agg_A_jsbar = aggregate_results(all_records, "A_small_weight_init", "max_j_s_bar_achieved")
    agg_grad_B = aggregate_results(all_records, "B_shift_ablation",    "grad_ratio_abs_deviation")

    # Max j_s_bar per condition (sub-exp A)
    max_jsbar_by_cond = defaultdict(list)
    for r in results_A:
        max_jsbar_by_cond[r["condition"]].append(r["max_j_s_bar_achieved"])
    max_jsbar_summary = {
        k: {"mean": float(np.mean(v)), "max": float(np.max(v)), "values": list(v)}
        for k, v in max_jsbar_by_cond.items()
    }

    # Pairwise t-tests sub-exp B
    ttest_full_vs_shift  = paired_ttest(all_records, "B_shift_ablation", "cwa_full",       "cwa_shift_only")
    ttest_shift_vs_tanh  = paired_ttest(all_records, "B_shift_ablation", "cwa_shift_only", "pure_tanh")
    ttest_full_vs_tanh   = paired_ttest(all_records, "B_shift_ablation", "cwa_full",       "pure_tanh")

    verdict = determine_mechanistic_verdict(agg_B, agg_A_jsbar)

    summary_meta = {
        "sub_exp_A": {
            "accuracy_by_condition":      agg_A_acc,
            "max_j_s_bar_by_condition":   max_jsbar_summary,
            "j_s_bar_trajectory_small_init": [
                r["j_s_bar_trajectory"]
                for r in results_A if r["condition"] == "cwa_small_init"
            ],
            "verdict": verdict["sub_exp_A_verdict"],
        },
        "sub_exp_B": {
            "accuracy_by_condition":                  agg_B,
            "grad_ratio_abs_deviation_by_condition":  agg_grad_B,
            "pairwise_ttests": {
                "cwa_full_vs_shift_only":      ttest_full_vs_shift,
                "cwa_shift_only_vs_pure_tanh": ttest_shift_vs_tanh,
                "cwa_full_vs_pure_tanh":       ttest_full_vs_tanh,
            },
            "verdict": verdict["sub_exp_B_verdict"],
            "verdict_description": verdict["sub_exp_B_description"],
        },
        "mechanistic_interpretation": verdict["sub_exp_B_verdict"],
        "mechanistic_description":    verdict["sub_exp_B_description"],
    }

    # Build schema-compliant exp_gen_sol_out format
    # Each record → one example with input (condition description) and output (result)
    def record_to_example(r: dict) -> dict:
        ex = {
            "input": (
                f"sub_exp={r['sub_exp']} condition={r['condition']} seed={r['seed']} "
                f"weight_init={'small' if 'small_init' in r['condition'] else 'kaiming'} "
                f"activation={r['condition'].replace('_small_init','').replace('_kaiming_init','').replace('_shift_only','_ShiftOnly')}"
            ),
            "output": (
                f"final_test_acc={r['final_test_acc']:.4f} "
                f"max_j_s_bar={r.get('max_j_s_bar_achieved', 0.0):.4f} "
                f"ift_triggered={r.get('ift_triggered_total', 0)} "
                f"grad_ratio_dev={r.get('grad_ratio_abs_deviation', abs(r['grad_ratio_trajectory'][-1] - 1.0)):.4f}"
            ),
            "metadata_sub_exp":             r["sub_exp"],
            "metadata_condition":           r["condition"],
            "metadata_seed":                str(r["seed"]),
            "metadata_final_test_acc":      str(round(r["final_test_acc"], 6)),
            "metadata_max_j_s_bar":         str(round(r.get("max_j_s_bar_achieved", 0.0), 6)),
            "metadata_ift_triggered_total": str(r.get("ift_triggered_total", 0)),
            "metadata_grad_ratio_final":    str(round(r["grad_ratio_trajectory"][-1], 6)),
            "metadata_test_acc_trajectory": json.dumps(r["test_acc_trajectory"]),
            "metadata_j_s_bar_trajectory":  json.dumps(r["j_s_bar_trajectory"]),
        }
        if r.get("grad_ratio_abs_deviation") is not None:
            ex["metadata_grad_ratio_abs_deviation"] = str(round(r["grad_ratio_abs_deviation"], 6))
        return ex

    output = {
        "metadata": {
            "title": "CWA Mechanistic Sub-Experiments: Small-Init and Shift Ablation",
            "summary": summary_meta,
            "n_epochs": 25,
            "n_seeds": 3,
            "architecture": "10-layer unnormalized MLP, hidden=256, CIFAR-10",
        },
        "datasets": [
            {
                "dataset": "CIFAR-10",
                "examples": [record_to_example(r) for r in all_records],
            }
        ],
    }

    out_file = Path(out_path)
    out_file.write_text(json.dumps(output, indent=2))
    logger.info(f"Written {out_file} ({out_file.stat().st_size / 1024:.1f} KB)")
    return output


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────

@logger.catch(reraise=True)
def main(n_epochs: int = 25, smoke_only: bool = False):
    logger.info(f"Starting CWA Mechanistic Sub-Experiments (n_epochs={n_epochs})")

    smoke_test(DEVICE)
    if smoke_only:
        logger.info("Smoke-only mode, exiting.")
        return

    train_loader, test_loader = get_cifar10_loaders(batch_size=256)
    logger.info("CIFAR-10 loaders ready")

    results_A = run_sub_exp_A(train_loader, test_loader, DEVICE, n_epochs=n_epochs)
    results_B = run_sub_exp_B(train_loader, test_loader, DEVICE, n_epochs=n_epochs)

    out = write_method_out(results_A, results_B)
    logger.info("DONE")
    return out


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=25)
    parser.add_argument("--smoke",  action="store_true", help="Run smoke test only")
    parser.add_argument("--mini",   action="store_true", help="Run 3-epoch mini test")
    args = parser.parse_args()

    if args.smoke:
        main(n_epochs=1, smoke_only=True)
    elif args.mini:
        main(n_epochs=3)
    else:
        main(n_epochs=args.epochs)
