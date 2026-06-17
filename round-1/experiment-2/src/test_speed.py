#!/usr/bin/env python3
"""Speed test for training configurations."""
import sys, time, torch
sys.path.insert(0, '.')

from train_cifar import train_one_config, get_cifar100_loaders

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Device: {device}')

# Test data loading speed
print('\n--- DataLoader speed ---')
t0 = time.time()
tl, vl = get_cifar100_loaders(batch_size=128)
for i, (x, y) in enumerate(tl):
    if i >= 10: break
print(f'10 batches: {time.time()-t0:.2f}s')

# Time 1 CWA epoch
print('\n--- CWA standard_no_bn ---')
t0 = time.time()
r = train_one_config('CWA', [16, 32, 64], use_bn=False, epochs=1, seed=0, device=device)
t_cwa = time.time() - t0
print(f'CWA 1 epoch: {t_cwa:.1f}s  acc={r["test_acc_per_epoch"]}')

# Time 1 GELU epoch
print('\n--- GELU standard_no_bn ---')
t0 = time.time()
r2 = train_one_config('GELU', [16, 32, 64], use_bn=False, epochs=1, seed=0, device=device)
t_gelu = time.time() - t0
print(f'GELU 1 epoch: {t_gelu:.1f}s  acc={r2["test_acc_per_epoch"]}')

print(f'\nCWA/GELU ratio: {t_cwa/t_gelu:.1f}x')
