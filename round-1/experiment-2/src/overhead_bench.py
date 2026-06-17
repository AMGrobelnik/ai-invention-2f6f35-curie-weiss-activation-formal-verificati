"""Experiment 5: Synthetic computational overhead benchmark CWA vs GELU."""
import math
import time

import torch
import torch.nn as nn
from loguru import logger

from cwa import CWA

TARGET_J_S_BARS = [0.1, 0.3, 0.5, 0.7, 0.8, 0.9, 0.95, 0.99]
N_WARMUP = 5
N_TIMING = 20
BATCH, C, H, W = 32, 256, 8, 8


def logit(t: float) -> torch.Tensor:
    t = max(min(t, 0.99), 0.01)
    return torch.tensor([math.log(t / (1 - t))], dtype=torch.float32)


def measure_cwa_overhead(device: torch.device) -> list[dict]:
    overhead_table = []
    gelu = nn.GELU().to(device)

    for target in TARGET_J_S_BARS:
        logger.info(f"  Benchmarking J*s_bar target={target}")
        cwa = CWA(K_max=100).to(device)
        cwa.benchmark_mode = True  # use full convergence checking for benchmark
        with torch.no_grad():
            cwa.J_raw.copy_(logit(target).to(device))
        cwa.J_raw.requires_grad_(False)

        x = torch.randn(BATCH, C, H, W, device=device) * 0.01
        x.requires_grad_(True)

        # Warmup CWA
        for _ in range(N_WARMUP):
            y = cwa(x)
            y.sum().backward()
            if x.grad is not None:
                x.grad.zero_()

        # Time CWA
        torch.cuda.synchronize()
        times_cwa = []
        for _ in range(N_TIMING):
            torch.cuda.synchronize()
            t0 = time.perf_counter()
            y = cwa(x)
            loss = y.sum()
            loss.backward()
            torch.cuda.synchronize()
            times_cwa.append(time.perf_counter() - t0)
            if x.grad is not None:
                x.grad.zero_()

        # Memory CWA
        torch.cuda.reset_peak_memory_stats(device)
        y = cwa(x)
        loss = y.sum()
        loss.backward()
        torch.cuda.synchronize()
        mem_cwa_mb = torch.cuda.max_memory_allocated(device) / 1024 ** 2

        actual_J_s_bar = cwa.last_J_s_bar
        actual_k = cwa.last_k
        actual_mode = cwa.last_mode

        # Warmup GELU
        x_gelu = x.detach().requires_grad_(True)
        for _ in range(N_WARMUP):
            y_g = gelu(x_gelu)
            y_g.sum().backward()
            if x_gelu.grad is not None:
                x_gelu.grad.zero_()

        # Time GELU
        torch.cuda.synchronize()
        times_gelu = []
        for _ in range(N_TIMING):
            torch.cuda.synchronize()
            t0 = time.perf_counter()
            y_g = gelu(x_gelu)
            y_g.sum().backward()
            torch.cuda.synchronize()
            times_gelu.append(time.perf_counter() - t0)
            if x_gelu.grad is not None:
                x_gelu.grad.zero_()

        # Memory GELU
        torch.cuda.reset_peak_memory_stats(device)
        y_g = gelu(x_gelu)
        y_g.sum().backward()
        torch.cuda.synchronize()
        mem_gelu_mb = torch.cuda.max_memory_allocated(device) / 1024 ** 2

        wall_cwa = sum(times_cwa) / len(times_cwa) * 1000
        wall_gelu = sum(times_gelu) / len(times_gelu) * 1000

        row = {
            "J_s_bar_target": target,
            "J_s_bar_actual": actual_J_s_bar,
            "J_value": float(torch.sigmoid(cwa.J_raw).item()),
            "K_star": actual_k,
            "backprop_mode": actual_mode,
            "wall_clock_ms_cwa": wall_cwa,
            "wall_clock_ms_gelu": wall_gelu,
            "wall_clock_ratio": wall_cwa / max(wall_gelu, 1e-9),
            "memory_mb_cwa": mem_cwa_mb,
            "memory_mb_gelu": mem_gelu_mb,
            "memory_ratio": mem_cwa_mb / max(mem_gelu_mb, 1e-9),
        }
        overhead_table.append(row)
        logger.info(
            f"    J*s_bar={target}: K={actual_k:.0f}, mode={actual_mode}, "
            f"wall={wall_cwa:.2f}ms/{wall_gelu:.2f}ms (ratio={row['wall_clock_ratio']:.2f}), "
            f"mem={mem_cwa_mb:.1f}/{mem_gelu_mb:.1f}MB (ratio={row['memory_ratio']:.2f})"
        )

    return overhead_table
