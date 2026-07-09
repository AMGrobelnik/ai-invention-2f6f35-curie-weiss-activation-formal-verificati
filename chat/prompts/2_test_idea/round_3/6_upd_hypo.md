# upd_hypo — test_idea

> Phase: `invention_loop` · round 3 · `upd_hypo`
> Run: `run_6gT5lHFn8559` — Novel Activation Function
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 22:24:28 UTC

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
  Curie-Weiss Activation Requires Targeted J Training: Fixed-J Coupling or Amplified J-LR for Gradient Stability in Unnormalized
  Deep Networks
hypothesis: >-
  A neural network hidden-layer activation function defined as the fixed point y* of the Curie-Weiss mean-field self-consistency
  equation — y_i = tanh(x_i + J·mean_neurons(y)) for all neurons i in a layer, where J = σ(J_raw) ∈ (0,1) is a per-layer scalar
  coupling — can provide gradient stability benefits in unnormalized deep networks (≥10 layers) ONLY when J is explicitly
  driven toward the near-critical regime (J·s̄ ≥ 0.7), either via (a) fixed near-critical coupling (J frozen at 0.7–0.9, no
  learning) or (b) a dedicated high learning rate for J_raw (100× the weight LR). Under standard gradient descent with a shared
  optimizer, J does not self-organize: J remains within 0.003 of its initialization (0.5) after 500 training steps, J·s̄ stabilizes
  at 0.44–0.46, and CWA performs uniformly worse than GELU (BPC 3.352 vs 3.225 on Tiny Shakespeare; PPL 767 vs 739 on WikiText-2;
  14.0% vs 18.9% CIFAR-100 no-BN). The gradient signal on J_raw is orders of magnitude weaker than weight gradients, making
  J a near-frozen parameter under shared-LR training. The primary claims that require validation in the next iteration are
  therefore: (1) GATING EXPERIMENT — whether any fixed J ∈ {0.1, 0.3, 0.5, 0.7, 0.9} in a 10-layer unnormalized MLP provides
  gradient stability (ratio < 2.0 at depth 10) compared to GELU (ratio > 5.0); if fixed J=0.7–0.9 already helps, the mean-field
  coupling mechanism itself is sound and the SOC failure is purely a training artifact; (2) CORE MISSING EXPERIMENT — CWA
  at depths {6, 10, 20} with 3 seeds and 25 epochs in unnormalized MLPs (the primary hypothesis domain, which was not evaluated
  in iter 1); (3) HIGH-LR SENSITIVITY — whether 100× learning rate on J_raw (with shared LR for weights) causes J to self-organize
  toward criticality and improve accuracy, tested for ≥5000 steps. The hybrid IFT/unrolled backprop strategy remains mathematically
  sound (Lean 4 verified), but the IFT branch was never triggered in iter 1 (0 IFT calls across all experiments since J·s̄
  < 0.8 throughout); a synthetic benchmark initializing J_raw = +4.0 (J ≈ 0.982) is required to demonstrate the IFT memory
  advantage empirically. Two implementation inconsistencies must be corrected: (a) the code uses tolerance δ = 1e-4·(1−J·s̄)
  but the Lean proof bounds bias with 1e-4·(1−J) — since J·s̄ < J, the code is looser and the proven bound does not apply
  as stated; (b) the 'unrolled autograd' backward is actually warm-start-3 (3 tracked steps from detached m*), introducing
  O(ρ^3 ≈ 0.09) relative gradient bias that must be acknowledged. The fixed-J ablation is the decisive test: if CWA at J=0.7
  or J=0.9 outperforms GELU in gradient stability and accuracy in unnormalized deep MLPs, then the Curie-Weiss mean-field
  coupling mechanism provides genuine value independent of self-organization, and CWA should be deployed with fixed near-critical
  J rather than learned J.
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
_relation_rationale: >-
  Same CWA frame; narrows positive claim to require explicit near-critical J after SOC failure confirmed in iter 1.
_confidence_delta: decreased
_key_changes:
- >-
  Primary positive claim narrowed: CWA only provides gradient stability benefits when J is explicitly driven near-critical
  (fixed J=0.7–0.9 or 100× J-LR), not under standard shared-LR training.
- >-
  SOC failure added as an established empirical finding: J ∈ [0.498, 0.501] after 500 steps (not a hypothesis anymore — confirmed
  negative result).
- >-
  Fixed-J ablation elevated to PRIORITY 1 gating experiment: if any fixed J provides gradient stability, mechanism is validated
  independent of self-organization.
- >-
  High-LR J sensitivity (100× J-LR, ≥5000 steps) added as new experiment to test whether amplified gradient signal enables
  J self-organization.
- >-
  IFT synthetic benchmark added (J_raw=+4.0 initialization) to empirically validate memory claims that were never exercised
  in iter 1 (0 IFT calls).
- Language model training extended from 500 to 5000 steps with cosine LR schedule.
- >-
  Implementation corrections mandated: K_max=50 (was 5), true unrolled backward (not warm-start-3), tolerance δ=1e-4·(1−J)
  matching Lean proof, uniform p_c=0.83.
- >-
  Null result framing added: if mechanism is DISCONFIRMED and SOC is BLOCKED, the finding is that within-layer mean-field
  coupling does not provide gradient stability in finite-width networks under gradient descent — a clean, publishable negative
  result.
- >-
  Competing Nonlinearities baseline standardized to p_c=0.83 uniformly across all experiments (was inconsistently p_c=0.5
  in Exp 1 of iter 1).
- >-
  Statistical significance tests (paired t-test, Welch's t-test) mandated for all multi-seed comparisons.
relation_type: evolution
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

--- Item 6 ---
id: art_v26XKv4_F1RM
type: experiment
in_dependencies:
- id: art_Lj-xi6yJR_yy
  label: IFT-implementation-guide
title: 'CWA vs Baselines: Depth Sweep + Fixed-J Ablation on CIFAR-10 (PARTIAL_CONFIRM)'
summary: |-
  This experiment implemented and evaluated the Curie-Weiss Activation (CWA) — a novel within-sample mean-field activation with learnable coupling J — against five baselines (ReLU, GELU, SELU, CompetingNonlinearities, GELU+LN) on CIFAR-10 image classification.

  **Experiment A — Depth Sweep (54 runs):** MLPs at depths {6, 10, 20} × 6 activations × 3 seeds, 25 epochs each, on GPU (RTX 5090). CWA uses a fixed-point iteration (K_max=50) to find m* = mean(tanh(x + J·m*)), then 3-step unrolled backward pass.

  **Experiment B — Fixed-J Ablation (21 runs):** J frozen at {0.1, 0.3, 0.5, 0.7, 0.9} plus learned J, at depth=10, 3 seeds each, testing the gradient-stability mechanism independently of learning.

  **Verdict: PARTIAL_CONFIRM.** The gradient stability mechanism is confirmed via fixed-J ablation (J=0.7 achieves grad_ratio=0.364, J=0.9 achieves 0.410 — both below 2.0 threshold), but the accuracy advantage claimed by the hypothesis is not observed (CWA accuracy < GELU at all depths: 0.483 vs 0.531 at depth 6; 0.472 vs 0.511 at depth 10; 0.141 vs 0.306 at depth 20).

  **Key quantitative results:**
  - Depth 6: CWA grad_ratio=0.305 vs GELU=0.712 (CWA more balanced), but CWA acc=0.483 vs GELU=0.531
  - Depth 10: CWA grad_ratio=0.347 vs GELU=0.735 (CWA more balanced), but CWA acc=0.472 vs GELU=0.511
  - Depth 20: CWA collapses (acc=0.141, grad_ratio=11.0) while GELU partially survives (acc=0.306, grad_ratio=2.76)
  - SELU performs best at depth 20 (acc=0.537), consistent with its self-normalizing property
  - Learned J converges to J*s_bar ≈ 0.285 (sub-critical regime), IFT branch (J*s_bar≥0.8) never triggered
  - Fixed-J ablation confirms the mechanism: near-critical J (0.7-0.9) achieves better gradient balance than GELU

  **Output files:** 72 experiment results in exp_gen_sol_out schema format, with full summary tables, statistical tests, and per-run gradient trajectory data.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 7 ---
id: art_V46hELP73T_t
type: experiment
in_dependencies:
- id: art_Lj-xi6yJR_yy
  label: IFT-formulas
title: 'CWA Iter2 Exp2: IFT Benchmark + Extended LM + 100x J-LR on RTX 5090'
summary: |-
  Three sub-experiments implemented and executed on RTX 5090 (32GB VRAM) for the Curie-Weiss Activation (CWA) with closed-form O(n) IFT backward pass.

  **Sub-Exp A (IFT Synthetic Benchmark):** Confirmed IFT branch triggers 50/50 runs with small-magnitude inputs (x_scale=0.1, J_raw=+4.0), yielding J·s̄=0.955 > 0.8 threshold. With standard-magnitude inputs, J·s̄≈0.59 (sech² saturates for large activations), which is a key implementation constraint. IFT peak memory 1.08× GELU baseline; unrolled path is comparable (0.97× memory saving vs unrolled at J_raw=4.0 with standard x, since IFT falls back to unrolled in that regime). Gradient check max_err=1.66e-1 (larger than target due to finite-diff error at near-critical regime; IFT backward analytically correct).

  **Sub-Exp B (Extended LM, 5000 steps, 2 seeds, cosine LR):** CWA mean val BPC=2.210 vs GELU mean=2.196 — within noise (no significant BPC advantage for CWA). J self-organizes very slowly under shared 3e-4 LR: J moves from 0.500→0.521 over 5000 steps. J·s̄ remains ~0.20 throughout (far below criticality), confirming weak SOC pressure from standard gradient signal.

  **Sub-Exp C (100× J-LR, 5000 steps, 2 seeds):** With J-dedicated AdamW at LR=3e-2, J moves dramatically: 0.500→0.833-0.848 (|ΔJ|=0.307-0.351, both seeds). J·s̄ rises to ~0.30. CWA 100×J-LR val BPC=2.212 (similar to shared-LR CWA). The large J movement confirms gradient signal exists and is learnable; standard LR is simply too small relative to weight gradients for J to move appreciably.

  **VERDICT: PARTIAL_CONFIRM** — IFT branch confirmed, J moves detectably with amplified LR. CWA does not improve BPC over GELU at 5000 steps, suggesting either insufficient training or that J·s̄ needs to reach criticality (>0.9) to unlock CWA's statistical-physics benefits. The 100×J-LR experiment shows J can reach 0.83-0.85, still below the J·s̄=0.9 criticality threshold in typical activation regimes.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 8 ---
id: art_a_2QuPkEZxKS
type: proof
in_dependencies:
- id: art_Lj-xi6yJR_yy
  label: mathematical-background
title: >-
  CWA Lean 4 Proofs: Revised Theorem 3 (code tolerance) + Theorem 4 (warm-start-T bias)
summary: |-
  CWA_Proof_v2.lean extends the iter-1 Lean 4 proof with two Lean-verified additions, both confirmed verified=true with zero sorries:

  **Theorem 3 Revision (cwa_ift_bias_code_tolerance):** Fixes a formal inconsistency — iter-1 used tolerance δ=1e-4*(1−J) but the actual CWA code uses δ=1e-4*(1−J·s̄) where s̄=mean(sech²(x+J·m*))∈[0,1]. Since s̄≤1 implies J·s̄≤J, the code tolerance is looser. The revised theorem accepts hypothesis `|F(m_approx)−m_approx| ≤ 1e-4*(1−J·s̄)` and proves `|m_approx−m*| ≤ 1e-4*(1−J·s̄)/(1−J)`. Auxiliary lemma `code_tol_bound_finite` confirms this bound is ≤1e-4/(1−J)=O(1e-4). Proof: contraction_residual_bound + div_le_div_of_nonneg_right calc chain (same pattern as iter-1).

  **Theorem 4 (warmstart_iteration_bound + cwa_warmstart_bias):** Formally proves the warm-start-T bias bound |F^[T](m̂)−m*| ≤ J^T·ε by induction on T. Base case: iterate_zero+simp+exact. Inductive step: Function.iterate_succ_apply' to unfold f^[n+1](m̂)=f(f^[n](m̂)), rewrite m*=f(m*), apply Lipschitz via hf_lip.dist_le_mul+NNReal.coe_mk simp, chain with mul_le_mul_of_nonneg_left+ring. Concrete corollary `cwa_warmstart3_concrete` shows T=3, J≤1/2 gives ≤12.5% relative bias via gcongr+norm_num.

  **cwa_main_v2** packages all four theorems (Banach fixed point, IFT gradient, revised bias bound, warm-start bound) as a single verified conjunction.

  All 14 lemmas/theorems compiler-verified. Output files: proof.lean (complete Lean 4 code, 287 lines), proof_out.json (schema-validated).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_proof_1
out_expected_files:
- proof.lean
- proof_out.json

--- Item 9 ---
id: art_PrGtqwcH3qpR
type: evaluation
in_dependencies:
- id: art_kKv207AAQYq2
  label: MLP-experiment-results
- id: art_DdhxnRglYGM6
  label: LM-experiment-results
- id: art_SVlh9mQatV8y
  label: ResNet-experiment-results
title: 'CWA Statistical Analysis: Paired Tests, K-Saturation, Gradient Bias & p_c Audit'
summary: |-
  ## CWA Statistical Evaluation — Summary

  ### What This Artifact Provides
  A comprehensive statistical analysis of three CWA experiments (LM GPT, MLP gradient stability, ResNet CIFAR-100) loading their full_method_out.json files and computing 8 metric categories.

  ### Key Results

  **1. Paired T-Tests (LM Experiment)**
  - Shakespeare BPC: CWA=3.3519 vs GELU=3.2253, diff=+0.1266 BPC (CWA WORSE), paired t-test p=0.0022, Cohen's d=13.76 (very large effect)
  - CWA vs SELU: diff=+0.0004 BPC (p=0.906, essentially tied)
  - CWA vs tanh+Swish: diff=+0.0147 BPC (p=0.020, CWA WORSE)
  - WikiText-2 PPL: CWA=767.4 vs GELU=738.7, diff=+28.7 PPL (Welch's t, p=0.099, trend CWA WORSE)

  **2. K-Saturation Diagnostic**
  - K_max=5 in code; 100% of logged K values equal K_max → K=5 is SATURATION, not convergence
  - Analytical residual at K=5: ~0.0187 >> tolerance 5.49e-5 → m* computed to only ~1.87% accuracy
  - Genuine convergence requires K≥13; iter-2 mandates K_max=50
  - PRIMARY CONFOUND: CWA's fixed point was not correctly computed

  **3. Gradient Bias Table**
  - Empirical rho (J·s̄) = 0.4513 across all layers/seeds
  - Warm-start-5 bias = rho^5 = 1.87% (negligible for training)
  - Warm-start-3 (code param) bias = rho^3 = 9.19%
  - IFT never triggered (J·s̄ stayed at ~0.45, far below 0.8 threshold)

  **4. p_c Consistency Audit**
  - Both MLP and LM experiments used p_c=0.50 instead of mandated p_c=0.83
  - Deviation = 0.33 — tanh+Swish baseline NOT at edge-of-chaos critical point
  - All tanh+Swish comparisons involve a handicapped competitor

  **5. MLP Gradient Ratio**
  - Only 2 of 27 planned configs completed (relu depth=6: ratio=0.4579, gelu depth=6: ratio=1.685)
  - CWA gradient ratios entirely unavailable — primary gradient stability hypothesis untestable

  **6. ResNet CIFAR-100**
  - CWA final=0.1401 vs GELU=0.1893 on standard_no_bn (gap=-4.92 pp, CWA WORSE)
  - Mean J·s̄=0.306 << 0.7 SOC threshold — self-organized criticality NOT observed
  - AUC diff=-7.52 pp; interim result (1 seed only)

  **7. SOC / J Stability**
  - J range: [0.498066, 0.501536] — drift of only 0.00347 from init=0.5
  - J·s̄ range: [0.437, 0.462] throughout training — no movement toward criticality
  - SOC definitively FAILED: J does not self-organize

  **8. Overall Verdict: DISCONFIRM (STRONG)**
  - CWA fails on all measured tasks
  - Primary confounds: K_max=5 (should be 50), p_c=0.50 (should be 0.83)
  - Iter-2 must fix K_max=50, p_c=0.83, and complete MLP depth ablation

  ### Output Files
  - eval_out.json / full_eval_out.json (33KB): Complete results with all 8 metric categories
  - mini_eval_out.json (25KB): First 3 items per dataset
  - preview_eval_out.json (18KB): Truncated strings for quick inspection
  - Schema: exp_eval_sol_out validated PASSED
  - Total LLM API cost: $0.00
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 10 ---
id: art_W-Ea4lflZ84v
type: evaluation
in_dependencies:
- id: art_v26XKv4_F1RM
  label: depth-sweep-results
- id: art_V46hELP73T_t
  label: ift-lm-results
- id: art_SVlh9mQatV8y
  label: resnet-results
- id: art_kKv207AAQYq2
  label: original-mlp-results
- id: art_DdhxnRglYGM6
  label: original-lm-results
title: 'CWA Re-Analysis: Six Reviewer Critiques Fixed via Corrected Metrics'
summary: |-
  ## CWA Comprehensive Re-Analysis: 6 Reviewer Critiques Fixed

  ### What This Evaluation Does
  Reprocesses five prior CWA experiment artifacts (iter1 MLP gradient-stability, iter1 ResNet-20 CIFAR-100, iter1 GPT LM, iter2 depth-sweep, iter2 IFT/LM benchmark) to fix six specific reviewer critiques via corrected metrics and analytical diagnostics. No new training required — all computations are derived from existing JSON outputs.

  ### Six Corrected Metrics / Findings

  **1. Corrected Gradient Stability (|ratio-1|):**
  Using the correct distance-to-ideal metric instead of raw ratio:
  - SELU is the gradient-stability leader at ALL depths (abs_dev=0.089 @ depth-6, 0.129 @ depth-10, 0.471 @ depth-20)
  - CWA ranks LAST (#6 of 6) at every depth: abs_dev=0.695 @ depth-6, 0.653 @ depth-10, 10.017 @ depth-20
  - CWA ratio=0.305–0.347 at shallow depths = gradient UNDERFLOW (<<1.0), not stability
  - Prior CONFIRM verdict for gradient-stability is REVISED to DISCONFIRM

  **2. GELU+LN Depth-20 Anomaly:**
  - GELU+LN shows ratio=9.661 AND accuracy=0.1394 (≈ random chance for 10-class)
  - Diagnosis: DUAL TRAINING FAILURE — both gradient instability and accuracy collapse
  - Indicates LayerNorm + deep stack interaction failure at 25-epoch budget
  - Caveat documented: gradient ratio metric not valid for normalized architectures

  **3. ResNet-20 CIFAR-100 Supplementary:**
  - CWA acc=0.1401 vs GELU acc=0.1893, delta=-0.0492 (preliminary negative)
  - Only 1 seed × 10 epochs — insufficient for significance
  - J·s̄=0.306 (sub-critical), SOC not observed — consistent with depth-sweep finding

  **4. p_c Reconciliation (INCONSISTENCY FOUND):**
  - iter1 MLP + iter1 LM: p_c=0.5 (sub-optimal for CompetingNL baseline)
  - iter2 depth-sweep: p_c=0.83 (theory-derived, correct)
  - INCONSISTENCY: CompetingNL baseline not standardized across experiments
  - iter1 comparisons under-optimized for CompetingNL; iter2 depth-sweep most valid

  **5. Warm-Start Bias (GOOD NEWS):**
  - Correct contraction rate is ρ=J·s̄≈0.20 (not J≈0.52)
  - Actual bias = (J·s̄)³ ≈ 0.86% (NOT J³ ≈ 13.6%)
  - Implementation is sound; naive bound overstated bias by 16×

  **6. IFT Gradient Check max_err=0.166 (EXPLAINED):**
  - J·s̄=0.9537 near criticality → amplification factor 1/(1-J·s̄)² ≈ 467×
  - max_err=0.166 is finite-difference amplification artifact, not IFT formula error
  - IFT backward analytically correct (0 NaN gradients); FD checks unreliable at J·s̄>0.9

  ### Positive Findings Retained
  - Fixed-J ablation confirms J·s̄ coupling mechanism (real physical mechanism)
  - J self-organizes with 100× J-LR (J=0.83–0.85), showing learnable gradient signal
  - IFT branch confirmed and memory-efficient (1.08× GELU)
  - Warm-start bias negligible in actual sub-critical training regime

  ### Output Files
  - `eval.py`: Complete evaluation script (pure computation, no LLM calls, ~$0)
  - `eval_out.json` / `full_eval_out.json`: 22 aggregate metrics + 5 datasets with 24 annotated examples
  - `mini_eval_out.json` / `preview_eval_out.json`: Compact variants for downstream use
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_3/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 11 ---
id: art_5zKSer_FGOKx
type: experiment
in_dependencies:
- id: art_Lj-xi6yJR_yy
  label: ift-formulas
title: >-
  CWA Mechanistic Sub-Experiments: Small-Weight Init and Constant-Shift Ablation on CIFAR-10
summary: |-
  Two mechanistic sub-experiments on 10-layer unnormalized MLPs (no BatchNorm/Dropout) trained on CIFAR-10 using the Curie-Weiss Activation (CWA): a novel activation function with a learned coupling J and closed-form IFT backward pass.

  Sub-Exp A (Small-Weight Init, σ=0.01 vs Kaiming): Tests whether reduced init magnitudes allow J·s̄ to reach near-critical values (>0.7). Three conditions × 3 seeds × 25 epochs. Result: max J·s̄ for cwa_small_init=0.412, cwa_kaiming_init=0.374 — neither reaches criticality. Verdict: init_does_not_help. Small init converges slowly (epoch-1 acc ~0.20 vs 0.36 for Kaiming) but closes the gap by epoch 25.

  Sub-Exp B (Shift Ablation — CWA-Full vs CWA-ShiftOnly vs Pure-Tanh): Isolates whether CWA's accuracy comes from inter-neuron coupling (full fixed-point) or just the mean-shift in pre-activations. Three conditions × 3 seeds × 25 epochs. Final test accuracies: cwa_full=0.4685, cwa_shift_only=0.4686, pure_tanh=0.4731. Verdict: bias_dominant — coupling adds nothing beyond the mean shift, and pure-tanh slightly outperforms both CWA variants. Paired t-tests show no significant difference between CWA-Full and CWA-ShiftOnly (the shift alone captures all the effect).

  Key finding: At Kaiming init the mean-field parameter J·s̄ sits at ~0.35–0.45, far from the critical point (J·s̄→1), and small-init does not push it higher. The CWA's inter-neuron coupling mechanism provides no accuracy benefit over a single detached mean-shift in this unnormalized MLP setting. These negative mechanistic results are informative for the hypothesis revision.

  Experiment ran on RTX 5090 (sm_120) with PyTorch 2.7.0+cu128, ~9 minutes total wall-clock time. Schema-validated exp_gen_sol_out JSON with 18 examples (one per sub-exp × condition × seed).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_3/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 12 ---
id: art_l4KqMWHu-dCe
type: proof
in_dependencies:
- id: art_Lj-xi6yJR_yy
  label: mathematical-background
title: 'CWA Proof v3: Corollary 4b (J≤0.55) Covering Experimental Regime'
summary: |-
  CWA Proof v3 extends the iter-2 verified Lean 4 proof by adding `cwa_warmstart_corollary_j55`, a new concrete warm-start-3 bias bound theorem covering J≤55/100 (bias≤167/1000·ε≈16.7%·ε). This fills a reviewer-visible gap: the existing iter-2 theorem `cwa_warmstart3_concrete` only covers J≤1/2, but the GPU experiments report J∈[0.515,0.521] — strictly above 0.5. The new corollary formally covers the entire observed experimental range with margin.

  The proof reuses the exact same tactic pattern as the existing J≤1/2 corollary: `cwa_warmstart_bias` provides J^T·ε bound, `gcongr` derives J^3≤(55/100)^3 from hJ_55, `norm_num` closes (55/100)^3≤167/1000 (since 166375/1000000≤167000/1000000), and a three-step calc chain applies `mul_le_mul_of_nonneg_right` twice. No existing theorems were modified.

  All 16 lemmas/theorems verified by Lean 4.14.0 with no sorries and no errors: hasDerivAt_sinh, hasDerivAt_cosh, hasDerivAt_tanh, differentiable_tanh, sech_sq_nonneg, sech_sq_le_one, nnnorm_deriv_tanh_le, tanh_lipschitzWith_one, lin_lipschitz, F_lipschitz, F_contracting, cwa_banach, one_sub_J_sbar_pos, ift_gradient_correct, ift_equation_unique_solution, contraction_residual_bound, cwa_ift_bias_code_tolerance, code_tol_bound_finite, warmstart_iteration_bound, cwa_warmstart_bias, cwa_warmstart3_concrete, cwa_warmstart_corollary_j55 (NEW), cwa_main_v2. Output: proof.lean (complete verified file) and proof_out.json (schema-validated).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_3/gen_art/gen_art_proof_1
out_expected_files:
- proof.lean
- proof_out.json
</all_artifacts>

<new_artifacts_this_iteration>
These 3 artifacts were created THIS iteration.

id: art_W-Ea4lflZ84v
type: evaluation
in_dependencies:
- id: art_v26XKv4_F1RM
  label: depth-sweep-results
- id: art_V46hELP73T_t
  label: ift-lm-results
- id: art_SVlh9mQatV8y
  label: resnet-results
- id: art_kKv207AAQYq2
  label: original-mlp-results
- id: art_DdhxnRglYGM6
  label: original-lm-results
title: 'CWA Re-Analysis: Six Reviewer Critiques Fixed via Corrected Metrics'
summary: |-
  ## CWA Comprehensive Re-Analysis: 6 Reviewer Critiques Fixed

  ### What This Evaluation Does
  Reprocesses five prior CWA experiment artifacts (iter1 MLP gradient-stability, iter1 ResNet-20 CIFAR-100, iter1 GPT LM, iter2 depth-sweep, iter2 IFT/LM benchmark) to fix six specific reviewer critiques via corrected metrics and analytical diagnostics. No new training required — all computations are derived from existing JSON outputs.

  ### Six Corrected Metrics / Findings

  **1. Corrected Gradient Stability (|ratio-1|):**
  Using the correct distance-to-ideal metric instead of raw ratio:
  - SELU is the gradient-stability leader at ALL depths (abs_dev=0.089 @ depth-6, 0.129 @ depth-10, 0.471 @ depth-20)
  - CWA ranks LAST (#6 of 6) at every depth: abs_dev=0.695 @ depth-6, 0.653 @ depth-10, 10.017 @ depth-20
  - CWA ratio=0.305–0.347 at shallow depths = gradient UNDERFLOW (<<1.0), not stability
  - Prior CONFIRM verdict for gradient-stability is REVISED to DISCONFIRM

  **2. GELU+LN Depth-20 Anomaly:**
  - GELU+LN shows ratio=9.661 AND accuracy=0.1394 (≈ random chance for 10-class)
  - Diagnosis: DUAL TRAINING FAILURE — both gradient instability and accuracy collapse
  - Indicates LayerNorm + deep stack interaction failure at 25-epoch budget
  - Caveat documented: gradient ratio metric not valid for normalized architectures

  **3. ResNet-20 CIFAR-100 Supplementary:**
  - CWA acc=0.1401 vs GELU acc=0.1893, delta=-0.0492 (preliminary negative)
  - Only 1 seed × 10 epochs — insufficient for significance
  - J·s̄=0.306 (sub-critical), SOC not observed — consistent with depth-sweep finding

  **4. p_c Reconciliation (INCONSISTENCY FOUND):**
  - iter1 MLP + iter1 LM: p_c=0.5 (sub-optimal for CompetingNL baseline)
  - iter2 depth-sweep: p_c=0.83 (theory-derived, correct)
  - INCONSISTENCY: CompetingNL baseline not standardized across experiments
  - iter1 comparisons under-optimized for CompetingNL; iter2 depth-sweep most valid

  **5. Warm-Start Bias (GOOD NEWS):**
  - Correct contraction rate is ρ=J·s̄≈0.20 (not J≈0.52)
  - Actual bias = (J·s̄)³ ≈ 0.86% (NOT J³ ≈ 13.6%)
  - Implementation is sound; naive bound overstated bias by 16×

  **6. IFT Gradient Check max_err=0.166 (EXPLAINED):**
  - J·s̄=0.9537 near criticality → amplification factor 1/(1-J·s̄)² ≈ 467×
  - max_err=0.166 is finite-difference amplification artifact, not IFT formula error
  - IFT backward analytically correct (0 NaN gradients); FD checks unreliable at J·s̄>0.9

  ### Positive Findings Retained
  - Fixed-J ablation confirms J·s̄ coupling mechanism (real physical mechanism)
  - J self-organizes with 100× J-LR (J=0.83–0.85), showing learnable gradient signal
  - IFT branch confirmed and memory-efficient (1.08× GELU)
  - Warm-start bias negligible in actual sub-critical training regime

  ### Output Files
  - `eval.py`: Complete evaluation script (pure computation, no LLM calls, ~$0)
  - `eval_out.json` / `full_eval_out.json`: 22 aggregate metrics + 5 datasets with 24 annotated examples
  - `mini_eval_out.json` / `preview_eval_out.json`: Compact variants for downstream use
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_3/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

id: art_5zKSer_FGOKx
type: experiment
in_dependencies:
- id: art_Lj-xi6yJR_yy
  label: ift-formulas
title: >-
  CWA Mechanistic Sub-Experiments: Small-Weight Init and Constant-Shift Ablation on CIFAR-10
summary: |-
  Two mechanistic sub-experiments on 10-layer unnormalized MLPs (no BatchNorm/Dropout) trained on CIFAR-10 using the Curie-Weiss Activation (CWA): a novel activation function with a learned coupling J and closed-form IFT backward pass.

  Sub-Exp A (Small-Weight Init, σ=0.01 vs Kaiming): Tests whether reduced init magnitudes allow J·s̄ to reach near-critical values (>0.7). Three conditions × 3 seeds × 25 epochs. Result: max J·s̄ for cwa_small_init=0.412, cwa_kaiming_init=0.374 — neither reaches criticality. Verdict: init_does_not_help. Small init converges slowly (epoch-1 acc ~0.20 vs 0.36 for Kaiming) but closes the gap by epoch 25.

  Sub-Exp B (Shift Ablation — CWA-Full vs CWA-ShiftOnly vs Pure-Tanh): Isolates whether CWA's accuracy comes from inter-neuron coupling (full fixed-point) or just the mean-shift in pre-activations. Three conditions × 3 seeds × 25 epochs. Final test accuracies: cwa_full=0.4685, cwa_shift_only=0.4686, pure_tanh=0.4731. Verdict: bias_dominant — coupling adds nothing beyond the mean shift, and pure-tanh slightly outperforms both CWA variants. Paired t-tests show no significant difference between CWA-Full and CWA-ShiftOnly (the shift alone captures all the effect).

  Key finding: At Kaiming init the mean-field parameter J·s̄ sits at ~0.35–0.45, far from the critical point (J·s̄→1), and small-init does not push it higher. The CWA's inter-neuron coupling mechanism provides no accuracy benefit over a single detached mean-shift in this unnormalized MLP setting. These negative mechanistic results are informative for the hypothesis revision.

  Experiment ran on RTX 5090 (sm_120) with PyTorch 2.7.0+cu128, ~9 minutes total wall-clock time. Schema-validated exp_gen_sol_out JSON with 18 examples (one per sub-exp × condition × seed).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_3/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

id: art_l4KqMWHu-dCe
type: proof
in_dependencies:
- id: art_Lj-xi6yJR_yy
  label: mathematical-background
title: 'CWA Proof v3: Corollary 4b (J≤0.55) Covering Experimental Regime'
summary: |-
  CWA Proof v3 extends the iter-2 verified Lean 4 proof by adding `cwa_warmstart_corollary_j55`, a new concrete warm-start-3 bias bound theorem covering J≤55/100 (bias≤167/1000·ε≈16.7%·ε). This fills a reviewer-visible gap: the existing iter-2 theorem `cwa_warmstart3_concrete` only covers J≤1/2, but the GPU experiments report J∈[0.515,0.521] — strictly above 0.5. The new corollary formally covers the entire observed experimental range with margin.

  The proof reuses the exact same tactic pattern as the existing J≤1/2 corollary: `cwa_warmstart_bias` provides J^T·ε bound, `gcongr` derives J^3≤(55/100)^3 from hJ_55, `norm_num` closes (55/100)^3≤167/1000 (since 166375/1000000≤167000/1000000), and a three-step calc chain applies `mul_le_mul_of_nonneg_right` twice. No existing theorems were modified.

  All 16 lemmas/theorems verified by Lean 4.14.0 with no sorries and no errors: hasDerivAt_sinh, hasDerivAt_cosh, hasDerivAt_tanh, differentiable_tanh, sech_sq_nonneg, sech_sq_le_one, nnnorm_deriv_tanh_le, tanh_lipschitzWith_one, lin_lipschitz, F_lipschitz, F_contracting, cwa_banach, one_sub_J_sbar_pos, ift_gradient_correct, ift_equation_unique_solution, contraction_residual_bound, cwa_ift_bias_code_tolerance, code_tol_bound_finite, warmstart_iteration_bound, cwa_warmstart_bias, cwa_warmstart3_concrete, cwa_warmstart_corollary_j55 (NEW), cwa_main_v2. Output: proof.lean (complete verified file) and proof_out.json (schema-validated).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_3/gen_art/gen_art_proof_1
out_expected_files:
- proof.lean
- proof_out.json
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# Introduction

Activation functions in neural networks have traditionally been designed pointwise: each neuron's output y_i depends only on its own pre-activation x_i, independent of other neurons in the same layer. This architectural independence is computationally convenient but requires external normalization layers — BatchNorm [8] or LayerNorm [9] — or precise initialization schemes [3, 4] to maintain stable gradient flow across depth. Three practically important settings make such requirements burdensome: (a) on-device inference, where normalization's running statistics incur memory and quantization distortion; (b) physics-informed neural networks, where normalization disrupts conservation laws encoded in the activations [5]; and (c) fast-inference transformer variants that eliminate LayerNorm to reduce memory bandwidth.

The *edge of chaos* in deep networks — the boundary where layer Jacobian singular values are near unity — correlates empirically with fast training and good generalization [3, 4]. Existing approaches achieve criticality only at initialization via weight variance tuning [3, 4] or static random activation mixtures [5], with no mechanism to track criticality adaptively during training. The Curie-Weiss model of ferromagnetism [15] provides a natural template for an adaptive mechanism: each spin aligns with the mean field of its neighbors, m = tanh(β(h + J·m)), with a critical point at βJ = 1 where magnetic susceptibility diverges. Transferring this structure to neural activations gives y_i = tanh(x_i + J·mean(y)), coupling all neurons in a layer through a learnable scalar J.

This paper reports a complete experimental investigation of the Curie-Weiss Activation (CWA), including mechanistic sub-experiments added specifically to address reviewer concerns about the interpretation of gradient-stability results and the isolation of the coupling mechanism from the mean-shift effect. The investigation yields precise positive and negative findings.

[FIGURE:fig1]

The contributions of this paper, grounded in specific artifacts, are:

- **Formally verified mathematical foundation** (Section 3): Five Lean 4 theorems without sorry — fixed-point existence, IFT gradient correctness, adaptive bias bound, warm-start-T bias bound, and a new corollary covering J ≤ 0.55 (bias ≤ 16.7%·ε), which closes the gap between the J ≤ 0.5 corollary and the experimentally observed J ∈ [0.515, 0.521] [ARTIFACT:art_l4KqMWHu-dCe].
- **Empirically confirmed IFT branch** (Section 4.1): The near-critical IFT branch triggers at J·s̄ = 0.955 with 1.05× GELU memory overhead; the numerical gradient check error of 0.166 is a finite-difference artifact caused by 467× amplification near the 1/(1−J·s̄) singularity, not a backward implementation error [ARTIFACT:art_V46hELP73T_t].
- **Gradient underflow, not balance** (Section 4.2): Using the corrected |ratio − 1| distance-to-ideal metric, CWA ranks last at all depths. CWA's ratio of 0.305 at depth 6 indicates gradient *underflow* (2.4× worse than GELU, 7.8× worse than SELU), not stability. At depth 20, CWA and GELU+LN both exhibit catastrophic dual training failure [ARTIFACT:art_W-Ea4lflZ84v].
- **Bias-dominant mechanism** (Section 4.3): A shift ablation experiment confirms that CWA's accuracy effect is entirely attributable to the mean-shift term J·m*, with the full fixed-point coupling adding zero additional benefit (p = 0.984) [ARTIFACT:art_5zKSer_FGOKx].
- **SOC failure with identified root cause** (Section 5): J·s̄ remains at ~0.20–0.40 under all tested training configurations because sech²(x+J·m*) saturates at typical activation magnitudes, capping J·s̄ well below the critical threshold J·s̄ = 1 even when J → 0.85.

# Background and Related Work

**Edge-of-chaos criticality.** Poole et al. [3] showed that infinite-depth networks initialized at the order-chaos boundary exhibit depth-independent gradient propagation, characterized by a unit Jacobian spectral radius. Yang and Schoenholz [4] extended this analysis to residual networks. Both methods fix the criticality condition at initialization through weight variance tuning; the property drifts during training. CWA introduces a per-layer learnable scalar J intended to maintain near-critical coupling adaptively, but the present experiments establish that the path to J·s̄ = 1 is blocked by sech² saturation at realistic activation scales (Section 5).

**Self-normalizing networks.** SELU [2] achieves self-normalization without external normalization by designing the activation's distributional fixed point to have mean 0 and variance 1. SELU is strictly pointwise. CWA couples all neurons within a layer via the mean-field term J·mean(y), making it categorically distinct. Empirically, SELU achieves the best gradient stability at all tested depths (|ratio − 1| = 0.089, 0.129, 0.471 at depths 6, 10, 20) and the best accuracy at depth 20 (0.535 vs. CWA's 0.141), suggesting that distributional fixed-point design is more effective for unnormalized deep networks than mean-field output coupling.

**Static activation mixtures.** Lesser and Chowdhury [5] achieve edge-of-chaos criticality by drawing each neuron's activation from a tanh/Swish mixture at analytically derived critical mixing fraction p_c = 32/35 ≈ 0.914 (K₀→0 limit), with empirical calibration yielding p_c ≈ 0.83 at K₀ = 1. This approach requires no learnable parameter and no inter-neuron coupling. CWA provides a learnable J but fails to achieve near-critical J·s̄ under standard training; static critical mixtures remain a competitive baseline.

**Deep Equilibrium Models.** Bai et al. [1] showed that any infinite-depth weight-tied network can be computed via fixed-point root-finding, with IFT providing O(1) activation memory. The CWA IFT backward (Section 3.2) is directly inspired by DEQ but reduces to a closed-form scalar formula — because CWA's fixed point m* ∈ ℝ rather than ℝⁿ — eliminating the need for iterative backward solvers. TorchDEQ [12] provides a practical library for the broader DEQ ecosystem [ARTIFACT:art_Lj-xi6yJR_yy].

**Mean-field theory of activations.** Milletarì et al. [7] provided post-hoc physical interpretations of standard pointwise activations as solutions to energy-based models. CWA instead proposes a new activation *defined by* the Curie-Weiss self-consistency equation with a learnable J, introducing within-layer coupling absent from all prior derived activations.

**Boltzmann Attention.** Kim and Park [6] introduced learnable Ising couplings J_{jk} between sequence positions in the attention operator. Boltzmann Attention and CWA are complementary: the former operates in the sequence dimension of the attention operator; the latter operates in the hidden dimension of the activation function.

**Mining activation functions.** Vitvitskyi et al. [13] and Ghavasieh [14] search for or analyze novel activation functions via evolutionary and statistical-mechanics methods, respectively. Neither proposes within-sample self-consistent mean-field coupling with a learnable scalar.

# Method: Curie-Weiss Activation

## Definition and Forward Pass

The Curie-Weiss Activation (CWA) for a layer with pre-activations x ∈ ℝⁿ is defined as the unique fixed point of the scalar mean-field self-consistency equation:

  m* = mean_neurons(tanh(x + J·m*))

where J = sigmoid(J_raw) ∈ (0, 1) is a per-layer learnable scalar and mean_neurons(y) = (1/n)Σᵢ yᵢ is the within-sample neuron mean (not the batch mean). The layer output is y_i = tanh(xᵢ + J·m*) for each neuron i. The effective coupling J·s̄ = J·mean_neurons(sech²(x+J·m*)) simultaneously quantifies: (i) the per-step convergence rate ρ of the fixed-point iteration; (ii) the spectral norm of the layer's input-output Jacobian; and (iii) proximity to the critical point J·s̄ = 1.

The fixed-point iteration m_{t+1} = mean_neurons(tanh(x + J·m_t)) is initialized at m₀ = 0 and terminated when |m_{t+1} − m_t| < δ(J·s̄) = 1e-4·(1 − J·s̄), with K_max = 50. In experiments, J·s̄ ≈ 0.20–0.40, giving typical convergence in K_mean ≈ 7.4 iterations with 100% of forward passes converging before K_max. The sigmoid parameterization J = sigmoid(J_raw) hard-constrains J below the ferromagnetic phase transition at J = 1, guaranteeing global convergence for all inputs.

## Hybrid IFT/Warm-Start Backpropagation

CWA uses a hybrid backward strategy determined by the forward-pass effective coupling J·s̄. When J·s̄ < 0.8, a warm-start approximation is used: K forward iterations run without gradient tracking to find m*, followed by T = 3 tracked iterations from the detached m*, with gradient bias bounded by J^T·ε (Theorem 4, Section 3.3). When J·s̄ ≥ 0.8, a custom `torch.autograd.Function` applies the closed-form IFT gradient:

  ∂L/∂xᵢ = sᵢ·[gᵢ + J·(Σₖ gₖ·sₖ) / (n·(1 − J·s̄))]
  ∂L/∂J = Σᵢ gᵢ·sᵢ·m* / (1 − J·s̄)

where sᵢ = sech²(xᵢ + J·m*) and gᵢ = ∂L/∂yᵢ. The IFT path requires only O(n) activation memory — storing the converged scalar m* — analogously to DEQ's memory reduction [1]. The adaptive tolerance δ(J·s̄) = 1e-4·(1 − J·s̄) ensures gradient bias from fixed-point approximation is bounded at O(1e-4/(1−J)) uniformly across all coupling strengths (Theorem 3 below).

## Formal Verification in Lean 4

Five properties of CWA are formally verified in Lean 4 + Mathlib v4.14.0 without sorry [ARTIFACT:art_l4KqMWHu-dCe]. The standard Mathlib `DerivHyp` module is broken in v4.14.0; all HasDerivAt results for sinh, cosh, tanh are derived from first principles via `HasDerivAt.inv` and `HasDerivAt.mul`.

**Theorem 1 (Banach Convergence).** For any x ∈ ℝ and J ∈ (0,1), there exists a unique m* satisfying tanh(x + J·m*) = m*. *Proof:* tanh is 1-Lipschitz; composition with J-Lipschitz affine map gives F J-Lipschitz; `ContractingWith.fixedPoint_isFixedPt` + `fixedPoint_unique` give existence and uniqueness.

**Theorem 2 (IFT Gradient).** With s̄ = 1 − tanh²(x + J·m*) and grad = s̄/(1 − J·s̄), the identity s̄·(1 + J·grad) = grad holds. *Proof:* `field_simp` after establishing 1 − J·s̄ > 0.

**Theorem 3 (Revised Bias Bound).** If |F(m_approx) − m_approx| ≤ 1e-4·(1−J·s̄), then |m_approx − m*| ≤ 1e-4·(1−J·s̄)/(1−J) ≤ 1e-4/(1−J). For J ≈ 0.52, this bound is ≈ 2.08e-4.

**Theorem 4 (Warm-Start-T Bias).** For T tracked iterations from detached m̂ with |m̂ − m*| ≤ ε, |F^[T](m̂) − m*| ≤ J^T·ε. Corollary 4a (J ≤ 0.5): T=3 gives ≤ (1/8)·ε ≈ 12.5%. Corollary 4b (J ≤ 0.55): T=3 gives ≤ (167/1000)·ε ≈ 16.7%.

Corollary 4b closes a gap observed by reviewers: the experimentally observed J ∈ [0.515, 0.521] exceeds the J ≤ 0.5 condition of Corollary 4a. With J = 0.521, J³ = 0.141, so the warm-start bias is ≤ 14.1%·ε, which is covered by Corollary 4b with margin. Critically, the *actual* contraction rate in training is ρ = J·s̄ ≈ 0.205 (not J ≈ 0.52), giving a realized bias of ρ³ ≈ 0.86%·ε — negligible in practice [ARTIFACT:art_W-Ea4lflZ84v].

# Experiments

All experiments use PyTorch on NVIDIA GPUs. CWA uses K_max = 50, adaptive tolerance δ = 1e-4·(1−J·s̄), and warm-start T=3 backward. Total experiment cost is $0 (no LLM API calls). Statistical tests use paired and Welch t-tests as specified.

## Experiment 1: IFT Branch Validation

A synthetic benchmark initializes J_raw = +4.0 (J ≈ 0.982) to force the near-critical regime [ARTIFACT:art_V46hELP73T_t].

**Small-magnitude inputs** (x_scale = 0.1): J·s̄ = 0.955 > 0.8 threshold, triggering the IFT branch in all 50/50 runs. Peak GPU memory is 1.05× GELU (1.047 MB IFT vs. 0.188 MB GELU baseline in this micro-benchmark), meeting the 2× criterion. **Numerical gradient check:** max_err = 0.166. This elevated error is not a backward implementation defect — the IFT formula is algebraically exact per Theorem 2, with zero NaN gradients confirmed. Rather, the 1/(1−J·s̄) denominator amplifies finite-difference perturbations by a second-order factor of 1/(1−J·s̄)² ≈ 467 at J·s̄ = 0.955; the finite-difference approximation is unreliable in this near-singular regime.

**Standard-magnitude inputs**: J·s̄ drops to 0.591 because sech²(x+J·m*) saturates toward zero at large |x|, reducing the effective coupling even at J ≈ 0.982. This saturation effect is fundamental: the IFT branch requires not only large J but also small enough pre-activations that sech² remains non-negligible.

[FIGURE:fig4]

## Experiment 2: Gradient Stability in Unnormalized Deep MLPs

MLPs at depths {6, 10, 20} with 256 hidden units are trained on CIFAR-10 for 25 epochs with 3 seeds and no normalization, comparing CWA against ReLU, GELU, SELU, Competing Nonlinearities (p_c = 0.83, the empirically calibrated critical mixing fraction at K₀ = 1 per Lesser and Chowdhury [5] Eq. 17), and GELU+LayerNorm [ARTIFACT:art_v26XKv4_F1RM]. We use the corrected gradient-stability metric |ratio − 1| = |log‖∇W₁‖/log‖∇W_L‖ − 1|, which measures distance from the ideal value of 1.0; lower values indicate better gradient propagation.

[FIGURE:fig2]

**Corrected gradient stability ranking** [ARTIFACT:art_W-Ea4lflZ84v]. At depth 6, SELU achieves the best gradient stability (|ratio − 1| = 0.089±0.048), followed by ReLU (0.220±0.058), GELU (0.288±0.141), CompNL (0.320±0.083), GELU+LN (0.630±0.081), and CWA (0.695±0.032). CWA's raw ratio of 0.305 indicates gradient *underflow* — the gradient signal diminishes moving toward the input — not balance. CWA deviates 7.8× more from the ideal than SELU and 2.4× more than GELU. At depth 10, CWA again ranks last (|ratio − 1| = 0.653±0.120 vs. SELU's 0.129±0.100). These results invalidate the prior claim that CWA achieves gradient balance: a ratio significantly below 1.0 is as problematic as one significantly above 1.0.

**Depth-20 failure.** At depth 20, CWA catastrophically over-shoots to ratio = 11.02 (|ratio − 1| = 10.02±2.66), far worse than all baselines. SELU remains closest to ideal (|ratio − 1| = 0.471±1.003). An important anomalous result concerns GELU+LayerNorm at depth 20: despite LayerNorm's explicit per-layer re-centering and re-scaling, GELU+LN achieves ratio = 9.661 (|ratio − 1| = 8.661±1.272) *and* accuracy = 0.139 — worse than plain GELU on both metrics. This is a dual training failure: both gradient instability and accuracy collapse. The diagnosis is that LayerNorm's internal gradient interactions with 20 stacked layers destabilize training under this 25-epoch budget. This result also implies that the |ratio − 1| gradient metric is unreliable for normalized architectures, where LayerNorm's internal re-scaling conflates with the measured gradient magnitudes; comparisons should be restricted to same-class (normalized vs. normalized) architectures.

**Accuracy results.** CWA is significantly below GELU at depths 6 and 10 (0.483±0.002 vs. 0.531±0.002 at depth 6, paired t p = 0.003; 0.472±0.003 vs. 0.511±0.001 at depth 10, paired t p = 0.003). SELU achieves the best accuracy at all depths (0.547, 0.542, 0.535), confirming that distributional fixed-point design outperforms mean-field coupling for unnormalized deep networks. Preliminary ResNet-20 CIFAR-100 results (1 seed, 10 epochs, no BatchNorm) are consistent: CWA 14.0% vs. GELU 18.9% (-4.9 pp) [ARTIFACT:art_SVlh9mQatV8y].

**CWA diagnostics.** J converges to values in [0.515, 0.521] — less than 0.01 from initialization — with J·s̄ following a declining trajectory (0.346→0.286 over 25 epochs at depth 6; 0.400→0.353 at depth 10). K_mean ≈ 7.4 per step, fraction_converged = 1.0, confirming correct fixed-point computation (cf. iter-1's K_max=5 saturation).

## Experiment 3: Fixed-J Ablation and Shift Ablation

Two ablations on 10-layer unnormalized MLPs on CIFAR-10, 3 seeds [ARTIFACT:art_v26XKv4_F1RM] [ARTIFACT:art_5zKSer_FGOKx].

[FIGURE:fig3]

**Fixed-J ablation.** With J frozen at {0.1, 0.3, 0.5, 0.7, 0.9}, gradient ratios all fall below 0.41 (J=0.1: ratio=0.245; J=0.9: ratio=0.410), confirming that the mean-field coupling mechanism itself — at any strength — compresses the gradient ratio below 1.0. However, all fixed-J variants achieve accuracy in 0.47–0.48, significantly below GELU (0.511±0.001). Accuracy is essentially J-independent (J=0.1: 0.471; J=0.5: 0.477; J=0.9: 0.472), ruling out coupling strength as a remedy. The learned-J variant performs identically (0.472±0.003). Importantly, *all* fixed-J gradient ratios are below 1.0, indicating that the coupling produces underflow at depth 10 regardless of J magnitude.

**Shift ablation.** A new mechanistic experiment directly tests whether CWA's accuracy effect arises from the self-consistent coupling or merely from injecting the mean-shift m* into the pre-activations. Three conditions run on 3 seeds: CWA-Full (standard fixed-point iteration), CWA-ShiftOnly (pre-activations shifted by a detached, non-self-consistent mean equal to mean_neurons(tanh(x))), and Pure-Tanh (standard pointwise tanh, no shift). Final test accuracies: CWA-Full = 0.4685±0.004, CWA-ShiftOnly = 0.4686±0.005, Pure-Tanh = 0.4731±0.001. The paired t-test between CWA-Full and CWA-ShiftOnly yields t = −0.023, p = 0.984 — statistically indistinguishable. The full self-consistent fixed point adds zero benefit over the simple mean-shift approximation. Pure-Tanh slightly outperforms both CWA variants (p = 0.126, CWA-Full vs. Pure-Tanh; the shift itself marginally hurts accuracy). This confirms the *bias-dominant* mechanistic interpretation: the coupling's accuracy effect is entirely attributable to the correlated mean-shift J·m* added to all pre-activations, not to the self-consistent coupling per se. An alternative explanation — that mean-field coupling reduces per-neuron activation diversity — is equally consistent with the data; the shift ablation cannot distinguish between bias injection and diversity reduction, since both mechanisms are activated by the mean-shift term.

**Small-weight initialization.** A separate sub-experiment tests whether small weight initialization (σ = 0.01 vs. Kaiming) allows J·s̄ to approach criticality. Maximum J·s̄ reaches 0.412 with small-init vs. 0.374 with Kaiming — neither approaches the J·s̄ = 0.7 near-critical threshold. Accuracy with small-init (0.423±0.011) is below Kaiming CWA (0.469±0.004) due to slow initial convergence.

## Experiment 4: Extended Language Modeling and J-Learning Dynamics

A 6-layer, 256-hidden, 8-head character-level GPT is trained on Tiny Shakespeare for 5000 steps with cosine LR (2 seeds) [ARTIFACT:art_V46hELP73T_t].

**Shared LR.** CWA val BPC = 2.210±0.014 vs. GELU = 2.196±0.037 — within noise. J moves from 0.500 to 0.521 over 5000 steps (rate ≈ 8.7×10⁻⁷ per step); J·s̄ remains at ≈ 0.205 throughout.

**100× J dedicated LR.** With J-specific AdamW at LR = 3×10⁻², J moves to 0.833–0.848 (|ΔJ| = 0.307–0.351). However, J·s̄ rises to only 0.29–0.31, because sech²(x+J·m*) saturates at typical activation magnitudes (~2.0), where sech²(2) ≈ 0.07. CWA 100×J-LR val BPC = 2.212±0.011 — no improvement over shared-LR CWA or GELU.

# Discussion

## Why CWA Produces Gradient Underflow, Not Balance

The corrected gradient stability analysis (using |ratio − 1|) reveals that CWA's mean-field coupling compresses gradient ratios *below* 1.0 at shallow depths, not toward 1.0. Three mechanisms contribute. First, the mean-field term J·m* adds a correlated bias to all pre-activations, effectively reducing the variance of the layer's input distribution and causing tanh to operate closer to its saturating regime for some inputs. Second, the coupling strength J·s̄ ≈ 0.20–0.35 is well below the critical point J·s̄ = 1; the expected gain amplification 1/(1−J·s̄) ≈ 1.2–1.5 is modest and does not compensate for the variance reduction. Third, at depth 20, the accumulated mean-shift J·m* across layers grows unbounded without normalization, driving tanh to saturation and producing the observed ratio = 11.02 collapse.

The GELU+LN depth-20 dual failure (ratio = 9.661, accuracy = 0.139) provides an important caveat: external normalization does not automatically stabilize training at depth 20 under a 25-epoch budget. This anomaly suggests that the gradient ratio metric conflates LayerNorm's internal re-scaling with true layer-wise gradient magnitudes, making cross-class comparisons (normalized vs. unnormalized) unreliable.

## Why the Coupling Adds Nothing Beyond the Mean Shift

The shift ablation (Section 4.3) establishes that CWA-Full and CWA-ShiftOnly are accuracy-equivalent (p = 0.984). This means the computational cost of the fixed-point iteration — K ≈ 7.4 iterations per layer per forward pass — produces no benefit over a single detached mean computation. The self-consistency constraint (m* = mean(tanh(x + J·m*))) is computationally non-trivial but accuracy-irrelevant at the sub-critical J·s̄ values observed in training. Near J·s̄ = 1, the self-consistent solution diverges qualitatively from the single-step estimate, and benefits might emerge; but the sech² saturation barrier prevents reaching this regime.

## Why Self-Organized Criticality Fails

Self-organized criticality would require gradient descent to push J·s̄ toward 1. Two independent barriers prevent this:

**Weak gradient signal.** Under shared LR, J moves at ≈ 8.7×10⁻⁷ per step — requiring ~350,000–590,000 steps to approach J = 0.9, far beyond practical training budgets.

**sech² saturation.** Even with 100× J dedicated LR driving J → 0.85, the product J·s̄ = J·mean(sech²(x+J·m*)) reaches only ~0.30 because sech²(x) ~ 0.07 at typical activation magnitudes |x| ~ 2.0. Reaching J·s̄ = 0.9 would require mean(sech²) ≥ 0.9, corresponding to |x| < 0.48 — impractically small for trained networks processing natural data.

Small-weight initialization (σ = 0.01) pushes the maximum J·s̄ from 0.374 to 0.412 but still falls far short of the near-critical threshold. These barriers explain why the IFT branch — designed for J·s̄ ≥ 0.8 — was never triggered during normal training experiments.

## Formal Proofs Remain Valid

All five Lean 4 theorems are mathematically valid and relevant to any implementation of CWA. The new Corollary 4b (J ≤ 0.55, bias ≤ 16.7%·ε) now formally covers the experimentally observed range J ∈ [0.515, 0.521], eliminating the gap in the prior corollary. The *realized* warm-start bias in training is ≈ 0.86%·ε (using the correct contraction rate ρ = J·s̄ ≈ 0.205, not J ≈ 0.52), confirming that the implementation is accurate throughout.

## Limitations

The depth-20 collapse dynamics are not fully characterized: it remains unclear whether the collapse is driven by compound mean shifts, gradient amplification through the 1/(1−J·s̄) IFT denominator, or both. The ResNet-20 CIFAR-100 result is preliminary (1 seed, 10 epochs) and cannot support statistical claims. The shift ablation uses the same architecture (10-layer MLP, 256 hidden) for all conditions; varying width might reveal whether the shift-only approximation remains accurate at larger n where mean-field theory is more precise. The sech² saturation argument assumes typical trained activation distributions; architectures with explicit auxiliary losses constraining pre-activation magnitudes would test whether the critical regime is attainable.

## Future Directions

- **Constrained pre-activation magnitudes.** An auxiliary loss penalizing mean(|x+J·m*|) > τ would directly target the sech² saturation barrier.
- **Coupling the IFT regime deliberately.** Jointly training with a near-critical initialization (J_raw = +3, x_scale = 0.1) and a warm-up schedule keeping pre-activations small might allow J·s̄ to reach the critical regime before activation magnitudes grow.
- **Vector coupling.** Replacing scalar J with a per-neuron vector J ∈ ℝⁿ would allow heterogeneous coupling, with some neurons operating near criticality independently of others.
- **CWA + Boltzmann Attention.** Combining CWA's intra-layer (hidden-dim) coupling with Boltzmann Attention's [6] inter-position (sequence-dim) coupling is a natural extension.

# Conclusion

We introduced the Curie-Weiss Activation (CWA), defined by the mean-field self-consistency equation y_i = tanh(x_i + J·mean(y)) with learnable coupling J per layer. Five Lean 4 theorems without sorry establish the mathematical foundation, including a new Corollary 4b (J ≤ 0.55, bias ≤ 16.7%·ε) that covers the experimentally observed parameter range.

Empirical investigation yields a precise account of CWA's behavior. The mean-field coupling is physically present: K_mean ≈ 7.4 fixed-point iterations per forward pass converge reliably, the IFT branch activates at J·s̄ = 0.955 with 1.05× GELU memory overhead, and the effective coupling J·s̄ measurably affects gradient flow dynamics. However, using the correct |ratio − 1| metric, CWA produces gradient *underflow* (ratio = 0.305–0.347 at depths 6–10) rather than balance, ranking last among six activations at all tested depths. At depth 20, CWA collapses catastrophically. A shift ablation confirms that the coupling's accuracy effect is entirely attributable to the mean-shift J·m*, with the self-consistent fixed point adding zero benefit (p = 0.984).

The root cause is the sech² saturation barrier: at typical activation magnitudes, sech²(x+J·m*) ≪ 1, capping J·s̄ at ~0.20–0.35 regardless of how large J becomes. The critical regime where CWA's mean-field coupling would provide qualitatively different behavior (J·s̄ → 1) is physically inaccessible under standard training. Future work should target this barrier directly through constrained pre-activation regularization or auxiliary magnitude losses.

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

[15] Pierre Curie. Propriétés magnétiques des corps à diverses températures. *Annales de Chimie et de Physique*, 5:289–405, 1895.
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (evidence) The IFT memory overhead claim contains a verifiable factual error traceable to a code bug. The paper states 'Peak GPU memory is 1.05× GELU (1.047 MB IFT vs. 0.188 MB GELU baseline in this micro-benchmark), meeting the 2× criterion.' However, 1.047 / 0.188 = 5.57×, not 1.05×. Examining artifact art_V46hELP73T_t (full_method_out.json), the fields are: GELU_peak_MB=0.18798828125, IFT_peak_MB=1.046875, IFT_ratio_vs_GELU=1.046875. The ratio field equals the IFT_peak_MB value exactly — a code bug where the ratio variable was set to IFT_peak_MB instead of IFT_peak_MB/GELU_peak_MB. The paper propagated this buggy ratio. The actual overhead is ~5.57×, which violates the stated '2× criterion' in this micro-benchmark. The artifact's summary_findings.ift_memory_within_2x_GELU=true is thus also incorrect, computed from the same buggy ratio.
  Action: Recompute the correct IFT/GELU memory ratio as 1.047/0.188 ≈ 5.57× and correct the paper. If the 2× criterion is the evaluation threshold, acknowledge that the micro-benchmark does not meet it, and explain why: the micro-benchmark baseline (0.188 MB for GELU) is anomalously small (possibly capturing only the output tensor, not full model state). Report instead the IFT vs. unrolled comparison (IFT_ratio_vs_unrolled_inverse=1.0 from the same artifact), which shows IFT uses the same peak memory as unrolled K=50 iterations in this benchmark — already a notable positive result. Alternatively, perform a dedicated memory benchmark on a realistic model and report that ratio.
- [MAJOR] (presentation) The paper has no abstract and no title. It begins directly with the 'Introduction' section. At any top-tier venue (NeurIPS, ICML, ICLR), this is a basic submission requirement. The absence makes it impossible for a reader to quickly understand what the paper is about, what it claims, and what the main results are.
  Action: Add a title and a 150-200 word abstract. The abstract should (1) state CWA's definition, (2) name the formal verification contribution, (3) state the key negative empirical results (gradient underflow, bias-dominance, SOC failure), and (4) identify the sech² saturation root cause. This does not require new experiments — it synthesizes what is already in the paper.
- [MAJOR] (clarity) The paper's contribution identity is ambiguous. The five contribution bullets mix positive results (#1 formal proofs, #2 IFT branch confirmation) with negative results (#3 gradient underflow, #4 bias dominance, #5 SOC failure) without a coherent framing. The Introduction reads as a proposal paper ('transferring this structure to neural activations gives...', 'The contributions of this paper...'), yet all major empirical findings are negative. A reader cannot determine whether CWA is being proposed as useful or definitively shown to be ineffective. The Conclusion ends with 'Future work should target this barrier' — implying CWA is worth pursuing — but no evidence supports this beyond theoretical arguments.
  Action: Revise the Introduction to explicitly position the paper as a mechanistic negative-results study: 'We propose CWA and provide a complete mechanistic investigation that identifies the precise conditions under which mean-field coupling fails and why it cannot self-organize to criticality under standard training.' The Abstract (once added) should lead with the negative findings. The Conclusion should clearly state whether the authors believe CWA is worth pursuing, supported by at least a minimal preliminary experiment or theoretical argument.
- [MINOR] (evidence) The shift ablation conclusion 'CWA's accuracy effect is entirely attributable to the mean-shift J·m*' is subtly misleading. The data shows: CWA-Full=0.4685, CWA-ShiftOnly=0.4686, Pure-Tanh=0.4731. CWA-Full vs Pure-Tanh yields t=-2.54, p=0.126 — NOT statistically significant. There is no confirmed 'accuracy effect' of CWA over the no-shift baseline. Attributing a non-significant effect to a mechanism is logically circular. Furthermore, if Pure-Tanh (numerically) outperforms both CWA variants, the shift does not help and may marginally hurt, so saying the effect is 'attributable to the shift' inverts the actual relationship.
  Action: Revise the ablation conclusion: 'CWA provides no statistically significant accuracy gain over Pure-Tanh (p=0.126). Within CWA variants, the self-consistent fixed-point coupling adds zero benefit over a simple detached mean shift (p=0.984, confirming the bias-dominant characterization). The mean shift itself does not improve accuracy over no-shift baseline.' Also, note that the 'alternative diversity-reduction explanation' is actually partially refuted by the ablation: CWA-ShiftOnly lacks the full self-consistent coupling but matches CWA-Full exactly (p=0.984), which argues against the diversity-reduction hypothesis (which would predict CWA-Full to differ from CWA-ShiftOnly).
- [MINOR] (clarity) GELU+LN underperforms on the gradient ratio metric at all three depths, not just depth 20. The artifact data shows abs_dev(GELU+LN)=0.630 at depth 6 (second-worst, only CWA is worse) and 0.642 at depth 10 (again second-worst). The paper discusses the depth-20 dual failure but attributes it to a 25-epoch budget and LayerNorm gradient interactions — but this explanation must also apply at depth 6 and 10, where the same training budget is used. Silently omitting these results makes the discussion look selective and weakens the methodological caveat that 'the gradient ratio metric is unreliable for normalized architectures.'
  Action: In Section 4.2 and the Discussion, report GELU+LN's abs_dev at all three depths (0.630, 0.642, 8.661) and state explicitly: 'GELU+LN underperforms on the |ratio-1| metric at all tested depths (second-worst at depth 6/10, catastrophic at depth 20), suggesting that the gradient ratio metric conflates LayerNorm's internal re-scaling with gradient magnitudes at any depth, not just depth 20. Cross-class comparisons (normalized vs. unnormalized) should therefore be interpreted with caution throughout.'
- [MINOR] (scope) The experimental scope is limited to unnormalized MLPs on CIFAR-10 and a small character-level GPT on Tiny Shakespeare. The ResNet-20 CIFAR-100 result is preliminary (1 seed, 10 epochs). The paper draws conclusions about CWA's general failure ('gradient underflow at all depths,' 'SOC failure'), but these are established only in the unnormalized MLP and small-GPT settings. Modern architectures (transformers with pre-norm, convolutional nets with residual connections) might exhibit different behavior, particularly since the sech² saturation argument depends on activation magnitudes which differ by architecture.
  Action: Explicitly scope the conclusions to the tested architectures: 'We establish CWA's gradient underflow and SOC failure for unnormalized MLPs at depths 6-20 and a 6-layer character-level GPT. Whether normalized or residual architectures exhibit the same pathologies — particularly the sech² saturation barrier — remains to be investigated.' This is an honest limitation that makes the conclusions more defensible.
- [MINOR] (rigor) The paper reports that IFT_ratio_vs_unrolled_inverse=1.0 (from artifact) — meaning IFT and unrolled backprop use the same peak memory in the micro-benchmark. This is surprising: IFT should store only m* (scalar) while unrolled K=50 stores all K intermediate activations. If IFT doesn't save memory over unrolled in this benchmark, the micro-benchmark may be dominated by model parameter memory (making activation memory negligible) or the unrolled path was not actually storing K intermediate activations. This comparison is more informative than the IFT/GELU ratio but is not reported in the paper.
  Action: Report the IFT/unrolled memory ratio explicitly and explain why it is 1.0. If the micro-benchmark is too small to show activation memory savings, clarify the limitation. The IFT advantage ('O(n) activation memory') should be verified in a setting where K·n intermediate activations are the bottleneck — e.g., a layer with n=4096 and K=50 forward passes should store 50× more memory in unrolled vs. just m* in IFT.
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

### [2] HUMAN-USER prompt · 2026-06-16 22:24:28 UTC

```
Role: You are an expert Deep Learning Research Scientist specializing in neural network architecture and mathematical optimization.Objective: Given a supervised learning dataset, design, implement, and validate an optimal, novel activation function $f(x)$ for a neural network. Your goal is to discover an activation function that empirically outperforms traditional baselines (ReLU, Swish, GELU, Tanh) in terms of final validation metrics, convergence speed, and gradient stability.Search Space & Constraints:The solution may be a parameterized function (with learnable parameters), a dynamic/gated composition of existing functions, or an entirely novel mathematical formulation.The function must be differentiable (or sub-differentiable) to allow for backpropagation.Consider computational efficiency; the function should not introduce prohibitive computational overhead compared to standard functions.
```

### [3] SYSTEM-USER prompt · 2026-06-16 22:26:11 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same CWA frame; adds IFT memory bug correction (5.57× not 1.05×), strengthens bias-dominant + underflow findings with mechanistic ablation, frames as negative-results study.' is too long (at most 120 characters, got 173)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [4] SYSTEM-USER prompt · 2026-06-16 22:26:17 UTC

```
<validation-feedback>
Attempt 2 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same CWA frame; IFT memory bug fixed (5.57× not 1.05×), bias-dominance confirmed, reframed as mechanistic negative-results study.' is too long (at most 120 characters, got 129)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
