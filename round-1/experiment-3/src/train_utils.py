"""Training utilities: train loop, evaluation, memory measurement."""

import math
import time
from collections import defaultdict
from typing import Callable
import torch
import torch.nn as nn
from loguru import logger


def get_cosine_lr(step: int, max_steps: int, lr: float, warmup_steps: int) -> float:
    if step < warmup_steps:
        return lr * step / max(warmup_steps, 1)
    t = (step - warmup_steps) / max(max_steps - warmup_steps, 1)
    return lr * 0.5 * (1.0 + math.cos(math.pi * t))


def evaluate(model: nn.Module, get_batch: Callable, n_batches: int = 20) -> float:
    """Return mean cross-entropy loss over n_batches random batches."""
    model.eval()
    losses = []
    with torch.no_grad():
        for _ in range(n_batches):
            x, y = get_batch("val")
            _, loss = model(x, y)
            losses.append(loss.item())
    model.train()
    return sum(losses) / len(losses)


def evaluate_test(model: nn.Module, get_batch: Callable, n_batches: int = 50) -> float:
    model.eval()
    losses = []
    with torch.no_grad():
        for _ in range(n_batches):
            x, y = get_batch("test")
            _, loss = model(x, y)
            losses.append(loss.item())
    model.train()
    return sum(losses) / len(losses)


def measure_peak_memory_mb(
    model: nn.Module, get_batch: Callable, device: str
) -> float:
    """Measure peak GPU memory (MB) over one forward+backward pass."""
    if not torch.cuda.is_available():
        return 0.0
    torch.cuda.reset_peak_memory_stats(device)
    model.train()
    x, y = get_batch("train")
    _, loss = model(x, y)
    loss.backward()
    model.zero_grad()
    return torch.cuda.max_memory_allocated(device) / (1024**2)


def train_model(
    model: nn.Module,
    get_batch: Callable,
    config: dict,
    activation_name: str,
) -> tuple[float, dict, dict, list[dict]]:
    """Train model for config['max_steps'] steps.

    Returns: (final_val_loss, cwa_trajectory, bp_stats, checkpoints).
    checkpoints: list of {step, train_loss, val_loss, lr, elapsed} dicts.
    """
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=config["lr"],
        weight_decay=0.1,
        betas=(0.9, 0.95),
    )
    cwa_traj: dict = defaultdict(list)
    backprop_counts = {"unrolled": 0, "ift": 0}
    checkpoints: list[dict] = []
    t0 = time.time()
    eval_n = config.get("eval_n_batches", 20)

    for step in range(config["max_steps"]):
        lr = get_cosine_lr(
            step, config["max_steps"], config["lr"], config["warmup_steps"]
        )
        for g in optimizer.param_groups:
            g["lr"] = lr

        x, y = get_batch("train")
        logits, loss = model(x, y)
        train_loss_val = loss.item()
        optimizer.zero_grad(set_to_none=True)
        loss.backward()

        has_nan = any(
            p.grad is not None and torch.isnan(p.grad).any()
            for p in model.parameters()
        )
        if has_nan:
            logger.warning(f"step {step}: NaN gradient detected, zeroing")
            model.zero_grad(set_to_none=True)
            continue

        nn.utils.clip_grad_norm_(model.parameters(), config["grad_clip"])
        optimizer.step()

        if activation_name == "cwa" and step % config.get("log_every", 200) == 0:
            stats = model.get_cwa_stats()
            for layer_key, s in stats.items():
                cwa_traj[layer_key].append({"step": step, **s})
                if s["mode"] == "unrolled":
                    backprop_counts["unrolled"] += 1
                else:
                    backprop_counts["ift"] += 1

        if step % config.get("eval_every", 200) == 0:
            val_loss = evaluate(model, get_batch, n_batches=eval_n)
            elapsed = time.time() - t0
            checkpoints.append({
                "step": step,
                "train_loss": round(train_loss_val, 4),
                "val_loss": round(val_loss, 4),
                "lr": round(lr, 6),
                "elapsed_s": round(elapsed, 1),
            })
            logger.info(
                f"  step {step}/{config['max_steps']}: "
                f"train={train_loss_val:.4f} val={val_loss:.4f} "
                f"lr={lr:.2e} elapsed={elapsed:.1f}s"
            )

    final_val = evaluate(model, get_batch, n_batches=eval_n)
    total = backprop_counts["unrolled"] + backprop_counts["ift"]
    bp_stats = {
        "unrolled_count": backprop_counts["unrolled"],
        "ift_count": backprop_counts["ift"],
        "unrolled_fraction": backprop_counts["unrolled"] / max(total, 1),
        "ift_fraction": backprop_counts["ift"] / max(total, 1),
    }
    return final_val, dict(cwa_traj), bp_stats, checkpoints
