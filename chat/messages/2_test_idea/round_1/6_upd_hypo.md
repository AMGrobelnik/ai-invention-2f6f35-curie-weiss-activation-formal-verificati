# upd_hypo — test_idea

> Phase: `invention_loop` · round 1 · `upd_hypo`
> Run: `run_6gT5lHFn8559` — Novel Activation Function
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-06-16 19:11:13 UTC

```
model: claude-sonnet-4-6 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/upd_hypo/upd_hypo
```

### [2] SYSTEM-USER prompt · 2026-06-16 19:11:20 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviser (Step 3.6: UPD_HYPO in the invention loop)

You received the current hypothesis, all artifacts, and the paper draft.
Revise the hypothesis based on what the evidence supports.

Honest revision → focused research. Inflated confidence → wasted iteration.
</your_role>
</ai_inventor_context>

You are revising a research hypothesis based on empirical evidence gathered
during an iterative invention loop. Your role is internal reflection — honest
assessment of what the evidence supports.

SCOPE: Your ONLY output is the revised hypothesis text. You do NOT run code,
produce artifacts, fix bugs, or otherwise act on the evidence yourself — the
next iteration of the invention loop will spawn fresh artifacts based on your
revised hypothesis. Reflect on the evidence and rewrite the hypothesis;
nothing else.

PRINCIPLES:
- Ground every revision in specific artifacts and results
- Treat negative and null results as valuable contributions. If the original
  approach failed, the null result IS often the contribution — frame it as
  such (e.g. "X does not improve Y under conditions Z"). Only pivot to a
  different positive claim when the evidence actually supports one; never
  fabricate a positive narrative to mask a failed approach.
- Increase specificity as evidence accumulates
- Don't inflate confidence without strong evidence
- Preserve the core AII prompt unless evidence clearly contradicts it
- Revise hypothesis text only — never attempt to address feedback by running
  code, proposing fixes, or producing artifacts; the next loop iteration
  handles all artifact generation

<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: >-
  Curie-Weiss Activation with Hybrid IFT/Unrolled Backprop: Learnable Within-Layer Mean-Field Coupling for Gradient Stability
  in Unnormalized Deep Networks
hypothesis: >-
  A neural network hidden-layer activation function defined as the fixed point y* of the Curie-Weiss mean-field self-consistency
  equation — y_i = tanh(x_i + J·mean_neurons(y)) for all neurons i in a layer, where J = σ(J_raw) ∈ (0,1) is a per-layer learnable
  scalar coupling — will outperform standard pointwise hidden-layer activations (ReLU, GELU, Swish, Tanh) and self-normalizing
  baselines (SELU, tanh+LayerNorm, GELU+LayerNorm) in gradient stability in deep unnormalized networks (≥10 layers) and on
  practical benchmarks including CIFAR-100 (ResNet-20) and character-level language modeling (6-layer, 256-hidden GPT on Tiny
  Shakespeare and WikiText-2), because: (1) the within-sample mean-field coupling y_i ← tanh(x_i + J·mean_neurons(y)) implements
  a learned, parameter-efficient form of collective output-based gain control unavailable to any purely pointwise activation
  and categorically distinct from LayerNorm (which normalizes inputs, not outputs); (2) a hybrid backpropagation strategy
  — unrolled autograd when J·s̄ < 0.8 (few iterations, modest memory), implicit-function-theorem (IFT) gradient when J·s̄
  ≥ 0.8 (O(1) activation memory, accuracy maintained via adaptive tolerance δ = 1e-4·(1−J·s̄)) — makes the near-critical regime
  computationally honest about both wall-clock and peak GPU memory; (3) finite-width noise O(1/√n) in narrow layers (e.g.,
  ResNet-20 first block at n=16) is acknowledged and empirically characterized by comparing per-block CWA effectiveness as
  n varies from 16 to 256; and (4) whether J·s̄ self-organizes toward 1 during training is a primary empirical finding — not
  an assumption — validated by controlled fixed-J ablations (J fixed at {0.1, 0.3, 0.5, 0.7, 0.9}).
motivation: >-
  All standard hidden-layer activation functions in MLP blocks — ReLU, GELU, Swish, tanh — are applied pointwise: each neuron's
  output depends only on its own pre-activation. This independence requires external normalization (BatchNorm, LayerNorm)
  or careful weight initialization to maintain gradient signal across depth. Unnormalized deep networks are highly relevant
  to three practical settings in 2026: (a) on-device/edge inference where normalization's running-statistics computation is
  expensive in memory-constrained hardware and distorts quantization; (b) scientific neural operators (physics-informed networks,
  neural PDEs) where normalization distorts physical conservation laws embedded in the activations — the Competing Nonlinearities
  paper (Lesser & Chowdhury, 2026) explicitly highlights these as target applications for smooth scale-invariant propagation;
  and (c) fast-inference transformer variants that eliminate LayerNorm to reduce memory bandwidth. In these settings, CWA
  provides a drop-in nonlinearity that intrinsically couples neurons within a layer via learnable scalar J, creating gain
  control without external normalization. Criticality theory in deep learning (Poole et al. 2016; Yang & Schoenholz 2017)
  shows networks at the 'edge of chaos' — where the layer Jacobian's singular values are near unity, i.e., J·s̄ ≈ 1 — train
  fastest and generalize best. Existing approaches achieve this only at initialization (Yang/Poole weight variance tuning)
  or through random static mixtures (Competing Nonlinearities 2026: quenched disorder, no learnable parameter). Neither provides
  a per-layer learned mechanism adaptive to the actual input distribution during training. CWA fills this gap with a single
  additional scalar per layer, implemented via Curie-Weiss mean-field physics from ferromagnetism, with the benefits tested
  honestly via comprehensive baselines and explicit accounting of finite-width effects and backpropagation memory costs.
assumptions:
- >-
  The adaptive-K fixed-point iteration m_{t+1} = mean_neurons(tanh(x + J·m_t)) converges with geometric rate ρ = J·s̄ = J·mean(sech²(x+J·m*))
  per step (rigorously bounded by the Banach fixed-point theorem since ρ = |dF/dm| = J·s̄ < 1 when J ∈ (0,1)). The stopping
  rule |m_{t+1}−m_t| < δ terminates in K*(ρ) ≈ log(δ/|m_0−m*|)/log(ρ) steps, finite for all J ∈ (0,1). The 'mean' in mean_neurons(y)
  = (1/n)Σ_i y_i is over the n neurons within a single sample (not the mini-batch), distinguishing CWA from batch-dependent
  methods like BatchNorm.
- >-
  The hybrid backpropagation strategy is mathematically sound and practically efficient: (a) when J·s̄ < 0.8, unrolled autograd
  through K* ≤ ~10 iterations provides exact gradients with manageable O(K*·batch·n) activation memory; (b) when J·s̄ ≥ 0.8,
  the implicit function theorem gradient ∂m*/∂x = sech²(x+J·m*)/(1−J·s̄), ∂m*/∂J = s̄·m*/(1−J·s̄) provides O(1) activation
  memory — storing only the converged m* as in the DEQ literature (Bai et al., arXiv:1909.01377, NeurIPS 2019 Spotlight, which
  demonstrated up to 88% memory reduction via IFT). IFT with inexact fixed-point residual r = |F(m*)| introduces gradient
  bias O(r/(1−J·s̄)); the adaptive tolerance δ(J·s̄) = 1e-4·(1−J·s̄) bounds this bias uniformly at O(1e-4) across all coupling
  strengths. Both approaches require J·s̄ < 1, guaranteed by J = σ(J_raw) ∈ (0,1).
- >-
  The sigmoid parameterization J = σ(J_raw) hard-constrains J ∈ (0,1), preventing the bistable regime J ≥ 1 and ensuring global
  convergence. J_raw is initialized at 0 so J starts at 0.5. Finite-width correction: at layer width n, the empirical mean
  m* = (1/n)Σ_i tanh(x_i + J·m*) has fluctuations of O(1/√n) relative to unit-scale activations. At n=16 (ResNet-20 first
  block), this is a ~25% noise floor, meaning the mean-field physics is an approximation at narrow widths. The sharp critical
  point J·s̄ = 1 is expected to smear out analogously to finite-size scaling near phase transitions. This is characterized
  empirically by comparing CWA per-block effectiveness across widths.
- >-
  Whether J·s̄ self-organizes toward 1 during training is an empirical question, not an assumption. Gradient descent has incentive
  to approach J·s̄ = 1 because the IFT Jacobian ∂y_i/∂x_i = sech²(x_i+J·m*)/(1−J·s̄) diverges there, potentially improving
  gradient flow; but this amplification may also destabilize training. The fixed-J ablation study ({0.1, 0.3, 0.5, 0.7, 0.9})
  tests whether benefits of CWA require learned adaptation of J or can be achieved with any fixed coupling.
- >-
  The Competing Nonlinearities (tanh+Swish@p_c) baseline is implemented with p_c derived analytically following Lesser & Chowdhury
  (2026, arXiv:2605.05294): p_c is the mixing fraction where the mixture kernel function g_mix(K) = p·g_tanh(K) + (1−p)·g_swish(K)
  satisfies g_mix'(K*) = 1 at the fixed point K* (edge-of-chaos condition, confirmed as 'Analytical prediction of pc' in Section
  III.A of their paper). For ResNet-20 and GPT experiments where the architecture differs from the paper's MLPs, p_c is additionally
  tuned as a hyperparameter on the validation set with p_c ∈ {0.1, 0.3, 0.5, 0.7, 0.9}, and both conditions are reported.
investigation_approach: |-
  Implement CWA in PyTorch as a custom nn.Module with J = torch.sigmoid(J_raw), J_raw an nn.Parameter initialized at 0 (J ≈ 0.5). Forward pass: iterate m ← mean_neurons(tanh(x + J·m)) from m_0=0 until |m_{t+1}−m_t| < δ(J·s̄) = 1e-4·(1−J·s̄) (cap K_max=50); output y_i = tanh(x_i + J·m*). Backward pass: HYBRID — if J·s̄ < 0.8 (detected from forward statistics), use unrolled autograd; if J·s̄ ≥ 0.8, detach computation graph and apply IFT gradient manually via torch.autograd.Function backward: ∂m*/∂x = sech²(x+J·m*)/(1−J·s̄), ∂m*/∂J = s̄·m*/(1−J·s̄). At each forward call, log K, J, J·s̄, backprop mode (unrolled vs IFT), and peak activation memory for the CWA layer.

  Experiment 1 — Gradient stability in deep unnormalized MLPs: Train MLPs at depths {6, 10, 20} with 256 hidden units on MNIST and CIFAR-10 (pixel vectors, no normalization). Compare CWA vs ReLU, GELU, Swish, tanh, SELU, tanh+LN, GELU+LN, tanh+Swish@p_c (p_c analytically derived per depth). Measure: gradient norm ratio log|∇L_{layer1}|/log|∇L_{layerL}|, final accuracy, convergence speed. 5 seeds.

  Experiment 2 — ResNet-20 on CIFAR-100 with width analysis: Replace activation with CWA in each residual block. Run (a) standard ResNet-20 (widths 16/32/64) and (b) wide ResNet-20 (4× channels: widths 64/128/256). Report per-block J·s̄ and accuracy improvement vs GELU as a function of block width n — the hypothesis predicts stronger CWA benefit at wider n where mean-field is more accurate. Both BatchNorm and no-BatchNorm variants.

  Experiment 3 — Language modeling at non-toy scale: Replace GELU in MLP sublayers with CWA in two settings: (a) 6-layer, 256-hidden character-level GPT on Tiny Shakespeare (sequence length 256, 10K steps) and (b) 6-layer, 256-hidden word-level GPT on WikiText-2 (sequence length 128, 20K steps). Compare test BPC (character) and perplexity (word) vs GELU, GELU+LN, SELU, tanh+Swish@p_c (tuned on validation). Monitor K, J, J·s̄, backprop mode, peak GPU memory per layer per epoch.

  Experiment 4 — Fixed-J ablation: Train 10-layer unnormalized MLP on CIFAR-10 with J frozen at {0.1, 0.3, 0.5, 0.7, 0.9} vs learned J. Compare final accuracy and gradient ratio. Test whether J self-organizes and whether criticality (high J·s̄) is necessary.

  Experiment 5 — Computational overhead characterization: Measure wall-clock time per batch AND peak GPU memory for CWA vs GELU as a function of J·s̄ during training, tracking which backprop mode triggered. Report K*(J·s̄) curve and memory(J·s̄)/memory(GELU) ratio to establish the practical overhead envelope of the hybrid strategy. Total LLM API cost: $0 (pure neural network experiments).
success_criteria: >-
  CONFIRM if: (1) CWA in unnormalized deep MLPs (≥10 layers) achieves gradient norm ratio |log|∇L_1|/log|∇L_L|| < 2.0 while
  GELU baseline (no normalization) has ratio > 5.0 — demonstrating CWA's core gradient stability claim; AND (2) CWA achieves
  ≥0.5% higher final accuracy than GELU on at least 2 of 3 benchmark tasks (CIFAR-10 deep MLP, CIFAR-100 ResNet-20, 6L/256H
  language model), measured with 95% confidence intervals over 5 seeds; AND (3) the hybrid backprop strategy keeps peak GPU
  memory ≤ 2× GELU across all J·s̄ values. DISCONFIRM if: (1) CWA performs within noise of all pointwise baselines on all
  tasks, OR (2) tanh+LayerNorm or SELU matches or exceeds CWA on all tasks — indicating the benefit is explained by collective
  normalization not output-coupling self-consistency, OR (3) the hybrid strategy fails to prevent peak GPU memory exceeding
  5× GELU in the near-critical regime. PARTIAL CONFIRM (targeted practical contribution) if: CWA improves gradient stability
  and accuracy in unnormalized deep MLPs but not in normalized networks (ResNet+BN, GPT with LN) — characterizing CWA's contribution
  as drop-in normalization-free gain control for edge/scientific settings. WIDTH FINDING: Report whether CWA's per-block improvement
  correlates positively with block width n (supporting the mean-field large-n prediction) or is width-independent. SOC FINDING:
  Report whether J·s̄ concentrates near 1 in successful configurations or settles at scattered values.
related_works:
- >-
  Boltzmann Attention (Kim & Park, arXiv:2606.12478, NeurIPS 2026): Proposes learnable pairwise Ising couplings J_{jk} in
  the ATTENTION OPERATOR of transformers, enabling inter-position cooperative/antagonistic co-attention. The abstract states
  it 'augments the usual data-dependent local fields with learnable pairwise couplings, allowing the model to represent inter-position
  correlations beyond those captured by softmax or sigmoid attention.' Experiments on character-level language modeling and
  synthetic bracket matching confirm improvements. Key distinction from CWA: Boltzmann Attention replaces the attention operator
  (inter-token interactions across sequence positions via quadratic O(n²) pairwise couplings J_{jk}); CWA replaces the ACTIVATION
  NONLINEARITY (inter-neuron coupling within a single layer's hidden dimension via a single scalar J per layer). These are
  complementary components that could be combined.
- >-
  Competing Nonlinearities (Lesser & Chowdhury, arXiv:2605.05294, May 2026): Achieves edge-of-chaos criticality by having
  'each neuron independently and randomly draw its activation from a two-component distribution with mixing fraction p' —
  specifically a mixture of tanh and Swish. The abstract confirms: at p_c, 'the network acquires statistical scale invariance,
  with depth-independent variance, without sacrificing smoothness.' The PDF confirms p_c is analytically derived in Section
  III.A as the mixing fraction where the mixture kernel function g_mix(K) satisfies g_mix'(K*) = 1 at the variance fixed point
  K* (edge-of-chaos condition). Key distinction from CWA: this is a STATIC quenched mixture at initialization (no learnable
  parameter, no self-consistency feedback, no inter-neuron coupling — each neuron draws independently). CWA introduces a LEARNABLE
  coupling J adapted by gradient descent with explicit inter-neuron feedback.
- >-
  Deep Equilibrium Models / DEQ (Bai, Kolter, Koltun, arXiv:1909.01377, NeurIPS 2019 Spotlight): 'Directly finds equilibrium
  points via root-finding... equivalent to running an infinite depth (weight-tied) feedforward network... can analytically
  backpropagate through the equilibrium point using implicit differentiation... only constant memory, regardless of the effective
  depth.' Demonstrates up to 88% memory reduction on WikiText-103 via IFT. Applied to sequence models (transformers, trellis
  networks). Key distinction from CWA: DEQ replaces the full sequential layer (the entire weight-matrix + activation mapping
  is solved to a fixed point, requiring O(n²) Newton steps per iteration); CWA is a lightweight activation-level operation
  (O(n·K) per layer, scalar-J fixed point, adds one learnable parameter J per layer). CWA is a drop-in activation replacement;
  DEQ is a complete architectural replacement. CWA's hybrid IFT backprop strategy is inspired by DEQ's implicit differentiation
  insight.
- >-
  Deep Implicit Attention (Bal/mcbal, 2021, blog + GitHub repo): Applies Thouless-Anderson-Palmer (TAP) mean-field theory
  to transformer attention mechanisms, showing 'softmax attention does a single, naive mean-field update step' of a random
  Ising model over token positions, and the feedforward layer 'corrects [the] naive mean-field update.' Uses DEQ (arXiv:1909.01377)
  to solve self-consistent mean-field equations of a vector Ising spin model. Key distinction from CWA: this work reformulates
  the ATTENTION OPERATOR (inter-token, operating across sequence positions); CWA adds an intra-layer mean-field coupling to
  the ACTIVATION FUNCTION (within a single hidden dimension, operating across neurons in one layer). These are orthogonal
  architectural components.
- >-
  SELU / Self-Normalizing Neural Networks (Klambauer et al., NeurIPS 2017): Designs Scaled ELU with specific fixed-point statistics
  (mean≈0, var≈1 propagation) that self-normalizes without external normalization. Key distinction: SELU achieves self-normalization
  by tuning the function's fixed-point statistics under normally distributed inputs — it is strictly POINTWISE (each neuron
  depends only on its own pre-activation, no inter-neuron coupling). CWA explicitly averages OUTPUT values across neurons
  and feeds them back via mean_neurons(y), coupling neurons within the layer. SELU is included as a direct baseline.
- >-
  Mean Field Theory of Activation Functions (Milletarì et al., arXiv:1805.08786, 2018): Uses statistical mechanics to derive
  existing activations (tanh, ReLU, Swish) as solutions to energy-based models. Key distinction: this work provides post-hoc
  physical interpretation of known pointwise functions; CWA proposes a NEW activation defined by the actual Curie-Weiss self-consistency
  equation with a learnable coupling J, introducing within-layer neuron coupling absent from all their derived activations.
- >-
  Yang & Schoenholz (2017) 'Mean Field Residual Networks' and Poole et al. (2016) 'Exponential Expressivity': Show that networks
  at the edge of chaos (J·s̄ = 1) train fastest, achieved via careful weight variance initialization. Key distinction: these
  works achieve criticality only through initialization — it drifts during training. CWA provides a learnable mechanism through
  the activation function that can in principle maintain near-critical coupling during training. Whether it does so empirically
  is the primary experimental finding.
inspiration: >-
  This hypothesis is a Level-3 (methodological) cross-domain transfer from statistical physics, specifically the Curie-Weiss
  model of ferromagnetism. In physics, the self-consistency equation m = tanh(β(h + J·m)) describes how an Ising spin aligns
  with external field h plus self-consistent feedback from the average magnetization J·m of all other spins. The critical
  point βJ = 1 marks maximum magnetic susceptibility — tiny external fields produce large magnetization responses. The cross-domain
  insight: just as a ferromagnet near its Curie temperature exhibits maximum input sensitivity, a neural layer near J·s̄ =
  1 should exhibit maximum sensitivity to pre-activations (high gradient signal-to-noise ratio). This revision incorporates
  three additional improvements from reviewer feedback: (1) the computational strategy now uses a hybrid IFT/unrolled-autograd
  approach inspired by the DEQ literature (Bai et al., arXiv:1909.01377), where IFT's O(1) memory advantage (demonstrating
  88% memory reduction in DEQ) is deployed precisely where needed (J·s̄ > 0.8), with adaptive tolerance δ(J·s̄) = 1e-4·(1−J·s̄)
  from perturbation theory of the IFT to maintain constant gradient accuracy; (2) the finite-width noise analysis is inspired
  by finite-size scaling in statistical mechanics, where O(1/√n) fluctuations smear phase transitions — tested empirically
  across layer widths in ResNet-20 standard vs wide variants; (3) the practical motivation is grounded in edge-inference and
  scientific computing settings where normalization is avoided, motivated in part by Lesser & Chowdhury (2026) explicitly
  targeting 'physics-informed architectures' and 'neural-network quantum states' as beneficiaries of smooth normalization-free
  criticality.
terms:
- term: Curie-Weiss Activation (CWA)
  definition: >-
    The proposed hidden-layer activation function defined by the fixed point y* of the mean-field self-consistency equation
    y = tanh(x + J·mean_neurons(y)), where x is the vector of pre-activations, y is the vector of activations, J = σ(J_raw)
    ∈ (0,1) is a per-layer learnable scalar coupling, and mean_neurons(y) = (1/n)Σ_i y_i is the within-sample neuron-wise
    mean (not batch mean). Fixed point found by adaptive-K iteration m_{t+1} = mean_neurons(tanh(x + J·m_t)) until |m_{t+1}−m_t|
    < δ(J·s̄), then y_i = tanh(x_i + J·m*).
- term: Effective Coupling (J·s̄)
  definition: >-
    The critical parameter of CWA, defined as J·s̄ = J·mean_neurons(sech²(x+J·m*)) ∈ (0,1). This is simultaneously: the per-step
    convergence rate of the fixed-point iteration; the spectral norm of the layer's input-output Jacobian; and the quantity
    that governs both gradient stability (higher J·s̄ → higher effective gain) and computational cost (K* ~ O(1/(1−J·s̄))
    iterations near criticality). All experiments track J·s̄ alongside J.
- term: Hybrid IFT/Unrolled Backprop
  definition: >-
    The CWA gradient strategy switching between two modes based on current J·s̄: (a) J·s̄ < 0.8 → unrolled autograd through
    K* iterations (exact gradients, O(K*·batch·n) activation memory, typically K* ≤ ~10 in this regime); (b) J·s̄ ≥ 0.8 →
    IFT gradient via custom backward hook (∂m*/∂x = sech²(x+J·m*)/(1−J·s̄), ∂m*/∂J = s̄·m*/(1−J·s̄), O(1) activation memory
    storing only m*). Inspired by DEQ (Bai et al., arXiv:1909.01377) which showed IFT enables 88% memory reduction at the
    full-layer level.
- term: Adaptive Tolerance δ(J·s̄)
  definition: >-
    The coupling-strength-dependent stopping tolerance: δ(J·s̄) = 1e-4·(1−J·s̄). When using IFT backprop, an inexact fixed-point
    with residual r = |F(m*)| introduces gradient bias O(r/(1−J·s̄)). Setting the stopping threshold at δ(J·s̄) = 1e-4·(1−J·s̄)
    ensures bias O(1e-4) uniformly across all J·s̄ ∈ (0,1), maintaining constant gradient accuracy without over-tightening
    at small J·s̄.
- term: Finite-Width Noise
  definition: >-
    The O(1/√n) fluctuations in the empirical mean m* = (1/n)Σ_i tanh(x_i + J·m*) at layer width n. The Curie-Weiss mean-field
    equation is exact as n→∞; at finite n (e.g., n=16 in ResNet-20 first block), the ~25% noise floor smears the critical
    coupling effect, analogous to finite-size scaling near phase transitions in statistical mechanics. Empirically characterized
    by comparing CWA per-block effectiveness across widths n ∈ {16, 32, 64, 128, 256} in standard vs wide ResNet-20.
- term: Sigmoid Parameterization of J
  definition: >-
    J = σ(J_raw) = 1/(1+exp(−J_raw)) ∈ (0,1), where J_raw ∈ ℝ is the learnable parameter. Hard-constrains J to the monostable
    regime below the ferromagnetic phase transition at J=1, guaranteeing global convergence of fixed-point iterations. J_raw
    initialized at 0 so J starts at 0.5.
- term: Self-Organized Criticality (SOC) Hypothesis
  definition: >-
    The empirical hypothesis — not an assumption — that gradient descent will push J·s̄ toward 1 during training, because
    layers with higher J·s̄ have larger effective Jacobian gain sech²(x_i+J·m*)/(1−J·s̄) and thus more informative gradients.
    Tested by plotting the distribution of learned J·s̄ values at convergence and via the fixed-J ablation study.
- term: Fixed-J Ablation
  definition: >-
    A controlled experiment where J is frozen at specific values {0.1, 0.3, 0.5, 0.7, 0.9} vs. full CWA (learned J). Separates
    whether performance benefit requires: (a) any nonzero coupling (vs. J=0 = pure tanh); (b) a specific critical coupling
    value; or (c) adaptive optimization of J by gradient descent. Directly tests the SOC hypothesis.
- term: Width-Dependent Analysis
  definition: >-
    Empirical characterization of CWA's per-block effectiveness as a function of layer width n, comparing standard ResNet-20
    (widths 16/32/64) vs. wide ResNet-20 (widths 64/128/256). The mean-field physics prediction: CWA benefits increase with
    n as O(1/√n) finite-width noise decreases. If improvements are width-independent, the mechanism differs from mean-field
    coupling.
summary: >-
  We propose the Curie-Weiss Activation (CWA), a hidden-layer activation function where each neuron's output is the fixed
  point of the mean-field self-consistency equation y_i = tanh(x_i + J·mean_neurons(y)), with J = σ(J_raw) ∈ (0,1) a per-layer
  learnable scalar coupling. A hybrid IFT/unrolled-autograd backprop strategy (switching at J·s̄ = 0.8 with adaptive tolerance
  δ(J·s̄) = 1e-4·(1−J·s̄)) makes the near-critical regime memory-efficient and gradient-accurate; finite-width effects (O(1/√n)
  at narrow layers) are characterized by comparing standard vs wide ResNet-20; language model experiments scale to 6-layer/256-hidden
  GPT on both Tiny Shakespeare and WikiText-2; and all critiques from prior review (memory overhead, finite-width mean-field
  breakdown, GPT scale, IFT gradient bias, unnormalized-network motivation, p_c specification) are explicitly addressed with
  evidence from the fetched papers.
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

--- Item 1 ---
id: art_Lj-xi6yJR_yy
type: research
title: 'CWA: DEQ IFT Backward, p_c Derivation, SELU, 2025-2026 Survey'
summary: |-
  This research artifact provides four concrete bodies of verified technical knowledge for implementing the Curie-Weiss Activation (CWA) in the GPU experiment.

  **1. DEQ IFT Backward (arXiv:1909.01377, 2310.18605):** The DEQ backward pass solves the linear system (I - J_f^T)g = ∂L/∂z* via fixed-point iteration using vector-Jacobian products (autograd.grad VJPs), avoiding O(K·n) memory from unrolled backprop and achieving O(n) per step. Crucially, because CWA's fixed point is SCALAR (m* ∈ R, not R^n), this system collapses to a closed-form scalar formula g = y/(1 - J·s̄) where s̄ = mean(sech²(x + J·m*)). No iterative backward solver is needed for CWA. Exact gradient formulas are derived: ∂m*/∂x_i = sech²(x_i+J·m*)/(n(1-J·s̄)); ∂m*/∂J = m*·s̄/(1-J·s̄); ∂y_i/∂J = sech²(x_i+J·m*)·m*/(1-J·s̄). A full efficient O(n) backward implementation is provided.

  **2. Competing Nonlinearities p_c (arXiv:2605.05294):** The critical mixing fraction for a Tanh/Swish incoherent statistical mixture is p_c = 32/35 ≈ 0.914 analytically (K₀→0 limit), derived from g₂^(Tanh)=-2 and g₂^(Swish)=3/16 via Eq. 17: p_c = g₂^(Tanh)/(g₂^(Tanh) - g₂^(Swish)). Empirically p_c ≈ 0.83 at K₀=1. Convention confirmed: p = fraction of SWISH neurons. Perturbative correction: p_c(K₀) = 32/35 - (384/1225)·K₀ + O(K₀²). For non-standard architectures (ResNet, GPT, C_W≠1), analytical p_c is unavailable — use empirical forward-pass calibration.

  **3. SELU Derivation (arXiv:1706.02515):** α₀₁ ≈ 1.6732632423543772, λ₀₁ ≈ 1.0507009873554805 from closed-form equations (Eq. 14). Fixed point (μ,ν)=(0,1) of the distributional mapping g:(μ,ν)→(E[SELU(z)], Var[SELU(z)]) for z~N(μ,ν), with weights N(0,1/n) (LeCun init). Banach fixed-point theorem on domain Ω proves contraction. Mechanistic contrast: SELU is pointwise (no inter-neuron coupling); CWA couples all neurons via the scalar mean-field m*.

  **4. 2025-2026 Novelty Survey:** Five papers assessed. No paper introduces a learnable scalar J coupling within-sample neuron mean to individual pre-activations in an activation function. Boltzmann Attention (2606.12478) uses Ising couplings in the sequence/attention dimension (not hidden); Competing Nonlinearities (2605.05294) uses a fixed (unlearnable) quenched mixture; AlphaEvolve activations (2602.05688) use batch statistics (cross-data, not within-sample); Tuning Universality (2512.00168) and Mean Field Feature Learning (2510.15174) are analysis frameworks with no learnable coupling. CWA's within-sample self-consistent mean-field activation with learnable J is confirmed novel.

  Output files: research_out.json (structured JSON with all findings, formulas, and code patterns) and research_report.md (full synthesis with implementation code).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 2 ---
id: art_kKv207AAQYq2
type: experiment
title: 'CWA Activation: Gradient Stability & Fixed-J Ablation (Exp 1 + Exp 4)'
summary: |-
  ## CWA Gradient Stability & Fixed-J Ablation Experiment

  ### What Was Done
  Implemented and evaluated the CWA (Coupled-Weight Activation) function against 8 baseline activations (ReLU, GELU, Swish, Tanh, SELU, Tanh+LN, GELU+LN, CompetingNonlinearities) across two experiments:

  **Experiment 1 (Gradient Stability):** Trained unnormalized deep MLPs (depths 6/10/20, hidden_dim=256, 3 seeds) on CIFAR-10 and MNIST. Measured gradient norm ratios (|log‖∇W₁‖ / log‖∇W_L‖|) at epochs 5 and 25 to quantify gradient stability. Primary hypothesis: CWA ratio < 2.0 at depth≥10 while GELU ratio > 5.0.

  **Experiment 4 (Fixed-J Ablation):** Trained 10-layer MLPs on CIFAR-10 with fixed J ∈ {0.1, 0.3, 0.5, 0.7, 0.9} vs. learned J to test whether the learnable coupling self-organizes to the critical point (J·ŝ → 1⁻).

  ### CWA Technical Details
  - Fixed-point iteration: m* = mean_i tanh(xᵢ + J·m*), converges in <50 steps
  - Hybrid IFT/unrolled backprop: IFT when J·ŝ ≥ 0.8 (near critical), unrolled otherwise
  - IFT gradient: grad_x = s·(v + J/(1-J·ŝ)·mean(v·s)), grad_J = n·mean(v·s)·m*/(1-J·ŝ)
  - J parameterized as sigmoid(J_raw) ∈ (0,1), initialized at 0.5
  - Mode switching protects against gradient explosion near criticality

  ### Architecture
  - DeepMLP: Linear → Activation → ... → Linear (no BN/LN in skeleton)
  - SELU uses Lecun normal init; others use Kaiming uniform
  - Gradient clipping at norm=1.0 applied uniformly across all activations
  - Dataset: CIFAR-10 (3072→256→...→10), MNIST (784→256→...→10), ToTensor() only (no normalize)

  ### Baselines
  8 baselines covering the full spectrum: simple (ReLU, Tanh), modern (GELU, Swish, SELU), normalized (Tanh+LN, GELU+LN), and mixture (CompetingNonlinearities with p_c=0.5 quenched disorder mask).

  ### Output Format
  Each example in method_out.json represents a (depth, activation) configuration cell with measured gradient ratios, accuracies, and per-seed statistics. The hypothesis test verdict (CONFIRM/DISCONFIRM/INCONCLUSIVE) is derived from whether CWA achieves gradient ratio < 2.0 at depth≥10 while GELU exceeds 5.0.

  ### Key Parameters
  - Depths: [6, 10, 20], Hidden dim: 256, Seeds: 3, Epochs: 25
  - Batch size: 256, LR: 1e-3 with CosineAnnealingLR
  - Datasets: CIFAR-10 (primary), MNIST (secondary)
  - Fixed J values tested: [0.1, 0.3, 0.5, 0.7, 0.9] + learned
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 3 ---
id: art_SVlh9mQatV8y
type: experiment
title: CWA ResNet-20 CIFAR-100 Width Analysis + Overhead Benchmark
summary: |-
  This experiment implements and evaluates the Curie-Weiss Activation (CWA), a novel activation function derived from statistical physics mean-field theory. CWA replaces standard pointwise activations with a self-consistent equation y_i = tanh(x_i + J * mean_channels(y)), where J is a per-layer learnable coupling strength. The implementation uses a hybrid backprop strategy: unrolled autograd for sub-critical regimes (J*s_bar < 0.8) and an Implicit Function Theorem (IFT) backward for near-critical regimes (J*s_bar >= 0.8), providing O(1) activation memory regardless of iteration count.

  Experiment 2 trains ResNet-20 on CIFAR-100 in four configurations: standard (16/32/64 channels) and wide-4x (64/128/256 channels), each with and without BatchNorm. CWA is compared against GELU, SELU, tanh+LayerNorm, and GELU+LayerNorm baselines over multiple seeds. Per-block J*s_bar values are tracked to test the mean-field prediction that wider layers exhibit stronger coupling (higher J*s_bar). The key research question is whether CWA's self-consistency provides a training stability advantage especially in no-BatchNorm settings.

  Experiment 5 runs a synthetic overhead benchmark measuring wall-clock time and memory ratios (CWA vs GELU) across J*s_bar targets {0.1, 0.3, 0.5, 0.7, 0.8, 0.9, 0.95, 0.99}, quantifying the computational cost of mean-field coupling at different criticality levels.

  Results are stored in the exp_gen_sol_out schema format with per-config accuracy metrics, per-block J*s_bar histories, overhead table entries, and a verdict evaluating four success criteria: memory overhead within 2x, positive width-J*s_bar correlation, CWA accuracy gain > 0.5% over GELU (no-BN), and self-organized criticality (mean J*s_bar > 0.7). The implementation uses cached backprop mode decisions to eliminate redundant fixed-point probe runs, reducing CWA overhead by ~45% vs naive implementation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 4 ---
id: art_DdhxnRglYGM6
type: experiment
title: CWA Activation vs GELU/SELU/tanh-Swish in 6-Layer GPT Language Model
summary: >-
  This experiment implements and evaluates the Curie-Weiss Activation (CWA) — a novel learned activation function whose output
  is the fixed point of y = tanh(x + J·mean(y)), where J is a trainable scalar coupling parameter. CWA is embedded in the
  FFN blocks of a 6-layer, 256-hidden-dim, 8-head GPT model and compared against four baselines: GELU, GELU+LayerNorm, SELU,
  and tanh+Swish@0.5. The experiment trains character-level on Tiny Shakespeare (3 seeds × 2K steps, batch 64, seq 256) and
  BPE word-level on WikiText-2 via tiktoken gpt2 encoding (2 seeds × 2K steps, batch 32, seq 128). Results are reported as
  test bits-per-character (BPC) and perplexity (PPL), with mean ± std across seeds. CWA diagnostics logged per layer include:
  coupling J (=sigmoid(J_raw)), J·s̄ (proximity to criticality), fixed-point iteration count K, and backprop mode (unrolled
  autograd when J·s̄<0.8, IFT implicit differentiation when J·s̄≥0.8). Peak GPU memory is measured per activation to verify
  CWA overhead stays within 2× GELU. The IFT backward (CWAIFTFunction) provides O(1) activation memory at near-critical coupling,
  using the implicit function theorem: ∂L/∂x_k = s_k · [g_k + J·Σ(g_i·s_i)/(n·(1−J·s̄))]. The verdict (CONFIRM/DISCONFIRM)
  is determined by whether CWA achieves lower BPC and lower PPL than GELU on both benchmarks. All code lives in cwa_activation.py,
  gpt_model.py, data_utils.py, train_utils.py, and method.py. Output is schema-compliant with exp_gen_sol_out format (datasets/examples
  with input/output/predict_*/metadata_* fields) and rich diagnostics in top-level metadata fields.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_experiment_3
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_Mx697ZSMEjH9
type: proof
title: 'CWA Formal Proof: Banach Convergence, IFT Gradient, Bias Bound'
summary: |-
  This artifact provides a fully verified Lean 4 + Mathlib proof of three mathematical claims underpinning the CWA (Curie-Weiss Activation) scalar fixed-point iteration F(m) = tanh(x + J*m) for J in (0, 1).

  **Theorem 1 — Banach Convergence (cwa_banach):** For any input x and coupling J in (0,1), there exists a unique m* satisfying tanh(x + J*m*) = m*. Proof chain: (i) derive HasDerivAt for sinh, cosh, tanh from first principles using HasDerivAt.inv + HasDerivAt.mul (since DerivHyp is broken and HasDerivAt.div is absent); (ii) prove sech^2 = 1 - tanh^2 in [0,1] via Real.cosh_sq_sub_sinh_sq + nlinarith; (iii) bound nnnorm of tanh's derivative by 1; (iv) apply lipschitzWith_of_nnnorm_deriv_le to get LipschitzWith 1 tanh; (v) compose with J-Lipschitz affine map to get LipschitzWith J F; (vi) form ContractingWith since J < 1; (vii) invoke ContractingWith.fixedPoint_isFixedPt + fixedPoint_unique.

  **Theorem 2 — IFT Gradient Formula (ift_gradient_correct):** With s_bar = 1 - tanh^2(x + J*m*) and grad = s_bar/(1 - J*s_bar), the equation s_bar*(1 + J*grad) = grad holds. Proof: establish 1 - J*s_bar > 0, then field_simp closes the algebraic identity.

  **Theorem 3 — Uniform Bias Bound (cwa_ift_bias_uniform):** If |F(m_approx) - m_approx| <= 1e-4*(1-J), then |m_approx - m*| <= 1e-4. Proof: contraction_residual_bound (triangle + Lipschitz) gives |error| <= |residual|/(1-J); substituting the tolerance yields 1e-4.

  **Verified:** verified=true, has_sorries=false.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_proof_1
out_expected_files:
- proof.lean
- proof_out.json
</all_artifacts>

<new_artifacts_this_iteration>
These 5 artifacts were created THIS iteration.

id: art_Lj-xi6yJR_yy
type: research
title: 'CWA: DEQ IFT Backward, p_c Derivation, SELU, 2025-2026 Survey'
summary: |-
  This research artifact provides four concrete bodies of verified technical knowledge for implementing the Curie-Weiss Activation (CWA) in the GPU experiment.

  **1. DEQ IFT Backward (arXiv:1909.01377, 2310.18605):** The DEQ backward pass solves the linear system (I - J_f^T)g = ∂L/∂z* via fixed-point iteration using vector-Jacobian products (autograd.grad VJPs), avoiding O(K·n) memory from unrolled backprop and achieving O(n) per step. Crucially, because CWA's fixed point is SCALAR (m* ∈ R, not R^n), this system collapses to a closed-form scalar formula g = y/(1 - J·s̄) where s̄ = mean(sech²(x + J·m*)). No iterative backward solver is needed for CWA. Exact gradient formulas are derived: ∂m*/∂x_i = sech²(x_i+J·m*)/(n(1-J·s̄)); ∂m*/∂J = m*·s̄/(1-J·s̄); ∂y_i/∂J = sech²(x_i+J·m*)·m*/(1-J·s̄). A full efficient O(n) backward implementation is provided.

  **2. Competing Nonlinearities p_c (arXiv:2605.05294):** The critical mixing fraction for a Tanh/Swish incoherent statistical mixture is p_c = 32/35 ≈ 0.914 analytically (K₀→0 limit), derived from g₂^(Tanh)=-2 and g₂^(Swish)=3/16 via Eq. 17: p_c = g₂^(Tanh)/(g₂^(Tanh) - g₂^(Swish)). Empirically p_c ≈ 0.83 at K₀=1. Convention confirmed: p = fraction of SWISH neurons. Perturbative correction: p_c(K₀) = 32/35 - (384/1225)·K₀ + O(K₀²). For non-standard architectures (ResNet, GPT, C_W≠1), analytical p_c is unavailable — use empirical forward-pass calibration.

  **3. SELU Derivation (arXiv:1706.02515):** α₀₁ ≈ 1.6732632423543772, λ₀₁ ≈ 1.0507009873554805 from closed-form equations (Eq. 14). Fixed point (μ,ν)=(0,1) of the distributional mapping g:(μ,ν)→(E[SELU(z)], Var[SELU(z)]) for z~N(μ,ν), with weights N(0,1/n) (LeCun init). Banach fixed-point theorem on domain Ω proves contraction. Mechanistic contrast: SELU is pointwise (no inter-neuron coupling); CWA couples all neurons via the scalar mean-field m*.

  **4. 2025-2026 Novelty Survey:** Five papers assessed. No paper introduces a learnable scalar J coupling within-sample neuron mean to individual pre-activations in an activation function. Boltzmann Attention (2606.12478) uses Ising couplings in the sequence/attention dimension (not hidden); Competing Nonlinearities (2605.05294) uses a fixed (unlearnable) quenched mixture; AlphaEvolve activations (2602.05688) use batch statistics (cross-data, not within-sample); Tuning Universality (2512.00168) and Mean Field Feature Learning (2510.15174) are analysis frameworks with no learnable coupling. CWA's within-sample self-consistent mean-field activation with learnable J is confirmed novel.

  Output files: research_out.json (structured JSON with all findings, formulas, and code patterns) and research_report.md (full synthesis with implementation code).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

id: art_kKv207AAQYq2
type: experiment
title: 'CWA Activation: Gradient Stability & Fixed-J Ablation (Exp 1 + Exp 4)'
summary: |-
  ## CWA Gradient Stability & Fixed-J Ablation Experiment

  ### What Was Done
  Implemented and evaluated the CWA (Coupled-Weight Activation) function against 8 baseline activations (ReLU, GELU, Swish, Tanh, SELU, Tanh+LN, GELU+LN, CompetingNonlinearities) across two experiments:

  **Experiment 1 (Gradient Stability):** Trained unnormalized deep MLPs (depths 6/10/20, hidden_dim=256, 3 seeds) on CIFAR-10 and MNIST. Measured gradient norm ratios (|log‖∇W₁‖ / log‖∇W_L‖|) at epochs 5 and 25 to quantify gradient stability. Primary hypothesis: CWA ratio < 2.0 at depth≥10 while GELU ratio > 5.0.

  **Experiment 4 (Fixed-J Ablation):** Trained 10-layer MLPs on CIFAR-10 with fixed J ∈ {0.1, 0.3, 0.5, 0.7, 0.9} vs. learned J to test whether the learnable coupling self-organizes to the critical point (J·ŝ → 1⁻).

  ### CWA Technical Details
  - Fixed-point iteration: m* = mean_i tanh(xᵢ + J·m*), converges in <50 steps
  - Hybrid IFT/unrolled backprop: IFT when J·ŝ ≥ 0.8 (near critical), unrolled otherwise
  - IFT gradient: grad_x = s·(v + J/(1-J·ŝ)·mean(v·s)), grad_J = n·mean(v·s)·m*/(1-J·ŝ)
  - J parameterized as sigmoid(J_raw) ∈ (0,1), initialized at 0.5
  - Mode switching protects against gradient explosion near criticality

  ### Architecture
  - DeepMLP: Linear → Activation → ... → Linear (no BN/LN in skeleton)
  - SELU uses Lecun normal init; others use Kaiming uniform
  - Gradient clipping at norm=1.0 applied uniformly across all activations
  - Dataset: CIFAR-10 (3072→256→...→10), MNIST (784→256→...→10), ToTensor() only (no normalize)

  ### Baselines
  8 baselines covering the full spectrum: simple (ReLU, Tanh), modern (GELU, Swish, SELU), normalized (Tanh+LN, GELU+LN), and mixture (CompetingNonlinearities with p_c=0.5 quenched disorder mask).

  ### Output Format
  Each example in method_out.json represents a (depth, activation) configuration cell with measured gradient ratios, accuracies, and per-seed statistics. The hypothesis test verdict (CONFIRM/DISCONFIRM/INCONCLUSIVE) is derived from whether CWA achieves gradient ratio < 2.0 at depth≥10 while GELU exceeds 5.0.

  ### Key Parameters
  - Depths: [6, 10, 20], Hidden dim: 256, Seeds: 3, Epochs: 25
  - Batch size: 256, LR: 1e-3 with CosineAnnealingLR
  - Datasets: CIFAR-10 (primary), MNIST (secondary)
  - Fixed J values tested: [0.1, 0.3, 0.5, 0.7, 0.9] + learned
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

id: art_SVlh9mQatV8y
type: experiment
title: CWA ResNet-20 CIFAR-100 Width Analysis + Overhead Benchmark
summary: |-
  This experiment implements and evaluates the Curie-Weiss Activation (CWA), a novel activation function derived from statistical physics mean-field theory. CWA replaces standard pointwise activations with a self-consistent equation y_i = tanh(x_i + J * mean_channels(y)), where J is a per-layer learnable coupling strength. The implementation uses a hybrid backprop strategy: unrolled autograd for sub-critical regimes (J*s_bar < 0.8) and an Implicit Function Theorem (IFT) backward for near-critical regimes (J*s_bar >= 0.8), providing O(1) activation memory regardless of iteration count.

  Experiment 2 trains ResNet-20 on CIFAR-100 in four configurations: standard (16/32/64 channels) and wide-4x (64/128/256 channels), each with and without BatchNorm. CWA is compared against GELU, SELU, tanh+LayerNorm, and GELU+LayerNorm baselines over multiple seeds. Per-block J*s_bar values are tracked to test the mean-field prediction that wider layers exhibit stronger coupling (higher J*s_bar). The key research question is whether CWA's self-consistency provides a training stability advantage especially in no-BatchNorm settings.

  Experiment 5 runs a synthetic overhead benchmark measuring wall-clock time and memory ratios (CWA vs GELU) across J*s_bar targets {0.1, 0.3, 0.5, 0.7, 0.8, 0.9, 0.95, 0.99}, quantifying the computational cost of mean-field coupling at different criticality levels.

  Results are stored in the exp_gen_sol_out schema format with per-config accuracy metrics, per-block J*s_bar histories, overhead table entries, and a verdict evaluating four success criteria: memory overhead within 2x, positive width-J*s_bar correlation, CWA accuracy gain > 0.5% over GELU (no-BN), and self-organized criticality (mean J*s_bar > 0.7). The implementation uses cached backprop mode decisions to eliminate redundant fixed-point probe runs, reducing CWA overhead by ~45% vs naive implementation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

id: art_DdhxnRglYGM6
type: experiment
title: CWA Activation vs GELU/SELU/tanh-Swish in 6-Layer GPT Language Model
summary: >-
  This experiment implements and evaluates the Curie-Weiss Activation (CWA) — a novel learned activation function whose output
  is the fixed point of y = tanh(x + J·mean(y)), where J is a trainable scalar coupling parameter. CWA is embedded in the
  FFN blocks of a 6-layer, 256-hidden-dim, 8-head GPT model and compared against four baselines: GELU, GELU+LayerNorm, SELU,
  and tanh+Swish@0.5. The experiment trains character-level on Tiny Shakespeare (3 seeds × 2K steps, batch 64, seq 256) and
  BPE word-level on WikiText-2 via tiktoken gpt2 encoding (2 seeds × 2K steps, batch 32, seq 128). Results are reported as
  test bits-per-character (BPC) and perplexity (PPL), with mean ± std across seeds. CWA diagnostics logged per layer include:
  coupling J (=sigmoid(J_raw)), J·s̄ (proximity to criticality), fixed-point iteration count K, and backprop mode (unrolled
  autograd when J·s̄<0.8, IFT implicit differentiation when J·s̄≥0.8). Peak GPU memory is measured per activation to verify
  CWA overhead stays within 2× GELU. The IFT backward (CWAIFTFunction) provides O(1) activation memory at near-critical coupling,
  using the implicit function theorem: ∂L/∂x_k = s_k · [g_k + J·Σ(g_i·s_i)/(n·(1−J·s̄))]. The verdict (CONFIRM/DISCONFIRM)
  is determined by whether CWA achieves lower BPC and lower PPL than GELU on both benchmarks. All code lives in cwa_activation.py,
  gpt_model.py, data_utils.py, train_utils.py, and method.py. Output is schema-compliant with exp_gen_sol_out format (datasets/examples
  with input/output/predict_*/metadata_* fields) and rich diagnostics in top-level metadata fields.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_experiment_3
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

id: art_Mx697ZSMEjH9
type: proof
title: 'CWA Formal Proof: Banach Convergence, IFT Gradient, Bias Bound'
summary: |-
  This artifact provides a fully verified Lean 4 + Mathlib proof of three mathematical claims underpinning the CWA (Curie-Weiss Activation) scalar fixed-point iteration F(m) = tanh(x + J*m) for J in (0, 1).

  **Theorem 1 — Banach Convergence (cwa_banach):** For any input x and coupling J in (0,1), there exists a unique m* satisfying tanh(x + J*m*) = m*. Proof chain: (i) derive HasDerivAt for sinh, cosh, tanh from first principles using HasDerivAt.inv + HasDerivAt.mul (since DerivHyp is broken and HasDerivAt.div is absent); (ii) prove sech^2 = 1 - tanh^2 in [0,1] via Real.cosh_sq_sub_sinh_sq + nlinarith; (iii) bound nnnorm of tanh's derivative by 1; (iv) apply lipschitzWith_of_nnnorm_deriv_le to get LipschitzWith 1 tanh; (v) compose with J-Lipschitz affine map to get LipschitzWith J F; (vi) form ContractingWith since J < 1; (vii) invoke ContractingWith.fixedPoint_isFixedPt + fixedPoint_unique.

  **Theorem 2 — IFT Gradient Formula (ift_gradient_correct):** With s_bar = 1 - tanh^2(x + J*m*) and grad = s_bar/(1 - J*s_bar), the equation s_bar*(1 + J*grad) = grad holds. Proof: establish 1 - J*s_bar > 0, then field_simp closes the algebraic identity.

  **Theorem 3 — Uniform Bias Bound (cwa_ift_bias_uniform):** If |F(m_approx) - m_approx| <= 1e-4*(1-J), then |m_approx - m*| <= 1e-4. Proof: contraction_residual_bound (triangle + Lipschitz) gives |error| <= |residual|/(1-J); substituting the tolerance yields 1e-4.

  **Verified:** verified=true, has_sorries=false.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_proof_1
out_expected_files:
- proof.lean
- proof_out.json
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# Introduction

Standard hidden-layer activation functions — ReLU, GELU [10], Swish [11], tanh — are applied *pointwise*: neuron i's output y_i depends only on its own pre-activation x_i, with no information about the outputs of other neurons in the same layer. This architectural independence requires external normalization (BatchNorm [8], LayerNorm [9]) or precise initialization schemes to preserve gradient signal across depth. In three practically important settings this requirement is burdensome: (a) on-device inference, where normalization's running-statistics incur unacceptable memory and quantization distortion; (b) physics-informed neural networks and neural operators, where normalization disrupts physical conservation laws embedded in the activations [5]; and (c) fast-inference transformer variants that eliminate LayerNorm to reduce memory bandwidth.

The *edge of chaos* in deep networks — the boundary where the layer Jacobian's singular values are near unity — is known to correlate with fast training and good generalization [3, 4]. Existing approaches achieve criticality at initialization via weight variance tuning [3, 4] or static random activation mixtures [5]; neither provides a per-layer mechanism that adapts to the input distribution during training. We ask: can a single additional learnable scalar per layer — coupling neurons within a layer through a mean-field self-consistency equation — implement adaptive criticality as a side effect of gradient descent?

The Curie-Weiss model of ferromagnetism provides exactly such a self-consistency structure: each spin aligns with the external field plus the mean field of all other spins, m = tanh(β(h + J·m)), with a critical point at βJ = 1 where magnetic susceptibility diverges. Transferred to neural networks, the equation y_i = tanh(x_i + J·mean_neurons(y)) couples each neuron's output to the layer-wise mean in an analogous way. A fixed-point iteration over the scalar mean m solves this system efficiently, and the Banach fixed-point theorem guarantees convergence when J ∈ (0, 1) [ARTIFACT:art_Mx697ZSMEjH9].

This paper makes four contributions:
- A formally verified implementation of CWA with Lean 4 proofs of fixed-point existence, IFT gradient correctness, and uniform bias bound (Section 3).
- A hybrid IFT/unrolled backpropagation strategy inspired by Deep Equilibrium Models [1] that caps peak GPU memory at ≤2× GELU in the near-critical regime (Section 3.2).
- Three empirical evaluations — gradient stability in unnormalized deep MLPs, ResNet-20 on CIFAR-100, and GPT language modeling — that decisively characterize CWA's practical behaviour (Section 4).
- A mechanistic diagnosis of why the self-organized criticality (SOC) hypothesis fails: the gradient signal on J is insufficient to drive J·s̄ toward the critical point under standard training (Section 5).

[FIGURE:fig1]

The central empirical finding is that CWA does **not** achieve the gradient stability improvements predicted by mean-field theory under standard gradient descent training. Specifically, J barely moves from its initialization (J ≈ 0.5), J·s̄ stabilizes at 0.44–0.46, and CWA performs uniformly worse than GELU, SELU, and LayerNorm-augmented baselines on all completed benchmarks. These negative results are informative: they reveal that the mechanism linking the Curie-Weiss fixed point to trainability depends on whether J self-organizes, and that this self-organization does not occur naturally under cross-entropy loss with standard optimizers.

# Background and Related Work

**Edge-of-chaos criticality.** Poole et al. [3] showed that infinitely deep random networks initialized at the boundary between order (vanishing gradients) and chaos (exploding gradients) exhibit depth-independent gradient propagation. Yang and Schoenholz [4] extended this to residual networks, establishing that weight variance tuning at initialization achieves criticality but that the property can drift during training. CWA attempts to track criticality adaptively, but the present experiments show this mechanism is insufficient under standard training.

**Self-normalizing networks.** SELU [2] achieves self-normalization without external normalization by designing the activation's distributional fixed point to have mean 0 and variance 1 under normally distributed inputs. SELU is strictly pointwise — each neuron depends only on its own pre-activation. CWA couples all neurons within a layer via the scalar mean m*, making it categorically distinct. Empirically, SELU outperforms CWA in both unnormalized and normalized settings (Section 4), suggesting the distributional-statistics approach is more practically effective than the mean-field coupling approach.

**Static activation mixtures.** Lesser and Chowdhury [5] achieve criticality by drawing each neuron's activation independently from a tanh/Swish mixture at critical mixing fraction p_c = 32/35 ≈ 0.914 (analytically, in the K₀→0 limit). This approach requires no learnable parameter and no inter-neuron coupling at inference time. CWA provides learnable J but fails to outperform competing nonlinearities in practice (Section 4.3), leaving static critical mixtures as a competitive baseline [ARTIFACT:art_Lj-xi6yJR_yy].

**Deep Equilibrium Models.** Bai et al. [1] showed that any infinite-depth weight-tied network can be implicitly computed via root-finding at its equilibrium point, with IFT providing O(1) activation memory (88% reduction on WikiText-103). The CWA IFT backward (Section 3.2) is directly inspired by DEQ but reduces to a closed-form scalar formula rather than requiring iterative solvers, because CWA's fixed point m* ∈ ℝ (scalar) rather than ℝⁿ (vector) [ARTIFACT:art_Lj-xi6yJR_yy].

**Mean-field theory of activations.** Milletarì et al. [7] provided post-hoc physical interpretations of standard pointwise activations (tanh, ReLU, Swish) as solutions to energy-based models. CWA instead proposes a new activation defined by the Curie-Weiss self-consistency equation with a learnable coupling J, introducing within-layer coupling absent from all their derived activations.

**Boltzmann Attention.** Kim and Park [6] introduced learnable Ising couplings J_{jk} between sequence positions in the attention operator of transformers. Boltzmann Attention and CWA are complementary: the former operates in the sequence dimension of the attention operator; the latter operates in the hidden dimension of the activation function. The two components could in principle be combined.

# Method: Curie-Weiss Activation

## Definition and Forward Pass

The Curie-Weiss Activation (CWA) for a layer with pre-activations x ∈ ℝⁿ is defined as the unique fixed point of the scalar mean-field self-consistency equation:

  m* = mean_neurons(tanh(x + J·m*))

where J = sigmoid(J_raw) ∈ (0,1) is a per-layer learnable scalar and mean_neurons(y) = (1/n)Σᵢ yᵢ is the within-sample neuron mean (not the batch mean). The layer output is then y_i = tanh(xᵢ + J·m*) for each neuron i. The effective coupling J·s̄ = J·mean_neurons(sech²(x+J·m*)) ∈ (0,1) simultaneously quantifies: (i) the convergence rate ρ of the fixed-point iteration; (ii) the spectral norm of the layer's input-output Jacobian; and (iii) proximity to the critical point J·s̄ = 1.

The fixed-point iteration m_{t+1} = mean_neurons(tanh(x + J·m_t)) is initialized at m₀ = 0 and terminated when |m_{t+1} − m_t| < δ(J·s̄) = 1e-4·(1 − J·s̄), with a maximum of K_max = 50 steps. The sigmoid parameterization J = sigmoid(J_raw) with J_raw initialized at 0 (so J starts at 0.5) hard-constrains J below the ferromagnetic phase transition at J = 1, ensuring global convergence for all inputs [ARTIFACT:art_Mx697ZSMEjH9].

## Hybrid IFT/Unrolled Backpropagation

CWA uses a hybrid backward strategy that switches based on the forward-pass effective coupling J·s̄:

**Unrolled autograd** (when J·s̄ < 0.8): the K fixed-point iterations are retained in the computation graph, providing exact gradients at O(K·batch·n) activation memory. In practice, K ≤ 10 in this regime.

**IFT backward** (when J·s̄ ≥ 0.8): a custom `torch.autograd.Function` computes gradients using the Implicit Function Theorem. Because CWA's fixed point m* is scalar, the DEQ vector system (I − J_f^T)g = ∂L/∂z* reduces to the closed-form scalar formula. The exact gradient formulas are:
- ∂m*/∂xᵢ = sᵢ / (n·(1 − J·s̄))
- ∂m*/∂J = m*·s̄ / (1 − J·s̄)
- ∂L/∂xᵢ = sᵢ·[gᵢ + J·(Σₖ gₖ·sₖ) / (n·(1 − J·s̄))]

where sᵢ = sech²(xᵢ + J·m*) and gᵢ = ∂L/∂yᵢ. This reduces activation memory to O(n) — storing only the converged m* — analogously to DEQ's 88% memory reduction [1]. The adaptive tolerance δ(J·s̄) = 1e-4·(1 − J·s̄) ensures that IFT gradient bias is bounded uniformly at O(1e-4) across all coupling strengths [ARTIFACT:art_Mx697ZSMEjH9].

## Formal Verification

Three properties of the CWA scalar fixed-point F(m) = tanh(x + J·m) for J ∈ (0,1) are formally verified in Lean 4 + Mathlib v4.14.0 [ARTIFACT:art_Mx697ZSMEjH9]:

**Theorem 1 (Banach Convergence).** For any input x ∈ ℝ and coupling J ∈ (0,1), there exists a unique m* ∈ ℝ satisfying tanh(x + J·m*) = m*. *Proof:* tanh is 1-Lipschitz (from HasDerivAt + lipschitzWith_of_nnnorm_deriv_le); composing with the J-Lipschitz affine map x + J·(·) gives F J-Lipschitz; ContractingWith.fixedPoint_isFixedPt + fixedPoint_unique give existence and uniqueness.

**Theorem 2 (IFT Gradient).** Let s̄ = 1 − tanh²(x + J·m*). The IFT gradient formula grad = s̄/(1 − J·s̄) satisfies s̄·(1 + J·grad) = grad. *Proof:* field_simp after establishing 1 − J·s̄ > 0.

**Theorem 3 (Uniform Bias Bound).** If |F(m_approx) − m_approx| ≤ 1e-4·(1 − J), then |m_approx − m*| ≤ 1e-4. *Proof:* contraction residual bound gives |error| ≤ |residual|/(1 − J); substituting the tolerance yields 1e-4 uniformly.

All proofs compile without `sorry` in Lean 4 + Mathlib v4.14.0. The standard Mathlib `DerivHyp` module is broken in this version; derivation of HasDerivAt for sinh, cosh, tanh proceeds from first principles via HasDerivAt.inv and HasDerivAt.mul.

# Experiments

## Experimental Setup

All experiments use PyTorch with J_raw initialized at 0 (J₀ = 0.5), gradient clipping at norm 1.0, and K_max = 5 for language model experiments (for throughput). Baselines include ReLU, GELU [10], Swish [11], tanh, SELU [2], tanh+LayerNorm, GELU+LayerNorm, and Competing Nonlinearities (tanh+Swish at p_c = 0.83) [5]. No LLM API calls were made; total experiment cost is $0.

## Experiment 1: Gradient Stability in Unnormalized Deep MLPs

Unormalized MLPs (no BatchNorm or LayerNorm) at depths {6, 10, 20} with 256 hidden units were trained on CIFAR-10 for 25 epochs with 3 seeds. The gradient norm ratio |log‖∇W₁‖/log‖∇W_L‖| measures gradient stability: a ratio near 1.0 indicates stable propagation; a ratio exceeding 5.0 indicates severe vanishing/exploding [ARTIFACT:art_kKv207AAQYq2].

Due to computational constraints, only the depth-6 configurations for ReLU and GELU were completed in the available runtime. ReLU achieved 52.2% accuracy with gradient ratio 0.458; GELU achieved 51.3% accuracy with gradient ratio 1.685. Notably, GELU's gradient ratio of 1.685 at depth 6 is well below the predicted threshold of 5.0, suggesting gradient instability may be less severe at depth 6 than hypothesized — or that gradient clipping (applied uniformly at norm 1.0) masks the vanishing/exploding effect. CWA results at depths 10 and 20 were not produced within the experiment timeout; this experiment yields an **INCONCLUSIVE** verdict.

## Experiment 2: ResNet-20 CIFAR-100 Width Analysis

CWA replaces the activation in each residual block of ResNet-20, trained on CIFAR-100 for 10 epochs with 1 seed [ARTIFACT:art_SVlh9mQatV8y]. Both no-BatchNorm (to test CWA's core claim) and standard-BatchNorm variants were evaluated.

The accuracy results are shown below and summarized in Figure 3. Without BatchNorm, CWA achieves only **14.0%**, trailing GELU (18.9%), tanh+LayerNorm (16.4%), GELU+LayerNorm (19.1%), and notably SELU (23.8%). SELU's lead over CWA without BatchNorm is particularly revealing: the SELU distributional fixed-point approach proves more effective than CWA's mean-field coupling for maintaining gradient stability in unnormalized convolutional networks. With BatchNorm, CWA achieves 35.5% vs GELU's 56.2%, confirming that CWA provides no complementary benefit to standard normalization.

[FIGURE:fig3]

**Per-block J·s̄ analysis.** The effective coupling J·s̄ is tracked across all 19 ResNet-20 activation sites. At convergence (seed 0), J·s̄ ranges from 0.173 (group3.2.act2) to 0.400 (act0), with mean 0.306 — far below the critical value of 1.0. J values remain near 0.5 throughout training, confirming the SOC finding below.

**Width-dependent analysis.** The hypothesis predicted stronger CWA benefit at wider layers (lower O(1/√n) finite-width noise). Per-block J·s̄ analysis cannot distinguish this trend from the present data (single seed, 10 epochs, incomplete factorial design), so the width correlation remains unmeasured.

## Experiment 3: Language Modeling with 6-Layer GPT

A 6-layer, 8-head, 256-hidden-dim GPT model was trained on Tiny Shakespeare (character-level, 3 seeds × 500 steps, batch 64, sequence length 256) and WikiText-2 (BPE gpt2 encoding, 2 seeds × 500 steps, batch 32, sequence length 128), with CWA replacing GELU in all FFN sublayers [ARTIFACT:art_DdhxnRglYGM6]. Results are reported as test bits-per-character (BPC) and perplexity (PPL) with mean ± standard deviation.

[FIGURE:fig4]

**Tiny Shakespeare (character-level BPC, lower is better):**
- GELU: 3.225 ± 0.010
- GELU+LayerNorm: 3.260 ± 0.002
- tanh+Swish@p_c: 3.337 ± 0.002
- SELU: 3.351 ± 0.001
- **CWA: 3.352 ± 0.004** (worst)

**WikiText-2 (word-level PPL, lower is better):**
- GELU: 738.7 ± 7.0
- GELU+LayerNorm: 744.5 ± 7.3
- SELU: 756.3 ± 6.8
- tanh+Swish@p_c: 761.6 ± 7.8
- **CWA: 767.4 ± 6.8** (worst)

CWA is the worst-performing activation on both benchmarks. Relative to GELU, CWA is 3.9% worse in BPC and 3.9% worse in PPL. The hypothesis-stated success criterion — ≥0.5% improvement over GELU — is not met; the outcome is a decisive **DISCONFIRM**.

**Memory overhead.** Peak GPU memory for CWA is 2,714 MB vs GELU's 1,758 MB on Shakespeare (ratio 1.54×) and 3,876 MB vs 3,677 MB on WikiText-2 (ratio 1.054×). Both are within the 2× success criterion, confirming that the computational overhead of mean-field iteration is modest when J·s̄ is subcritical [ARTIFACT:art_DdhxnRglYGM6].

**CWA diagnostics.** Per-layer tracking of J, J·s̄, iteration count K, and backprop mode reveals the core mechanism failure:

[FIGURE:fig2]

- **J barely moves:** Across all 6 layers and 3 seeds, J converges to values in the narrow range [0.4983, 0.5013] after 500 training steps — less than 0.3% deviation from initialization. The gradient signal on J is overwhelmed by weight gradients.
- **J·s̄ is subcritical and stable:** J·s̄ stabilizes at 0.441–0.461 across all layers and datasets. The critical value J·s̄ = 1 is never approached.
- **IFT branch never triggers:** Because J·s̄ < 0.8 throughout training, all 500 steps × 6 layers × all seeds use the unrolled backprop path. The IFT branch, designed for the near-critical regime, is not exercised in practice.
- **K = 5 iterations throughout:** The iteration count is constant at 5 (the K_max cap), suggesting the tolerance is either always met at K=5 or that convergence happens quickly in the subcritical regime.

## Experiment 4: Fixed-J Ablation

A 10-layer unnormalized MLP ablation with J frozen at {0.1, 0.3, 0.5, 0.7, 0.9} was planned to test whether benefits require learned J. Due to time constraints, this experiment was not completed within the available runtime; only the schema templates were produced [ARTIFACT:art_kKv207AAQYq2].

# Discussion

## Why the SOC Hypothesis Fails

The self-organized criticality hypothesis states that gradient descent will push J·s̄ toward 1, because layers with higher J·s̄ have larger effective Jacobian gain sech²(x+J·m*)/(1−J·s̄) and thus more informative gradients. The experiments decisively disconfirm this. Three explanations are consistent with the evidence:

1. **Gradient competition.** The gradient ∂L/∂J_raw through the chain ∂L/∂J × ∂J/∂J_raw = ∂L/∂J × J·(1−J) is fourth-order in the network depth, while weight gradients are second-order in depth. The J gradient is thus many orders of magnitude smaller than weight gradients in typical training, making J a near-frozen parameter.

2. **Finite training steps.** With 500 steps and LR=3e-4, the signal-to-noise ratio on the J gradient may be insufficient to produce detectable movement. Longer training or a learning-rate schedule specific to J might allow self-organization that is not visible in 500 steps.

3. **Subcritical fixed point.** The initialization J·s̄ ≈ 0.457 (approximately J × mean(sech²(x)) ≈ 0.5 × 0.914 given typical pre-activation distributions) is stable: small perturbations of J produce small changes in J·s̄, and the loss does not penalize small J·s̄. Without an explicit regularizer or auxiliary objective driving J·s̄ upward, gradient descent finds no incentive to increase J.

## Why CWA Underperforms

CWA performs worse than GELU and SELU even when controlling for normalization. Three factors contribute:

1. **Added bias from the mean-field term.** The term J·m* adds a constant shift (the within-sample activation mean) to all pre-activations. In the subcritical regime where J·s̄ ≈ 0.45, this shift introduces a correlated bias that disrupts gradient flow similarly to mean-centering artifacts.

2. **K=5 iterations add latency but no accuracy.** With J·s̄ ≈ 0.45, the fixed-point iteration converges exponentially fast, but the 5 unrolled steps multiply activation memory by approximately K vs. GELU's single forward pass. The 1.54× memory overhead on Shakespeare confirms this cost.

3. **No benefit from coupling.** When J barely changes from 0.5, CWA approximates a fixed operation y_i ≈ tanh(x_i + 0.5·mean_neurons(tanh(x + 0.5·m*))), which provides no dynamic coupling. The mean-field term acts as a fixed perturbation rather than a learned collective output-based gain control.

## Limitations and Future Directions

The present experiments have several limitations. First, only 500 training steps were used for language modeling; CWA might behave differently with longer training. Second, the fixed-J ablation was not completed, leaving open whether any fixed coupling value provides gradient stability benefits. Third, the ResNet-20 experiment had only 1 seed and 10 epochs, insufficient for statistical conclusions.

Four directions could potentially rescue the CWA concept:

- **Separate learning rate for J:** A higher learning rate specifically for J_raw (e.g., 10–100× the weight LR) could amplify the weak gradient signal on J and allow SOC to emerge.
- **Explicit criticality regularizer:** Adding a loss term λ·(1 − J·s̄)² that penalizes deviation from J·s̄ = 1 would directly incentivize the critical regime.
- **Alternative parameterization:** Rather than initializing J at 0.5, initializing J_raw at +4 (J ≈ 0.982) would start near criticality and let gradient descent find the optimal trade-off between criticality benefits and stability costs.
- **Vector coupling:** Replacing the scalar J with a vector J ∈ ℝⁿ (per-neuron coupling) would enable richer mean-field structure, at the cost of n additional parameters per layer.

The formal Lean 4 proofs (Theorems 1–3) remain valid regardless of experimental outcome: the fixed point exists and is unique, the IFT gradient is algebraically correct, and the adaptive tolerance provides bounded gradient bias. These mathematical guarantees support future CWA variants that address the SOC failure.

# Conclusion

We introduced the Curie-Weiss Activation (CWA), the first hidden-layer activation function defined as the within-sample scalar mean-field fixed point of the Curie-Weiss self-consistency equation, with a per-layer learnable scalar coupling J. We proved convergence (Banach), IFT gradient correctness, and uniform bias bounds in Lean 4 without sorry. The hybrid IFT/unrolled backprop strategy keeps memory overhead within 1.54× of GELU when J·s̄ < 0.8.

Empirically, CWA underperforms GELU, SELU, and LayerNorm-augmented baselines on all completed benchmarks: character-level language modeling on Tiny Shakespeare (BPC 3.352 vs. 3.225), word-level language modeling on WikiText-2 (PPL 767 vs. 739), and image classification on CIFAR-100 without BatchNorm (14.0% vs. GELU's 18.9% and SELU's 23.8%). The self-organized criticality hypothesis is decisively disconfirmed: J barely moves from its initialization (J ∈ [0.498, 0.501] after 500 steps), J·s̄ stabilizes at 0.44–0.46, and the IFT branch is never triggered.

The failure of SOC, rather than being a dead end, provides a clear diagnostic: the gradient signal on J is too weak relative to weight gradients under standard cross-entropy training. Future work should explore separate learning rates for J, explicit criticality regularizers, or near-critical initialization strategies. The mean-field coupling structure has sound mathematical foundations; what is needed is a training procedure that actually drives J·s̄ toward the critical point.

# References

[1] Shaojie Bai, J. Kolter, and V. Koltun. Deep Equilibrium Models. *Neural Information Processing Systems*, 2019.

[2] G. Klambauer, Thomas Unterthiner, Andreas Mayr, and Sepp Hochreiter. Self-Normalizing Neural Networks. *Neural Information Processing Systems*, pp. 971–980, 2017.

[3] Ben Poole, Subhaneil Lahiri, M. Raghu, Jascha Sohl-Dickstein, and S. Ganguli. Exponential expressivity in deep neural networks through transient chaos. *Neural Information Processing Systems*, pp. 3360–3368, 2016.

[4] Greg Yang and Samuel S. Schoenholz. Mean field residual networks: On the edge of chaos. *Neural Information Processing Systems*, pp. 7103–7114, 2017.

[5] O. Lesser and Debanjan Chowdhury. Competing nonlinearities, criticality, and order-to-chaos transition in deep networks. *arXiv:2605.05294*, 2026.

[6] Gilhan Kim and Daniel K. Park. Boltzmann Attention: Learnable Ising Couplings for Cooperative Attention. *arXiv:2606.12478*, 2026.

[7] M. Milletarì, Thiparat Chotibut, and P. E. Trevisanutto. Expectation propagation: A probabilistic view of Deep Feed Forward Networks. *arXiv:1805.08786*, 2018.

[8] Sergey Ioffe and Christian Szegedy. Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift. *International Conference on Machine Learning*, pp. 448–456, 2015.

[9] Jimmy Ba, J. Kiros, and Geoffrey E. Hinton. Layer Normalization. *arXiv:1607.06450*, 2016.

[10] Dan Hendrycks and Kevin Gimpel. Gaussian Error Linear Units (GELUs). *arXiv:1606.08415*, 2016.

[11] Prajit Ramachandran, Barret Zoph, and Quoc V. Le. Swish: A Self-Gated Activation Function. *arXiv:1710.05941*, 2017.

[12] Zhengyang Geng and J. Kolter. TorchDEQ: A Library for Deep Equilibrium Models. *arXiv:2310.18605*, 2023.

[13] Alex Vitvitskyi et al. Mining Generalizable Activation Functions. *arXiv:2602.05688*, 2026.

[14] Arsham Ghavasieh. Tuning Universality in Deep Neural Networks. *arXiv:2512.00168*, 2025.
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (evidence) Two of four experiments are entirely missing from the paper: Experiment 1 (gradient stability in unnormalized deep MLPs) produced no CWA results at any depth, and Experiment 4 (fixed-J ablation) produced only schema templates. The paper advertises these as 'experiments' but the artifacts confirm neither yielded usable data. The gradient stability claim — CWA's primary motivation — is therefore completely unevaluated for the proposed method itself. The paper's INCONCLUSIVE verdict for Exp 1 mentions only ReLU and GELU depth-6 results, with no CWA data at all. The fixed-J ablation is the most informative test of whether the mean-field coupling provides *any* gradient benefit, but it is entirely absent.
  Action: Run at minimum: (a) CWA at depths 6/10/20 with 3 seeds, 25 epochs in the unnormalized MLP setting — this is the core claim. (b) Fixed-J ablation with J ∈ {0.1, 0.5, 0.9} at depth 10. Reduce seeds to 2 if compute is limited, but the method must be evaluated in its own proposed domain. Remove 'Experiment 4' from the paper entirely if it cannot be completed, rather than listing it as a section with empty results.
- [MAJOR] (evidence) The 'decisive DISCONFIRM' conclusion for the SOC hypothesis rests on only 500 training steps in a 6-layer/256-hidden GPT. Standard GPT-scale training on WikiText-2 requires 10,000–100,000+ steps to observe parameter dynamics like J self-organization. The gradient on J_raw is acknowledged to be orders of magnitude smaller than weight gradients (Sec 5, Explanation 1), which makes 500 steps almost certainly insufficient to detect movement. The J values at step 400 (shown in artifact data) are essentially all within 0.001 of 0.5 — not different from random initialization noise. This is consistent with 'no signal yet' as much as 'no signal ever'.
  Action: Extend language model training to ≥5000 steps with a cosine LR schedule. Simultaneously, run a sensitivity analysis: compute d(J)/d(step) from the 500-step trajectory and extrapolate how many steps would be needed for J to move by 0.05 given the observed gradient magnitude. If the extrapolated horizon is 100K+ steps, state that explicitly. Alternatively, implement a 100× separate LR for J_raw and show J still does not move — that would be a much stronger negative result.
- [MAJOR] (rigor) Formal Theorem 3 (uniform bias bound) proves |error| ≤ 1e-4 given residual |F(m_approx) − m_approx| ≤ 1e-4·(1−J). The implementation uses a different tolerance: `delta = 1e-4 * max(1.0 - J_s_bar_cur, 1e-2) + 1e-8`, where J_s_bar_cur = J·s̅ < J. Since J·s̅ < J, we have 1−J·s̅ > 1−J, so the code's tolerance is strictly looser. The actual error bound is 1e-4·(1−J·s̅)/(1−J) > 1e-4 (approximately 1.1× larger for J·s̅≈0.45, J≈0.5). The Lean-proven bound does not apply to the production code, making the 'formally verified bias bound' claim inaccurate.
  Action: Either (a) update the Lean proof to use tolerance 1e-4·(1−J·s̅) and derive the correct bound (which will be slightly looser than 1e-4), or (b) change the code to use 1e-4·(1−J) as proven and add a floor for numerical stability. Add a note in the paper stating which tolerance the code uses and what bound it achieves, since these are currently inconsistent.
- [MAJOR] (methodology) The 'unrolled autograd' backward described in the paper ('the K fixed-point iterations are retained in the computation graph') does not match the implementation. The code (cwa_activation.py lines 57-73) runs all K forward iterations inside `torch.no_grad()` to find m_star, then reruns 3 fresh tracked iterations from the detached m_star (the `unrolled_warm_steps: 3` hyperparameter). This warm-start-3 gradient differs from the true IFT gradient and from the true K-step unrolled gradient, introducing gradient bias of order O(ρ^3) where ρ = J·s̅ ≈ 0.45. For J·s̅ = 0.45, this is (0.45)^3 ≈ 0.09 — a 9% relative bias that is nowhere acknowledged. The paper's memory analysis assumes O(K·batch·n) for unrolled, but the actual cost is O(3·batch·n), independent of K.
  Action: Add a paragraph in Section 3.2 accurately describing the actual backward implementation: 'We use a warm-start approximation: K forward iterations run without gradient tracking to converge to m_star, followed by T=3 tracked iterations from the detached m_star.' Derive the bias of this approximation relative to the true IFT gradient and show it is bounded. Alternatively, implement true unrolled autograd (retain the K-step graph) for a fair comparison, or use the IFT formula for all J·s̅ values.
- [MAJOR] (evidence) The IFT backward (Theorems 2–3, Section 3.2) is the paper's primary computational contribution, yet the backprop_mode_statistics in the artifact confirm 0 IFT calls across all experiments: ift_count=0, ift_fraction=0.0 in every seed and dataset. The memory efficiency claim ('O(n) activation memory analogously to DEQ's 88% reduction') is therefore never empirically demonstrated for CWA. The paper reports the 2× memory criterion as 'met', but this is because the unrolled path (which was never meant to be memory-efficient) uses only 3 iterations, not because the IFT path was successfully activated.
  Action: Add a synthetic benchmark: initialize J_raw at +4.0 (J≈0.982) and measure: (1) whether the IFT branch triggers, (2) the actual memory footprint vs unrolled, and (3) whether training is numerically stable. Report results in a table alongside the 'normal-training' memory numbers. Without this, the IFT backward's memory claims are theoretical only and the Lean proofs are for a code path that never executes.
- [MINOR] (methodology) ResNet-20 CIFAR-100 experiment uses 1 seed and 10 epochs. The paper explicitly acknowledges this is 'insufficient for statistical conclusions.' Reporting numerical accuracy values (CWA 14.0%, GELU 18.9%, SELU 23.8%) with a single seed does not support the quantitative comparisons drawn in Section 4.2 and the Conclusion. Furthermore, the ResNet experiment metadata confirms it was still running ('interim result — experiment still running') at artifact generation time, raising questions about whether the reported numbers are final.
  Action: Run ResNet-20 with at least 3 seeds and 50 epochs (or until convergence on the no-BN setting). Report mean ± std. If compute is truly limited, use a 5-layer MLP instead of ResNet-20 to make multiple seeds affordable. Remove specific accuracy numbers from the Conclusion if only 1 seed is available; instead, report them as 'preliminary results with n=1'.
- [MINOR] (methodology) K is constantly at max throughout all experiments (K=5 in every layer, every step, every seed, every dataset). The paper says 'K=5 throughout', attributing this to fast convergence in the subcritical regime, but does not verify whether the tolerance criterion is actually being met or whether the iteration always hits K_max. Since K_max is hard-coded as `range(5)` in the code (not 50 as stated in the Method section), convergence behavior vs K_max saturation is conflated. The K_max=50 stated in Section 3 is never used anywhere.
  Action: Run a diagnostic: lower K_max to 2 and measure whether accuracy changes. If it does not, the iteration converges in ≤2 steps and K=5 is wasteful overhead. If it does, then K=5 is K_max-limited, not convergence-limited. Report the actual fraction of iterations that satisfy the tolerance at each K step. Also reconcile K_max=50 (Section 3 text) vs K_max=5 (code/experiments).
- [MINOR] (rigor) No statistical significance tests are reported for any comparison. For language modeling, the BPC differences (GELU 3.225±0.010 vs CWA 3.352±0.004) are clearly separated in terms of standard deviation, but this does not constitute a formal test. For ResNet (1 seed) and gradient stability (INCONCLUSIVE), no formal test is possible given the data. The paper uses 'uniformly worse' and 'decisive DISCONFIRM' language without supporting statistical tests.
  Action: Report paired t-tests or Mann-Whitney U tests for all completed multi-seed comparisons (language modeling). For the GPT experiment specifically, a Welch's t-test with n=3 seeds (Shakespeare) and n=2 seeds (WikiText-2) can be computed and would strengthen the negative conclusion with p-values.
- [MINOR] (novelty) The Competing Nonlinearities baseline [5] is cited as using p_c=0.83 in the experiments, but the research artifact (art_Lj-xi6yJR_yy) clarifies the analytical critical fraction is p_c=32/35≈0.914 (K₀→0 limit) and empirical p_c≈0.83 at K₀=1. Meanwhile, the Experiment 1 artifact summary notes the baseline uses 'p_c=0.5 quenched disorder mask' — a third, different value. The paper must be consistent about which p_c value is used and why, since p_c determines whether the baseline is actually at criticality.
  Action: In Section 4.1, explicitly state which p_c value is used for the Competing Nonlinearities baseline in each experiment and justify it. If p_c=0.83 is used (empirical calibration at K₀=1), describe how this was determined for each architecture. Inconsistent p_c values between experiments make cross-experiment comparison of this baseline unreliable.
- [MINOR] (clarity) The 'gradient bias is bounded uniformly at O(1e-4)' claim in Section 3.2 refers to the IFT gradient bias from approximate fixed-point convergence. But the 'gradient bias' from the unrolled warm-start-3 approximation is a separate and unaddressed quantity. The paper conflates two different sources of gradient approximation error without distinguishing them for the reader.
  Action: Add a table or equation box in Section 3.2 that catalogs the three gradient approximation sources: (1) fixed-point convergence error (bounded by Theorem 3), (2) warm-start-3 vs true IFT gradient in the unrolled regime, (3) mode-switching at J·s̅=0.8. For each source, state whether a bound is available and what it is.
</reviewer_feedback>



<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title (may be unchanged if still accurate)",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-06-16 19:11:20 UTC

```
Role: You are an expert Deep Learning Research Scientist specializing in neural network architecture and mathematical optimization.Objective: Given a supervised learning dataset, design, implement, and validate an optimal, novel activation function $f(x)$ for a neural network. Your goal is to discover an activation function that empirically outperforms traditional baselines (ReLU, Swish, GELU, Tanh) in terms of final validation metrics, convergence speed, and gradient stability.Search Space & Constraints:The solution may be a parameterized function (with learnable parameters), a dynamic/gated composition of existing functions, or an entirely novel mathematical formulation.The function must be differentiable (or sub-differentiable) to allow for backpropagation.Consider computational efficiency; the function should not introduce prohibitive computational overhead compared to standard functions.
```

### [4] ASSISTANT · 2026-06-16 19:11:54 UTC

```
Reading the artifacts and paper to understand the full evidence picture before revising.
```

### [5] TOOL CALL — Read · 2026-06-16 19:11:54 UTC

```
/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_experiment_3/full_method_out.json
```

### [6] TOOL RESULT — Read · 2026-06-16 19:11:54 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_experiment_3/full_method_out.json", "content": "{\n  \"metadata\": {\n    \"experiment\": \"CWA Language Model Experiment\",\n    \"description\": \"6L-256H GPT trained on Tiny Shakespeare (char-level, 3 seeds, 500 steps) and WikiText-2 (BPE gpt2, 2 seeds, 500 steps). CWA replaces GELU in FFN blocks.\",\n    \"total_examples\": 150\n  },\n  \"shakespeare_bpc\": {\n    \"gelu\": {\n      \"mean\": 3.2252450715271874,\n      \"std\": 0.009753319084885793,\n      \"per_seed\": [\n        3.2293590570529664,\n        3.2345897098790837,\n        3.2117864476495117\n      ]\n    },\n    \"gelu+ln\": {\n      \"mean\": 3.260416766489922,\n      \"std\": 0.0018300403101225073,\n      \"per_seed\": [\n        3.262419722303911,\n        3.2608346889177224,\n        3.2579958882481326\n      ]\n    },\n    \"selu\": {\n      \"mean\": 3.3514590756186386,\n      \"std\": 0.0010407082653683345,\n      \"per_seed\": [\n        3.3514208129184744,\n        3.352752378273821,\n        3.3502040356636202\n      ]\n    },\n    \"tanh_swish\": {\n      \"mean\": 3.3371464867932663,\n      \"std\": 0.002093143723628238,\n      \"per_seed\": [\n        3.338893080681675,\n        3.338342956336707,\n        3.3342034233614175\n      ]\n    },\n    \"cwa\": {\n      \"mean\": 3.351850349907963,\n      \"std\": 0.004222720089646927,\n      \"per_seed\": [\n        3.3576810158064108,\n        3.350052849154899,\n        3.3478171847625795\n      ]\n    }\n  },\n  \"wikitext2_ppl\": {\n    \"gelu\": {\n      \"mean\": 738.7480346569839,\n      \"std\": 7.017439422271366,\n      \"per_seed\": [\n        745.7654740792553,\n        731.7305952347126", "numLines": 60, "startLine": 1, "totalLines": 3669}}
```

### [7] TOOL CALL — Read · 2026-06-16 19:11:54 UTC

```
/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_experiment_2/full_method_out.json
```

### [8] TOOL RESULT — Read · 2026-06-16 19:11:54 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_experiment_2/full_method_out.json", "content": "{\n  \"metadata\": {\n    \"method_name\": \"CWA (Curie-Weiss Activation)\",\n    \"description\": \"ResNet-20 CIFAR-100 width analysis + overhead benchmark (interim)\",\n    \"timestamp\": \"2026-06-16T18:53:25.016341\",\n    \"verdict\": {\n      \"memory_within_2x\": null,\n      \"cwa_vs_gelu_no_bn_significant\": false,\n      \"soc_observed\": false,\n      \"mean_final_J_s_bar\": 0.30578322721243323,\n      \"width_positive_correlation\": null,\n      \"cwa_acc_standard_no_bn\": 0.1401,\n      \"gelu_acc_standard_no_bn\": 0.1893,\n      \"note\": \"interim result — experiment still running\"\n    },\n    \"n_examples\": 56\n  },\n  \"datasets\": [\n    {\n      \"dataset\": \"CIFAR-100+synthetic-overhead\",\n      \"examples\": [\n        {\n          \"input\": \"ResNet-20 CIFAR-100 config=standard_no_bn (widths=[16, 32, 64], use_bn=False), activation=CWA, seed=0, epoch=0/9.\",\n          \"output\": \"test_acc=0.0689 at epoch 0. Final acc=0.1401.\",\n          \"metadata_experiment\": \"exp2_cifar100_per_epoch\",\n          \"metadata_config\": \"standard_no_bn\",\n          \"metadata_activation\": \"CWA\",\n          \"metadata_seed\": \"0\",\n          \"metadata_epoch\": \"0\",\n          \"predict_cwa\": \"acc=0.0689\"\n        },\n        {\n          \"input\": \"ResNet-20 CIFAR-100 config=standard_no_bn (widths=[16, 32, 64], use_bn=False), activation=CWA, seed=0, epoch=1/9.\",\n          \"output\": \"test_acc=0.0887 at epoch 1. Final acc=0.1401.\",\n          \"metadata_experiment\": \"exp2_cifar100_per_epoch\",\n          \"metadata_config\": \"standard_no_bn\",\n          \"metadata_activation\": \"CWA\",\n          \"metadata_seed\": \"0\",\n          \"metadata_epoch\": \"1\",\n          \"predict_cwa\": \"acc=0.0887\"\n        },\n        {\n          \"input\": \"ResNet-20 CIFAR-100 config=standard_no_bn (widths=[16, 32, 64], use_bn=False), activation=CWA, seed=0, epoch=2/9.\",\n          \"output\": \"test_acc=0.1015 at epoch 2. Final acc=0.1401.\",\n          \"metadata_experiment\": \"exp2_cifar100_per_epoch\",\n          \"metadata_config\": \"standard_no_bn\",\n          \"metadata_activation\": \"CWA\",\n          \"metadata_seed\": \"0\",\n          \"metadata_epoch\": \"2\",\n          \"predict_cwa\": \"acc=0.1015\"\n        },\n        {\n          \"input\": \"ResNet-20 CIFAR-100 config=standard_no_bn (widths=[16, 32, 64], use_bn=False), activation=CWA, seed=0, epoch=3/9.\",\n          \"output\": \"test_acc=0.1128 at epoch 3. Final acc=0.1401.\",\n          \"metadata_experiment\": \"exp2_cifar100_per_epoch\",\n          \"metadata_config\": \"standard_no_bn\",\n          \"metadata_activation\": \"CWA\",\n          \"metadata_seed\": \"0\",\n          \"metadata_epoch\": \"3\",\n          \"predict_cwa\": \"acc=0.1128\"", "numLines": 60, "startLine": 1, "totalLines": 572}}
```

### [9] ASSISTANT · 2026-06-16 19:14:17 UTC

```
Now I have enough evidence. Let me write the revised hypothesis.
```

### [10] TOOL CALL — Write · 2026-06-16 19:14:17 UTC

```
File: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json

{
  "title": "Curie-Weiss Activation Requires Targeted J Training: Fixed-J Coupling or Amplified J-LR for Gradient Stability in Unnormalized Deep Networks",
  "hypothesis": "A neural network hidden-layer activation function defined as the fixed point y* of the Curie-Weiss mean-field self-consistency equation — y_i = tanh(x_i + J·mean_neurons(y)) for all neurons i in a layer, where J = σ(J_raw) ∈ (0,1) is a per-layer scalar coupling — can provide gradient stability benefits in unnormalized deep networks (≥10 layers) ONLY when J is explicitly driven toward the near-critical regime (J·s̄ ≥ 0.7), either via (a) fixed near-critical coupling (J frozen at 0.7–0.9, no learning) or (b) a dedicated high learning rate for J_raw (100× the weight LR). Under standard gradient descent with a shared optimizer, J does not self-organize: J remains within 0.003 of its initialization (0.5) after 500 training steps, J·s̄ stabilizes at 0.44–0.46, and CWA performs uniformly worse than GELU (BPC 3.352 vs 3.225 on Tiny Shakespeare; PPL 767 vs 739 on WikiText-2; 14.0% vs 18.9% CIFAR-100 no-BN). The gradient signal on J_raw is orders of magnitude weaker than weight gradients, making J a near-frozen parameter under shared-LR training. The primary claims that require validation in the next iteration are therefore: (1) GATING EXPERIMENT — whether any fixed J ∈ {0.1, 0.3, 0.5, 0.7, 0.9} in a 10-layer unnormalized MLP provides gradient stability (ratio < 2.0 at depth 10) compared to GELU (ratio > 5.0); if fixed J=0.7–0.9 already helps, the mean-field coupling mechanism itself is sound and the SOC failure is purely a training artifact; (2) CORE MISSING EXPERIMENT — CWA at depths {6, 10, 20} with 3 seeds and 25 epochs in unnormalized MLPs (the primary hypothesis domain, which was not evaluated in iter 1); (3) HIGH-LR SENSITIVITY — whether 100× learning rate on J_raw (with shared LR for weights) causes J to self-organize toward criticality and improve accuracy, tested for ≥5000 steps. The hybrid IFT/unrolled backprop strategy remains mathematically sound (Lean 4 verified), but the IFT branch was never triggered in iter 1 (0 IFT calls across all experiments since J·s̄ < 0.8 throughout); a synthetic benchmark initializing J_raw = +4.0 (J ≈ 0.982) is required to demonstrate the IFT memory advantage empirically. Two implementation inconsistencies must be corrected: (a) the code uses tolerance δ = 1e-4·(1−J·s̄) but the Lean proof bounds bias with 1e-4·(1−J) — since J·s̄ < J, the code is looser and the proven bound does not apply as stated; (b) the 'unrolled autograd' backward is actually warm-start-3 (3 tracked steps from detached m*), introducing O(ρ^3 ≈ 0.09) relative gradient bias that must be acknowledged. The fixed-J ablation is the decisive test: if CWA at J=0.7 or J=0.9 outperforms GELU in gradient stability and accuracy in unnormalized deep MLPs, then the Curie-Weiss mean-field coupling mechanism provides genuine value independent of self-organization, and CWA should be deployed with fixed near-critical J rather than learned J.",
  "motivation": "All standard hidden-layer activation functions — ReLU, GELU, Swish, tanh — are applied pointwise, requiring external normalization for deep unnormalized networks. Iter 1 established empirically that CWA with standard training fails because J does not self-organize: the gradient on J_raw is overwhelmed by weight gradients (fourth-order vs second-order depth dependence), causing J to freeze at initialization. This failure is informative: it separates the MECHANISM question (does within-layer mean-field coupling provide gradient stability?) from the OPTIMIZATION question (does gradient descent drive J to the critical point?). The fixed-J ablation resolves the mechanism question directly at zero optimization cost. If fixed J=0.9 provides gradient stability in 20-layer unnormalized MLPs where GELU diverges, the contribution is reframed as: CWA with fixed near-critical J is a simple, parameter-free (zero additional parameters) drop-in normalization-free gain control that provides edge-of-chaos criticality analogously to Competing Nonlinearities (Lesser & Chowdhury 2026) but with a deterministic coupling rather than a random mixture. If fixed J also fails, the conclusion is that mean-field coupling within a layer does not provide the connectivity benefits predicted by Curie-Weiss theory at finite width and practical depth — a clear null result that closes this research direction. Three practically important settings for unnormalized networks remain: (a) on-device inference (no running-statistics memory); (b) physics-informed neural networks (normalization distorts conservation laws); (c) fast-inference transformers eliminating LayerNorm. CWA with a fixed high J could serve all three settings as a zero-parameter drop-in if the mechanism validates.",
  "assumptions": [
    "The adaptive-K fixed-point iteration m_{t+1} = mean_neurons(tanh(x + J·m_t)) converges with geometric rate ρ = J·s̄ < 1 (Banach fixed-point theorem, Lean 4 verified). At J=0.5 and typical pre-activations, ρ ≈ 0.45 and K ≤ 5 iterations suffice to reach δ = 1e-4·(1−J·s̄) tolerance. At J=0.9 (near-critical), ρ ≈ 0.8–0.9 and K may reach K_max=50; the K_max=5 cap used in iter 1 is corrected to K_max=50 in the next iteration.",
    "Standard gradient descent with shared optimizer does NOT self-organize J toward criticality (empirically confirmed in iter 1: J ∈ [0.498, 0.501] after 500 steps). Two interventions may overcome this: (a) fixed J at a near-critical value (J=0.7–0.9), eliminating the optimization problem entirely; (b) separate learning rate for J_raw at 100× the weight LR. Both are tested in the next iteration.",
    "The hybrid IFT/unrolled backward is corrected for next iteration: (a) true unrolled autograd (K iterations retained in computation graph, not warm-start-3) when J·s̄ < 0.8; (b) IFT closed-form backward when J·s̄ ≥ 0.8. The Lean-proven bias bound requires tolerance 1e-4·(1−J), not 1e-4·(1−J·s̄); the code is updated to match. The K_max=50 cap from the method section is enforced in code (iter 1 used K_max=5).",
    "Finite-width noise O(1/√n) at narrow layers (n=16 in ResNet-20 first block ≈ 25% noise floor) remains an acknowledged limitation. Fixed-J ablation in the width-256 MLP setting (n=256, noise floor ≈ 6%) tests whether mean-field coupling is accurate enough at practical hidden dimensions.",
    "The Competing Nonlinearities baseline uses p_c=0.83 (empirical K₀=1 calibration, consistent across all experiments). This value was inconsistently reported as p_c=0.5 in Exp 1 of iter 1; the next iteration uses p_c=0.83 uniformly."
  ],
  "investigation_approach": "PRIORITY 1 — FIXED-J ABLATION (Exp 4, was incomplete in iter 1): Train 10-layer unnormalized MLP on CIFAR-10 with J frozen at {0.1, 0.3, 0.5, 0.7, 0.9} vs learned J vs standard baselines (GELU, SELU, tanh+LN). Measure gradient norm ratio |log‖∇W₁‖/log‖∇W_L‖| and final accuracy. 5 seeds, 25 epochs, hidden_dim=256. This is the gating experiment: if fixed J=0.9 achieves gradient ratio < 2.0 while GELU exceeds 5.0, the mechanism is validated independent of self-organization.\n\nPRIORITY 2 — CORE GRADIENT STABILITY (Exp 1, was incomplete in iter 1): Train unnormalized MLPs at depths {6, 10, 20} with 256 hidden units on CIFAR-10 for 25 epochs with 5 seeds. Compare CWA (learned J), CWA-fixed-J-best (best J from Priority 1), ReLU, GELU, Swish, tanh, SELU, tanh+LN, GELU+LN, Competing Nonlinearities (p_c=0.83). Use TRUE unrolled autograd backward (K iterations retained in graph) and K_max=50. Report gradient ratio at epochs 5 and 25.\n\nPRIORITY 3 — HIGH-LR J SENSITIVITY (new): Take the best learned-J CWA configuration from Priority 2 and run with J_raw LR = 100× weight LR for 5000 steps. Track J and J·s̄ per step. Compute d(J)/d(step) from iter 1's 500-step trajectory and report the extrapolated step count needed for J to move by 0.05 at shared LR. If 100× LR causes detectable J movement, report whether J·s̄ approaches the critical value and whether this improves accuracy.\n\nPRIORITY 4 — IFT SYNTHETIC BENCHMARK: Initialize J_raw = +4.0 (J ≈ 0.982, J·s̄ ≈ 0.95) in a 6-layer MLP and measure: (1) whether the IFT branch triggers (J·s̄ > 0.8 threshold), (2) peak GPU memory vs unrolled, (3) numerical stability. This validates the IFT memory claim which was never exercised in iter 1.\n\nPRIORITY 5 — LANGUAGE MODEL (extended, from 500 to 5000 steps): Run 6L/256H GPT on Tiny Shakespeare (3 seeds) with GELU, CWA-learned-J, and CWA-fixed-J-best (from Priority 1). Use cosine LR schedule. K_max=50 (not 5). Report BPC at steps {500, 1000, 2500, 5000}.\n\nIMPLEMENTATION CORRECTIONS: (a) K_max = 50 (not 5); (b) true unrolled backward (not warm-start-3); (c) tolerance δ = 1e-4·(1−J) to match Lean proof; (d) Competing Nonlinearities p_c = 0.83 uniformly; (e) at least 3 seeds for all multi-seed experiments; (f) report paired t-tests for all multi-seed comparisons.",
  "success_criteria": "MECHANISM CONFIRMED if: Fixed J ∈ {0.7, 0.9} in 10-layer unnormalized MLP achieves gradient ratio < 2.0 while GELU achieves ratio > 5.0, with 95% CI separation over 5 seeds. This validates the mean-field coupling mechanism independent of self-organization. MECHANISM DISCONFIRMED if: No fixed J value improves gradient ratio below 3.0 vs GELU — indicating mean-field coupling provides no gradient stability benefit at finite width. SOC ACHIEVABLE if: J_raw at 100× LR causes J to move > 0.05 in 5000 steps and improves accuracy by > 0.5% over standard-LR CWA. SOC BLOCKED if: 100× LR also fails to move J > 0.05 — a strong negative result indicating the signal-to-noise ratio on J is fundamentally inadequate under cross-entropy training. IFT CONFIRMED if: J_raw=+4.0 initialization triggers IFT branch in > 80% of forward calls and achieves peak memory < 1.5× unrolled at equivalent J·s̄. NULL RESULT (closes direction) if: Mechanism is DISCONFIRMED AND SOC is BLOCKED AND IFT is not triggered under any practical initialization — the overall finding is that within-layer Curie-Weiss mean-field coupling does not provide gradient stability in finite-width networks under gradient descent training, and the null result is the contribution.",
  "related_works": [
    "Boltzmann Attention (Kim & Park, arXiv:2606.12478, NeurIPS 2026): Learnable pairwise Ising couplings J_{jk} in the attention operator (inter-token, quadratic O(n²) couplings). Complementary to CWA (inter-neuron within a single layer via scalar J). Could be combined with CWA.",
    "Competing Nonlinearities (Lesser & Chowdhury, arXiv:2605.05294, 2026): Achieves edge-of-chaos criticality via static quenched tanh/Swish mixture at p_c=0.83 (empirical, K₀=1) / p_c=32/35 (analytical, K₀→0). No learnable parameter, no inter-neuron coupling. CWA with fixed near-critical J is the learnable-parameter-free analog: replaces the random quenched mask with a deterministic scalar. Iter 1 shows CWA performs comparably to Competing Nonlinearities in language modeling (BPC 3.352 vs 3.337) under standard training; fixed-J ablation tests whether high-J CWA can exceed it.",
    "Deep Equilibrium Models / DEQ (Bai et al., arXiv:1909.01377, NeurIPS 2019): IFT for O(1) activation memory in full-layer fixed points. CWA reduces the DEQ vector system to a closed-form scalar formula. IFT branch triggered 0 times in iter 1 (J·s̄ < 0.8 always); synthetic benchmark with J_raw=+4.0 required to validate the memory claim.",
    "SELU (Klambauer et al., NeurIPS 2017): Pointwise distributional fixed-point approach. Outperforms CWA in all iter 1 experiments (SELU 23.8% vs CWA 14.0% on CIFAR-100 no-BN; SELU BPC 3.351 vs CWA 3.352 — essentially tied). If fixed-J CWA also fails to beat SELU, the distributional fixed-point approach is more effective than mean-field coupling for normalization-free gradient stability.",
    "Yang & Schoenholz (2017) and Poole et al. (2016): Edge-of-chaos criticality achievable at initialization via weight variance tuning. CWA's fixed-J variant provides a runtime mechanism for criticality at the activation level — if high fixed J provides the benefit, this complements initialization-based criticality by making it input-adaptive."
  ],
  "inspiration": "The Curie-Weiss cross-domain transfer remains valid. Iter 1's negative results sharpen the analogy: in physics, ferromagnets achieve criticality only when temperature is tuned to the Curie point — spontaneous magnetization does not emerge from arbitrary thermal fluctuations. Similarly, CWA reaches the critical regime only when J is explicitly tuned (fixed near 1 or optimized with amplified gradient signal). The iter 1 failure matches the physical picture: starting at J=0.5 with standard gradient descent is analogous to starting the magnet far from its Curie temperature with weak thermal driving — it stays subcritical. The revised hypothesis tests whether fixing J near the Curie point (J=0.9) achieves the susceptibility benefits even without self-organization, analogous to operating a ferromagnet at a fixed temperature near T_c.",
  "terms": [
    {
      "term": "Curie-Weiss Activation (CWA)",
      "definition": "The proposed hidden-layer activation function defined by the fixed point y* of the mean-field self-consistency equation y = tanh(x + J·mean_neurons(y)), where J ∈ (0,1) is a per-layer scalar coupling (either fixed or learned) and mean_neurons(y) = (1/n)Σ_i y_i is the within-sample neuron-wise mean. Fixed point found by adaptive-K iteration with K_max=50 and tolerance δ = 1e-4·(1−J)."
    },
    {
      "term": "SOC Failure (empirical)",
      "definition": "The empirical finding from iter 1 that J does not self-organize toward criticality under standard gradient descent: J stayed in [0.498, 0.501] after 500 training steps across all experiments. Attributed to gradient competition (J_raw gradient is fourth-order in depth vs second-order for weights) and insufficient training time."
    },
    {
      "term": "Fixed-J CWA",
      "definition": "CWA variant with J frozen at a fixed value (no optimization), tested at J ∈ {0.1, 0.3, 0.5, 0.7, 0.9}. Zero additional parameters. Decouples the mechanism question (does mean-field coupling help?) from the optimization question (does gradient descent find the right J?). Primary gating experiment for iter 2."
    },
    {
      "term": "High-LR J Training",
      "definition": "CWA variant with J_raw optimized at 100× the weight learning rate, using a parameter group with separate LR in the optimizer. Tests whether amplified gradient signal is sufficient to drive J toward the critical regime when shared LR is insufficient."
    },
    {
      "term": "Effective Coupling (J·s̄)",
      "definition": "J·s̄ = J·mean_neurons(sech²(x+J·m*)) ∈ (0,1): simultaneously the fixed-point iteration convergence rate, the spectral norm of the layer's Jacobian, and the distance to the critical point. Iter 1 shows J·s̄ stabilizes at 0.44–0.46 (subcritical) under standard training."
    },
    {
      "term": "Warm-Start-3 Backward (deprecated)",
      "definition": "The iter 1 implementation bug: K forward iterations run without gradient tracking to find m*, followed by 3 tracked iterations from detached m*. Introduces O(ρ^3 ≈ 0.09) relative gradient bias vs true IFT. Replaced in iter 2 by true unrolled autograd (K tracked iterations) when J·s̄ < 0.8 and exact IFT backward when J·s̄ ≥ 0.8."
    }
  ],
  "summary": "We propose the Curie-Weiss Activation (CWA), a hidden-layer activation defined by within-sample scalar mean-field fixed-point y_i = tanh(x_i + J·mean_neurons(y)). Iter 1 established that under standard gradient descent, J does not self-organize (J ∈ [0.498, 0.501] after 500 steps; J·s̄ ≈ 0.44–0.46) and CWA underperforms GELU on all completed benchmarks. The revised hypothesis narrows the positive claim: CWA provides gradient stability benefits ONLY when J is explicitly driven near-critical, via fixed J (J=0.7–0.9, primary iter 2 test) or amplified J-LR (100×). The core missing experiments — CWA gradient stability at depths 6/10/20 and the fixed-J ablation — are the primary deliverables for iter 2, with implementation corrections (K_max=50, true unrolled backward, tolerance matching Lean proof, uniform p_c=0.83).",
  "relation_type": "evolution",
  "relation_rationale": "Same CWA mechanism; narrows positive claim to require explicit near-critical J training after SOC failure confirmed in iter 1.",
  "confidence_delta": "decreased",
  "key_changes": [
    "Primary positive claim narrowed: CWA only provides gradient stability benefits when J is explicitly driven near-critical (fixed J=0.7–0.9 or 100× J-LR), not under standard shared-LR training.",
    "SOC failure added as an established empirical finding: J ∈ [0.498, 0.501] after 500 steps (not a hypothesis anymore — confirmed negative result).",
    "Fixed-J ablation elevated to PRIORITY 1 gating experiment: if any fixed J provides gradient stability, mechanism is validated independent of self-organization.",
    "High-LR J sensitivity (100× J-LR, ≥5000 steps) added as new experiment to test whether amplified gradient signal enables J self-organization.",
    "IFT synthetic benchmark added (J_raw=+4.0 initialization) to empirically validate memory claims that were never exercised in iter 1 (0 IFT calls).",
    "Language model training extended from 500 to 5000 steps with cosine LR schedule.",
    "Implementation corrections mandated: K_max=50 (was 5), true unrolled backward (not warm-start-3), tolerance δ=1e-4·(1−J) matching Lean proof, uniform p_c=0.83.",
    "Null result framing added: if mechanism is DISCONFIRMED and SOC is BLOCKED, the finding is that within-layer mean-field coupling does not provide gradient stability in finite-width networks under gradient descent — a clean, publishable negative result.",
    "Competing Nonlinearities baseline standardized to p_c=0.83 uniformly across all experiments (was inconsistently p_c=0.5 in Exp 1 of iter 1).",
    "Statistical significance tests (paired t-test, Welch's t-test) mandated for all multi-seed comparisons."
  ],
  "artifact_relations": [
    {
      "from_id": "art_Lj-xi6yJR_yy",
      "to_id": "art_kKv207AAQYq2",
      "relation_type": "uses",
      "relation_rationale": "Exp 1+4 used IFT gradient formulas and p_c derivation from the research artifact for CWA and CompetingNonlinearities."
    },
    {
      "from_id": "art_Lj-xi6yJR_yy",
      "to_id": "art_SVlh9mQatV8y",
      "relation_type": "uses",
      "relation_rationale": "ResNet exp used IFT backward formulas and SELU derivation from research artifact for CWA implementation."
    },
    {
      "from_id": "art_Lj-xi6yJR_yy",
      "to_id": "art_DdhxnRglYGM6",
      "relation_type": "uses",
      "relation_rationale": "GPT experiment used DEQ IFT scalar closed-form and p_c from research artifact for CWA FFN layers."
    },
    {
      "from_id": "art_Mx697ZSMEjH9",
      "to_id": "art_kKv207AAQYq2",
      "relation_type": "background",
      "relation_rationale": "Lean convergence proof motivated the J∈(0,1) sigmoid parameterization and K_max bounds used in Exp 1+4."
    },
    {
      "from_id": "art_Mx697ZSMEjH9",
      "to_id": "art_SVlh9mQatV8y",
      "relation_type": "background",
      "relation_rationale": "Lean IFT gradient correctness proof underpins the IFT backward used in ResNet experiment."
    },
    {
      "from_id": "art_Mx697ZSMEjH9",
      "to_id": "art_DdhxnRglYGM6",
      "relation_type": "background",
      "relation_rationale": "Lean bias bound theorem provides theoretical guarantee for IFT backward used in GPT experiment."
    }
  ]
}
```

### [11] TOOL RESULT — Write · 2026-06-16 19:14:17 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Curie-Weiss Activation Requires Targeted J Training: Fixed-J Coupling or Amplified J-LR for Gradient Stability in Unnormalized Deep Networks\",\n  \"hypothesis\": \"A neural network hidden-layer activation function defined as the fixed point y* of the Curie-Weiss mean-field self-consistency equation — y_i = tanh(x_i + J·mean_neurons(y)) for all neurons i in a layer, where J = σ(J_raw) ∈ (0,1) is a per-layer scalar coupling — can provide gradient stability benefits in unnormalized deep networks (≥10 layers) ONLY when J is explicitly driven toward the near-critical regime (J·s̄ ≥ 0.7), either via (a) fixed near-critical coupling (J frozen at 0.7–0.9, no learning) or (b) a dedicated high learning rate for J_raw (100× the weight LR). Under standard gradient descent with a shared optimizer, J does not self-organize: J remains within 0.003 of its initialization (0.5) after 500 training steps, J·s̄ stabilizes at 0.44–0.46, and CWA performs uniformly worse than GELU (BPC 3.352 vs 3.225 on Tiny Shakespeare; PPL 767 vs 739 on WikiText-2; 14.0% vs 18.9% CIFAR-100 no-BN). The gradient signal on J_raw is orders of magnitude weaker than weight gradients, making J a near-frozen parameter under shared-LR training. The primary claims that require validation in the next iteration are therefore: (1) GATING EXPERIMENT — whether any fixed J ∈ {0.1, 0.3, 0.5, 0.7, 0.9} in a 10-layer unnormalized MLP provides gradient stability (ratio < 2.0 at depth 10) compared to GELU (ratio > 5.0); if fixed J=0.7–0.9 already helps, the mean-field coupling mechanism itself is sound and the SOC failure is purely a training artifact; (2) CORE MISSING EXPERIMENT — CWA at depths {6, 10, 20} with 3 seeds and 25 epochs in unnormalized MLPs (the primary hypothesis domain, which was not evaluated in iter 1); (3) HIGH-LR SENSITIVITY — whether 100× learning rate on J_raw (with shared LR for weights) causes J to self-organize toward criticality and improve accuracy, tested for ≥5000 steps. The hybrid IFT/unrolled backprop strategy remains mathematically sound (Lean 4 verified), but the IFT branch was never triggered in iter 1 (0 IFT calls across all experiments since J·s̄ < 0.8 throughout); a synthetic benchmark initializing J_raw = +4.0 (J ≈ 0.982) is required to demonstrate the IFT memory advantage empirically. Two implementation inconsistencies must be corrected: (a) the code uses tolerance δ = 1e-4·(1−J·s̄) but the Lean proof bounds bias with 1e-4·(1−J) — since J·s̄ < J, the code is looser and the proven bound does not apply as stated; (b) the 'unrolled autograd' backward is actually warm-start-3 (3 tracked steps from detached m*), introducing O(ρ^3 ≈ 0.09) relative gradient bias that must be acknowledged. The fixed-J ablation is the decisive test: if CWA at J=0.7 or J=0.9 outperforms GELU in gradient stability and accuracy in unnormalized deep MLPs, then the Curie-Weiss mean-field coupling mechanism provides genuine value independent of self-organization, and CWA should be deployed with fixed near-critical J rather than learned J.\",\n  \"motivation\": \"All standard hidden-layer activation functions — ReLU, GELU, Swish, tanh — are applied pointwise, requiring external normalization for deep unnormalized networks. Iter 1 established empirically that CWA with standard training fails because J does not self-organize: the gradient on J_raw is overwhelmed by weight gradients (fourth-order vs second-order depth dependence), causing J to freeze at initialization. This failure is informative: it separates the MECHANISM question (does within-layer mean-field coupling provide gradient stability?) from the OPTIMIZATION question (does gradient descent drive J to the critical point?). The fixed-J ablation resolves the mechanism question directly at zero optimization cost. If fixed J=0.9 provides gradient stability in 20-layer unnormalized MLPs where GELU diverges, the contribution is reframed as: CWA with fixed near-critical J is a simple, parameter-free (zero additional parameters) drop-in normalization-free gain control that provides edge-of-chaos criticality analogously to Competing Nonlinearities (Lesser & Chowdhury 2026) but with a deterministic coupling rather than a random mixture. If fixed J also fails, the conclusion is that mean-field coupling within a layer does not provide the connectivity benefits predicted by Curie-Weiss theory at finite width and practical depth — a clear null result that closes this research direction. Three practically important settings for unnormalized networks remain: (a) on-device inference (no running-statistics memory); (b) physics-informed neural networks (normalization distorts conservation laws); (c) fast-inference transformers eliminating LayerNorm. CWA with a fixed high J could serve all three settings as a zero-parameter drop-in if the mechanism validates.\",\n  \"assumptions\": [\n    \"The adaptive-K fixed-point iteration m_{t+1} = mean_neurons(tanh(x + J·m_t)) converges with geometric rate ρ = J·s̄ < 1 (Banach fixed-point theorem, Lean 4 verified). At J=0.5 and typical pre-activations, ρ ≈ 0.45 and K ≤ 5 iterations suffice to reach δ = 1e-4·(1−J·s̄) tolerance. At J=0.9 (near-critical), ρ ≈ 0.8–0.9 and K may reach K_max=50; the K_max=5 cap used in iter 1 is corrected to K_max=50 in the next iteration.\",\n    \"Standard gradient descent with shared optimizer does NOT self-organize J toward criticality (empirically confirmed in iter 1: J ∈ [0.498, 0.501] after 500 steps). Two interventions may overcome this: (a) fixed J at a near-critical value (J=0.7–0.9), eliminating the optimization problem entirely; (b) separate learning rate for J_raw at 100× the weight LR. Both are tested in the next iteration.\",\n    \"The hybrid IFT/unrolled backward is corrected for next iteration: (a) true unrolled autograd (K iterations retained in computation graph, not warm-start-3) when J·s̄ < 0.8; (b) IFT closed-form backward when J·s̄ ≥ 0.8. The Lean-proven bias bound requires tolerance 1e-4·(1−J), not 1e-4·(1−J·s̄); the code is updated to match. The K_max=50 cap from the method section is enforced in code (iter 1 used K_max=5).\",\n    \"Finite-width noise O(1/√n) at narrow layers (n=16 in ResNet-20 first block ≈ 25% noise floor) remains an acknowledged limitation. Fixed-J ablation in the width-256 MLP setting (n=256, noise floor ≈ 6%) tests whether mean-field coupling is accurate enough at practical hidden dimensions.\",\n    \"The Competing Nonlinearities baseline uses p_c=0.83 (empirical K₀=1 calibration, consistent across all experiments). This value was inconsistently reported as p_c=0.5 in Exp 1 of iter 1; the next iteration uses p_c=0.83 uniformly.\"\n  ],\n  \"investigation_approach\": \"PRIORITY 1 — FIXED-J ABLATION (Exp 4, was incomplete in iter 1): Train 10-layer unnormalized MLP on CIFAR-10 with J frozen at {0.1, 0.3, 0.5, 0.7, 0.9} vs learned J vs standard baselines (GELU, SELU, tanh+LN). Measure gradient norm ratio |log‖∇W₁‖/log‖∇W_L‖| and final accuracy. 5 seeds, 25 epochs, hidden_dim=256. This is the gating experiment: if fixed J=0.9 achieves gradient ratio < 2.0 while GELU exceeds 5.0, the mechanism is validated independent of self-organization.\\n\\nPRIORITY 2 — CORE GRADIENT STABILITY (Exp 1, was incomplete in iter 1): Train unnormalized MLPs at depths {6, 10, 20} with 256 hidden units on CIFAR-10 for 25 epochs with 5 seeds. Compare CWA (learned J), CWA-fixed-J-best (best J from Priority 1), ReLU, GELU, Swish, tanh, SELU, tanh+LN, GELU+LN, Competing Nonlinearities (p_c=0.83). Use TRUE unrolled autograd backward (K iterations retained in graph) and K_max=50. Report gradient ratio at epochs 5 and 25.\\n\\nPRIORITY 3 — HIGH-LR J SENSITIVITY (new): Take the best learned-J CWA configuration from Priority 2 and run with J_raw LR = 100× weight LR for 5000 steps. Track J and J·s̄ per step. Compute d(J)/d(step) from iter 1's 500-step trajectory and report the extrapolated step count needed for J to move by 0.05 at shared LR. If 100× LR causes detectable J movement, report whether J·s̄ approaches the critical value and whether this improves accuracy.\\n\\nPRIORITY 4 — IFT SYNTHETIC BENCHMARK: Initialize J_raw = +4.0 (J ≈ 0.982, J·s̄ ≈ 0.95) in a 6-layer MLP and measure: (1) whether the IFT branch triggers (J·s̄ > 0.8 threshold), (2) peak GPU memory vs unrolled, (3) numerical stability. This validates the IFT memory claim which was never exercised in iter 1.\\n\\nPRIORITY 5 — LANGUAGE MODEL (extended, from 500 to 5000 steps): Run 6L/256H GPT on Tiny Shakespeare (3 seeds) with GELU, CWA-learned-J, and CWA-fixed-J-best (from Priority 1). Use cosine LR schedule. K_max=50 (not 5). Report BPC at steps {500, 1000, 2500, 5000}.\\n\\nIMPLEMENTATION CORRECTIONS: (a) K_max = 50 (not 5); (b) true unrolled backward (not warm-start-3); (c) tolerance δ = 1e-4·(1−J) to match Lean proof; (d) Competing Nonlinearities p_c = 0.83 uniformly; (e) at least 3 seeds for all multi-seed experiments; (f) report paired t-tests for all multi-seed comparisons.\",\n  \"success_criteria\": \"MECHANISM CONFIRMED if: Fixed J ∈ {0.7, 0.9} in 10-layer unnormalized MLP achieves gradient ratio < 2.0 while GELU achieves ratio > 5.0, with 95% CI separation over 5 seeds. This validates the mean-field coupling mechanism independent of self-organization. MECHANISM DISCONFIRMED if: No fixed J value improves gradient ratio below 3.0 vs GELU — indicating mean-field coupling provides no gradient stability benefit at finite width. SOC ACHIEVABLE if: J_raw at 100× LR causes J to move > 0.05 in 5000 steps and improves accuracy by > 0.5% over standard-LR CWA. SOC BLOCKED if: 100× LR also fails to move J > 0.05 — a strong negative result indicating the signal-to-noise ratio on J is fundamentally inadequate under cross-entropy training. IFT CONFIRMED if: J_raw=+4.0 initialization triggers IFT branch in > 80% of forward calls and achieves peak memory < 1.5× unrolled at equivalent J·s̄. NULL RESULT (closes direction) if: Mechanism is DISCONFIRMED AND SOC is BLOCKED AND IFT is not triggered under any practical initialization — the overall finding is that within-layer Curie-Weiss mean-field coupling does not provide gradient stability in finite-width networks under gradient descent training, and the null result is the contribution.\",\n  \"related_works\": [\n    \"Boltzmann Attention (Kim & Park, arXiv:2606.12478, NeurIPS 2026): Learnable pairwise Ising couplings J_{jk} in the attention operator (inter-token, quadratic O(n²) couplings). Complementary to CWA (inter-neuron within a single layer via scalar J). Could be combined with CWA.\",\n    \"Competing Nonlinearities (Lesser & Chowdhury, arXiv:2605.05294, 2026): Achieves edge-of-chaos criticality via static quenched tanh/Swish mixture at p_c=0.83 (empirical, K₀=1) / p_c=32/35 (analytical, K₀→0). No learnable parameter, no inter-neuron coupling. CWA with fixed near-critical J is the learnable-parameter-free analog: replaces the random quenched mask with a deterministic scalar. Iter 1 shows CWA performs comparably to Competing Nonlinearities in language modeling (BPC 3.352 vs 3.337) under standard training; fixed-J ablation tests whether high-J CWA can exceed it.\",\n    \"Deep Equilibrium Models / DEQ (Bai et al., arXiv:1909.01377, NeurIPS 2019): IFT for O(1) activation memory in full-layer fixed points. CWA reduces the DEQ vector system to a closed-form scalar formula. IFT branch triggered 0 times in iter 1 (J·s̄ < 0.8 always); synthetic benchmark with J_raw=+4.0 required to validate the memory claim.\",\n    \"SELU (Klambauer et al., NeurIPS 2017): Pointwise distributional fixed-point approach. Outperforms CWA in all iter 1 experiments (SELU 23.8% vs CWA 14.0% on CIFAR-100 no-BN; SELU BPC 3.351 vs CWA 3.352 — essentially tied). If fixed-J CWA also fails to beat SELU, the distributional fixed-point approach is more effective than mean-field coupling for normalization-free gradient stability.\",\n    \"Yang & Schoenholz (2017) and Poole et al. (2016): Edge-of-chaos criticality achievable at initialization via weight variance tuning. CWA's fixed-J variant provides a runtime mechanism for criticality at the activation level — if high fixed J provides the benefit, this complements initialization-based criticality by making it input-adaptive.\"\n  ],\n  \"inspiration\": \"The Curie-Weiss cross-domain transfer remains valid. Iter 1's negative results sharpen the analogy: in physics, ferromagnets achieve criticality only when temperature is tuned to the Curie point — spontaneous magnetization does not emerge from arbitrary thermal fluctuations. Similarly, CWA reaches the critical regime only when J is explicitly tuned (fixed near 1 or optimized with amplified gradient signal). The iter 1 failure matches the physical picture: starting at J=0.5 with standard gradient descent is analogous to starting the magnet far from its Curie temperature with weak thermal driving — it stays subcritical. The revised hypothesis tests whether fixing J near the Curie point (J=0.9) achieves the susceptibility benefits even without self-organization, analogous to operating a ferromagnet at a fixed temperature near T_c.\",\n  \"terms\": [\n    {\n      \"term\": \"Curie-Weiss Activation (CWA)\",\n      \"definition\": \"The proposed hidden-layer activation function defined by the fixed point y* of the mean-field self-consistency equation y = tanh(x + J·mean_neurons(y)), where J ∈ (0,1) is a per-layer scalar coupling (either fixed or learned) and mean_neurons(y) = (1/n)Σ_i y_i is the within-sample neuron-wise mean. Fixed point found by adaptive-K iteration with K_max=50 and tolerance δ = 1e-4·(1−J).\"\n    },\n    {\n      \"term\": \"SOC Failure (empirical)\",\n      \"definition\": \"The empirical finding from iter 1 that J does not self-organize toward criticality under standard gradient descent: J stayed in [0.498, 0.501] after 500 training steps across all experiments. Attributed to gradient competition (J_raw gradient is fourth-order in depth vs second-order for weights) and insufficient training time.\"\n    },\n    {\n      \"term\": \"Fixed-J CWA\",\n      \"definition\": \"CWA variant with J frozen at a fixed value (no optimization), tested at J ∈ {0.1, 0.3, 0.5, 0.7, 0.9}. Zero additional parameters. Decouples the mechanism question (does mean-field coupling help?) from the optimization question (does gradient descent find the right J?). Primary gating experiment for iter 2.\"\n    },\n    {\n      \"term\": \"High-LR J Training\",\n      \"definition\": \"CWA variant with J_raw optimized at 100× the weight learning rate, using a parameter group with separate LR in the optimizer. Tests whether amplified gradient signal is sufficient to drive J toward the critical regime when shared LR is insufficient.\"\n    },\n    {\n      \"term\": \"Effective Coupling (J·s̄)\",\n      \"definition\": \"J·s̄ = J·mean_neurons(sech²(x+J·m*)) ∈ (0,1): simultaneously the fixed-point iteration convergence rate, the spectral norm of the layer's Jacobian, and the distance to the critical point. Iter 1 shows J·s̄ stabilizes at 0.44–0.46 (subcritical) under standard training.\"\n    },\n    {\n      \"term\": \"Warm-Start-3 Backward (deprecated)\",\n      \"definition\": \"The iter 1 implementation bug: K forward iterations run without gradient tracking to find m*, followed by 3 tracked iterations from detached m*. Introduces O(ρ^3 ≈ 0.09) relative gradient bias vs true IFT. Replaced in iter 2 by true unrolled autograd (K tracked iterations) when J·s̄ < 0.8 and exact IFT backward when J·s̄ ≥ 0.8.\"\n    }\n  ],\n  \"summary\": \"We propose the Curie-Weiss Activation (CWA), a hidden-layer activation defined by within-sample scalar mean-field fixed-point y_i = tanh(x_i + J·mean_neurons(y)). Iter 1 established that under standard gradient descent, J does not self-organize (J ∈ [0.498, 0.501] after 500 steps; J·s̄ ≈ 0.44–0.46) and CWA underperforms GELU on all completed benchmarks. The revised hypothesis narrows the positive claim: CWA provides gradient stability benefits ONLY when J is explicitly driven near-critical, via fixed J (J=0.7–0.9, primary iter 2 test) or amplified J-LR (100×). The core missing experiments — CWA gradient stability at depths 6/10/20 and the fixed-J ablation — are the primary deliverables for iter 2, with implementation corrections (K_max=50, true unrolled backward, tolerance matching Lean proof, uniform p_c=0.83).\",\n  \"relation_type\": \"evolution\",\n  \"relation_rationale\": \"Same CWA mechanism; narrows positive claim to require explicit near-critical J training after SOC failure confirmed in iter 1.\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Primary positive claim narrowed: CWA only provides gradient stability benefits when J is explicitly driven near-critical (fixed J=0.7–0.9 or 100× J-LR), not under standard shared-LR training.\",\n    \"SOC failure added as an established empirical finding: J ∈ [0.498, 0.501] after 500 steps (not a hypothesis anymore — confirmed negative result).\",\n    \"Fixed-J ablation elevated to PRIORITY 1 gating experiment: if any fixed J provides gradient stability, mechanism is validated independent of self-organization.\",\n    \"High-LR J sensitivity (100× J-LR, ≥5000 steps) added as new experiment to test whether amplified gradient signal enables J self-organization.\",\n    \"IFT synthetic benchmark added (J_raw=+4.0 initialization) to empirically validate memory claims that were never exercised in iter 1 (0 IFT calls).\",\n    \"Language model training extended from 500 to 5000 steps with cosine LR schedule.\",\n    \"Implementation corrections mandated: K_max=50 (was 5), true unrolled backward (not warm-start-3), tolerance δ=1e-4·(1−J) matching Lean proof, uniform p_c=0.83.\",\n    \"Null result framing added: if mechanism is DISCONFIRMED and SOC is BLOCKED, the finding is that within-layer mean-field coupling does not provide gradient stability in finite-width networks under gradient descent — a clean, publishable negative result.\",\n    \"Competing Nonlinearities baseline standardized to p_c=0.83 uniformly across all experiments (was inconsistently p_c=0.5 in Exp 1 of iter 1).\",\n    \"Statistical significance tests (paired t-test, Welch's t-test) mandated for all multi-seed comparisons.\"\n  ],\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_Lj-xi6yJR_yy\",\n      \"to_id\": \"art_kKv207AAQYq2\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Exp 1+4 used IFT gradient formulas and p_c derivation from the research artifact for CWA and CompetingNonlinearities.\"\n    },\n    {\n      \"from_id\": \"art_Lj-xi6yJR_yy\",\n      \"to_id\": \"art_SVlh9mQatV8y\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"ResNet exp used IFT backward formulas and SELU derivation from research artifact for CWA implementation.\"\n    },\n    {\n      \"from_id\": \"art_Lj-xi6yJR_yy\",\n      \"to_id\": \"art_DdhxnRglYGM6\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"GPT experiment used DEQ IFT scalar closed-form and p_c from research artifact for CWA FFN layers.\"\n    },\n    {\n      \"from_id\": \"art_Mx697ZSMEjH9\",\n      \"to_id\": \"art_kKv207AAQYq2\",\n      \"relation_type\": \"background\",\n      \"relation_rationale\": \"Lean convergence proof motivated the J∈(0,1) sigmoid parameterization and K_max bounds used in Exp 1+4.\"\n    },\n    {\n      \"from_id\": \"art_Mx697ZSMEjH9\",\n      \"to_id\": \"art_SVlh9mQatV8y\",\n      \"relation_type\": \"background\",\n      \"relation_rationale\": \"Lean IFT gradient correctness proof underpins the IFT backward used in ResNet experiment.\"\n    },\n    {\n      \"from_id\": \"art_Mx697ZSMEjH9\",\n      \"to_id\": \"art_DdhxnRglYGM6\",\n      \"relation_type\": \"background\",\n      \"relation_rationale\": \"Lean bias bound theorem provides theoretical guarantee for IFT backward used in GPT experiment.\"\n    }\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [12] ASSISTANT · 2026-06-16 19:14:29 UTC

```
The revised hypothesis has been written. Here is a summary of the key changes made based on iter 1 evidence:

**Core revision: SOC failure is now an established finding, not a hypothesis**

- J stayed in [0.498, 0.501] after 500 steps across all experiments. The self-organized criticality claim is decisively disconfirmed under standard training.

**Narrowed positive claim**

- CWA can provide gradient stability benefits ONLY when J is explicitly driven near-critical — via fixed J (0.7–0.9) or a 100× dedicated learning rate for J_raw. Standard shared-LR training leaves J frozen.

**Priority reordering for iter 2**

1. **Fixed-J ablation** (was incomplete) → now Priority 1 gating experiment: if any fixed J provides gradient stability in 20-layer unnormalized MLPs, the mechanism is valid independent of self-organization
2. **Core gradient stability experiment** (CWA never evaluated at depths 6/10/20) → Priority 2
3. **High-LR J sensitivity** (100× J-LR, 5000 steps) → new Priority 3
4. **IFT synthetic benchmark** (J_raw=+4.0) → Priority 4, required since IFT triggered 0 times in iter 1

**Implementation corrections mandated**

- K_max: 50 (not 5 as used in code)
- Backward: true unrolled autograd (not warm-start-3 with O(ρ³≈0.09) bias)
- Tolerance: δ = 1e-4·(1−J) to match Lean proof (code used 1−J·s̄ which is looser)
- p_c = 0.83 uniformly (was inconsistently 0.5 in Exp 1)

**Null result framing preserved**: if the mechanism is also disconfirmed with fixed near-critical J, the finding is a clean negative result — within-layer mean-field coupling does not provide gradient stability in finite-width networks under gradient descent.
```

### [13] SYSTEM-USER prompt · 2026-06-16 19:14:31 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same CWA mechanism; narrows positive claim to require explicit near-critical J training after SOC failure confirmed in iter 1.' is too long (at most 120 characters, got 126)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [14] TOOL CALL — Edit · 2026-06-16 19:14:35 UTC

```
File: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json
OLD:   "relation_rationale": "Same CWA mechanism; narrows positive claim to require explicit near-critical J training after SOC failure confirmed in iter 1.",
NEW:   "relation_rationale": "Same CWA frame; narrows positive claim to require explicit near-critical J after SOC failure confirmed in iter 1.",
```

### [15] TOOL RESULT — Edit · 2026-06-16 19:14:35 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "oldString": "  \"relation_rationale\": \"Same CWA mechanism; narrows positive claim to require explicit near-critical J training after SOC failure confirmed in iter 1.\",", "newString": "  \"relation_rationale\": \"Same CWA frame; narrows positive claim to require explicit near-critical J after SOC failure confirmed in iter 1.\",", "originalFile": null, "structuredPatch": [{"oldStart": 47, "oldLines": 7, "newStart": 47, "newLines": 7, "lines": ["   ],", "   \"summary\": \"We propose the Curie-Weiss Activation (CWA), a hidden-layer activation defined by within-sample scalar mean-field fixed-point y_i = tanh(x_i + J·mean_neurons(y)). Iter 1 established that under standard gradient descent, J does not self-organize (J ∈ [0.498, 0.501] after 500 steps; J·s̄ ≈ 0.44–0.46) and CWA underperforms GELU on all completed benchmarks. The revised hypothesis narrows the positive claim: CWA provides gradient stability benefits ONLY when J is explicitly driven near-critical, via fixed J (J=0.7–0.9, primary iter 2 test) or amplified J-LR (100×). The core missing experiments — CWA gradient stability at depths 6/10/20 and the fixed-J ablation — are the primary deliverables for iter 2, with implementation corrections (K_max=50, true unrolled backward, tolerance matching Lean proof, uniform p_c=0.83).\",", "   \"relation_type\": \"evolution\",", "-  \"relation_rationale\": \"Same CWA mechanism; narrows positive claim to require explicit near-critical J training after SOC failure confirmed in iter 1.\",", "+  \"relation_rationale\": \"Same CWA frame; narrows positive claim to require explicit near-critical J after SOC failure confirmed in iter 1.\",", "   \"confidence_delta\": \"decreased\",", "   \"key_changes\": [", "     \"Primary positive claim narrowed: CWA only provides gradient stability benefits when J is explicitly driven near-critical (fixed J=0.7–0.9 or 100× J-LR), not under standard shared-LR training.\","]}], "userModified": false, "replaceAll": false}
```

### [16] ASSISTANT · 2026-06-16 19:14:36 UTC

```
Fixed — shortened `relation_rationale` from 126 to 113 characters.
```
