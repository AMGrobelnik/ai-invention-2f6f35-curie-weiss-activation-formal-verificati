#!/usr/bin/env python3
"""Build partial method_out.json from checkpoint for immediate validation."""
import json
from pathlib import Path

DEPTHS = [6, 10, 20]
HIDDEN_DIM = 256
NUM_SEEDS = 3
NUM_EPOCHS = 25
BATCH_SIZE = 256
LR = 1e-3
ACTIVATIONS_EXP1 = ['relu', 'gelu', 'swish', 'tanh', 'selu', 'tanh_ln', 'gelu_ln', 'competing', 'cwa']
FIXED_J_VALUES = [0.1, 0.3, 0.5, 0.7, 0.9]
DEPTH_EXP4 = 10

# Load checkpoint data
ckpt = {}
ckpt_path = Path("logs/exp1_checkpoint.json")
if ckpt_path.exists():
    ckpt = json.loads(ckpt_path.read_text())

# Empty Exp4
exp4_results = {'fixed_j': {}, 'learned_j': None}

# Build hypothesis test placeholder
hyp_test = {
    'overall_verdict': 'INCONCLUSIVE',
    'gradient_stability': {},
    'accuracy_improvements_vs_gelu': {},
    'soc_finding': {}
}

def get_result(dataset, depth_key, act_name):
    """Get result from checkpoint, or None if not available yet."""
    return ckpt.get(dataset, {}).get(depth_key, {}).get(act_name, None)

examples_cifar10 = []
examples_mnist = []

for depth in DEPTHS:
    depth_key = f'depth_{depth}'
    depth_data = ckpt.get('cifar10', {}).get(depth_key, {})
    for act_name in ACTIVATIONS_EXP1:
        act_data = depth_data.get(act_name, {})
        acc_mean = act_data.get('accuracy_mean')
        grad_ratio = act_data.get('gradient_ratio_mean')
        gelu_acc = depth_data.get('gelu', {}).get('accuracy_mean') or 0

        inp = (f"Train {depth}-layer unnormalized MLP with {act_name} activation "
               f"on CIFAR-10 (hidden_dim={HIDDEN_DIM}, batch={BATCH_SIZE}, "
               f"epochs={NUM_EPOCHS}, seeds={NUM_SEEDS}). "
               f"Measure gradient ratio and test accuracy.")
        out = ("CWA hypothesis: gradient ratio < 2.0 (stable) vs GELU > 5.0 "
               "(vanishing/exploding), competitive accuracy within 5pp of GELU.")

        examples_cifar10.append({
            'input': inp,
            'output': out,
            'predict_accuracy': str(round(acc_mean, 4)) if acc_mean is not None else 'None',
            'predict_gradient_ratio': str(round(grad_ratio, 4)) if grad_ratio is not None else 'None',
            'metadata_depth': depth,
            'metadata_activation': act_name,
            'metadata_dataset': 'cifar10',
            'metadata_num_seeds': NUM_SEEDS,
            'metadata_accuracy_vs_gelu_delta': str(round(float(acc_mean or 0) - float(gelu_acc), 4)),
        })

    # MNIST examples (not run - placeholder)
    for act_name in ACTIVATIONS_EXP1:
        examples_mnist.append({
            'input': (f"Train {depth}-layer unnormalized MLP with {act_name} on MNIST "
                      f"(hidden_dim={HIDDEN_DIM}, seeds={NUM_SEEDS}, epochs={NUM_EPOCHS})."),
            'output': "CWA hypothesis: gradient ratio < 2.0 with competitive accuracy.",
            'predict_accuracy': 'None',
            'predict_gradient_ratio': 'None',
            'metadata_depth': depth,
            'metadata_activation': act_name,
            'metadata_dataset': 'mnist',
            'metadata_num_seeds': 0,
            'metadata_accuracy_vs_gelu_delta': '0',
        })

# Exp4 placeholder examples
examples_exp4 = []
for jv in FIXED_J_VALUES:
    examples_exp4.append({
        'input': (f"Train 10-layer MLP on CIFAR-10 with fixed J={jv} CWA "
                  f"(hidden_dim={HIDDEN_DIM}, seeds={NUM_SEEDS}). Fixed-J ablation."),
        'output': "Learned J should outperform fixed J by finding SOC critical point.",
        'predict_accuracy': 'None',
        'predict_gradient_ratio': 'None',
        'predict_j_s_bar_mean': 'None',
        'metadata_j_condition': str(jv),
        'metadata_dataset': 'cifar10_exp4',
        'metadata_depth': DEPTH_EXP4,
        'metadata_num_seeds': NUM_SEEDS,
    })
examples_exp4.append({
    'input': (f"Train 10-layer MLP on CIFAR-10 with learned J (CWA) "
              f"(hidden_dim={HIDDEN_DIM}, seeds={NUM_SEEDS}). Learned J ablation."),
    'output': "Learned J should self-organize to SOC and achieve best gradient stability.",
    'predict_accuracy': 'None',
    'predict_gradient_ratio': 'None',
    'predict_j_s_bar_mean': 'None',
    'metadata_j_condition': 'learned',
    'metadata_dataset': 'cifar10_exp4',
    'metadata_depth': DEPTH_EXP4,
    'metadata_num_seeds': NUM_SEEDS,
})

# Hypothesis test summary
examples_hyp = [{
    'input': (f"Evaluate CWA hypothesis: gradient ratio < 2.0 on ≥10-layer unnormalized "
              f"networks vs GELU > 5.0. Datasets: CIFAR-10. Depths: {DEPTHS}. Seeds: {NUM_SEEDS}."),
    'output': ("CONFIRM if CWA ratio < 2.0 AND GELU > 5.0 at depth≥10. "
               "DISCONFIRM if accuracy delta < 0.5pp. INCONCLUSIVE otherwise."),
    'predict_overall_verdict': hyp_test['overall_verdict'],
    'predict_cwa_gradient_ratio_d10': 'None',
    'predict_gelu_gradient_ratio_d10': 'None',
    'predict_primary_criterion_d10': 'False',
    'predict_soc_mean_j_s_bar': 'None',
    'predict_soc_fraction_above_0_8': 'None',
    'metadata_verdict': hyp_test['overall_verdict'],
}]

method_out = {
    'metadata': {
        'method_name': 'CWA (Coupled-Weight Activation)',
        'description': (
            'CWA uses mean-field fixed-point iteration with learnable coupling J. '
            'Hybrid IFT/unrolled backprop. Tested against 8 baselines across depths '
            '6/10/20 on CIFAR-10 (Exp1) and fixed-J ablation (Exp4). '
            'NOTE: Experiment in progress - partial results shown.'
        ),
        'hypothesis_verdict': hyp_test['overall_verdict'],
        'depths': DEPTHS,
        'hidden_dim': HIDDEN_DIM,
        'num_seeds': NUM_SEEDS,
        'num_epochs': NUM_EPOCHS,
        'batch_size': BATCH_SIZE,
        'lr': LR,
        'activations': ACTIVATIONS_EXP1,
        'datasets': ['cifar10'],
        'status': 'experiment_in_progress',
        'completed_configs': {
            k: list(v.keys()) for k, v in ckpt.get('cifar10', {}).items()
        },
        'gradient_stability_results': hyp_test.get('gradient_stability', {}),
        'accuracy_improvements_vs_gelu': hyp_test.get('accuracy_improvements_vs_gelu', {}),
        'soc_finding': hyp_test.get('soc_finding', {}),
    },
    'datasets': [
        {'dataset': 'cifar10_gradient_stability', 'examples': examples_cifar10},
        {'dataset': 'mnist_gradient_stability', 'examples': examples_mnist},
        {'dataset': 'cifar10_fixed_j_ablation', 'examples': examples_exp4},
        {'dataset': 'hypothesis_test', 'examples': examples_hyp},
    ]
}

total_examples = sum(len(d['examples']) for d in method_out['datasets'])
print(f"Total examples: {total_examples}")
print(f"  cifar10: {len(examples_cifar10)}")
print(f"  mnist: {len(examples_mnist)}")
print(f"  exp4: {len(examples_exp4)}")
print(f"  hyp: {len(examples_hyp)}")

Path("method_out.json").write_text(json.dumps(method_out, indent=2, default=str))
print(f"Written method_out.json ({Path('method_out.json').stat().st_size/1024:.1f} KB)")
