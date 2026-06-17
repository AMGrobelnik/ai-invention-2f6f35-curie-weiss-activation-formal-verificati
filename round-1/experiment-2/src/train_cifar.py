"""Training loop, data loaders, and per-block J*s_bar logging for CIFAR-100."""
import math
import time
from pathlib import Path

import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from loguru import logger

from cwa import CWA
from resnet20 import ResNet20


def get_cifar100_loaders(batch_size: int = 128, data_dir: str = "./data"):
    mean = (0.5071, 0.4867, 0.4408)
    std = (0.2675, 0.2565, 0.2761)

    train_transform = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])
    test_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])

    train_ds = torchvision.datasets.CIFAR100(root=data_dir, train=True, download=True, transform=train_transform)
    test_ds = torchvision.datasets.CIFAR100(root=data_dir, train=False, download=True, transform=test_transform)

    train_loader = torch.utils.data.DataLoader(
        train_ds, batch_size=batch_size, shuffle=True,
        num_workers=2, pin_memory=True, persistent_workers=True,
    )
    test_loader = torch.utils.data.DataLoader(
        test_ds, batch_size=256, shuffle=False,
        num_workers=2, pin_memory=True, persistent_workers=True,
    )
    return train_loader, test_loader


def evaluate(model: nn.Module, loader, device: torch.device) -> float:
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            correct += (model(x).argmax(1) == y).sum().item()
            total += y.size(0)
    return correct / total


def train_one_config(
    act_name: str,
    widths: list[int],
    use_bn: bool,
    num_classes: int = 100,
    epochs: int = 100,
    lr: float = None,
    seed: int = 0,
    device: torch.device = None,
    checkpoint_path: str = None,
) -> dict:
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if lr is None:
        lr = 0.1 if use_bn else 0.01

    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    model = ResNet20(widths=widths, act_name=act_name, use_bn=use_bn, num_classes=num_classes)
    model = model.to(device)

    optimizer = torch.optim.SGD(model.parameters(), lr=lr, momentum=0.9, weight_decay=5e-4)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
    criterion = nn.CrossEntropyLoss()

    train_loader, test_loader = get_cifar100_loaders()

    per_block_J_s_bar_history: dict[str, list[float]] = {}
    test_acc_per_epoch: list[float] = []
    t_start = time.time()

    for epoch in range(epochs):
        model.train()
        epoch_block_J_s_bar: dict[str, list[float]] = {}

        for x, y in train_loader:
            x, y = x.to(device), y.to(device)
            optimizer.zero_grad()
            logits = model(x)
            loss = criterion(logits, y)
            loss.backward()

            if not use_bn:
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

            optimizer.step()

            if act_name == "CWA":
                # Clamp J_raw to keep J <= 0.95 (prevent instability)
                with torch.no_grad():
                    for m in model.modules():
                        if isinstance(m, CWA):
                            m.J_raw.data.clamp_(max=2.944)

                stats = model.collect_cwa_stats()
                for s in stats:
                    if s["J_s_bar"] is not None:
                        name = s["layer"]
                        epoch_block_J_s_bar.setdefault(name, []).append(s["J_s_bar"])

        scheduler.step()

        if act_name == "CWA":
            for name, vals in epoch_block_J_s_bar.items():
                avg = float(sum(vals) / len(vals)) if vals else 0.0
                per_block_J_s_bar_history.setdefault(name, []).append(avg)

        test_acc = evaluate(model, test_loader, device)
        test_acc_per_epoch.append(test_acc)

        if epoch % 10 == 0:
            logger.info(f"  epoch={epoch:3d} test_acc={test_acc:.4f}")

        # Save partial checkpoint
        if checkpoint_path and epoch % 20 == 0:
            torch.save({"epoch": epoch, "test_acc": test_acc}, checkpoint_path + ".ckpt")

    train_time = time.time() - t_start
    logger.info(f"  Done: final_acc={test_acc_per_epoch[-1]:.4f} time={train_time:.0f}s")

    return {
        "final_test_acc": test_acc_per_epoch[-1],
        "test_acc_per_epoch": test_acc_per_epoch,
        "per_block_J_s_bar_history": per_block_J_s_bar_history,
        "train_time_sec": train_time,
    }
