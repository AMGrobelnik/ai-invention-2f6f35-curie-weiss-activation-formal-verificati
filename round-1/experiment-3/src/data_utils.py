"""Data loading utilities for Shakespeare (char-level) and WikiText-2 (BPE)."""

import os
from pathlib import Path
from typing import Callable
import requests
import torch
from loguru import logger


def load_shakespeare(
    seq_len: int, batch_size: int, device: str
) -> tuple[Callable, int, Callable]:
    """Download and tokenize Tiny Shakespeare.

    Returns (get_batch_fn, vocab_size, decode_fn).
    """
    workspace = Path(__file__).parent
    data_dir = workspace / "data"
    data_dir.mkdir(exist_ok=True)
    path = data_dir / "shakespeare.txt"

    if not path.exists():
        url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
        logger.info(f"Downloading Shakespeare from {url}")
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            path.write_text(r.text)
            logger.info(f"Downloaded {len(r.text):,} chars")
        except Exception as e:
            logger.warning(f"Download failed ({e}), trying fallback URL")
            fallback = "https://www.gutenberg.org/files/100/100-0.txt"
            r = requests.get(fallback, timeout=30)
            path.write_text(r.text[:1_000_000])  # first 1M chars
            logger.info("Used Gutenberg fallback")

    text = path.read_text()
    chars = sorted(set(text))
    vocab_size = len(chars)
    stoi = {ch: i for i, ch in enumerate(chars)}
    itos = {i: ch for ch, i in stoi.items()}
    data = torch.tensor([stoi[c] for c in text], dtype=torch.long)
    n = len(data)
    train_data = data[: int(0.90 * n)]
    val_data = data[int(0.90 * n) : int(0.95 * n)]
    test_data = data[int(0.95 * n) :]
    logger.info(
        f"Shakespeare: vocab={vocab_size}, train={len(train_data):,}, "
        f"val={len(val_data):,}, test={len(test_data):,}"
    )

    def get_batch(split: str) -> tuple[torch.Tensor, torch.Tensor]:
        d = {"train": train_data, "val": val_data, "test": test_data}[split]
        ix = torch.randint(len(d) - seq_len, (batch_size,))
        x = torch.stack([d[i : i + seq_len] for i in ix]).to(device)
        y = torch.stack([d[i + 1 : i + seq_len + 1] for i in ix]).to(device)
        return x, y

    decode = lambda ids: "".join(itos[i] for i in ids)
    return get_batch, vocab_size, decode


def load_wikitext2(
    seq_len: int, batch_size: int, device: str
) -> tuple[Callable, int]:
    """Load WikiText-2 with tiktoken BPE (gpt2 encoding, vocab=50257).

    Returns (get_batch_fn, vocab_size).
    """
    import tiktoken
    from datasets import load_dataset

    enc = tiktoken.get_encoding("gpt2")
    vocab_size = enc.n_vocab
    logger.info(f"Loading WikiText-2 with tiktoken gpt2 (vocab={vocab_size})")

    try:
        ds = load_dataset("Salesforce/wikitext", "wikitext-2-raw-v1")
    except Exception:
        ds = load_dataset("wikitext", "wikitext-2-raw-v1")

    def tokenize_split(split_name: str) -> torch.Tensor:
        texts = ds[split_name]["text"]
        tokens = []
        for t in texts:
            t = t.strip()
            if t:
                tokens.extend(enc.encode_ordinary(t))
        logger.info(f"  {split_name}: {len(tokens):,} tokens")
        return torch.tensor(tokens, dtype=torch.long)

    train_data = tokenize_split("train")
    val_data = tokenize_split("validation")
    test_data = tokenize_split("test")

    def get_batch(split: str) -> tuple[torch.Tensor, torch.Tensor]:
        d = {"train": train_data, "val": val_data, "test": test_data}[split]
        ix = torch.randint(len(d) - seq_len, (batch_size,))
        x = torch.stack([d[i : i + seq_len] for i in ix]).to(device)
        y = torch.stack([d[i + 1 : i + seq_len + 1] for i in ix]).to(device)
        return x, y

    return get_batch, vocab_size
