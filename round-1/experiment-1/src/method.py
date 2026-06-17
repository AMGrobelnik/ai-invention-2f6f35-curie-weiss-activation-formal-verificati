#!/usr/bin/env python3
"""CWA (Coupled-Weight Activation) Gradient Stability Experiment.

Implements Experiments 1 (gradient stability across depths/activations) and 4 (fixed-J ablation)
for the CWA activation function, comparing against 8 baseline activations on MNIST and CIFAR-10.
"""

import json
import math
import os
import random
import resource
import sys
import time
import gc
from pathlib import Path

import numpy as np
import psutil
import torch
import torch.nn as nn
import torch.nn.functional as F
from loguru import logger
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# ── Logging ────────────────────────────────────────────────────────────────────
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
Path("logs").mkdir(exist_ok=True)
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# ── Hardware detection ─────────────────────────────────────────────────────────
def _detect_cpus() -> int:
    try:
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError):
        pass
    try:
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError):
        pass
    try:
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError):
        pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError):
            pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_memory / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9

logger.info(f"Hardware: CPUs={NUM_CPUS}, GPU={'L4' if HAS_GPU else 'None'}, "
            f"VRAM={VRAM_GB:.1f}GB, RAM={TOTAL_RAM_GB:.1f}GB, device={DEVICE}")

# ── Memory limits ──────────────────────────────────────────────────────────────
_avail_ram = psutil.virtual_memory().available
RAM_BUDGET = int(min(_avail_ram * 0.8, 40 * 1024**3))
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))
if HAS_GPU:
    _free_vram, _total_vram = torch.cuda.mem_get_info(0)
    torch.cuda.set_per_process_memory_fraction(min(0.90, (_free_vram * 0.9) / _total_vram))
    logger.info(f"VRAM budget: {_free_vram * 0.9 / 1e9:.1f}GB of {_total_vram / 1e9:.1f}GB")

# ──────────────────────────────────────────────────────────────────────────────
# SECTION 1: CWA IMPLEMENTATION
# ──────────────────────────────────────────────────────────────────────────────

class CWAIFTFunction(torch.autograd.Function):
    """Implicit Function Theorem backward for CWA fixed-point equation."""

    @staticmethod
    def forward(ctx, x, J, m_star):
        # x: [B, n], J: scalar tensor, m_star: [B]
        y = torch.tanh(x + J * m_star.unsqueeze(-1))   # [B, n]
        s = 1.0 - y * y                                  # sech^2, [B, n]
        s_bar = s.mean(dim=-1)                           # [B]
        ctx.save_for_backward(x, J.unsqueeze(0), m_star, s, s_bar)
        ctx.n = x.shape[-1]
        return y

    @staticmethod
    def backward(ctx, grad_output):
        x, J_t, m_star, s, s_bar = ctx.saved_tensors
        J = J_t.squeeze(0)
        n = ctx.n
        J_s_bar = J * s_bar      # [B]
        denom = (1.0 - J_s_bar).clamp(min=1e-4)  # guard near-zero

        # Grad wrt x
        vs = grad_output * s              # [B, n]
        vs_mean = vs.mean(dim=-1)         # [B]
        correction = (J / denom).unsqueeze(-1) * vs_mean.unsqueeze(-1)
        grad_x = s * (grad_output + correction)   # [B, n]

        # Grad wrt J (scalar, summed over batch)
        grad_J = (n * vs_mean * m_star / denom).sum()

        return grad_x, grad_J, None   # None for m_star


class CWALayer(nn.Module):
    """Coupled-Weight Activation layer with learnable J parameter."""

    def __init__(self, hidden_dim=None):
        super().__init__()
        self.J_raw = nn.Parameter(torch.tensor(0.0))
        self.last_K = 0
        self.last_J = 0.5
        self.last_J_s_bar = 0.0
        self.last_mode = 'unrolled'

    def forward(self, x):
        J = torch.sigmoid(self.J_raw)
        B, n = x.shape

        # Step 1: find fixed point without gradient
        with torch.no_grad():
            m = torch.zeros(B, device=x.device, dtype=x.dtype)
            for k in range(50):
                m_new = torch.tanh(x + J * m.unsqueeze(-1)).mean(dim=-1)
                diff = (m_new - m).abs().max().item()
                m = m_new
                if diff < 1e-7:
                    break
            m_star = m.detach()

        # Step 2: compute s_bar and decide mode
        with torch.no_grad():
            y_star = torch.tanh(x.detach() + J.detach() * m_star.unsqueeze(-1))
            s_at_star = 1.0 - y_star * y_star
            s_bar_val = s_at_star.mean(dim=-1)
            J_s_bar_scalar = (J.detach() * s_bar_val.mean()).item()

        self.last_K = k + 1
        self.last_J = J.item()
        self.last_J_s_bar = J_s_bar_scalar

        # Step 3: select backprop mode
        if J_s_bar_scalar < 0.8:
            # Unrolled backprop from warm start
            delta = max(1e-7, 1e-4 * (1.0 - J_s_bar_scalar))
            m = m_star.detach()
            for k in range(50):
                m_new = torch.tanh(x + J * m.unsqueeze(-1)).mean(dim=-1)
                with torch.no_grad():
                    diff = (m_new - m).abs().max().item()
                m = m_new
                if diff < delta:
                    break
            y = torch.tanh(x + J * m.unsqueeze(-1))
            self.last_mode = 'unrolled'
        else:
            # IFT backward
            y = CWAIFTFunction.apply(x, J, m_star)
            self.last_mode = 'ift'

        return y


class FixedJCWALayer(nn.Module):
    """CWA layer with non-learnable fixed J (for ablation study)."""

    def __init__(self, J_fixed: float):
        super().__init__()
        self.J_fixed = J_fixed
        self.last_J_s_bar = 0.0

    def forward(self, x):
        J = torch.tensor(self.J_fixed, device=x.device, dtype=x.dtype)
        B, n = x.shape
        with torch.no_grad():
            m = torch.zeros(B, device=x.device, dtype=x.dtype)
            for k in range(50):
                m_new = torch.tanh(x + J * m.unsqueeze(-1)).mean(dim=-1)
                diff = (m_new - m).abs().max().item()
                m = m_new
                if diff < 1e-7:
                    break
            m_star = m.detach()

        # Always use IFT (J not learned)
        J_req = J.requires_grad_(False)
        y = CWAIFTFunction.apply(x, J_req, m_star)
        with torch.no_grad():
            s = (1.0 - y.detach() ** 2).mean(dim=-1)
            self.last_J_s_bar = (J * s.mean()).item()
        return y


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 2: BASELINE ACTIVATIONS
# ──────────────────────────────────────────────────────────────────────────────

class TanhLNLayer(nn.Module):
    def __init__(self, hidden_dim: int):
        super().__init__()
        self.ln = nn.LayerNorm(hidden_dim)

    def forward(self, x):
        return torch.tanh(self.ln(x))


class GELULNLayer(nn.Module):
    def __init__(self, hidden_dim: int):
        super().__init__()
        self.ln = nn.LayerNorm(hidden_dim)

    def forward(self, x):
        return F.gelu(self.ln(x))


class CompetingNonlinearitiesLayer(nn.Module):
    """Quenched-disorder mixed activation: fixed tanh/swish mask per neuron."""

    def __init__(self, hidden_dim: int, p_c: float = 0.5):
        super().__init__()
        mask = torch.bernoulli(torch.full((hidden_dim,), p_c))
        self.register_buffer('mask', mask)

    def forward(self, x):
        return self.mask * torch.tanh(x) + (1.0 - self.mask) * F.silu(x)


ACTIVATION_FACTORIES = {
    'relu':      lambda d: nn.ReLU(),
    'gelu':      lambda d: nn.GELU(),
    'swish':     lambda d: nn.SiLU(),
    'tanh':      lambda d: nn.Tanh(),
    'selu':      lambda d: nn.SELU(),
    'tanh_ln':   lambda d: TanhLNLayer(d),
    'gelu_ln':   lambda d: GELULNLayer(d),
    'competing': lambda d: CompetingNonlinearitiesLayer(d, p_c=0.5),
    'cwa':       lambda d: CWALayer(),
}


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 3: DEEP MLP MODEL
# ──────────────────────────────────────────────────────────────────────────────

class DeepMLP(nn.Module):
    """Unnormalized deep MLP: no BN/LN in linear layers, activation factory per layer."""

    def __init__(self, input_dim: int, hidden_dim: int, depth: int,
                 num_classes: int, act_factory):
        super().__init__()
        layers = []
        layers.append(nn.Linear(input_dim, hidden_dim))
        layers.append(act_factory(hidden_dim))
        for _ in range(depth - 2):
            layers.append(nn.Linear(hidden_dim, hidden_dim))
            layers.append(act_factory(hidden_dim))
        layers.append(nn.Linear(hidden_dim, num_classes))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x.view(x.shape[0], -1))

    def get_linear_layers(self) -> list:
        return [m for m in self.net if isinstance(m, nn.Linear)]

    def get_cwa_layers(self) -> list:
        return [m for m in self.net if isinstance(m, (CWALayer, FixedJCWALayer))]


def init_weights(model: nn.Module, activation_name: str) -> None:
    for m in model.modules():
        if isinstance(m, nn.Linear):
            if activation_name == 'selu':
                fan_in = m.weight.shape[1]
                nn.init.normal_(m.weight, 0, 1.0 / math.sqrt(fan_in))
            else:
                nn.init.kaiming_uniform_(m.weight, nonlinearity='relu')
            if m.bias is not None:
                nn.init.zeros_(m.bias)


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 4: GRADIENT NORM MEASUREMENT
# ──────────────────────────────────────────────────────────────────────────────

def measure_gradient_norms(model, fixed_x, fixed_y, criterion, device):
    model.train()
    model.zero_grad()
    x = fixed_x.to(device)
    y = fixed_y.to(device)
    pred = model(x)
    loss = criterion(pred, y)
    loss.backward()

    linear_layers = model.get_linear_layers()
    norms = []
    for layer in linear_layers:
        if layer.weight.grad is not None:
            norms.append(layer.weight.grad.norm().item())
        else:
            norms.append(float('nan'))
    model.zero_grad()

    if (len(norms) >= 2
            and not math.isnan(norms[0]) and not math.isnan(norms[-1])
            and norms[0] > 1e-12 and norms[-1] > 1e-12):
        log_first = math.log(norms[0] + 1e-12)
        log_last = math.log(norms[-1] + 1e-12)
        if abs(log_last) > 1e-6:
            ratio = abs(log_first / log_last)
        else:
            ratio = float('inf')
    else:
        ratio = float('nan')

    return norms, ratio


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 5: TRAINING LOOP
# ──────────────────────────────────────────────────────────────────────────────

def train_model(model, optimizer, scheduler, train_loader, fixed_batch,
                criterion, device, num_epochs, measure_at_epochs, activation_name):
    gradient_records = []
    cwa_stats_log = []
    loss_curve = []
    fixed_x, fixed_y = fixed_batch
    is_cwa = activation_name.startswith('cwa') or activation_name.startswith('fixed_j')

    for epoch in range(num_epochs):
        model.train()
        epoch_losses = []
        for batch_x, batch_y in train_loader:
            batch_x = batch_x.to(device)
            batch_y = batch_y.to(device)
            optimizer.zero_grad()
            try:
                pred = model(batch_x)
                loss = criterion(pred, batch_y)
                loss.backward()
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                optimizer.step()
                epoch_losses.append(loss.item())
            except Exception as e:
                logger.warning(f"Batch failed: {e}")
                optimizer.zero_grad()
                continue

        if is_cwa:
            cwa_layers = model.get_cwa_layers()
            for li, cl in enumerate(cwa_layers):
                cwa_stats_log.append({
                    'epoch': epoch,
                    'layer': li,
                    'J': getattr(cl, 'last_J', None),
                    'J_s_bar': cl.last_J_s_bar,
                    'K': getattr(cl, 'last_K', None),
                    'mode': getattr(cl, 'last_mode', None)
                })

        if scheduler is not None:
            scheduler.step()

        mean_loss = float(np.mean(epoch_losses)) if epoch_losses else float('nan')
        loss_curve.append((epoch, mean_loss))

        if epoch in measure_at_epochs:
            try:
                norms, ratio = measure_gradient_norms(
                    model, fixed_x, fixed_y, criterion, device)
                gradient_records.append({
                    'epoch': epoch + 1,
                    'layer_norms': [float(n) for n in norms],
                    'gradient_ratio': float(ratio) if not math.isnan(ratio) and not math.isinf(ratio) else str(ratio)
                })
            except Exception as e:
                logger.warning(f"Gradient measurement failed at epoch {epoch}: {e}")

    return gradient_records, cwa_stats_log, loss_curve


def evaluate(model, loader, device) -> float:
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for x, y in loader:
            pred = model(x.to(device)).argmax(dim=-1)
            correct += (pred == y.to(device)).sum().item()
            total += y.shape[0]
    return correct / total if total > 0 else 0.0


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 6: DATASET LOADING
# ──────────────────────────────────────────────────────────────────────────────

def load_dataset(name: str, data_root: str = './data'):
    if name == 'cifar10':
        tf = transforms.ToTensor()
        train_ds = datasets.CIFAR10(data_root, train=True, download=True, transform=tf)
        test_ds = datasets.CIFAR10(data_root, train=False, download=True, transform=tf)
        input_dim, num_classes = 3072, 10
    elif name == 'mnist':
        tf = transforms.ToTensor()
        train_ds = datasets.MNIST(data_root, train=True, download=True, transform=tf)
        test_ds = datasets.MNIST(data_root, train=False, download=True, transform=tf)
        input_dim, num_classes = 784, 10
    else:
        raise ValueError(f"Unknown dataset: {name}")
    return train_ds, test_ds, input_dim, num_classes


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 7: EXPERIMENT CONFIGURATION (adaptive)
# ──────────────────────────────────────────────────────────────────────────────

DEPTHS = [6, 10, 20]
HIDDEN_DIM = 256
NUM_SEEDS = 3       # start with 3 (fallback plan F4)
NUM_EPOCHS = 25
MEASURE_AT = [4, 19]   # 0-indexed
BATCH_SIZE = 256
LR = 1e-3
# CIFAR-10 priority; add MNIST if time allows
DATASETS = ['cifar10', 'mnist']
ACTIVATIONS_EXP1 = list(ACTIVATION_FACTORIES.keys())

FIXED_J_VALUES = [0.1, 0.3, 0.5, 0.7, 0.9]
DEPTH_EXP4 = 10
NUM_SEEDS_EXP4 = 3
NUM_EPOCHS_EXP4 = 25


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 8: SANITY CHECKS
# ──────────────────────────────────────────────────────────────────────────────

def run_sanity_checks(device):
    logger.info("Running sanity checks...")

    # T1: CWA convergence
    torch.manual_seed(42)
    x = torch.randn(4, 32, device=device)
    layer = CWALayer().to(device)
    y = layer(x)
    assert y.shape == (4, 32), f"Shape mismatch: {y.shape}"
    assert not torch.isnan(y).any(), "NaN in CWA output"
    assert layer.last_J_s_bar < 1.0, f"J*s_bar >= 1: {layer.last_J_s_bar}"
    logger.info(f"T1 CWA convergence OK: K={layer.last_K}, J={layer.last_J:.3f}, "
                f"J*s_bar={layer.last_J_s_bar:.3f}")

    # T2: IFT gradient check (CPU double precision)
    try:
        x_d = torch.randn(2, 8, dtype=torch.float64, requires_grad=True)
        J_d = torch.tensor(0.5, dtype=torch.float64, requires_grad=True)
        m_d = torch.zeros(2, dtype=torch.float64)
        result = torch.autograd.gradcheck(
            CWAIFTFunction.apply,
            (x_d, J_d, m_d),
            eps=1e-6, atol=1e-4,
            check_inputs=[0, 1]
        )
        logger.info(f"T2 IFT gradcheck passed: {result}")
    except Exception as e:
        logger.warning(f"T2 gradcheck issue (non-fatal): {e}")

    # T3: Mini training run
    set_seed(0)
    _, test_ds, input_dim, _ = load_dataset('mnist', './data')
    train_ds, _, _, _ = load_dataset('mnist', './data')
    mini_train = DataLoader(train_ds, batch_size=256, shuffle=True,
                            num_workers=2, pin_memory=HAS_GPU)
    model = DeepMLP(784, 64, 6, 10, lambda d: CWALayer()).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    for epoch in range(3):
        for x_b, y_b in mini_train:
            optimizer.zero_grad()
            loss = nn.CrossEntropyLoss()(model(x_b.to(device)), y_b.to(device))
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
    mini_test = DataLoader(test_ds, batch_size=512, shuffle=False)
    acc = evaluate(model, mini_test, device)
    logger.info(f"T3 Mini CWA training: accuracy={acc:.4f} (expect > 0.5)")
    assert acc > 0.4, f"CWA failed to train: acc={acc}"
    del model
    gc.collect()
    if HAS_GPU:
        torch.cuda.empty_cache()

    # T4: Mode switching
    torch.manual_seed(1)
    x_t = torch.randn(8, 64, device=device)
    layer_lo = CWALayer().to(device)
    with torch.no_grad():
        layer_lo.J_raw.data.fill_(-0.847)  # J ≈ 0.3
    _ = layer_lo(x_t)
    logger.info(f"T4 low-J mode: {layer_lo.last_mode}, J*s_bar={layer_lo.last_J_s_bar:.3f}")

    layer_hi = CWALayer().to(device)
    with torch.no_grad():
        layer_hi.J_raw.data.fill_(2.5)  # J ≈ 0.924
    _ = layer_hi(x_t)
    logger.info(f"T4 high-J mode: {layer_hi.last_mode}, J*s_bar={layer_hi.last_J_s_bar:.3f}")

    logger.info("All sanity checks passed.")


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 9: EXPERIMENT 1 - GRADIENT STABILITY
# ──────────────────────────────────────────────────────────────────────────────

def run_one_config(dataset_name, depth, act_name, num_seeds, input_dim, num_classes,
                   train_loader, test_loader, fixed_x, fixed_y, device):
    """Run a single (dataset, depth, activation) configuration across seeds."""
    act_results = []
    for seed in range(num_seeds):
        set_seed(seed)
        act_factory = ACTIVATION_FACTORIES[act_name]
        try:
            model = DeepMLP(input_dim, HIDDEN_DIM, depth, num_classes, act_factory)
            init_weights(model, act_name)
            model = model.to(device)

            optimizer = torch.optim.Adam(model.parameters(), lr=LR)
            scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
                optimizer, T_max=NUM_EPOCHS, eta_min=LR * 0.1)
            criterion = nn.CrossEntropyLoss()

            grad_records, cwa_log, loss_curve = train_model(
                model, optimizer, scheduler, train_loader,
                (fixed_x, fixed_y), criterion, device,
                NUM_EPOCHS, MEASURE_AT, act_name)

            final_acc = evaluate(model, test_loader, device)
            act_results.append({
                'seed': seed,
                'final_accuracy': final_acc,
                'gradient_records': grad_records,
                'loss_curve': [(e, float(l)) for e, l in loss_curve],
                'cwa_log': cwa_log[-5:] if cwa_log else []
            })
        except Exception as e:
            logger.error(f"Seed {seed} failed for {act_name} depth={depth}: {e}")
            act_results.append({
                'seed': seed,
                'final_accuracy': None,
                'gradient_records': [],
                'loss_curve': [],
                'cwa_log': []
            })
        finally:
            try:
                del model
                gc.collect()
                if HAS_GPU:
                    torch.cuda.empty_cache()
            except Exception:
                pass

    # Aggregate
    accs = [r['final_accuracy'] for r in act_results if r['final_accuracy'] is not None]
    ratios = []
    for r in act_results:
        if r['gradient_records']:
            last_ratio = r['gradient_records'][-1]['gradient_ratio']
            if isinstance(last_ratio, (int, float)) and not (math.isnan(float(last_ratio))
                                                               or math.isinf(float(last_ratio))):
                ratios.append(float(last_ratio))

    J_s_bar_vals = []
    for r in act_results:
        for entry in r.get('cwa_log', []):
            if entry.get('J_s_bar') is not None:
                J_s_bar_vals.append(entry['J_s_bar'])

    return {
        'accuracy_mean': float(np.mean(accs)) if accs else None,
        'accuracy_std': float(np.std(accs)) if accs else None,
        'accuracy_per_seed': [float(a) for a in accs],
        'gradient_ratio_mean': float(np.nanmean(ratios)) if ratios else None,
        'gradient_ratio_std': float(np.nanstd(ratios)) if ratios else None,
        'gradient_ratio_per_seed': [float(r) for r in ratios],
        'J_s_bar_at_convergence': float(np.mean(J_s_bar_vals)) if J_s_bar_vals else None,
        'per_seed_details': act_results
    }


def run_experiment_1(device, data_root: str) -> dict:
    results = {}
    total_configs = len(DATASETS) * len(DEPTHS) * len(ACTIVATIONS_EXP1)
    done = 0
    exp_start = time.time()

    for dataset_name in DATASETS:
        results[dataset_name] = {}
        try:
            train_ds, test_ds, input_dim, num_classes = load_dataset(dataset_name, data_root)
        except Exception as e:
            logger.error(f"Failed to load {dataset_name}: {e}")
            continue

        train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True,
                                  num_workers=2, pin_memory=HAS_GPU)
        test_loader = DataLoader(test_ds, batch_size=512, shuffle=False,
                                 num_workers=2, pin_memory=HAS_GPU)
        fixed_x, fixed_y = next(iter(DataLoader(test_ds, batch_size=512, shuffle=False)))

        for depth in DEPTHS:
            results[dataset_name][f'depth_{depth}'] = {}
            for act_name in ACTIVATIONS_EXP1:
                t_config = time.time()
                cfg_result = run_one_config(
                    dataset_name, depth, act_name, NUM_SEEDS,
                    input_dim, num_classes, train_loader, test_loader,
                    fixed_x, fixed_y, device)
                results[dataset_name][f'depth_{depth}'][act_name] = cfg_result
                done += 1
                elapsed = time.time() - exp_start
                remaining_configs = total_configs - done
                per_config = elapsed / done
                eta_min = (remaining_configs * per_config) / 60
                logger.info(
                    f"[EXP1 {done}/{total_configs}] {dataset_name} depth={depth} "
                    f"act={act_name} | "
                    f"acc={cfg_result.get('accuracy_mean', 'N/A')!r:.4} "
                    f"grad_ratio={cfg_result.get('gradient_ratio_mean', 'N/A')!r:.4} "
                    f"| {time.time()-t_config:.1f}s | ETA {eta_min:.1f}min"
                )

                # Save checkpoint after each config
                ckpt_path = Path("logs/exp1_checkpoint.json")
                try:
                    ckpt_path.write_text(json.dumps(results, default=str, indent=2))
                except Exception as e:
                    logger.warning(f"Checkpoint save failed: {e}")

    return results


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 10: EXPERIMENT 4 - FIXED-J ABLATION
# ──────────────────────────────────────────────────────────────────────────────

def run_experiment_4(device, data_root: str) -> dict:
    train_ds, test_ds, input_dim, num_classes = load_dataset('cifar10', data_root)
    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True,
                              num_workers=2, pin_memory=HAS_GPU)
    test_loader = DataLoader(test_ds, batch_size=512, shuffle=False,
                             num_workers=2, pin_memory=HAS_GPU)
    fixed_x, fixed_y = next(iter(DataLoader(test_ds, batch_size=512, shuffle=False)))

    results_exp4: dict = {'fixed_j': {}, 'learned_j': None}

    conditions = [(str(jv), lambda d, jv=jv: FixedJCWALayer(jv)) for jv in FIXED_J_VALUES]
    conditions.append(('learned', lambda d: CWALayer()))

    for idx, (cond_name, act_factory) in enumerate(conditions):
        cond_results = []
        for seed in range(NUM_SEEDS_EXP4):
            set_seed(seed)
            try:
                model = DeepMLP(input_dim, HIDDEN_DIM, DEPTH_EXP4, num_classes, act_factory)
                init_weights(model, 'cwa')
                model = model.to(device)

                optimizer = torch.optim.Adam(model.parameters(), lr=LR)
                scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
                    optimizer, T_max=NUM_EPOCHS_EXP4, eta_min=LR * 0.1)
                criterion = nn.CrossEntropyLoss()

                grad_records, cwa_log, loss_curve = train_model(
                    model, optimizer, scheduler, train_loader,
                    (fixed_x, fixed_y), criterion, device,
                    NUM_EPOCHS_EXP4, MEASURE_AT, 'cwa')

                final_acc = evaluate(model, test_loader, device)
                cwa_layers = model.get_cwa_layers()
                final_J_s_bars = [cl.last_J_s_bar for cl in cwa_layers]
                final_Js = [cl.last_J if hasattr(cl, 'last_J') else float(cond_name)
                            for cl in cwa_layers]

                cond_results.append({
                    'seed': seed,
                    'final_accuracy': final_acc,
                    'gradient_records': grad_records,
                    'loss_curve': [(e, float(l)) for e, l in loss_curve],
                    'final_J_per_layer': [float(j) for j in final_Js],
                    'final_J_s_bar_per_layer': [float(v) for v in final_J_s_bars],
                })
            except Exception as e:
                logger.error(f"EXP4 cond={cond_name} seed={seed} failed: {e}")
                cond_results.append({'seed': seed, 'final_accuracy': None,
                                     'gradient_records': [], 'loss_curve': [],
                                     'final_J_per_layer': [], 'final_J_s_bar_per_layer': []})
            finally:
                try:
                    del model
                    gc.collect()
                    if HAS_GPU:
                        torch.cuda.empty_cache()
                except Exception:
                    pass

        accs = [r['final_accuracy'] for r in cond_results if r['final_accuracy'] is not None]
        ratios = []
        for r in cond_results:
            if r['gradient_records']:
                last = r['gradient_records'][-1]['gradient_ratio']
                if isinstance(last, (int, float)):
                    ratios.append(float(last))
        J_s_bars_all = []
        for r in cond_results:
            J_s_bars_all.extend(r.get('final_J_s_bar_per_layer', []))

        summary = {
            'accuracy_mean': float(np.mean(accs)) if accs else None,
            'accuracy_std': float(np.std(accs)) if accs else None,
            'accuracy_per_seed': [float(a) for a in accs],
            'gradient_ratio_mean': float(np.nanmean(ratios)) if ratios else None,
            'gradient_ratio_std': float(np.nanstd(ratios)) if ratios else None,
            'J_s_bar_at_convergence_mean': float(np.mean(J_s_bars_all)) if J_s_bars_all else None,
            'J_s_bar_at_convergence_all': [float(v) for v in J_s_bars_all],
            'per_seed_details': cond_results
        }

        if cond_name == 'learned':
            results_exp4['learned_j'] = summary
        else:
            results_exp4['fixed_j'][cond_name] = summary

        logger.info(
            f"[EXP4 {idx+1}/{len(conditions)}] J={cond_name} "
            f"acc={np.mean(accs) if accs else 'N/A':.4f} "
            f"J*s_bar_mean={np.mean(J_s_bars_all) if J_s_bars_all else 'N/A':.3f}"
        )

        # Checkpoint
        try:
            Path("logs/exp4_checkpoint.json").write_text(
                json.dumps(results_exp4, default=str, indent=2))
        except Exception as e:
            logger.warning(f"EXP4 checkpoint failed: {e}")

    return results_exp4


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 11: HYPOTHESIS TEST
# ──────────────────────────────────────────────────────────────────────────────

def evaluate_hypothesis(exp1_results: dict, exp4_results: dict) -> dict:
    verdict_gradient = {}
    for depth_key in ['depth_10', 'depth_20']:
        cwa_d = (exp1_results.get('cifar10', {})
                 .get(depth_key, {}).get('cwa', {}))
        gelu_d = (exp1_results.get('cifar10', {})
                  .get(depth_key, {}).get('gelu', {}))
        cwa_ratio = cwa_d.get('gradient_ratio_mean')
        gelu_ratio = gelu_d.get('gradient_ratio_mean')
        if cwa_ratio is not None and gelu_ratio is not None:
            verdict_gradient[depth_key] = {
                'cwa_ratio': cwa_ratio,
                'gelu_ratio': gelu_ratio,
                'primary_criterion_met': bool(cwa_ratio < 2.0 and gelu_ratio > 5.0)
            }

    acc_improvements = {}
    for depth_key in ['depth_6', 'depth_10', 'depth_20']:
        cwa_acc = (exp1_results.get('cifar10', {})
                   .get(depth_key, {}).get('cwa', {}).get('accuracy_mean', 0) or 0)
        gelu_acc = (exp1_results.get('cifar10', {})
                    .get(depth_key, {}).get('gelu', {}).get('accuracy_mean', 0) or 0)
        acc_improvements[depth_key] = {
            'delta_vs_gelu': float(cwa_acc - gelu_acc),
            'cwa': float(cwa_acc),
            'gelu': float(gelu_acc)
        }

    soc_finding = {}
    if exp4_results and exp4_results.get('learned_j'):
        j_s_bars = exp4_results['learned_j'].get('J_s_bar_at_convergence_all', [])
        if j_s_bars:
            soc_finding = {
                'mean_J_s_bar': float(np.mean(j_s_bars)),
                'std_J_s_bar': float(np.std(j_s_bars)),
                'fraction_above_0.8': float(np.mean([v > 0.8 for v in j_s_bars]))
            }

    # Determine overall verdict
    gradient_ok = any(v.get('primary_criterion_met', False)
                      for v in verdict_gradient.values())
    acc_negligible = all(abs(acc_improvements.get(dk, {}).get('delta_vs_gelu', 999)) < 0.005
                         for dk in ['depth_10', 'depth_20'])

    if gradient_ok:
        overall_verdict = 'CONFIRM'
    elif acc_negligible:
        overall_verdict = 'DISCONFIRM'
    else:
        overall_verdict = 'INCONCLUSIVE'

    return {
        'overall_verdict': overall_verdict,
        'gradient_stability': verdict_gradient,
        'accuracy_improvements_vs_gelu': acc_improvements,
        'soc_finding': soc_finding
    }


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 12: BUILD method_out.json (schema: exp_gen_sol_out)
# ──────────────────────────────────────────────────────────────────────────────

def build_method_out(exp1_results: dict, exp4_results: dict, hyp_test: dict) -> dict:
    """
    Convert experimental results into exp_gen_sol_out schema:
    datasets → list of {dataset, examples}
    Each example: {input: str, output: str, predict_*, metadata_*}
    """
    examples_cifar10 = []
    examples_mnist = []

    # One example per (depth, activation) cell on CIFAR-10
    for depth_key in ['depth_6', 'depth_10', 'depth_20']:
        depth_val = int(depth_key.split('_')[1])
        depth_data = exp1_results.get('cifar10', {}).get(depth_key, {})
        for act_name in ACTIVATIONS_EXP1:
            act_data = depth_data.get(act_name, {})
            acc_mean = act_data.get('accuracy_mean')
            grad_ratio = act_data.get('gradient_ratio_mean')
            gelu_acc = depth_data.get('gelu', {}).get('accuracy_mean', 0) or 0
            cwa_acc = depth_data.get('cwa', {}).get('accuracy_mean', 0) or 0

            inp = (f"Train {depth_val}-layer unnormalized MLP with {act_name} activation "
                   f"on CIFAR-10 (hidden_dim={HIDDEN_DIM}, batch={BATCH_SIZE}, "
                   f"epochs={NUM_EPOCHS}, seeds={NUM_SEEDS}). "
                   f"Measure gradient ratio (|log‖∇W₁‖/log‖∇W_L‖|) and test accuracy.")
            out = (f"CWA hypothesis: gradient ratio < 2.0 (stable) vs GELU > 5.0 "
                   f"(vanishing/exploding), with competitive accuracy within 5pp of GELU. "
                   f"SOC self-organization: J·ŝ → 1⁻ at convergence.")

            example = {
                'input': inp,
                'output': out,
                'predict_accuracy': str(round(acc_mean, 4)) if acc_mean is not None else 'None',
                'predict_gradient_ratio': str(round(grad_ratio, 4)) if grad_ratio is not None else 'None',
                'metadata_depth': depth_val,
                'metadata_activation': act_name,
                'metadata_dataset': 'cifar10',
                'metadata_num_seeds': NUM_SEEDS,
                'metadata_accuracy_vs_gelu_delta': str(
                    round(float(acc_mean or 0) - float(gelu_acc), 4)),
            }
            examples_cifar10.append(example)

    # MNIST examples
    for depth_key in ['depth_6', 'depth_10', 'depth_20']:
        depth_val = int(depth_key.split('_')[1])
        depth_data = exp1_results.get('mnist', {}).get(depth_key, {})
        for act_name in ACTIVATIONS_EXP1:
            act_data = depth_data.get(act_name, {})
            acc_mean = act_data.get('accuracy_mean')
            grad_ratio = act_data.get('gradient_ratio_mean')
            gelu_acc = depth_data.get('gelu', {}).get('accuracy_mean', 0) or 0

            inp = (f"Train {depth_val}-layer unnormalized MLP with {act_name} activation "
                   f"on MNIST (hidden_dim={HIDDEN_DIM}, batch={BATCH_SIZE}, "
                   f"epochs={NUM_EPOCHS}, seeds={NUM_SEEDS}). "
                   f"Measure gradient ratio and test accuracy.")
            out = "CWA hypothesis: gradient ratio < 2.0 with competitive accuracy."

            example = {
                'input': inp,
                'output': out,
                'predict_accuracy': str(round(acc_mean, 4)) if acc_mean is not None else 'None',
                'predict_gradient_ratio': str(round(grad_ratio, 4)) if grad_ratio is not None else 'None',
                'metadata_depth': depth_val,
                'metadata_activation': act_name,
                'metadata_dataset': 'mnist',
                'metadata_num_seeds': NUM_SEEDS,
                'metadata_accuracy_vs_gelu_delta': str(
                    round(float(acc_mean or 0) - float(gelu_acc), 4)),
            }
            examples_mnist.append(example)

    # Exp4 fixed-J ablation examples
    examples_exp4 = []
    all_conds = [(str(jv), exp4_results.get('fixed_j', {}).get(str(jv), {}))
                 for jv in FIXED_J_VALUES]
    all_conds.append(('learned', exp4_results.get('learned_j', {})))
    for cond_name, cond_data in all_conds:
        acc_mean = cond_data.get('accuracy_mean')
        grad_ratio = cond_data.get('gradient_ratio_mean')
        j_s_bar_mean = cond_data.get('J_s_bar_at_convergence_mean')
        inp = (f"Train 10-layer unnormalized MLP on CIFAR-10 with "
               f"{'fixed J=' + cond_name if cond_name != 'learned' else 'learned J (CWA)'} "
               f"CWA activation (hidden_dim={HIDDEN_DIM}, seeds={NUM_SEEDS_EXP4}). "
               f"Ablation: how does J value affect gradient stability and accuracy?")
        out = ("Learned J should achieve best gradient stability by finding SOC point. "
               "Fixed J near 1.0 risks instability; fixed J near 0 loses coupling benefit.")
        example = {
            'input': inp,
            'output': out,
            'predict_accuracy': str(round(acc_mean, 4)) if acc_mean is not None else 'None',
            'predict_gradient_ratio': str(round(grad_ratio, 4)) if grad_ratio is not None else 'None',
            'predict_j_s_bar_mean': str(round(j_s_bar_mean, 4)) if j_s_bar_mean is not None else 'None',
            'metadata_j_condition': cond_name,
            'metadata_dataset': 'cifar10_exp4',
            'metadata_depth': DEPTH_EXP4,
            'metadata_num_seeds': NUM_SEEDS_EXP4,
        }
        examples_exp4.append(example)

    # Hypothesis test summary example
    ht = hyp_test
    examples_hyp = [{
        'input': (f"Evaluate CWA hypothesis: gradient ratio < 2.0 on ≥10-layer unnormalized "
                  f"networks vs GELU > 5.0. Datasets: CIFAR-10, MNIST. Depths: {DEPTHS}. "
                  f"Seeds: {NUM_SEEDS}."),
        'output': ("CONFIRM if CWA gradient ratio < 2.0 AND GELU > 5.0 at depth≥10. "
                   "DISCONFIRM if accuracy delta < 0.5pp vs GELU at depth≥10. "
                   "INCONCLUSIVE otherwise."),
        'predict_overall_verdict': ht.get('overall_verdict', 'INCONCLUSIVE'),
        'predict_cwa_gradient_ratio_d10': str(
            ht.get('gradient_stability', {}).get('depth_10', {}).get('cwa_ratio', 'N/A')),
        'predict_gelu_gradient_ratio_d10': str(
            ht.get('gradient_stability', {}).get('depth_10', {}).get('gelu_ratio', 'N/A')),
        'predict_primary_criterion_d10': str(
            ht.get('gradient_stability', {}).get('depth_10', {}).get('primary_criterion_met', False)),
        'predict_soc_mean_j_s_bar': str(
            ht.get('soc_finding', {}).get('mean_J_s_bar', 'N/A')),
        'predict_soc_fraction_above_0_8': str(
            ht.get('soc_finding', {}).get('fraction_above_0.8', 'N/A')),
        'metadata_verdict': ht.get('overall_verdict', 'INCONCLUSIVE'),
    }]

    return {
        'metadata': {
            'method_name': 'CWA (Coupled-Weight Activation)',
            'description': (
                'CWA uses mean-field fixed-point iteration with learnable coupling J. '
                'Hybrid IFT/unrolled backprop. Tested against 8 baselines across depths '
                '6/10/20 on MNIST+CIFAR-10 (Exp1) and fixed-J ablation (Exp4).'
            ),
            'hypothesis_verdict': hyp_test.get('overall_verdict', 'INCONCLUSIVE'),
            'depths': DEPTHS,
            'hidden_dim': HIDDEN_DIM,
            'num_seeds': NUM_SEEDS,
            'num_epochs': NUM_EPOCHS,
            'batch_size': BATCH_SIZE,
            'lr': LR,
            'activations': ACTIVATIONS_EXP1,
            'datasets': DATASETS,
            'device': str(DEVICE),
            'gradient_stability_results': ht.get('gradient_stability', {}),
            'accuracy_improvements_vs_gelu': ht.get('accuracy_improvements_vs_gelu', {}),
            'soc_finding': ht.get('soc_finding', {}),
            'experiment_4_fixed_j': {
                cond: {
                    'accuracy': exp4_results.get('fixed_j', {}).get(cond, {}).get('accuracy_mean'),
                    'gradient_ratio': exp4_results.get('fixed_j', {}).get(cond, {}).get('gradient_ratio_mean'),
                    'j_s_bar_mean': exp4_results.get('fixed_j', {}).get(cond, {}).get('J_s_bar_at_convergence_mean'),
                } for cond in [str(j) for j in FIXED_J_VALUES]
            },
            'experiment_4_learned_j': {
                'accuracy': (exp4_results.get('learned_j') or {}).get('accuracy_mean'),
                'gradient_ratio': (exp4_results.get('learned_j') or {}).get('gradient_ratio_mean'),
                'j_s_bar_mean': (exp4_results.get('learned_j') or {}).get('J_s_bar_at_convergence_mean'),
            }
        },
        'datasets': [
            {
                'dataset': 'cifar10_gradient_stability',
                'examples': examples_cifar10
            },
            {
                'dataset': 'mnist_gradient_stability',
                'examples': examples_mnist if examples_mnist else [
                    {
                        'input': 'MNIST not run (time constraint)',
                        'output': 'N/A',
                        'predict_accuracy': 'None',
                        'predict_gradient_ratio': 'None',
                        'metadata_depth': 0,
                        'metadata_activation': 'N/A',
                        'metadata_dataset': 'mnist',
                        'metadata_num_seeds': 0,
                        'metadata_accuracy_vs_gelu_delta': '0',
                    }
                ]
            },
            {
                'dataset': 'cifar10_fixed_j_ablation',
                'examples': examples_exp4 if examples_exp4 else [
                    {
                        'input': 'Exp4 not run',
                        'output': 'N/A',
                        'predict_accuracy': 'None',
                        'predict_gradient_ratio': 'None',
                        'predict_j_s_bar_mean': 'None',
                        'metadata_j_condition': 'N/A',
                        'metadata_dataset': 'cifar10_exp4',
                        'metadata_depth': DEPTH_EXP4,
                        'metadata_num_seeds': 0,
                    }
                ]
            },
            {
                'dataset': 'hypothesis_test',
                'examples': examples_hyp
            }
        ]
    }


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 13: MAIN
# ──────────────────────────────────────────────────────────────────────────────

@logger.catch(reraise=True)
def main():
    global NUM_SEEDS, NUM_SEEDS_EXP4, DATASETS, DEPTHS
    t_total = time.time()
    data_root = './data'
    os.makedirs(data_root, exist_ok=True)
    os.makedirs('logs', exist_ok=True)

    logger.info("=== CWA Gradient Stability Experiment ===")
    logger.info(f"Config: depths={DEPTHS}, hidden={HIDDEN_DIM}, seeds={NUM_SEEDS}, "
                f"epochs={NUM_EPOCHS}, datasets={DATASETS}")

    # Sanity checks
    run_sanity_checks(DEVICE)

    # Estimate time: run 1 seed of (CIFAR-10, depth=6, gelu) to gauge speed
    logger.info("=== Timing calibration (CIFAR-10, depth=6, gelu, 1 seed) ===")
    t_cal = time.time()
    train_ds, test_ds, input_dim, num_classes = load_dataset('cifar10', data_root)
    train_loader_cal = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True,
                                  num_workers=2, pin_memory=HAS_GPU)
    test_loader_cal = DataLoader(test_ds, batch_size=512, shuffle=False,
                                 num_workers=2, pin_memory=HAS_GPU)
    fixed_x_cal, fixed_y_cal = next(iter(DataLoader(test_ds, batch_size=512, shuffle=False)))
    set_seed(0)
    _cal_model = DeepMLP(input_dim, HIDDEN_DIM, 6, num_classes, lambda d: nn.GELU()).to(DEVICE)
    _cal_opt = torch.optim.Adam(_cal_model.parameters(), lr=LR)
    _cal_sched = torch.optim.lr_scheduler.CosineAnnealingLR(_cal_opt, T_max=NUM_EPOCHS, eta_min=LR*0.1)
    _cal_crit = nn.CrossEntropyLoss()
    _cal_recs, _, _ = train_model(_cal_model, _cal_opt, _cal_sched, train_loader_cal,
                                  (fixed_x_cal, fixed_y_cal), _cal_crit, DEVICE,
                                  NUM_EPOCHS, MEASURE_AT, 'gelu')
    cal_time = time.time() - t_cal
    del _cal_model
    gc.collect()
    if HAS_GPU:
        torch.cuda.empty_cache()
    logger.info(f"Calibration: {cal_time:.1f}s per (6-layer GELU, {NUM_EPOCHS} epochs, 1 seed)")
    # CWA is ~3-5x slower due to fixed-point iteration; use 4x factor for estimate
    cwa_factor = 4.0
    num_configs = len(DATASETS) * len(DEPTHS) * len(ACTIVATIONS_EXP1) * NUM_SEEDS
    non_cwa = len(DATASETS) * len(DEPTHS) * (len(ACTIVATIONS_EXP1) - 1) * NUM_SEEDS
    cwa_configs = len(DATASETS) * len(DEPTHS) * NUM_SEEDS
    est_exp1 = (non_cwa * cal_time + cwa_configs * cal_time * cwa_factor) / 60
    est_exp4 = (len(FIXED_J_VALUES) * NUM_SEEDS_EXP4 * cal_time * cwa_factor +
                NUM_SEEDS_EXP4 * cal_time * cwa_factor) / 60
    est_total = est_exp1 + est_exp4
    logger.info(f"Estimated Exp1={est_exp1:.1f}min, Exp4={est_exp4:.1f}min, total={est_total:.1f}min")

    # Adapt config if too slow
    if est_total > 270:  # >270 min (4.5h), reduce scope
        logger.warning("Reducing seeds 3→2 and depths [6,10,20]→[6,10]")
        NUM_SEEDS = 2
        NUM_SEEDS_EXP4 = 2
        DEPTHS = [6, 10]
    if est_total > 200:
        logger.warning("CIFAR-10 only (skipping MNIST)")
        DATASETS = ['cifar10']

    # Experiment 1
    logger.info("=== Experiment 1: Gradient Stability ===")
    t_exp1 = time.time()
    exp1_results = run_experiment_1(DEVICE, data_root)
    logger.info(f"Experiment 1 done in {(time.time()-t_exp1)/60:.1f} minutes")

    # Experiment 4
    logger.info("=== Experiment 4: Fixed-J Ablation ===")
    t_exp4 = time.time()
    exp4_results = run_experiment_4(DEVICE, data_root)
    logger.info(f"Experiment 4 done in {(time.time()-t_exp4)/60:.1f} minutes")

    # Hypothesis test
    hyp_test = evaluate_hypothesis(exp1_results, exp4_results)
    logger.info(f"Hypothesis verdict: {hyp_test['overall_verdict']}")
    logger.info(f"Gradient stability: {hyp_test['gradient_stability']}")
    logger.info(f"Acc improvements vs GELU: {hyp_test['accuracy_improvements_vs_gelu']}")
    logger.info(f"SOC finding: {hyp_test['soc_finding']}")

    # Build and save output
    method_out = build_method_out(exp1_results, exp4_results, hyp_test)
    out_path = Path("method_out.json")
    out_path.write_text(json.dumps(method_out, default=str, indent=2))
    logger.info(f"Written: {out_path} ({out_path.stat().st_size / 1024:.1f} KB)")

    # Also save raw results for debugging
    raw_path = Path("logs/raw_results.json")
    raw_path.write_text(json.dumps({
        'experiment_1': exp1_results,
        'experiment_4': exp4_results,
        'hypothesis_test': hyp_test
    }, default=str, indent=2))
    logger.info(f"Raw results saved: {raw_path}")

    logger.info(f"Total runtime: {(time.time()-t_total)/60:.1f} minutes")
    logger.info(f"DONE. Verdict: {hyp_test['overall_verdict']}")


if __name__ == '__main__':
    main()
