"""Minimal GPT model with configurable activation function."""

import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from cwa_activation import CWAActivation


class TanhSwishMixture(nn.Module):
    """p * tanh(x) + (1-p) * swish(x); p_c=0.5 as default."""

    def __init__(self, p: float = 0.5):
        super().__init__()
        self.p = p

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.p * torch.tanh(x) + (1.0 - self.p) * F.silu(x)


def make_activation(name: str, n_embd: int) -> nn.Module:
    """Return activation module for use inside MLP."""
    mlp_dim = 4 * n_embd
    if name == "gelu":
        return nn.GELU()
    elif name == "gelu+ln":
        return nn.Sequential(nn.GELU(), nn.LayerNorm(mlp_dim))
    elif name == "selu":
        return nn.SELU()
    elif name == "tanh_swish":
        return TanhSwishMixture(p=0.5)
    elif name == "cwa":
        return CWAActivation()
    else:
        raise ValueError(f"Unknown activation: {name}")


class MLP(nn.Module):
    def __init__(self, n_embd: int, activation_name: str = "gelu", dropout: float = 0.1):
        super().__init__()
        self.c_fc = nn.Linear(n_embd, 4 * n_embd)
        self.act = make_activation(activation_name, n_embd)
        self.c_proj = nn.Linear(4 * n_embd, n_embd)
        self.drop = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.c_fc(x)
        x = self.act(x)
        x = self.c_proj(x)
        return self.drop(x)


class CausalSelfAttention(nn.Module):
    def __init__(
        self,
        n_embd: int,
        n_head: int,
        dropout: float = 0.1,
        block_size: int = 2048,
    ):
        super().__init__()
        assert n_embd % n_head == 0
        self.c_attn = nn.Linear(n_embd, 3 * n_embd)
        self.c_proj = nn.Linear(n_embd, n_embd)
        self.attn_drop = nn.Dropout(dropout)
        self.resid_drop = nn.Dropout(dropout)
        self.n_head = n_head
        self.n_embd = n_embd
        self.register_buffer(
            "bias",
            torch.tril(torch.ones(block_size, block_size)).view(
                1, 1, block_size, block_size
            ),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, T, C = x.shape
        q, k, v = self.c_attn(x).split(self.n_embd, dim=2)
        k = k.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)
        q = q.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)
        v = v.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)
        if hasattr(F, "scaled_dot_product_attention"):
            y = F.scaled_dot_product_attention(
                q, k, v, attn_mask=None, dropout_p=0.0, is_causal=True
            )
        else:
            att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(k.size(-1)))
            att = att.masked_fill(self.bias[:, :, :T, :T] == 0, float("-inf"))
            att = F.softmax(att, dim=-1)
            att = self.attn_drop(att)
            y = att @ v
        y = y.transpose(1, 2).contiguous().view(B, T, C)
        return self.resid_drop(self.c_proj(y))


class Block(nn.Module):
    def __init__(
        self,
        n_embd: int,
        n_head: int,
        activation_name: str = "gelu",
        dropout: float = 0.1,
        block_size: int = 2048,
    ):
        super().__init__()
        self.ln_1 = nn.LayerNorm(n_embd)
        self.attn = CausalSelfAttention(n_embd, n_head, dropout, block_size)
        self.ln_2 = nn.LayerNorm(n_embd)
        self.mlp = MLP(n_embd, activation_name, dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = x + self.attn(self.ln_1(x))
        x = x + self.mlp(self.ln_2(x))
        return x


class GPT(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        n_layer: int = 6,
        n_head: int = 8,
        n_embd: int = 256,
        block_size: int = 256,
        dropout: float = 0.1,
        activation_name: str = "gelu",
    ):
        super().__init__()
        self.tok_emb = nn.Embedding(vocab_size, n_embd)
        self.pos_emb = nn.Embedding(block_size, n_embd)
        self.drop = nn.Dropout(dropout)
        self.blocks = nn.ModuleList(
            [
                Block(n_embd, n_head, activation_name, dropout, block_size)
                for _ in range(n_layer)
            ]
        )
        self.ln_f = nn.LayerNorm(n_embd)
        self.lm_head = nn.Linear(n_embd, vocab_size, bias=False)
        self.block_size = block_size
        self.apply(self._init_weights)

    def _init_weights(self, module: nn.Module) -> None:
        if isinstance(module, nn.Linear):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def forward(
        self,
        idx: torch.Tensor,
        targets: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor | None]:
        B, T = idx.shape
        assert T <= self.block_size
        pos = torch.arange(T, device=idx.device, dtype=torch.long)
        x = self.drop(self.tok_emb(idx) + self.pos_emb(pos))
        for block in self.blocks:
            x = block(x)
        x = self.ln_f(x)
        logits = self.lm_head(x)
        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1))
        return logits, loss

    def get_cwa_stats(self) -> dict:
        """Collect CWA diagnostics from all layers (if activation is CWA)."""
        stats = {}
        for i, block in enumerate(self.blocks):
            act = block.mlp.act
            if isinstance(act, CWAActivation):
                stats[f"layer_{i}"] = {
                    "J": act._last_J,
                    "J_s_bar": act._last_J_s_bar,
                    "K": act._last_K,
                    "mode": act._last_mode,
                }
        return stats
