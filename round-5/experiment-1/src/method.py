#!/usr/bin/env python3
"""CWA LM Diagnostic: SELU Baseline + Activation-Magnitude Trajectory on Tiny Shakespeare.

Compares CWA (Curie-Weiss Activation with IFT backward), SELU (LeCun init), and GELU
on a 6-layer char-GPT trained on Tiny Shakespeare for 5000 steps. 2 seeds each.
"""

import math
import json
import os
import sys
import time
import urllib.request
import argparse
import gc
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import psutil
import resource
from loguru import logger

# ─── Logging ───────────────────────────────────────────────────────────────────
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
Path("logs").mkdir(exist_ok=True)
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# ─── Hardware Detection ─────────────────────────────────────────────────────────
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

logger.info(f"Hardware: CPUs={NUM_CPUS}, GPU={HAS_GPU}, VRAM={VRAM_GB:.1f}GB, RAM={TOTAL_RAM_GB:.1f}GB, device={DEVICE}")

# Set memory limits (use 22GB of 28GB container)
RAM_BUDGET = int(22 * 1024**3)
try:
    resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET, RAM_BUDGET))
    logger.info(f"RAM limit set to 22GB")
except ValueError:
    logger.warning("Could not set RAM limit (may already be set lower)")

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    # Use up to 85% of VRAM
    torch.cuda.set_per_process_memory_fraction(0.85)
    logger.info(f"VRAM budget: 85% of {_total/1e9:.1f}GB")

# ─── Dataset ───────────────────────────────────────────────────────────────────
WORKSPACE = Path(__file__).parent
DATA_FILE = WORKSPACE / "input.txt"
URL = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"


def load_dataset() -> tuple[torch.Tensor, torch.Tensor, dict, int]:
    if not DATA_FILE.exists():
        logger.info(f"Downloading Tiny Shakespeare from {URL}")
        try:
            urllib.request.urlretrieve(URL, str(DATA_FILE))
            logger.info("Download complete")
        except Exception as e:
            logger.warning(f"Download failed ({e}), trying fallback via HuggingFace datasets")
            try:
                from datasets import load_dataset as hf_load
                ds = hf_load("tiny_shakespeare")
                text = "\n".join(ds["train"]["text"] + ds["validation"]["text"] + ds["test"]["text"])
                DATA_FILE.write_text(text)
                logger.info("HuggingFace fallback succeeded")
            except Exception as e2:
                logger.error(f"All download attempts failed: {e2}")
                raise

    text = DATA_FILE.read_text()
    logger.info(f"Dataset: {len(text):,} characters")

    chars = sorted(set(text))
    vocab_size = len(chars)
    stoi = {c: i for i, c in enumerate(chars)}
    itos = {i: c for i, c in enumerate(chars)}
    logger.info(f"Vocab size: {vocab_size}")

    data = torch.tensor([stoi[c] for c in text], dtype=torch.long)
    n = int(0.9 * len(data))
    train_data = data[:n]
    val_data = data[n:]
    logger.info(f"Train: {len(train_data):,} tokens, Val: {len(val_data):,} tokens")
    return train_data, val_data, itos, vocab_size


def get_batch(split: str, train_data: torch.Tensor, val_data: torch.Tensor,
              seq_len: int, batch: int, device: torch.device) -> tuple[torch.Tensor, torch.Tensor]:
    data = train_data if split == "train" else val_data
    ix = torch.randint(len(data) - seq_len, (batch,))
    x = torch.stack([data[i:i + seq_len] for i in ix])
    y = torch.stack([data[i + 1:i + seq_len + 1] for i in ix])
    return x.to(device), y.to(device)


# ─── CWA Custom Backward ────────────────────────────────────────────────────────
class CWAFunction(torch.autograd.Function):
    """Curie-Weiss Activation with closed-form IFT backward.

    Fixed-point equation: m* = mean(tanh(x + J*m*))  [scalar mean-field]
    IFT gives closed-form: grad_x_i = s2_i*(grad_i + J*sum_gs2/(n*(1-J*s_bar)))
    """

    @staticmethod
    def forward(ctx, x: torch.Tensor, J_raw: torch.Tensor, K_max: int, warm_T: int) -> torch.Tensor:
        J = torch.sigmoid(J_raw)
        B, T, H = x.shape

        # Warm start (no grad)
        m = x.new_zeros(B, T, 1)
        with torch.no_grad():
            for _ in range(warm_T):
                m = torch.tanh(x + J * m).mean(dim=-1, keepdim=True)

            # Adaptive delta based on current J·s̄
            s2_tmp = torch.cosh(x + J * m).pow(-2)
            s_bar_tmp = s2_tmp.mean(dim=-1, keepdim=True)
            J_s_bar_scalar = (J * s_bar_tmp.mean()).item()
            delta = max(1e-4 * max(1 - J_s_bar_scalar, 1e-3), 1e-7)

            # Iterate to convergence
            k_used = K_max
            for k in range(K_max):
                m_new = torch.tanh(x + J * m).mean(dim=-1, keepdim=True)
                if (m_new - m).abs().max().item() < delta:
                    m = m_new
                    k_used = k + 1
                    break
                m = m_new

            # Final s2, s_bar at converged m*
            s2 = torch.cosh(x + J * m).pow(-2)
            s_bar = s2.mean(dim=-1, keepdim=True)
            J_s_bar = J * s_bar

        y = torch.tanh(x + J * m)
        ctx.save_for_backward(x, J_raw, m, s2, s_bar, J_s_bar)
        ctx.k_used = k_used
        return y

    @staticmethod
    def backward(ctx, grad_y: torch.Tensor):
        x, J_raw, m, s2, s_bar, J_s_bar = ctx.saved_tensors
        J = torch.sigmoid(J_raw)
        n = x.shape[-1]

        # Clamp denominator to avoid instability
        denom = (1.0 - J_s_bar).clamp(min=1e-6)

        # IFT gradient: ∂L/∂x_i = s2_i*(grad_i + J*sum(grad_k*s2_k)/(n*denom))
        sum_g_s2 = (grad_y * s2).sum(dim=-1, keepdim=True)
        grad_x = s2 * (grad_y + J * sum_g_s2 / (n * denom))

        # ∂L/∂J: chain via dJ/dJ_raw = J*(1-J)
        grad_J = (grad_y * s2 * m / denom).sum()
        grad_J_raw = grad_J * J * (1.0 - J)

        return grad_x, grad_J_raw, None, None


class CWAActivation(nn.Module):
    """Curie-Weiss Activation: learnable scalar coupling J with IFT backward."""

    def __init__(self, K_max: int = 50, warm_T: int = 3):
        super().__init__()
        self.J_raw = nn.Parameter(torch.zeros(1))  # J = sigmoid(0) = 0.5
        self.K_max = K_max
        self.warm_T = warm_T
        self.last_diag: dict = {}

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        y = CWAFunction.apply(x, self.J_raw, self.K_max, self.warm_T)

        # Collect diagnostics (cheap: reuse last converged state)
        with torch.no_grad():
            J = torch.sigmoid(self.J_raw)
            m = x.new_zeros(*x.shape[:-1], 1)
            for _ in range(self.warm_T + 5):
                m = torch.tanh(x + J * m).mean(dim=-1, keepdim=True)
            s2 = torch.cosh(x + J * m).pow(-2)
            s_bar = s2.mean(dim=-1, keepdim=True)
            self.last_diag = {
                "mean_act_mag": (x + J * m).abs().mean().item(),
                "mean_sech2": s2.mean().item(),
                "J_s_bar": (J * s_bar.mean()).item(),
                "J": J.item(),
            }
        return y


# ─── SELU LeCun init ────────────────────────────────────────────────────────────
def lecun_normal_init(module: nn.Module) -> None:
    """Apply LeCun normal init (std=1/sqrt(fan_in)) to all Linear layers."""
    for m in module.modules():
        if isinstance(m, nn.Linear):
            fan_in = m.weight.size(1)
            nn.init.normal_(m.weight, 0.0, 1.0 / math.sqrt(fan_in))
            if m.bias is not None:
                nn.init.zeros_(m.bias)


# ─── GPT Architecture ───────────────────────────────────────────────────────────
class CausalSelfAttention(nn.Module):
    def __init__(self, n_embd: int, n_head: int, seq_len: int):
        super().__init__()
        assert n_embd % n_head == 0
        self.c_attn = nn.Linear(n_embd, 3 * n_embd)
        self.c_proj = nn.Linear(n_embd, n_embd)
        self.n_head = n_head
        self.n_embd = n_embd
        self.register_buffer(
            "mask",
            torch.tril(torch.ones(seq_len, seq_len)).view(1, 1, seq_len, seq_len),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, T, C = x.shape
        q, k, v = self.c_attn(x).split(self.n_embd, dim=2)
        hs = C // self.n_head
        q = q.view(B, T, self.n_head, hs).transpose(1, 2)
        k = k.view(B, T, self.n_head, hs).transpose(1, 2)
        v = v.view(B, T, self.n_head, hs).transpose(1, 2)
        att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(hs))
        att = att.masked_fill(self.mask[:, :, :T, :T] == 0, float("-inf"))
        att = F.softmax(att, dim=-1)
        y = att @ v
        y = y.transpose(1, 2).contiguous().view(B, T, C)
        return self.c_proj(y)


class MLP(nn.Module):
    def __init__(self, n_embd: int, act_type: str):
        super().__init__()
        self.fc1 = nn.Linear(n_embd, 4 * n_embd)
        self.fc2 = nn.Linear(4 * n_embd, n_embd)
        self.act_type = act_type
        if act_type == "cwa":
            self.act = CWAActivation(K_max=50, warm_T=3)
        elif act_type == "selu":
            self.act = nn.SELU()
        else:  # gelu
            self.act = nn.GELU()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.fc2(self.act(self.fc1(x)))


class Block(nn.Module):
    def __init__(self, n_embd: int, n_head: int, seq_len: int, act_type: str):
        super().__init__()
        self.ln1 = nn.LayerNorm(n_embd)
        self.ln2 = nn.LayerNorm(n_embd)
        self.attn = CausalSelfAttention(n_embd, n_head, seq_len)
        self.mlp = MLP(n_embd, act_type)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = x + self.attn(self.ln1(x))
        x = x + self.mlp(self.ln2(x))
        return x


class CharGPT(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        n_embd: int = 256,
        n_head: int = 8,
        n_layer: int = 6,
        seq_len: int = 256,
        act_type: str = "gelu",
    ):
        super().__init__()
        self.tok_emb = nn.Embedding(vocab_size, n_embd)
        self.pos_emb = nn.Embedding(seq_len, n_embd)
        self.blocks = nn.ModuleList(
            [Block(n_embd, n_head, seq_len, act_type) for _ in range(n_layer)]
        )
        self.ln_f = nn.LayerNorm(n_embd)
        self.head = nn.Linear(n_embd, vocab_size, bias=False)
        self.seq_len = seq_len
        self.act_type = act_type

        self.apply(self._init_weights)
        if act_type == "selu":
            # Override FFN linears with LeCun normal init (applied after default init)
            for block in self.blocks:
                lecun_normal_init(block.mlp)

    def _init_weights(self, m: nn.Module) -> None:
        if isinstance(m, nn.Linear):
            nn.init.normal_(m.weight, 0.0, 0.02)
            if m.bias is not None:
                nn.init.zeros_(m.bias)
        elif isinstance(m, nn.Embedding):
            nn.init.normal_(m.weight, 0.0, 0.02)

    def forward(self, idx: torch.Tensor, targets: torch.Tensor | None = None):
        B, T = idx.shape
        pos = torch.arange(T, device=idx.device)
        x = self.tok_emb(idx) + self.pos_emb(pos)
        for block in self.blocks:
            x = block(x)
        x = self.ln_f(x)
        logits = self.head(x)
        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1))
        return logits, loss

    def get_cwa_diagnostics(self) -> dict:
        diags = [
            block.mlp.act.last_diag
            for block in self.blocks
            if isinstance(block.mlp.act, CWAActivation) and block.mlp.act.last_diag
        ]
        if not diags:
            return {}
        return {k: sum(d[k] for d in diags) / len(diags) for k in diags[0]}


# ─── Training ───────────────────────────────────────────────────────────────────
def get_lr(step: int, n_steps: int, lr: float, warmup: int) -> float:
    if step < warmup:
        return lr * step / max(warmup, 1)
    progress = (step - warmup) / max(n_steps - warmup, 1)
    return lr * 0.5 * (1 + math.cos(math.pi * progress))


@torch.no_grad()
def estimate_val_loss(
    model: CharGPT,
    train_data: torch.Tensor,
    val_data: torch.Tensor,
    eval_iters: int,
    seq_len: int,
    batch: int,
    device: torch.device,
) -> float:
    model.eval()
    losses = []
    for _ in range(eval_iters):
        xb, yb = get_batch("val", train_data, val_data, seq_len, batch, device)
        _, loss = model(xb, yb)
        losses.append(loss.item())
    model.train()
    return float(np.mean(losses))


def train_run(
    act_type: str,
    seed: int,
    vocab_size: int,
    train_data: torch.Tensor,
    val_data: torch.Tensor,
    config: dict,
    device: torch.device,
) -> dict:
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)

    logger.info(f"Starting {act_type} seed={seed}")
    model = CharGPT(
        vocab_size=vocab_size,
        n_embd=config["n_embd"],
        n_head=config["n_head"],
        n_layer=config["n_layer"],
        seq_len=config["seq_len"],
        act_type=act_type,
    ).to(device)

    n_params = sum(p.numel() for p in model.parameters())
    logger.info(f"{act_type} seed={seed}: {n_params:,} parameters")

    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=config["lr"],
        betas=(0.9, 0.99),
        weight_decay=0.1,
    )

    val_bpc_history = []
    cwa_diag_history = []

    t0 = time.time()
    for step in range(config["n_steps"] + 1):
        if step % config["eval_interval"] == 0:
            val_loss = estimate_val_loss(
                model, train_data, val_data,
                config["eval_iters"], config["seq_len"], config["batch"], device
            )
            val_bpc = val_loss / math.log(2)
            val_bpc_history.append({"step": step, "val_bpc": round(val_bpc, 6)})

            if act_type == "cwa":
                model.eval()
                xb, _ = get_batch("train", train_data, val_data, config["seq_len"], config["batch"], device)
                with torch.no_grad():
                    model(xb)
                diag = model.get_cwa_diagnostics()
                diag["step"] = step
                cwa_diag_history.append({k: round(float(v), 6) if k != "step" else v for k, v in diag.items()})
                model.train()
                logger.info(
                    f"step={step:5d} | {act_type} seed={seed} | val_bpc={val_bpc:.4f} | "
                    f"J={diag.get('J', 0):.3f} Js̄={diag.get('J_s_bar', 0):.3f} "
                    f"|x+Jm*|={diag.get('mean_act_mag', 0):.3f}"
                )
            else:
                logger.info(f"step={step:5d} | {act_type} seed={seed} | val_bpc={val_bpc:.4f}")

        if step == config["n_steps"]:
            break

        lr = get_lr(step, config["n_steps"], config["lr"], config["warmup"])
        for pg in optimizer.param_groups:
            pg["lr"] = lr

        xb, yb = get_batch("train", train_data, val_data, config["seq_len"], config["batch"], device)
        _, loss = model(xb, yb)
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()

    elapsed = time.time() - t0
    final_bpc = val_bpc_history[-1]["val_bpc"]
    logger.info(f"DONE {act_type} seed={seed}: val_bpc={final_bpc:.4f} ({elapsed:.1f}s)")

    # Free GPU memory
    del model, optimizer
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    gc.collect()

    return {
        "val_bpc_final": final_bpc,
        "val_bpc_history": val_bpc_history,
        "cwa_diag_history": cwa_diag_history,
        "elapsed_s": round(elapsed, 2),
    }


# ─── Smoke test ─────────────────────────────────────────────────────────────────
def smoke_test(device: torch.device) -> None:
    logger.info("=== SMOKE TEST ===")
    cfg_smoke = {
        "n_embd": 64, "n_head": 4, "n_layer": 2,
        "seq_len": 64, "batch": 8, "lr": 3e-4,
        "n_steps": 20, "warmup": 5, "eval_interval": 5, "eval_iters": 2,
    }
    # Minimal dataset
    text = "hello world " * 1000
    chars = sorted(set(text))
    stoi = {c: i for i, c in enumerate(chars)}
    data = torch.tensor([stoi[c] for c in text], dtype=torch.long)
    td, vd = data[:int(0.9 * len(data))], data[int(0.9 * len(data)):]
    vocab_size = len(chars)

    for act in ["gelu", "selu", "cwa"]:
        r = train_run(act, 42, vocab_size, td, vd, cfg_smoke, device)
        logger.info(f"Smoke {act}: val_bpc={r['val_bpc_final']:.4f}, "
                    f"cwa_diag={len(r['cwa_diag_history'])} entries")
        assert 0.5 < r["val_bpc_final"] < 20.0, f"Implausible BPC for {act}"
        if act == "cwa":
            assert len(r["cwa_diag_history"]) >= 3, "CWA diag too short"

    # Gradient check on CWA
    logger.info("Running gradient check on CWAFunction...")
    torch.manual_seed(0)
    x_check = torch.randn(2, 4, 8, dtype=torch.float64, requires_grad=True)
    J_raw_check = torch.zeros(1, dtype=torch.float64, requires_grad=True)
    result = torch.autograd.gradcheck(
        lambda x, j: CWAFunction.apply(x, j, 50, 5),
        (x_check, J_raw_check),
        eps=1e-4, atol=1e-3, rtol=1e-3,
    )
    logger.info(f"gradcheck passed: {result}")
    logger.info("=== SMOKE TEST PASSED ===")


# ─── Main ───────────────────────────────────────────────────────────────────────
@logger.catch(reraise=True)
def main(n_steps: int = 5000, seeds: list[int] | None = None, smoke: bool = False,
         activations: list[str] | None = None, eval_interval: int = 100,
         eval_iters: int = 50, batch: int = 64) -> None:
    if seeds is None:
        seeds = [42, 7]
    if activations is None:
        activations = ["selu", "cwa", "gelu"]

    if smoke:
        smoke_test(DEVICE)
        return

    train_data, val_data, itos, vocab_size = load_dataset()

    CONFIG = {
        "n_embd": 256, "n_head": 8, "n_layer": 6,
        "seq_len": 256, "batch": batch, "lr": 3e-4,
        "n_steps": n_steps, "warmup": min(100, n_steps // 5),
        "eval_interval": eval_interval, "eval_iters": eval_iters,
    }
    logger.info(f"Config: {CONFIG}")

    results: dict[str, dict] = {}
    for act in activations:
        for seed in seeds:
            key = f"{act}_seed{seed}"
            logger.info(f"\n=== {key} ===")
            results[key] = train_run(act, seed, vocab_size, train_data, val_data, CONFIG, DEVICE)

    # ─── Build output in exp_gen_sol_out schema ─────────────────────────────────
    # Schema: {datasets: [{dataset: str, examples: [{input: str, output: str, ...}]}]}
    # Each example = one (activation, seed, eval_step) checkpoint — gives 51*6=306 examples

    def _mean(xs: list[float]) -> float:
        return sum(xs) / len(xs) if xs else 0.0

    def _std(xs: list[float]) -> float:
        if len(xs) < 2:
            return 0.0
        m = _mean(xs)
        return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))

    # Build index from CWA diag history for fast lookup
    def _build_cwa_diag_index(cwa_diag_history: list[dict]) -> dict[int, dict]:
        return {entry["step"]: entry for entry in cwa_diag_history}

    examples = []
    init_type_map = {
        "selu": "lecun_normal_1_sqrt_fan_in",
        "gelu": "gpt_normal_0.02",
        "cwa": "gpt_normal_0.02_Jraw0",
    }
    for act in activations:
        for seed in seeds:
            key = f"{act}_seed{seed}"
            r = results[key]
            cwa_idx = _build_cwa_diag_index(r["cwa_diag_history"])
            # One example per evaluation checkpoint
            for ckpt in r["val_bpc_history"]:
                step = ckpt["step"]
                val_bpc = ckpt["val_bpc"]
                cwa_diag_at_step = cwa_idx.get(step, {})
                input_str = json.dumps({
                    "activation": act,
                    "seed": seed,
                    "eval_step": step,
                    "n_steps_total": CONFIG["n_steps"],
                    "architecture": "gpt_6layer_256embd_8head_seqlen256",
                    "lr": CONFIG["lr"],
                    "batch": CONFIG["batch"],
                    "init_type": init_type_map.get(act, "gpt_normal_0.02"),
                })
                output_str = json.dumps({
                    "val_bpc": val_bpc,
                    "is_final": step == CONFIG["n_steps"],
                    "cwa_J": cwa_diag_at_step.get("J"),
                    "cwa_J_s_bar": cwa_diag_at_step.get("J_s_bar"),
                    "cwa_mean_act_mag": cwa_diag_at_step.get("mean_act_mag"),
                    "cwa_mean_sech2": cwa_diag_at_step.get("mean_sech2"),
                })
                ex = {
                    "input": input_str,
                    "output": output_str,
                    "metadata_activation": act,
                    "metadata_seed": str(seed),
                    "metadata_eval_step": str(step),
                    "predict_val_bpc": str(round(val_bpc, 6)),
                }
                examples.append(ex)

    # Aggregate summaries per activation
    act_summary = {}
    for act in activations:
        bpcs = [results[f"{act}_seed{s}"]["val_bpc_final"] for s in seeds if f"{act}_seed{s}" in results]
        act_summary[act] = {
            "mean_val_bpc": round(_mean(bpcs), 6),
            "std_val_bpc": round(_std(bpcs), 6),
            "min_val_bpc": round(min(bpcs), 6) if bpcs else None,
            "max_val_bpc": round(max(bpcs), 6) if bpcs else None,
        }

    # CWA trajectory summary (seed 42)
    cwa_key = f"cwa_seed{seeds[0]}"
    cwa_diag = results.get(cwa_key, {}).get("cwa_diag_history", [])
    cwa_trajectory_summary = {}
    if cwa_diag:
        first, last = cwa_diag[0], cwa_diag[-1]
        cwa_trajectory_summary = {
            "step_0_J_s_bar": first.get("J_s_bar"),
            "step_final_J_s_bar": last.get("J_s_bar"),
            "step_0_mean_act_mag": first.get("mean_act_mag"),
            "step_final_mean_act_mag": last.get("mean_act_mag"),
            "step_0_J": first.get("J"),
            "step_final_J": last.get("J"),
            "n_diag_entries": len(cwa_diag),
            "sech2_saturation_confirmed": (
                last.get("mean_act_mag", 0) > first.get("mean_act_mag", 0)
                and last.get("J_s_bar", 1) < first.get("J_s_bar", 0)
            ),
        }

    method_out = {
        "metadata": {
            "method": "CWA vs SELU vs GELU on Tiny Shakespeare char-GPT",
            "config": CONFIG,
            "dataset": "tiny_shakespeare",
            "n_runs": len(activations) * len(seeds),
            "n_checkpoints_per_run": CONFIG["n_steps"] // CONFIG["eval_interval"] + 1,
            "total_examples": len(examples),
            "act_summary": act_summary,
            "cwa_trajectory_summary": cwa_trajectory_summary,
            "primary_comparison": {
                "selu_mean_val_bpc": act_summary.get("selu", {}).get("mean_val_bpc"),
                "cwa_mean_val_bpc": act_summary.get("cwa", {}).get("mean_val_bpc"),
                "gelu_mean_val_bpc": act_summary.get("gelu", {}).get("mean_val_bpc"),
            },
        },
        "datasets": [
            {
                "dataset": "tiny_shakespeare",
                "examples": examples,
            }
        ],
    }

    out_path = WORKSPACE / "method_out.json"
    out_path.write_text(json.dumps(method_out, indent=2))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size / 1024:.1f} KB)")

    # ─── Validation checks ──────────────────────────────────────────────────────
    n_runs = len(activations) * len(seeds)
    expected_checkpoints = CONFIG["n_steps"] // CONFIG["eval_interval"] + 1
    expected_examples = n_runs * expected_checkpoints
    assert len(examples) == expected_examples, \
        f"Expected {expected_examples} examples, got {len(examples)}"
    assert len(examples) >= 50, f"Need ≥50 examples, got {len(examples)}"

    for ex in examples:
        out = json.loads(ex["output"])
        bpc = out["val_bpc"]
        assert 0.8 < bpc < 8.0, f"Implausible bpc={bpc}"

    # Check final BPCs are plausible
    for act in activations:
        for seed in seeds:
            final_bpc = results[f"{act}_seed{seed}"]["val_bpc_final"]
            assert 0.8 < final_bpc < 4.0, \
                f"Implausible final bpc={final_bpc} for {act}_seed{seed}"

    # Check CWA diagnostics populated (expect one entry per eval checkpoint)
    expected_cwa_entries = CONFIG["n_steps"] // CONFIG["eval_interval"]
    for seed in seeds:
        cwa_hist = results.get(f"cwa_seed{seed}", {}).get("cwa_diag_history", [])
        assert len(cwa_hist) >= expected_cwa_entries - 2, \
            f"CWA diag too short for seed {seed}: {len(cwa_hist)} (expected ~{expected_cwa_entries})"

    logger.info(f"All validation checks passed ({len(examples)} checkpoint examples from {n_runs} runs)")
    logger.info(f"Summary: SELU={act_summary.get('selu', {}).get('mean_val_bpc')} "
                f"CWA={act_summary.get('cwa', {}).get('mean_val_bpc')} "
                f"GELU={act_summary.get('gelu', {}).get('mean_val_bpc')}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true", help="Run quick smoke test")
    parser.add_argument("--n_steps", type=int, default=5000)
    parser.add_argument("--eval_interval", type=int, default=100)
    parser.add_argument("--eval_iters", type=int, default=50)
    parser.add_argument("--batch", type=int, default=64)
    parser.add_argument("--seeds", type=str, default="42,7", help="Comma-separated seeds")
    parser.add_argument("--activations", type=str, default="selu,cwa,gelu",
                        help="Comma-separated activations to run")
    args = parser.parse_args()

    seeds = [int(s) for s in args.seeds.split(",")]
    activations = args.activations.split(",")
    main(n_steps=args.n_steps, seeds=seeds, smoke=args.smoke, activations=activations,
         eval_interval=args.eval_interval, eval_iters=args.eval_iters, batch=args.batch)
