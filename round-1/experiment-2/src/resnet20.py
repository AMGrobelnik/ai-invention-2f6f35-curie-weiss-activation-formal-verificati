"""ResNet-20 with pluggable activation and optional BatchNorm."""
import torch
import torch.nn as nn

from cwa import CWA


def _make_act(act_name: str, planes: int) -> nn.Module:
    if act_name == "CWA":
        return CWA()
    if act_name == "GELU":
        return nn.GELU()
    if act_name == "SELU":
        return nn.SELU()
    if act_name == "ReLU":
        return nn.ReLU()
    if act_name == "tanhLN":
        return nn.Sequential(nn.Tanh(), nn.GroupNorm(1, planes))
    if act_name == "GELULN":
        return nn.Sequential(nn.GELU(), nn.GroupNorm(1, planes))
    raise ValueError(f"Unknown activation: {act_name}")


class BasicBlock(nn.Module):
    def __init__(self, in_planes: int, planes: int, stride: int, act_name: str, use_bn: bool):
        super().__init__()
        self.conv1 = nn.Conv2d(in_planes, planes, 3, stride=stride, padding=1, bias=not use_bn)
        self.bn1 = nn.BatchNorm2d(planes) if use_bn else nn.Identity()
        self.conv2 = nn.Conv2d(planes, planes, 3, stride=1, padding=1, bias=not use_bn)
        self.bn2 = nn.BatchNorm2d(planes) if use_bn else nn.Identity()

        self.act1 = _make_act(act_name, planes)
        self.act2 = _make_act(act_name, planes)

        self.shortcut = nn.Sequential()
        if stride != 1 or in_planes != planes:
            layers: list[nn.Module] = [nn.Conv2d(in_planes, planes, 1, stride=stride, bias=not use_bn)]
            if use_bn:
                layers.append(nn.BatchNorm2d(planes))
            self.shortcut = nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out = self.act1(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out = out + self.shortcut(x)
        out = self.act2(out)
        return out


class ResNet20(nn.Module):
    def __init__(
        self,
        widths: list[int] = (16, 32, 64),
        n_blocks_per_group: int = 3,
        num_classes: int = 100,
        act_name: str = "GELU",
        use_bn: bool = False,
    ):
        super().__init__()
        self.act_name = act_name
        self.use_bn = use_bn

        self.conv0 = nn.Conv2d(3, widths[0], 3, padding=1, bias=not use_bn)
        self.bn0 = nn.BatchNorm2d(widths[0]) if use_bn else nn.Identity()
        self.act0 = _make_act(act_name, widths[0])

        self.group1 = self._make_group(widths[0], widths[0], n_blocks_per_group, stride=1)
        self.group2 = self._make_group(widths[0], widths[1], n_blocks_per_group, stride=2)
        self.group3 = self._make_group(widths[1], widths[2], n_blocks_per_group, stride=2)

        self.pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Linear(widths[2], num_classes)

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode="fan_out", nonlinearity="relu")
            elif isinstance(m, nn.Linear):
                nn.init.xavier_uniform_(m.weight)
                if m.bias is not None:
                    nn.init.zeros_(m.bias)

    def _make_group(self, in_planes: int, planes: int, n_blocks: int, stride: int) -> nn.Sequential:
        blocks: list[nn.Module] = [BasicBlock(in_planes, planes, stride, self.act_name, self.use_bn)]
        for _ in range(n_blocks - 1):
            blocks.append(BasicBlock(planes, planes, 1, self.act_name, self.use_bn))
        return nn.Sequential(*blocks)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out = self.act0(self.bn0(self.conv0(x)))
        out = self.group1(out)
        out = self.group2(out)
        out = self.group3(out)
        out = self.pool(out).flatten(1)
        return self.fc(out)

    def collect_cwa_stats(self) -> list[dict]:
        stats = []
        for name, module in self.named_modules():
            if isinstance(module, CWA):
                stats.append(
                    {
                        "layer": name,
                        "J": module.last_J,
                        "J_s_bar": module.last_J_s_bar,
                        "k": module.last_k,
                        "mode": module.last_mode,
                    }
                )
        return stats
