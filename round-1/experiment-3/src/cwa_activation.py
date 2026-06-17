"""Curie-Weiss Activation (CWA) — fixed-point mean-field activation with IFT backward."""

import torch
import torch.nn as nn


class CWAIFTFunction(torch.autograd.Function):
    """IFT backward for CWA when J·s̄ >= 0.8 (O(1) activation memory)."""

    @staticmethod
    def forward(ctx, x, J, m_star):
        # m_star: [B, T, 1] — already converged fixed point (detached)
        y_star = torch.tanh(x + J * m_star)
        s_bar = 1.0 - y_star.pow(2)  # sech² per element [B, T, H]
        s_bar_mean = s_bar.mean(dim=-1, keepdim=True)  # [B, T, 1]
        ctx.save_for_backward(J, m_star, s_bar, s_bar_mean)
        return y_star

    @staticmethod
    def backward(ctx, grad_y):
        J, m_star, s_bar, s_bar_mean = ctx.saved_tensors
        J_val = J.item()
        n = grad_y.shape[-1]  # hidden dim = 4 * n_embd
        denom = (1.0 - J_val * s_bar_mean).clamp(min=1e-4)  # [B, T, 1]

        # IFT gradient for x:
        # ∂L/∂x_i = sech²_i * [grad_y_i + (J/n) * Σ_j(grad_y_j * sech²_j) / denom]
        weighted_sum = (grad_y * s_bar).sum(dim=-1, keepdim=True)  # [B, T, 1]
        grad_x = s_bar * (grad_y + J_val * weighted_sum / (n * denom))

        # IFT gradient for J (scalar):
        grad_J = (grad_y * s_bar * m_star / denom).sum().unsqueeze(0)

        return grad_x, grad_J, None  # no grad for m_star


class CWAActivation(nn.Module):
    """Curie-Weiss Activation: fixed point of y = tanh(x + J * mean_h(y)).

    J = sigmoid(J_raw) in (0, 1). init J_raw=0 so J starts at 0.5.
    Hybrid backward: unrolled autograd if J·s̄ < 0.8, IFT if J·s̄ >= 0.8.
    """

    def __init__(self):
        super().__init__()
        self.J_raw = nn.Parameter(torch.zeros(1))
        self._last_J = 0.5
        self._last_J_s_bar = 0.5
        self._last_K = 0
        self._last_mode = "unrolled"

    def forward(self, x):
        # x: [B, T, H] where H = 4 * n_embd (MLP expanded dimension)
        J = torch.sigmoid(self.J_raw)  # scalar in (0,1)
        J_val = J.item()

        # --- Step 1: Find m* without gradient tracking ---
        with torch.no_grad():
            m = torch.zeros(*x.shape[:-1], 1, device=x.device, dtype=x.dtype)
            K_used = 0
            J_s_bar_final = J_val
            for k in range(5):
                y_tmp = torch.tanh(x + J_val * m)
                m_new = y_tmp.mean(dim=-1, keepdim=True)
                s_bar_tmp = (1.0 - y_tmp.pow(2)).mean().item()
                J_s_bar_cur = J_val * s_bar_tmp
                delta = 1e-4 * max(1.0 - J_s_bar_cur, 1e-2) + 1e-8
                diff = (m_new - m).abs().max().item()
                m = m_new
                K_used = k + 1
                J_s_bar_final = J_s_bar_cur
                if diff < delta:
                    break
            m_star = m.clone()

        # --- Step 2: Decide backprop mode based on J·s̄ ---
        if J_s_bar_final < 0.8:
            # Unrolled autograd: warm-start from m_star (detached), run 3 tracked steps
            m_tracked = m_star.detach()
            for _ in range(3):
                m_tracked = torch.tanh(x + J * m_tracked).mean(dim=-1, keepdim=True)
            y_out = torch.tanh(x + J * m_tracked)
            mode = "unrolled"
        else:
            # IFT mode: O(1) activation memory, analytic gradient
            y_out = CWAIFTFunction.apply(x, J, m_star)
            mode = "ift"

        # Update logging stats
        with torch.no_grad():
            y_check = torch.tanh(x + J_val * m_star)
            s_bar_check = (1.0 - y_check.pow(2)).mean().item()
            J_s_bar_final = J_val * s_bar_check
        self._last_J = J_val
        self._last_J_s_bar = J_s_bar_final
        self._last_K = K_used
        self._last_mode = mode

        return y_out
