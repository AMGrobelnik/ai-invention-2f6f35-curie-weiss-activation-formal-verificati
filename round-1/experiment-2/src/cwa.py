"""CWA (Curie-Weiss Activation) — PyTorch nn.Module with hybrid IFT/unrolled backprop.

Key implementation choices:
- Training mode: fixed K_train iterations (no per-step convergence check — eliminates
  GPU→CPU sync overhead from .item() calls inside the batch loop).
- IFT mode: used when J*s_bar >= 0.8 (near-critical); triggered by cached mode from
  previous forward pass to avoid a probe run on every batch.
- Overhead benchmark: uses K_max=100 with full convergence checking.
"""
import torch
import torch.nn as nn

# Fixed iteration counts for training (avoids Python-loop sync overhead)
K_TRAIN_UNROLLED = 8   # steps in unrolled mode (J*s_bar < 0.8)
K_TRAIN_IFT = 20       # steps in IFT mode (near-critical; IFT needs convergence but fewer steps)


class CWAFunction(torch.autograd.Function):
    """IFT-based custom backward. Used when J*s_bar >= 0.8."""

    @staticmethod
    def forward(ctx, x, J_raw, k_iters: int = 20):
        J = torch.sigmoid(J_raw)
        n = x.shape[1]

        m = torch.zeros(x.shape[0], 1, *x.shape[2:], device=x.device, dtype=x.dtype)
        for _ in range(k_iters):
            m = torch.tanh(x + J * m).mean(dim=1, keepdim=True)

        h_star = x + J * m
        sech2 = 1.0 / torch.cosh(h_star) ** 2
        s_bar = sech2.mean()
        J_s_bar = J * s_bar
        y = torch.tanh(h_star)

        ctx.save_for_backward(x, m, J_raw, sech2, s_bar, J_s_bar)
        ctx.n = n
        ctx.k_iters = k_iters
        ctx.J_s_bar_val = J_s_bar.item()

        return y, J_s_bar.detach(), torch.tensor(float(k_iters), device=x.device)

    @staticmethod
    def backward(ctx, grad_y, _g1, _g2):
        x, m_star, J_raw, sech2, s_bar, J_s_bar = ctx.saved_tensors
        J = torch.sigmoid(J_raw)
        n = ctx.n

        denom = (1.0 - J_s_bar).clamp(min=1e-3)
        G = (grad_y * sech2).sum(dim=1, keepdim=True)
        grad_x = sech2 * (grad_y + J * G / (n * denom))

        grad_J = (grad_y * sech2 * m_star / denom).sum()
        grad_J_raw = grad_J * J * (1.0 - J)

        return grad_x, grad_J_raw, None


class CWA(nn.Module):
    """
    Curie-Weiss Activation: y_i = tanh(x_i + J * mean_channels(y))
    J = sigmoid(J_raw) in (0,1) is a per-layer learnable scalar.

    Backprop modes:
      - unrolled: K_TRAIN_UNROLLED fixed steps, autograd tracks through them.
      - IFT: K_TRAIN_IFT fixed steps, IFT backward (no autograd through iterations).

    Mode decision uses cached J*s_bar from previous forward pass — avoids an extra
    no_grad probe on every batch (which was ~40% of CWA wall-clock).
    """

    def __init__(self, K_max: int = 50):
        super().__init__()
        self.J_raw = nn.Parameter(torch.zeros(1))
        self.K_max = K_max  # used only in benchmark mode
        self.last_J: float | None = None
        self.last_J_s_bar: float | None = None
        self.last_k: float | None = None
        self.last_mode: str | None = None
        self._prev_use_ift: bool = False
        self.benchmark_mode: bool = False  # if True, use K_max with convergence check

    def _forward_train(self, x: torch.Tensor, J: torch.Tensor) -> tuple:
        """Fast training forward: fixed K steps, no per-step convergence check."""
        if self._prev_use_ift:
            y, J_s_bar_t, k_t = CWAFunction.apply(x, self.J_raw, K_TRAIN_IFT)
            mode = "IFT"
        else:
            # Unrolled: K_TRAIN_UNROLLED steps through autograd
            m = torch.zeros(x.shape[0], 1, *x.shape[2:], device=x.device, dtype=x.dtype)
            for _ in range(K_TRAIN_UNROLLED):
                m = torch.tanh(x + J * m).mean(dim=1, keepdim=True)
            y = torch.tanh(x + J * m)
            with torch.no_grad():
                sech2_f = 1.0 / torch.cosh(x + J * m.detach()) ** 2
                J_s_bar_t = J * sech2_f.mean()
            k_t = torch.tensor(float(K_TRAIN_UNROLLED))
            mode = "unrolled"
        return y, J_s_bar_t, k_t, mode

    def _forward_benchmark(self, x: torch.Tensor, J: torch.Tensor) -> tuple:
        """Benchmark forward: full convergence checking with K_max iterations."""
        m = torch.zeros(x.shape[0], 1, *x.shape[2:], device=x.device, dtype=x.dtype)
        k_final = 0
        for k in range(self.K_max):
            h = x + J * m
            m_new = torch.tanh(h).mean(dim=1, keepdim=True)
            with torch.no_grad():
                sech2_tmp = 1.0 / torch.cosh(h) ** 2
                J_s_bar_tmp = J * sech2_tmp.mean()
                delta = 1e-4 * (1.0 - J_s_bar_tmp.clamp(max=0.9999))
                diff = (m_new - m).abs().max()
            m = m_new
            k_final = k + 1
            if diff.item() < delta.item():
                break

        use_ift = self._prev_use_ift
        if use_ift:
            y, J_s_bar_t, k_t = CWAFunction.apply(x, self.J_raw, k_final)
            mode = "IFT"
        else:
            y = torch.tanh(x + J * m)
            with torch.no_grad():
                sech2_f = 1.0 / torch.cosh(x + J * m.detach()) ** 2
                J_s_bar_t = J * sech2_f.mean()
            k_t = torch.tensor(float(k_final))
            mode = "unrolled"
        return y, J_s_bar_t, k_t, mode

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        J = torch.sigmoid(self.J_raw)

        if self.benchmark_mode:
            y, J_s_bar_t, k_t, mode = self._forward_benchmark(x, J)
        else:
            y, J_s_bar_t, k_t, mode = self._forward_train(x, J)

        J_s_bar_val = J_s_bar_t.item() if torch.is_tensor(J_s_bar_t) else float(J_s_bar_t)
        self._prev_use_ift = J_s_bar_val >= 0.8

        self.last_J = J.item()
        self.last_J_s_bar = J_s_bar_val
        self.last_k = k_t.item() if torch.is_tensor(k_t) else float(k_t)
        self.last_mode = mode
        return y

    def reset_cache(self) -> None:
        self._prev_use_ift = False
