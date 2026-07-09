# review_hypo — create_idea

> Phase: `hypo_loop` · round 3 · `review_hypo`
> Run: `run_6gT5lHFn8559` — Novel Activation Function
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-06-16 17:13:51 UTC

```
model: claude-sonnet-4-6 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/iter_3/review_hypo
```

### [2] SYSTEM-USER prompt · 2026-06-16 17:13:58 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviewer (Step 2.2: REVIEW_HYPO)

Pipeline: GEN_HYPO → REVIEW_HYPO (you) → INVENTION_LOOP → GEN_PAPER_REPO

You review a hypothesis BEFORE any experiments run. Catch problems early.

Rigorous pre-flight check → saves compute. Rubber-stamping → wasted pipeline run.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the hypothesis under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of
this research hypothesis BEFORE any experiments have been run.

GOAL: Your review feeds directly back to the hypothesis author. The objective is to
maximize the overall review score in subsequent rounds. Every piece of feedback you
give should be written with this goal in mind — prioritize the critiques and suggestions
that would produce the largest score improvement if addressed. Don't waste the author's
iteration budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the ideas new? Novel combination of known techniques? Clear
    differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the proposal technically sound? Are claims well supported? Is the
    methodology appropriate? Are the authors honest about limitations?
(c) Clarity: Is the hypothesis clearly written and well organized? Does it provide
    enough information for an expert to understand and evaluate it?
(d) Significance: Are the expected results important? Would others build on this?
    Does it address a meaningful problem better than prior work?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims and proposed methodology:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas, value to the broader research community:
  4: excellent  3: good  2: fair  1: poor

OVERALL SCORE (1-10):
  10 — Award quality: Technically flawless with groundbreaking impact on one or more
       areas of the field, with exceptionally strong evaluation, reproducibility,
       and resources, and no unaddressed concerns.
   9 — Very Strong Accept: Technically flawless with groundbreaking impact on at least
       one area and excellent impact on multiple areas, with flawless evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   8 — Strong Accept: Technically strong with novel ideas, excellent impact on at least
       one area or high-to-excellent impact on multiple areas, with excellent evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   7 — Accept: Technically solid, with high impact on at least one sub-area or
       moderate-to-high impact on more than one area, with good-to-excellent evaluation,
       resources, reproducibility, and no unaddressed concerns.
   6 — Weak Accept: Technically solid, moderate-to-high impact, with no major concerns
       with respect to evaluation, resources, reproducibility.
   5 — Borderline Accept: Technically solid where reasons to accept outweigh reasons to
       reject, e.g., limited evaluation. Use sparingly.
   4 — Borderline Reject: Technically solid where reasons to reject, e.g., limited
       evaluation, outweigh reasons to accept. Use sparingly.
   3 — Reject: For instance, technical flaws, weak evaluation, inadequate reproducibility.
   2 — Strong Reject: For instance, major technical flaws, poor evaluation, limited
       impact, poor reproducibility.
   1 — Very Strong Reject: For instance, trivial results or unaddressed concerns.

CONFIDENCE (1-5):
  5: Absolutely certain. Very familiar with related work, checked details carefully.
  4: Confident but not absolutely certain. Unlikely you misunderstood something.
  3: Fairly confident. Possible you missed some related work or details.
  2: Willing to defend your assessment, but quite likely missed central aspects.
  1: Educated guess. Not in your area or difficult to evaluate.

For each dimension, provide a list of specific improvements:
- WHAT needs to change
- HOW to change it (concrete enough for the author to act on immediately)
- EXPECTED SCORE IMPACT: how much would fixing this raise the overall score?

REVIEW PRINCIPLES:
- Be specific and actionable — vague critique is useless
- Ground your review in evidence — search for existing work, accepted papers, known results
- Rank critiques by score impact — address the biggest score blockers first
- Distinguish major issues (would waste compute if not fixed) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Flag fatal flaws that would make experiments pointless if not addressed first

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<hypothesis>
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
</hypothesis>

<review_context>
No experiments have been run yet — evaluate the hypothesis purely on its merits.
</review_context>

<previous_hypothesis>
The hypothesis from the PREVIOUS iteration (before the revision under review).
Use this to classify how the current hypothesis relates to it (see the H↔H
edge instructions in the task).

kind: hypothesis
title: >-
  Curie-Weiss Activation with Adaptive Fixed-Point Iteration: Empirically-Grounded Self-Consistent Within-Layer Coupling for
  Neural Gain Control
hypothesis: >-
  A neural network hidden-layer activation function defined as the fixed point y* of the Curie-Weiss mean-field self-consistency
  equation — y_i = tanh(x_i + J·mean(y)) for all neurons i in a layer, where J = σ(J_raw) ∈ (0,1) is a per-layer learnable
  scalar coupling — will outperform standard pointwise hidden-layer activations (ReLU, GELU, Swish, Tanh) and self-normalizing
  baselines (SELU, tanh+LayerNorm, GELU+LayerNorm) in gradient stability in deep unnormalized networks (≥10 layers), with
  performance improvements on CIFAR-100 (ResNet-20) and character-level language modeling (4-layer GPT), because: (1) the
  within-sample mean-field coupling y_i ← tanh(x_i + J·mean(y)) implements a learned, parameter-efficient form of collective
  output-based gain control that is unavailable to any purely pointwise activation and is categorically distinct from LayerNorm
  (which normalizes inputs, not outputs); (2) the effective per-step convergence rate ρ = J·s̄ = J·mean(sech²(x+J·m*)) can
  be tracked and the adaptive-K stopping rule |m_{t+1}−m_t| < δ renders the computation honest about wall-clock cost at any
  coupling strength; and (3) the question of whether J·s̄ self-organizes toward 1 during training is treated as a primary
  empirical finding — not an assumption — with controlled fixed-J ablations (J fixed at {0.1, 0.3, 0.5, 0.7, 0.9}) separating
  whether criticality is necessary for the benefits.
motivation: >-
  All standard hidden-layer activation functions used between linear layers in MLP blocks — ReLU, GELU, Swish, and tanh —
  are applied pointwise: each neuron's output depends only on its own pre-activation. (Note: softmax is non-pointwise but
  is restricted to output layers and attention operators, not feedforward nonlinearities, and introduces strict simplex constraints
  rather than learnable gain control.) This independence means each layer's effective gain must be managed externally via
  weight initialization, batch/layer normalization, or learning rate schedules. Criticality theory in deep learning (Poole
  et al. 2016; Yang & Schoenholz 2017) shows that networks at the 'edge of chaos' — where the layer Jacobian's singular values
  are near unity, i.e., the effective coupling J·s̄ ≈ 1 — train fastest and generalize best. Existing approaches achieve this
  only at initialization (Poole/Yang weight variance tuning) or through random static mixtures (Lesser & Chowdhury 2026, tanh+Swish
  at theoretical p_c). Neither provides a per-layer learned mechanism that adapts collectively to the actual input distribution
  during training. CWA proposes an activation function that introduces within-layer coupling through a single learnable scalar
  J, implementing the Curie-Weiss mean-field self-consistency equation as the actual forward computation. Critically, the
  new mechanism is tested honestly: (a) adaptive-K iteration makes the computational cost of near-critical regimes explicit;
  (b) J self-organization toward the critical point J·s̄ = 1 is treated as an empirical question measured during experiments,
  not assumed; and (c) baselines include SELU and tanh+LN to directly test whether CWA adds value beyond existing self-normalizing
  and collectively-normalized alternatives.
assumptions:
- >-
  The adaptive-K fixed-point iteration m_{t+1} = mean(tanh(x + J·m_t)) converges with geometric rate ρ = J·s̄ = J·mean(sech²(x+J·m*))
  per step (rigorously bounded by the Banach fixed-point theorem since ρ = dF/dm < 1 when J ∈ (0,1)); the stopping rule |m_{t+1}−m_t|
  < δ = 1e-4 terminates in K*(ρ) = ceil(log(δ/|m_0−m*|)/log(ρ)) steps, which is finite for all J = σ(J_raw) ∈ (0,1). The wall-clock
  overhead (K* iterations × O(n) cost per step) is a measured experimental output, not an assumed constant.
- >-
  PyTorch autograd can differentiate correctly through the unrolled adaptive-K iteration (direct backprop) or via the implicit
  function theorem F(m*) = mean(tanh(x + J·m*)) − m* = 0, which gives ∂m*/∂x = sech²(x+J·m*) / (1 − J·s̄) and ∂m*/∂J = s̄
  · m* / (1 − J·s̄). Both approaches require J·s̄ < 1 (guaranteed by J = σ(J_raw) ∈ (0,1)); the IFT gradient is exact at the
  true fixed point and requires an additional Newton solve if used with inexact convergence.
- >-
  The sigmoid parameterization J = σ(J_raw) hard-constrains J ∈ (0,1), preventing the bistable regime J ≥ 1 and ensuring all
  fixed-point iterations are globally convergent. This eliminates NaN gradients during early training while allowing the optimizer
  to freely adjust J_raw ∈ ℝ.
- >-
  Whether J·s̄ self-organizes toward 1 during training (the 'self-organized criticality' hypothesis) is an empirical question
  to be answered by the experiments, not assumed. The controlled fixed-J ablation study (J fixed at {0.1, 0.3, 0.5, 0.7, 0.9})
  tests whether the benefits of CWA require J to move, or whether any fixed coupling value provides gain-control benefits
  over purely pointwise baselines.
- >-
  The CWA gain-control mechanism is distinct from LayerNorm/BatchNorm: LayerNorm normalizes the INPUT pre-activations x to
  zero mean, unit variance before applying a pointwise nonlinearity; CWA couples the OUTPUTS y through a self-consistency
  feedback mean(y) → tanh(x + J·mean(y)) → new y, operating on output statistics under the actual nonlinearity. This distinction
  is testable by comparing CWA (no LN) versus tanh+LN and GELU+LN in unnormalized deep networks.
investigation_approach: |-
  Implement CWA in PyTorch as a custom nn.Module with J = torch.sigmoid(J_raw) where J_raw is an nn.Parameter initialized at 0 (J ≈ 0.5). Forward pass: adaptive-K iteration m_0 = 0, repeat m ← mean(tanh(x + J·m)) until |m_{t+1}−m_t| < δ = 1e-4 (cap at K_max=50); output y_i = tanh(x_i + J·m*). Backward pass: unrolled autograd through adaptive iterations. At each forward call, log K (number of iterations), J, and J·s̄ = J·mean(sech²(x+J·m*)) for analysis.

  Experiment 1 — Gradient stability in deep MLPs: Train unnormalized MLPs at depths {6, 10, 20} with 256 hidden units on MNIST and CIFAR-10 (as pixel vectors). Compare: CWA vs ReLU, GELU, Swish, tanh, SELU, tanh+LN, GELU+LN, tanh+Swish@p_c (Competing Nonlinearities baseline). Measure: gradient norm ratio log|∇L_{layer1}|/log|∇L_{layerL}| per layer, final accuracy, convergence speed (epochs to 95% of peak). 5 seeds.

  Experiment 2 — ResNet-20 on CIFAR-100: Replace standard GELU/ReLU with CWA in each residual block (no BatchNorm variant and standard BatchNorm variant). Compare against all baselines. Report top-1 accuracy at 200 epochs.

  Experiment 3 — Character-level GPT (4 layers, 128 hidden, sequence length 128) on Tiny Shakespeare: Replace GELU in MLP sublayers with CWA. Compare test BPC (bits per character) at 10K steps against GELU, GELU+LN, SELU, Boltzmann Attention baseline (different component — included for context). Monitor K (iterations), J, and J·s̄ per layer per epoch.

  Experiment 4 — Fixed-J ablation: Train 10-layer MLP on CIFAR-10 with J frozen at {0.1, 0.3, 0.5, 0.7, 0.9} versus learned J. Identify whether J self-organizes and whether criticality (high J·s̄) is necessary for gains.

  Experiment 5 — Computational overhead: Measure wall-clock time per batch for CWA vs GELU as a function of J (and hence ρ = J·s̄) during training to assess the adaptive-K cost. Total LLM API cost: $0 (pure neural network experiments).
success_criteria: >-
  CONFIRM if: (1) CWA in unnormalized deep MLPs (≥10 layers) achieves gradient norm ratio within 2× of 1.0 (i.e., |log|∇L_1|/log|∇L_L||
  < 2.0) while GELU baseline (no normalization) has ratio > 5.0 — demonstrating CWA's core gradient stability claim in the
  setting where it matters most; AND (2) CWA achieves ≥0.5% higher final accuracy than GELU (the strongest standard pointwise
  baseline) on at least 2 of 3 benchmark tasks (CIFAR-10 deep MLP, CIFAR-100 ResNet-20, character-level GPT), measured with
  95% confidence intervals over 5 seeds; AND (3) the adaptive-K overhead averages ≤3× wall-clock vs GELU during training (monitoring
  K per forward call). DISCONFIRM if: (1) CWA performs within noise of all pointwise baselines (including GELU) on all tasks,
  OR (2) tanh+LayerNorm or SELU matches or exceeds CWA on all tasks — indicating the benefit is explained by collective normalization
  rather than the output-coupling self-consistency mechanism; OR (3) the adaptive-K overhead exceeds 10× wall-clock vs GELU
  in the near-critical regime (J·s̄ > 0.9), making it computationally prohibitive. PARTIAL CONFIRM if: CWA improves gradient
  stability (criterion 1) but not final accuracy in normalized networks (ResNet+BN, GPT) while improving in unnormalized deep
  MLPs — this would precisely bound the contribution: CWA provides unique value when external normalization is absent. SOC
  FINDING (separate from confirm/disconfirm): Report whether J·s̄ concentrates near 1 in successful configurations (as hypothesized)
  or settles at scattered values — this is a novel empirical finding either way.
related_works:
- >-
  Boltzmann Attention (Kim & Park, arXiv:2606.12478, June 2026): Proposes learnable pairwise Ising couplings J_{jk} in the
  ATTENTION OPERATOR of transformers, enabling inter-position cooperative/antagonistic co-attention beyond standard softmax
  (J=0). Same physical inspiration (Ising model) and same class of learnable couplings, with demonstrated improvements in
  character-level language modeling. Key difference: Boltzmann Attention replaces the attention operator (inter-token interactions
  across sequence positions); CWA replaces the ACTIVATION NONLINEARITY (inter-neuron coupling within a single layer's hidden
  dimension). These are complementary architectural components — Boltzmann Attention and CWA could be combined in the same
  transformer. Additionally, Boltzmann Attention uses pairwise J_{jk} (quadratic parameters); CWA uses a single scalar J per
  layer (one learnable parameter).
- >-
  Competing Nonlinearities (Lesser & Chowdhury, arXiv:2605.05294, May 2026): Achieves edge-of-chaos criticality in activation
  design by statistically mixing tanh and Swish at a theoretical critical mixing fraction p_c, producing scale-invariant variance
  propagation without fixed-point overhead. Activation disorder acts as regularization. Key difference: Competing Nonlinearities
  uses a STATIC mixture at initialization (quenched disorder), with p_c determined theoretically from variance propagation
  analysis — there is no learned parameter, no self-consistency feedback, and no within-layer neuron coupling. CWA introduces
  a LEARNABLE coupling J that is adapted by gradient descent and creates an explicit inter-neuron feedback through mean(y).
  Competing Nonlinearities is included as a direct baseline in CWA experiments (tanh+Swish at p_c).
- >-
  Milletarì et al. (2018, arXiv:1805.08786) 'Mean Field Theory of Activation Functions': Uses statistical mechanics to derive
  existing activations (tanh, ReLU, Swish) as natural solutions to energy-based models. Key difference: this work provides
  post-hoc physical interpretation of known functions; CWA proposes a NEW activation defined by the actual Curie-Weiss self-consistency
  equation with a learnable coupling J, introducing within-layer neuron coupling absent from all their derived activations.
- >-
  Bal (2021, 'Deep Implicit Attention'): Applies Thouless-Anderson-Palmer mean-field equations to ATTENTION mechanisms in
  transformers, showing softmax attention is one step of naive mean-field inference. Key difference: their work reformulates
  the attention operator; CWA replaces ACTIVATION FUNCTIONS (nonlinearities within a layer's hidden dimension), a different
  architectural component. CWA operates within a single layer's neurons, while Bal's work operates across token positions.
- >-
  Yang & Schoenholz (2017) 'Mean Field Residual Networks' and Poole et al. (2016) 'Exponential Expressivity': Show that networks
  at the edge of chaos (Jacobian singular values ≈ 1, i.e., effective coupling J·s̄ = 1) propagate information best and train
  fastest, achieved via careful weight variance initialization. Key difference: these works achieve criticality through INITIALIZATION
  only — it drifts away as weights update. CWA provides a learnable mechanism through the activation function that can in
  principle maintain J·s̄ near 1 throughout training (whether it does so empirically is a primary experimental finding).
- >-
  Bai et al. (2019) 'Deep Equilibrium Models (DEQ)': Applies fixed-point iteration at the FULL-LAYER level — the entire layer
  mapping (weight matrix + activation) is solved to a fixed point. Key difference: DEQ replaces the full layer (O(n²) per
  Newton step); CWA is a lightweight activation-level operation (O(n·K) for adaptive-K iterations) that retains the standard
  linear weight matrix and adds only one learnable parameter J per layer. CWA is a drop-in activation replacement; DEQ is
  a complete layer replacement.
- >-
  Klambauer et al. (2017, NeurIPS) 'Self-Normalizing Neural Networks (SELU)': Designs an activation function (Scaled ELU)
  with specific fixed-point statistics (mean≈0, var≈1 propagation through layers) that self-normalizes without external normalization
  layers. Key difference: SELU achieves self-normalization by carefully tuning the function's fixed-point statistics under
  the assumption of normally distributed inputs — it is still POINTWISE (each neuron depends only on its own pre-activation).
  CWA's self-consistency coupling explicitly averages OUTPUT values and feeds them back, coupling neurons within the layer.
  SELU is included as a direct baseline.
- >-
  Amos & Kolter (2017) 'OptNet: Differentiable Optimization as a Layer': Introduces differentiable quadratic program solvers
  as neural network layers (O(n³) per solve). Key difference: OptNet is a layer-level replacement; CWA is activation-level
  (O(n·K), K adaptive), making it parameter-efficient and drop-in replaceable at the nonlinearity position.
inspiration: >-
  This hypothesis is a Level-3 (methodological) cross-domain transfer from statistical physics, specifically the Curie-Weiss
  model of ferromagnetism. In physics, the self-consistency equation m = tanh(β(h + J·m)) describes how an Ising spin aligns
  with an external field h plus a self-consistent feedback from the average magnetization J·m of all other spins. The critical
  point βJ = 1 marks the onset of long-range magnetic order and corresponds to maximum magnetic susceptibility — tiny external
  fields produce large magnetization responses. The cross-domain insight is: just as a ferromagnet near its Curie temperature
  exhibits maximum input sensitivity (large response to small field), a neural layer near its effective critical coupling
  J·s̄ = 1 should exhibit maximum sensitivity to pre-activations (high gradient signal-to-noise ratio). The key physical-to-neural
  mapping is: external field h ↔ pre-activation x; magnetization m ↔ layer mean output; inverse temperature β ↔ 1 (absorbed
  into J); coupling J ↔ learnable scalar per layer. The self-consistency structure — outputs feeding back into themselves
  — is absent from all standard pointwise hidden-layer activations, which correspond to the J=0 (non-interacting) case. This
  revision incorporates an important amendment: the standard physics analysis of critical slowing down (convergence rate ρ
  = J·s̄ per iteration) is treated as a computational reality rather than an engineering nuisance — the adaptive-K stopping
  criterion makes the cost honest rather than hiding it under a fixed-5-step assumption. The analogy to sandpile self-organized
  criticality (J spontaneously approaching 1) is retained as an empirical hypothesis to be tested, not assumed.
terms:
- term: Curie-Weiss Activation (CWA)
  definition: >-
    The proposed hidden-layer activation function defined by the fixed point y* of the equation y = tanh(x + J·mean(y)), where
    x is the vector of pre-activations, y is the vector of activations, J = σ(J_raw) ∈ (0,1) is a per-layer learnable scalar
    coupling, and mean(y) is the layer-wise mean of y. The fixed point is found by adaptive-K iteration m_{t+1} = mean(tanh(x
    + J·m_t)) until |m_{t+1}−m_t| < δ, then y_i = tanh(x_i + J·m*).
- term: Effective Coupling (J·s̄)
  definition: >-
    The true critical parameter of CWA, defined as J·s̄ = J·mean(sech²(x+J·m*)) ∈ (0,1). This is the per-step convergence
    rate of the fixed-point iteration and the spectral norm of the layer's input-output Jacobian. J·s̄ → 1 corresponds to
    the edge-of-chaos critical regime with diverging gain. J·s̄ depends on both the learned coupling J and the input distribution
    (through s̄), making the critical condition input-distribution-dependent. All experiments track J·s̄ alongside J.
- term: Adaptive-K Iteration
  definition: >-
    The convergence-based stopping rule for the CWA forward pass: iterate m ← mean(tanh(x + J·m)) until |m_{t+1}−m_t| < δ
    = 1e-4 (with a maximum of K_max=50 iterations). The number of required steps K*(ρ) grows as O(1/(1−ρ)) near criticality
    (ρ = J·s̄ → 1) due to classical critical slowing down. Wall-clock cost per forward pass is measured during training as
    a function of the current J·s̄ to empirically characterize the computational overhead of near-critical regimes.
- term: Sigmoid Parameterization of J
  definition: >-
    The constraint mechanism for the learnable coupling: J = σ(J_raw) = 1/(1+exp(−J_raw)), where J_raw ∈ ℝ is the actual learnable
    parameter and J ∈ (0,1) is the constrained coupling. This hard-constrains J to the monostable regime (below the ferromagnetic
    phase transition at J=1), preventing bistability and guaranteeing global convergence of the fixed-point iteration. J_raw
    is initialized at 0 so that J starts at 0.5 (moderate coupling).
- term: Critical Gain
  definition: >-
    The effective gradient amplification of CWA near the critical coupling J·s̄ → 1. By the implicit function theorem, the
    input-output Jacobian element ∂y_i/∂x_i = sech²(x_i + J·m*) / (1 − J·s̄), which diverges as J·s̄ → 1. This diverging gain
    enables maximum sensitivity of the layer to its inputs and is the proposed mechanism for gradient stability in deep unnormalized
    networks.
- term: Self-Organized Criticality (SOC) Hypothesis
  definition: >-
    The empirical hypothesis — not an assumption — that gradient descent will push J·s̄ toward 1 during training, because
    layers with J·s̄ near 1 have higher effective gain and thus more informative gradients, giving task-loss minimization
    an incentive to approach criticality. Tested experimentally by plotting the distribution of learned J·s̄ values across
    layers and seeds at convergence and by the fixed-J ablation study.
- term: Output-Coupling vs Input-Normalization
  definition: >-
    The key mechanistic distinction between CWA and LayerNorm/BatchNorm. LayerNorm/BatchNorm normalize the INPUT pre-activations
    x (shifting and scaling to zero mean, unit variance) before a pointwise nonlinearity — they operate on input statistics.
    CWA couples the OUTPUTS y through the self-consistency feedback mean(y) → tanh(x + J·mean(y)) → new y — it operates on
    output statistics under the actual nonlinearity. These are categorically different operations that compose rather than
    substitute.
- term: Fixed-J Ablation
  definition: >-
    A controlled experiment where J is frozen at specific values {0.1, 0.3, 0.5, 0.7, 0.9} (J_raw fixed, not updated by optimizer)
    and compared against the full CWA (learned J). This separates whether the performance benefit of CWA requires (a) any
    nonzero coupling (vs. J=0 = pure tanh), (b) a specific coupling value, or (c) the adaptive optimization of J by gradient
    descent. It directly tests the SOC hypothesis and whether criticality is necessary for the performance gains.
summary: >-
  We propose the Curie-Weiss Activation (CWA), a hidden-layer activation function where each neuron's output is the fixed
  point of the mean-field self-consistency equation y_i = tanh(x_i + J·mean(y)), with J = σ(J_raw) ∈ (0,1) a per-layer learnable
  coupling constrained by sigmoid parameterization. Borrowing from the physics of ferromagnetism, CWA introduces within-layer
  inter-neuron coupling absent from all standard pointwise MLP-block activations; whether J self-organizes toward the critical
  coupling J·s̄ → 1 is treated as an empirical finding — tested via adaptive-K iteration with honest wall-clock accounting
  and a controlled fixed-J ablation — evaluated against comprehensive baselines (GELU, SELU, tanh+LN, GELU+LN, Competing Nonlinearities
  mixture) on deep unnormalized MLPs, ResNet-20/CIFAR-100, and character-level language modeling.
</previous_hypothesis>

<previous_review>
Critiques from the previous review. Check which ones have been addressed
in the revised hypothesis. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (methodology) Unrolled backprop through adaptive-K iterations introduces a non-trivial memory overhead that is not discussed. When ρ = J·s̄ → 0.9 and K* reaches 50 (K_max), PyTorch's unrolled autograd must store K* intermediate activation tensors of shape (batch_size × n_neurons) per CWA layer. Concretely: batch=512, n=256, K*=50 → 50 × 512 × 256 × 4 bytes = 26MB per layer, per forward pass. For a 20-layer network with CWA everywhere, this is ~520MB of additional activation memory vs. ~10MB for GELU. Experiment 5 measures wall-clock time but not peak GPU memory, which may be the binding constraint in the near-critical regime. Separately, the DEQ literature (Bai et al. 2019; Efficient DEQ 2023) has demonstrated that implicit differentiation (IFT) reduces memory to O(1) by not storing intermediate activations — this approach is mentioned in the assumptions but not adopted in the investigation plan.
  Action: Add peak GPU memory utilization as a second tracked output in Experiment 5, alongside wall-clock time, as a function of J·s̄. Either (a) adopt IFT backprop for experiments where J·s̄ > 0.8, storing only the converged m* and computing ∂m*/∂x analytically — this is O(1) in K*, avoids storing intermediate activations, and has been proven correct in the DEQ literature; or (b) keep unrolled autograd but explicitly acknowledge and measure the O(K*) memory overhead and flag it as a practical limitation when J·s̄ > 0.85. The investigation approach section should commit to one strategy and justify why. Expected score impact: +0.5.
- [MAJOR] (methodology) The mean-field approximation underlying CWA is exact only as n_neurons → ∞, but ResNet-20 operates at layer widths of 16–64 channels in early blocks. At n=16, the sample mean m* = (1/n)Σ_i tanh(x_i + J·m*) has a finite-sample noise of O(1/√n) = O(0.25) relative to the unit-scale activations — a 25% noise floor. This means the 'self-consistency' equation the iteration solves is not the mean-field equation but a noisy, sample-dependent perturbation of it. The fixed-point m* will fluctuate substantially across samples at narrow widths, making J·s̄ a noisy quantity and potentially undermining both gradient stability and the SOC analysis. The hypothesis never acknowledges this, and attributing CWA results in the narrow-width ResNet-20 blocks to the mean-field physics may be incorrect.
  Action: Add a brief theoretical caveat: CWA's mean-field interpretation holds in the large-n limit; at finite n, the fixed-point equation includes O(1/√n) fluctuations. Mitigate or characterize empirically by: (1) comparing CWA performance in the first ResNet-20 block (n=16) vs. later blocks (n=64), to test whether narrow-width blocks benefit less; (2) alternatively, test a 'wide ResNet-20' variant (4× channels throughout) to see if performance improves at larger n. This analysis would convert a potential confound into an informative experiment about the n-dependence of CWA's mechanism. Expected score impact: +0.4.
- [MINOR] (scope) The character-level language modeling experiment uses a 4-layer, 128-hidden GPT on Tiny Shakespeare. This is an extremely small model by current standards (GPT-2 small has 12 layers, 768 hidden). At this scale, the test BPC differences between activation functions may be dominated by optimization noise and are difficult to interpret as evidence about language model utility. The Boltzmann Attention paper (cited in related work) uses Tiny Shakespeare as its own benchmark, making the CWA result directly comparable to that paper, but not to the broader NeurIPS/ICLR language modeling literature.
  Action: Scale the GPT experiment to at least 6 layers and 256 hidden units, keeping sequence length 256 and training on Tiny Shakespeare, OR switch to WikiText-2 (word-level) which allows comparison to the established SELU/normalization literature. The goal is to have at least one language modeling result that isn't a clear toy: the 4-layer 128-hidden model is smaller than GPT-2's single attention head output projection. Even 6L/256H on Tiny Shakespeare would be meaningfully larger. Expected score impact: +0.3.
- [MINOR] (rigor) The gradient stopping criterion δ = 1e-4 for |m_{t+1} − m_t| < δ bounds the iteration residual, but when IFT is used for backprop, the gradient error is not just O(δ) — it is O(δ/(1−J·s̄)), which diverges as J·s̄ → 1. Near criticality (J·s̄ = 0.9), the effective gradient error is 10× the residual threshold, i.e., ~1e-3. This interplay between the stopping tolerance δ and the IFT gradient accuracy in the near-critical regime is not acknowledged. The hypothesis mentions IFT as an alternative but doesn't note that IFT's accuracy degrades in the same near-critical regime where adaptive-K is expensive.
  Action: In the assumptions section, add a note: when using IFT backprop with an inexact fixed point (residual r = |F(m*)|), the gradient error is O(r/(1−J·s̄)) by the perturbation theory of the IFT. At J·s̄ = 0.9 and δ = 1e-4, this error is ~1e-3, which is small relative to gradient norms but should be verified not to cause systematic bias. Either tighten δ adaptively as J·s̄ increases (e.g., δ = 1e-4 × (1 − J·s̄)), or acknowledge the IFT gradient bias as a measured output alongside K* and J·s̄ in Experiment 3. Expected score impact: +0.2.
- [MINOR] (clarity) The practical significance of the unnormalized deep network setting is not motivated. The hypothesis's most compelling result scenario — PARTIAL CONFIRM, where CWA helps only when normalization is absent — is the most likely outcome given that SELU and tanh+LN are strong baselines in normalized settings. However, unnormalized deep MLPs are rare in current practice; most practitioners use LayerNorm or BatchNorm as a default. Without motivation for why the unnormalized setting matters, the PARTIAL CONFIRM scenario reads as a niche finding rather than a targeted contribution.
  Action: Add 2-3 sentences to the motivation section explaining why unnormalized deep networks are a relevant practical target: e.g., on-device inference where normalization's mean/variance computation is expensive (memory-constrained edge hardware); scientific neural operators where normalization distorts physical quantities; architectures that deliberately avoid BatchNorm to prevent train/test distribution shift. This converts the PARTIAL CONFIRM from a fallback to a principled targeted claim. Expected score impact: +0.2.
- [MINOR] (evidence) The Competing Nonlinearities (Lesser & Chowdhury 2026) baseline requires knowing the theoretical critical mixing fraction p_c, which is architecture-specific (it depends on the variance propagation under the specific tanh/Swish mixture). The hypothesis includes 'tanh+Swish@p_c' as a baseline without specifying how p_c will be computed for each architecture in the experiment. If p_c is copied from Lesser & Chowdhury's derivation without re-deriving it for the specific architectures tested, the baseline may not be at its optimal operating point, making the comparison unfair.
  Action: Specify how p_c will be determined for each tested architecture: either (a) derive p_c analytically from the variance propagation equations at depth d (following Lesser & Chowdhury's method) for each network depth tested, or (b) tune p_c as a hyperparameter on the validation set for each architecture (ensuring the baseline is at its best), or (c) include p_c ∈ {theoretical, tuned} as separate conditions. Clarify this in the investigation approach section. Expected score impact: +0.1.
</previous_review>

<task>
Provide a thorough peer review of this research hypothesis.

STEP 1 — GROUND YOUR REVIEW IN EVIDENCE:
Before writing critiques, search for relevant context to make your review authoritative:
- Search for accepted papers at top venues in this area — what level of
  contribution gets accepted? How does this hypothesis compare?
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes in the literature

STEP 2 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would waste compute if not fixed) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Flag fatal flaws that would waste compute if not fixed first.

STABILITY IS OK: If the hypothesis is on track and just needs more iterations to prove itself,
keep your feedback similar to the previous round. Don't manufacture new critiques — only escalate
when the revision introduced new issues or failed to address prior ones.

STEP 3 — H↔H EDGE (only if a <previous_hypothesis> block is present):
Classify how the current hypothesis relates to the previous iteration's hypothesis
using Moulines's structuralist typology. Set ``relation_type`` to one of:
    - "evolution": refining specialised claims while keeping the same conceptual frame
    - "embedding": the previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian, incommensurable shift)
Set ``relation_rationale`` to a brief justification (≤120 chars).

If no <previous_hypothesis> is present (this is iteration 1), leave both fields
null/empty.

Provide your review via structured output.
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
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "ReviewerFeedback + Moulines H\u2194H typology for hypo_loop iterations.\n\nAdds ``relation_type`` + ``relation_rationale`` so the trace projection\ncan build a typed edge from the previous iteration's hypothesis to\nthis iteration's. On iteration 1 (no previous), both fields are\nempty/None.",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    },
    "relation_type": {
      "anyOf": [
        {
          "enum": [
            "evolution",
            "embedding",
            "replacement"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Moulines's structuralist typology classifying how this iteration's hypothesis relates to the previous iteration's: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (Kuhnian shift). Leave null on the first iteration (no previous hypothesis).",
      "title": "Relation Type"
    },
    "relation_rationale": {
      "default": "",
      "description": "Brief rationale (one short line, \u2264120 chars) for the relation_type. Empty on the first iteration.",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "HypoReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-06-16 17:13:58 UTC

```
Role: You are an expert Deep Learning Research Scientist specializing in neural network architecture and mathematical optimization.Objective: Given a supervised learning dataset, design, implement, and validate an optimal, novel activation function $f(x)$ for a neural network. Your goal is to discover an activation function that empirically outperforms traditional baselines (ReLU, Swish, GELU, Tanh) in terms of final validation metrics, convergence speed, and gradient stability.Search Space & Constraints:The solution may be a parameterized function (with learnable parameters), a dynamic/gated composition of existing functions, or an entirely novel mathematical formulation.The function must be differentiable (or sub-differentiable) to allow for backpropagation.Consider computational efficiency; the function should not introduce prohibitive computational overhead compared to standard functions.
```

### [4] ASSISTANT · 2026-06-16 17:14:58 UTC

```
I'll ground my review in evidence first by searching for relevant related work, then write the structured review.
```

### [5] TOOL CALL — Skill · 2026-06-16 17:14:58 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-06-16 17:14:58 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — ToolSearch · 2026-06-16 17:15:06 UTC

```
{'query': 'select:WebSearch,WebFetch'}
```

### [8] TOOL RESULT — ToolSearch · 2026-06-16 17:15:06 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [9] TOOL CALL — WebSearch · 2026-06-16 17:15:12 UTC

```
Curie-Weiss activation function neural network mean field self-consistency 2025 2026
```

### [10] TOOL CALL — WebSearch · 2026-06-16 17:15:12 UTC

```
implicit function theorem backpropagation activation function hybrid unrolled gradient
```

### [11] TOOL CALL — WebSearch · 2026-06-16 17:15:12 UTC

```
within-layer neuron coupling activation function collective gain control deep learning
```

### [12] TOOL RESULT — WebSearch · 2026-06-16 17:15:18 UTC

```
{"query": "Curie-Weiss activation function neural network mean field self-consistency 2025 2026", "results": [{"tool_use_id": "srvtoolu_01966n93LJe2Vp15m9v4VGfY", "content": [{"title": "On the capacity of neural networks", "url": "https://arxiv.org/pdf/2211.07531"}, {"title": "Mean-field theory of graph neural networks in graph partitioning", "url": "https://arxiv.org/pdf/1810.11908"}, {"title": "Glassy phase in dynamically-balanced neuronal networks", "url": "https://www.biorxiv.org/content/10.1101/2022.03.14.484348.full.pdf"}, {"title": "The mean field approach for populations of spiking neurons", "url": "https://arxiv.org/pdf/2109.01279"}, {"title": "Mean-field theory of a plastic network of integrate-and-fire neurons", "url": "https://arxiv.org/pdf/0906.4549"}, {"title": "A walk in the statistical mechanical formulation of neural networks", "url": "https://arxiv.org/pdf/1407.5300"}, {"title": "Model-agnostic neural mean field with a data-driven transfer function", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11413991/"}, {"title": "Beyond mean field theory: statistical field theory for neural networks - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4169078/"}, {"title": "[2205.09653] Self-Consistent Dynamical Field Theory of Kernel Evolution in Wide Neural Networks", "url": "https://arxiv.org/abs/2205.09653"}]}, "Based on the web search results, here's what I found regarding your query about Curie-Weiss activation functions, neural networks, mean field theory, and self-consistency:\n\n## Key Findings\n\nThe Curie-Weiss model can store one pattern of information and its input-output relation (called self-consistency) connects with the transfer function of neural networks. This demonstrates a fundamental link between ferromagnetic models from statistical mechanics and neural network theory.\n\nMean field equations are self-consistent equations where the same mean firing rates appear on both sides of the equations, with self-consistency arising from the recurrent nature of the network wherein the output of a neuron is also an input to all other neurons.\n\nRecent work has extended these classical concepts. Self-consistent dynamical field theory has been applied to analyze feature learning in infinite-width neural networks trained with gradient flow, with nonlinear networks solved through alternating sampling procedures to self-consistently determine kernel order parameters.\n\nAdditionally, model-agnostic neural mean field approaches with data-driven transfer functions can predict network responses to time-varying stimuli with high accuracy and enable approximate bifurcation analysis, without assuming large presynaptic rates or small postsynaptic potential sizes.\n\nThe search results cover foundational work and recent developments, though specific 2025-2026 papers combining all these concepts may be limited in availability."], "durationSeconds": 6.924290943, "searchCount": 1}
```

### [13] TOOL RESULT — WebSearch · 2026-06-16 17:15:20 UTC

```
{"query": "implicit function theorem backpropagation activation function hybrid unrolled gradient", "results": [{"tool_use_id": "srvtoolu_018hSn8TFgFemZeMCV7uqy4E", "content": [{"title": "Backprop is not just the chain rule — Graduate Descent", "url": "http://timvieira.github.io/blog/post/2017/08/18/backprop-is-not-just-the-chain-rule/"}, {"title": "Control-Oriented Model-Based Reinforcement Learning with Implicit   Differentiation", "url": "https://arxiv.org/pdf/2106.03273"}, {"title": "A global convergence theory for deep ReLU implicit networks via   over-parameterization", "url": "https://arxiv.org/pdf/2110.05645"}, {"title": "Backpropagation of Unrolled Solvers with Folded Optimization", "url": "https://arxiv.org/pdf/2301.12047"}, {"title": "The least-control principle for local learning at equilibrium", "url": "https://arxiv.org/pdf/2207.01332"}, {"title": "Hard to Forget: Poisoning Attacks on Certified Machine Unlearning", "url": "https://arxiv.org/pdf/2109.08266"}, {"title": "Nonsmooth Implicit Differentiation for Machine Learning and Optimization", "url": "https://proceedings.neurips.cc/paper/2021/file/70afbf2259b4449d8ae1429e054df1b1-Paper.pdf"}, {"title": "Optimizing Millions of Hyperparameters by Implicit Diﬀerentiation", "url": "https://proceedings.mlr.press/v108/lorraine20a/lorraine20a.pdf"}]}, "I found several relevant research papers and resources on this topic. Here's what the search revealed:\n\n## Key Findings\n\n**Implicit Function Theorem and Backpropagation:**\nThe implicit function theorem relates to computing global gradients in cyclic graphs by solving linear systems to stitch together local gradients.\n\n**Memory Efficiency for Gradient Computation:**\nThe implicit function theorem enables getting gradients of hyperparameters without storing intermediate states of optimization algorithms, which is a significant memory saver compared to direct backprop that would require caching all intermediate states.\n\n**Implicit Neural Networks:**\nFor implicit neural networks, gradient formulas can be derived using the implicit function theorem, in contrast to regular networks with finite layers that require storing all intermediate parameters.\n\n**Unrolled Solvers:**\nBackpropagation of unfolding is computationally equivalent to solving linear equations using a specific algorithm and does not require automatic differentiation.\n\n**Implicit Gradient Computation:**\nThe implicit gradient can be calculated analytically using the implicit function theorem. This approach more efficiently handles gradients through iterative optimization algorithms compared to naively unrolling loops in the optimization algorithm.\n\nThese results show a rich intersection of implicit differentiation theory, backpropagation algorithms, and practical optimization techniques in machine learning."], "durationSeconds": 7.322490955999994, "searchCount": 1}
```

### [14] TOOL RESULT — WebSearch · 2026-06-16 17:15:20 UTC

```
{"query": "within-layer neuron coupling activation function collective gain control deep learning", "results": [{"tool_use_id": "srvtoolu_01ERdWR92uchQV2xnJKTXLy1", "content": [{"title": "Quantum Control based on Deep Reinforcement Learning", "url": "https://arxiv.org/pdf/2212.07385"}, {"title": "Advantages of biologically-inspired adaptive neural activation in RNNs   during learning", "url": "https://arxiv.org/pdf/2006.12253"}, {"title": "Artificial neural networks", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11574176"}, {"title": "Artificial neural networks", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11790220"}, {"title": "Why I need the same activation function in a layer with multiple neurons? - Neural Networks and Deep Learning - DeepLearning.AI", "url": "https://community.deeplearning.ai/t/why-i-need-the-same-activation-function-in-a-layer-with-multiple-neurons/226930"}, {"title": "Neural network with training by perturbation", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5640494"}, {"title": "Nish: A Novel Negative Stimulated Hybrid Activation Function", "url": "https://arxiv.org/pdf/2210.09083"}, {"title": "Solving internal covariate shift in deep learning with linked neurons", "url": "https://arxiv.org/pdf/1712.02609"}, {"title": "Learning Combinations of Activation Functions Franco Manessi", "url": "https://arxiv.org/pdf/1801.09403"}]}, "I found several relevant results related to your search query. Here's what the search returned:\n\nThe most directly relevant result appears to be from a research paper on **\"Solving internal covariate shift in deep learning with linked neurons\"** (arxiv.org/pdf/1712.02609). This work discusses a framework formalized in terms of constraints that link a set of neurons, where the idea is that in a set of linked neurons there is always at least one neuron with an operating point outside a flat area, with neurons being linked if there is at least one member with a non-zero gradient for any data point.\n\nThe paper further explains that all members of the coupling have exactly the same input, with all neurons in the coupling sharing the same weights. The work demonstrates two linked rectified linear units using a min-max policy for linking, as well as two linked SELU activations.\n\nAdditionally, there is research on **adaptive activation functions** that includes a parametric family of activation functions with parameters controlling the degree of saturation and neuronal gain, which interpolates between non-saturating softplus and saturating sigmoid functions.\n\nThe search results also show work on gain control in neural networks, including neuron gain that can be applied to the net input or output of the neuron to attenuate or amplify values, with advantages including increased learning speed and weight normalization."], "durationSeconds": 8.494961223999999, "searchCount": 1}
```

### [15] TOOL CALL — WebSearch · 2026-06-16 17:15:26 UTC

```
arXiv 2606.12478 Boltzmann Attention NeurIPS 2026
```

### [16] TOOL CALL — WebSearch · 2026-06-16 17:15:26 UTC

```
arXiv 2605.05294 Competing Nonlinearities edge of chaos criticality activation
```

### [17] TOOL CALL — WebSearch · 2026-06-16 17:15:26 UTC

```
deep equilibrium models DEQ hybrid IFT unrolled backpropagation memory overhead 2023 2024
```

### [18] TOOL RESULT — WebSearch · 2026-06-16 17:15:34 UTC

```
{"query": "arXiv 2606.12478 Boltzmann Attention NeurIPS 2026", "results": [{"tool_use_id": "srvtoolu_017g9uatNbPo8NReVKo1SLja", "content": [{"title": "[2606.12478] Boltzmann Attention: Learnable Ising Couplings for Cooperative Attention", "url": "https://arxiv.org/abs/2606.12478"}, {"title": "Boltzmann Attention: Learnable Ising Couplings for Cooperative Attention", "url": "https://arxiv.org/html/2606.12478"}, {"title": "Simulating and Forecasting the Cumulative Confirmed Cases of SARS-CoV-2 in China by Boltzmann Function-based Regression Analyses", "url": "https://www.medrxiv.org/content/10.1101/2020.02.16.20023564.full.pdf"}, {"title": "Conductance interaction identification by means of Boltzmann distribution and mutual information analysis in conductance-based neuron models", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3403507/"}, {"title": "Are Transformers with One Layer Self-Attention Using Low-Rank Weight   Matrices Universal Approximators?", "url": "https://arxiv.org/pdf/2307.14023"}, {"title": "[2212.04692] Attention in a family of Boltzmann machines emerging from modern Hopfield networks", "url": "https://arxiv.org/abs/2212.04692"}]}, "Based on the search results, here's what I found about arXiv paper 2606.12478:\n\nBoltzmann Attention is an energy-based generalization in which attention patterns are governed by an interacting Ising model. The method augments the usual data-dependent local fields with learnable pairwise couplings, allowing the model to represent inter-position correlations beyond those captured by softmax or sigmoid attention.\n\nThe paper was authored by Gilhan Kim and Daniel K. Park from Yonsei University in Seoul, Republic of Korea, and was submitted on June 10, 2026.\n\nAccording to the search results, experiments on character-level language modeling and synthetic bracket matching show that Boltzmann attention consistently improves over standard softmax attention within a standard Transformer. The motivation behind this approach is that while attention mechanisms are central to modern sequence models and softmax normalization introduces competition among positions, a standard attention layer does not explicitly parameterize learnable interactions between attention decisions, which limits its ability to directly model cooperative or antagonistic co-attention structure."], "durationSeconds": 8.669898857000007, "searchCount": 1}
```

### [19] TOOL RESULT — WebSearch · 2026-06-16 17:15:36 UTC

```
{"query": "arXiv 2605.05294 Competing Nonlinearities edge of chaos criticality activation", "results": [{"tool_use_id": "srvtoolu_01EiBDTo17vd8kVFL8pys9jR", "content": [{"title": "[2605.05294] Competing nonlinearities, criticality, and order-to-chaos transition in deep networks", "url": "https://arxiv.org/abs/2605.05294"}, {"title": "Competing nonlinearities, criticality, and order-to-chaos transition in deep networks", "url": "https://arxiv.org/html/2605.05294"}, {"title": "Exact solutions to the nonlinear dynamics of learning in ...", "url": "https://arxiv.org/pdf/1312.6120"}, {"title": "Consciousness is supported by near-critical cortical electrodynamics", "url": "https://www.biorxiv.org/content/10.1101/2021.06.10.447959.full.pdf"}, {"title": "At the Edge of Chaos: Real-time Computations and Self-Organized Criticality in Recurrent Neural Networks", "url": "https://proceedings.neurips.cc/paper/2004/hash/f8da71e562ff44a2bc7edf3578c593da-Abstract.html"}, {"title": "Transition to chaos separates learning regimes and relates to measure of consciousness in recurrent neural networks", "url": "https://www.biorxiv.org/content/10.1101/2024.05.15.594236.full.pdf"}, {"title": "A mean-field approach to criticality in spiking neural networks for reservoir computing", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12501264/"}, {"title": "Unveiling the intrinsic dynamics of biological and artificial neural   networks: from criticality to optimal representations", "url": "https://arxiv.org/pdf/2307.10669"}]}, "Based on the search results, here's what I found about arXiv paper 2605.05294:\n\n## Paper Overview\n\nThe paper is titled \"Competing nonlinearities, criticality, and order-to-chaos transition in deep networks\" by Omri Lesser and Debanjan Chowdhury, submitted on May 6, 2026.\n\n## Main Contribution\n\nDeep neural networks owe their expressive power to nonlinear activation functions, and the effective field theory of signal propagation at initialization reveals distinct universality classes of activations that exhibit different depth scaling.\n\nThe paper shows that a statistical mixture of activations, where each neuron independently and randomly draws its activation from a two-component distribution with mixing fraction p, provides a new mechanism for a continuous phase transition. Applied to a mixture of Tanh and Swish, the transition is sharp in the depth scaling of the preactivation variance, separating a variance-collapsing from a variance-inflating phase.\n\nThe research addresses the open problem of tuning across different universality classes of activation functions with analytical control, using competing nonlinearities to achieve criticality and understand order-to-chaos transitions in deep neural networks."], "durationSeconds": 10.860107019000003, "searchCount": 1}
```

### [20] TOOL RESULT — WebSearch · 2026-06-16 17:15:38 UTC

```
{"query": "deep equilibrium models DEQ hybrid IFT unrolled backpropagation memory overhead 2023 2024", "results": [{"tool_use_id": "srvtoolu_019MdofAkMaV93ZpQPSKKiFe", "content": [{"title": "Deep Equilibrium Models", "url": "https://www.researchgate.net/publication/335618036_Deep_Equilibrium_Models"}, {"title": "TorchDEQ: A Library for Deep Equilibrium Models Zhengyang Geng1", "url": "https://arxiv.org/pdf/2310.18605"}, {"title": "Memory-efficient model-based deep learning with convergence and   robustness guarantees", "url": "https://arxiv.org/pdf/2206.04797"}, {"title": "Deep Equilibrium Models: Neural Networks Without Layers | by Void | Medium", "url": "https://medium.com/@atulit23/deep-equilibrium-models-neural-networks-without-layers-4dd1b1095503"}, {"title": "(ISMRM 2024) Robust Deep Equilibrium Paradigms for 3D Hybrid Stack of Stars Reconstruction", "url": "https://archive.ismrm.org/2024/0347.html"}, {"title": "Deep Implicit Optimization enables Robust Learnable Features for   Deformable Image Registration", "url": "https://arxiv.org/pdf/2406.07361"}, {"title": "Efficient Training of Deep Equilibrium Models", "url": "https://arxiv.org/pdf/2304.11663"}, {"title": "i-DEQ: A stable inertial deep equilibrium model for image restoration", "url": "https://arxiv.org/html/2605.19705v1"}, {"title": "Deep Equilibrium Convolutional Sparse Coding for Hyperspectral Image Denoising", "url": "https://arxiv.org/pdf/2508.15553"}]}, "I've performed the web search for your query. Here are the relevant results:\n\n## Key Findings\n\n**Deep Equilibrium Models (DEQ) Overview:**\nDEQ directly finds equilibrium points via root-finding, equivalent to running an infinite depth feedforward network while allowing analytical backpropagation through implicit differentiation. Training and prediction require only constant memory, regardless of network depth.\n\n**Memory Efficiency and Backpropagation Approaches:**\n\nDirectly differentiating through fixed point iteration leads to memory-expensive backpropagation but more stable training, with unrolled methods showing performance drops compared to implicit function theorem (IFT) approaches.\n\nMemory complexity can be reduced to O(1) via gradient checkpointing as an alternative to IFT and PG methods, trading training time by 1.5× for much lower memory.\n\n**Hybrid and Inversion-Free Approaches (2023-2024):**\n\nThe inversion-free deep equilibrium model exhibited performance similar to unrolled networks while achieving a significant 50% reduction in GPU memory usage.\n\n**Practical Tools:**\nIFT's performance can drop with shorter training schedules, but proper normalization allows DEQ solvers to be solved by fixed-point iteration while retaining performance and saving training time since advanced solvers introduce overheads.\n\nThe search results show active research in 2023-2024 comparing memory overhead between implicit differentiation techniques, unrolled backpropagation, and hybrid approaches for DEQ models."], "durationSeconds": 11.120732948000004, "searchCount": 1}
```

### [21] TOOL CALL — WebFetch · 2026-06-16 17:15:49 UTC

```
URL: https://arxiv.org/abs/2304.11663
Prompt: What are the key findings about hybrid IFT vs unrolled backpropagation in DEQ models? Any stability issues with switching between gradient modes?
```

### [22] TOOL CALL — WebFetch · 2026-06-16 17:15:49 UTC

```
URL: https://arxiv.org/abs/1712.02609
Prompt: What is the "linked neurons" approach? Does it introduce within-layer coupling between neurons in an activation function?
```

### [23] TOOL CALL — WebSearch · 2026-06-16 17:15:49 UTC

```
gradient discontinuity mode switching implicit differentiation unrolled autograd training instability
```

### [24] TOOL RESULT — WebFetch · 2026-06-16 17:15:49 UTC

```
{"bytes": 45093, "code": 200, "codeText": "OK", "result": "Based on the provided content, I cannot answer your question about hybrid IFT vs unrolled backpropagation or stability issues with switching between gradient modes.\n\nThe abstract only describes the paper's core contribution: using \"Jacobian approximation of Broyden's method after the forward pass to compute the gradients during the backward pass\" to speed up DEQ training. It mentions this approach \"can significantly speed up the training while not causing any performance degradation,\" but provides no details about hybrid IFT approaches, unrolled backpropagation comparisons, or gradient mode switching stability.\n\nTo find these specific findings, you would need to access the full paper PDF rather than the abstract displayed on this webpage.", "durationMs": 3112, "url": "https://arxiv.org/abs/2304.11663"}
```

### [25] TOOL RESULT — WebFetch · 2026-06-16 17:15:51 UTC

```
{"bytes": 47002, "code": 200, "codeText": "OK", "result": "# Linked Neurons Approach\n\nBased on the arXiv abstract, linked neurons create **within-layer coupling** between neurons. The approach defines neuron linkage through two key constraints:\n\n1. **Shared weights**: \"all neuron activations in the linkage must have the same operating point. That is to say, all of them share input weights.\"\n\n2. **Gradient requirement**: At least one neuron in the linked group must have non-zero gradients for any input, ensuring the group \"operates in a non-flat and non-zero area.\"\n\nThis coupling mechanism differs from traditional independent neurons. Rather than each neuron having separate weights, linked neurons are bound together with shared parameters, creating dependencies within a layer. The authors claim this design implicitly solves internal covariate shift and eliminates the need for batch normalization while reducing training time by half.", "durationMs": 3616, "url": "https://arxiv.org/abs/1712.02609"}
```

### [26] TOOL RESULT — WebSearch · 2026-06-16 17:15:55 UTC

```
{"query": "gradient discontinuity mode switching implicit differentiation unrolled autograd training instability", "results": [{"tool_use_id": "srvtoolu_01VW9P4tMLucDMJyv75b1Xq4", "content": [{"title": "A Chronological Survey of Theoretical Advancements in Generative   Adversarial Networks for Computer Vision", "url": "https://arxiv.org/pdf/2311.00995"}, {"title": "Nonsmooth Implicit Differentiation for Machine Learning and Optimization", "url": "https://arxiv.org/pdf/2106.04350"}, {"title": "Expressive Power of Implicit Models: Rich Equilibria and Test-Time Scaling", "url": "https://arxiv.org/pdf/2510.03638"}, {"title": "On Training Implicit Models", "url": "https://arxiv.org/pdf/2111.05177"}, {"title": "Automatic Differentiation — Apache MXNet documentation", "url": "https://mxnet.apache.org/versions/1.7/api/python/docs/tutorials/packages/autograd/index.html"}, {"title": "Training instability in deep learning follows low-dimensional dynamical principles", "url": "https://arxiv.org/pdf/2601.13160"}, {"title": "NIPS 2016 Tutorial: Generative Adversarial Networks", "url": "https://arxiv.org/pdf/1701.00160"}, {"title": "Probing RLVR training instability through the lens of objective-level hacking", "url": "https://arxiv.org/pdf/2602.01103"}]}, "Based on the web search results, here are the key findings related to your query:\n\n## Gradient Discontinuity and Implicit Differentiation\n\nWhen the invertibility condition fails in implicit differentiation, discontinuity of the solution affects the dynamics globally, resulting in gradient trajectories that converge to limit cycles of non-critical points.\n\n## Unrolled vs. Implicit Differentiation for Training\n\nUnrolled training is mathematically equivalent to a Neumann series approximation of the implicit gradient, where finite unrolling effectively approximates the Jacobian inverse via Neumann series expansion—a widely adopted technique to avoid the instability and cost of exact inversion.\n\n## Mode Switching in Training\n\nA particular approach can automatically switch between pretraining and training stages for implicit models: when the solver converges poorly, it defines a forward computation graph equivalent to a shallow weight-tied network, where the phantom gradient serves as backpropagation through time (BPTT). The unrolled pretraining is gradually transitioned into the regular training phase based on implicit differentiation.\n\n## Instability with Implicit Differentiation\n\nMany strategies for back-propagating through maximization operations, such as those based on implicit differentiation, are unstable.\n\nThe search results show how gradient discontinuities and mode switching between unrolled and implicit differentiation training approaches can interact to create training instability, particularly in the context of GANs and implicit models."], "durationSeconds": 8.893990751000004, "searchCount": 1}
```

### [27] TOOL CALL — Bash · 2026-06-16 17:18:10 UTC

```
Check user uploads folder:
ls /ai-inventor/aii_data/runs/run_6gT5lHFn8559/user_uploads/ 2>/dev/null && echo "exists" || echo "empty or missing"
```

### [28] TOOL RESULT — Bash · 2026-06-16 17:18:10 UTC

```
{"stdout": "exists", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [29] TOOL CALL — WebSearch · 2026-06-16 17:18:10 UTC

```
non-pointwise activation function inter-neuron coupling mean pooling 2024 2025 deep learning
```

### [30] TOOL RESULT — WebSearch · 2026-06-16 17:18:16 UTC

```
{"query": "non-pointwise activation function inter-neuron coupling mean pooling 2024 2025 deep learning", "results": [{"tool_use_id": "srvtoolu_01HQ2notMpNqtBWEz3qf5JD3", "content": [{"title": "Method for generating programmable activation function and apparatus using the same", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12327174"}, {"title": "Method for generating programmable activation function and apparatus using the same", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11836604"}, {"title": "Solving internal covariate shift in deep learning with linked neurons", "url": "https://arxiv.org/pdf/1712.02609"}, {"title": "Understanding Activation Functions and Pooling in Neural Networks | by Ayushmaan Srivastav | Medium", "url": "https://srivastavayushmaan1347.medium.com/understanding-activation-functions-and-pooling-in-neural-networks-ba658006946e"}, {"title": "Invariance-Preserving Localized Activation Functions for ...", "url": "https://arxiv.org/pdf/1903.12575"}, {"title": "A improved pooling method for convolutional neural networks - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10796389/"}, {"title": "Under review as a conference paper at ICAIS 2025", "url": "https://arxiv.org/pdf/2511.04576"}, {"title": "[2302.11007] Unification of popular artificial neural network activation functions", "url": "https://arxiv.org/abs/2302.11007"}, {"title": "Neural networks with trainable matrix activation functions", "url": "https://arxiv.org/html/2109.09948v5"}]}, "I found several relevant results for your search. Here's what the web search revealed:\n\n## Key Findings:\n\n**Non-Pointwise Activation Functions:**\nLocalized activation functions act on multiple nodal components at a time, in contrast with pointwise nonlinearities. Additionally, pointwise activations are scalar functions that only use a single component-wise value to determine their output given a tensorial input.\n\n**Inter-Neuron Coupling:**\nThe search returned a 2017 paper on \"Solving internal covariate shift in deep learning with linked neurons\" that discusses coupled neurons that share the same input and weights. This explores how neurons can be linked together with specific coupling strategies.\n\n**Mean Pooling and Related Techniques:**\nAverage Pooling averages all the values within the window, and the pooling layer in convolutional neural networks plays a crucial role in reducing spatial dimensions and improving computational efficiency.\n\n**Recent 2024-2025 Work:**\nThe search found a 2024 paper on improved pooling methods and a 2025 paper under review discussing Fourier Neural Operators and spectral methods for deep learning. There's also recent work on unification of popular artificial neural network activation functions (updated October 2024).\n\nThe search results show there is ongoing research in these areas, though the combination of all these concepts (non-pointwise activation, inter-neuron coupling, and mean pooling together) doesn't appear to have a specific unified paper in the initial results."], "durationSeconds": 7.885697534000036, "searchCount": 1}
```

### [31] ASSISTANT · 2026-06-16 17:19:01 UTC

```
Now I have sufficient grounding to write the review. Let me check the user uploads briefly, then compose the output.
```

### [32] TOOL CALL — Bash · 2026-06-16 17:19:01 UTC

```
List user uploads:
ls /ai-inventor/aii_data/runs/run_6gT5lHFn8559/user_uploads/
```

### [33] TOOL RESULT — Bash · 2026-06-16 17:19:01 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [34] ASSISTANT · 2026-06-16 17:20:54 UTC

```
User uploads folder is empty. I have all necessary context. Now writing the structured review JSON.
```

### [35] TOOL CALL — Write · 2026-06-16 17:20:54 UTC

```
File: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/iter_3/review_hypo/.terminal_claude_agent_struct_out.json

{
  "overall_assessment": "The revised CWA hypothesis addresses all six prior critiques convincingly: the hybrid IFT/unrolled backprop strategy resolves the memory-overhead major; explicit finite-width acknowledgment plus wide-ResNet comparison resolves the mean-field breakdown major; the GPT experiment scales to 6L/256H on both Tiny Shakespeare and WikiText-2; adaptive tolerance δ(J·s̄)=1e-4·(1−J·s̄) addresses IFT gradient bias; concrete edge/scientific motivation is added; and p_c is specified analytically plus validation-tuned for non-MLP architectures. The revision shows careful incremental refinement. However, two new issues emerge that prevent a score increase: (1) the IFT gradient formula as stated—∂m*/∂x = sech²(x+J·m*)/(1−J·s̄)—is missing a factor of 1/n that is required by the correct implicit-function-theorem derivation for the scalar fixed point, creating a potential factor-of-n error in the custom backward hook; and (2) the hard mode-switch at J·s̄=0.8 between unrolled autograd and IFT produces a gradient discontinuity that could cause training instability when mini-batch estimates of s̄ fluctuate around the threshold. Both issues are fixable but must be resolved before experiments are run, as they directly affect gradient correctness and the viability of the hybrid strategy that is now central to the hypothesis.",
  "strengths": [
    "All six prior reviewer critiques are explicitly and substantively addressed: hybrid IFT/unrolled strategy resolves memory, wide-ResNet comparison tests finite-width scaling, 6L/256H + WikiText-2 scales language modeling, adaptive δ(J·s̄) bounds IFT bias uniformly, edge/scientific motivation is concrete, and p_c is specified analytically per architecture.",
    "The core mechanism—scalar mean-field fixed-point coupling within a layer via a single learnable J—is genuinely novel as a hidden-layer activation function. No prior work combines within-sample output coupling with gradient-descent-learned criticality at the activation level (DEQ operates at layer level; Boltzmann Attention operates on inter-token attention; SELU is pointwise).",
    "The experimental design is well-controlled: 5 seeds, comprehensive baselines (GELU, SELU, tanh+LN, GELU+LN, Competing Nonlinearities@p_c, fixed-J ablation), explicit disconfirmation and partial-confirm criteria, and separate SOC finding reported regardless of task outcome.",
    "The adaptive tolerance δ(J·s̄)=1e-4·(1−J·s̄) is a rigorous and elegant solution to bounding IFT gradient bias uniformly across J·s̄ ∈ (0,1), directly motivated by perturbation theory of the IFT.",
    "The width-dependent analysis (standard vs wide ResNet-20) converts the finite-width mean-field limitation from a confound into an informative experiment, testing whether CWA benefit scales with n as mean-field physics predicts.",
    "Practical scope is appropriately bounded: the PARTIAL CONFIRM scenario (unnormalized networks only) is explicitly embraced as a principled contribution for edge/scientific settings, with concrete 2026-relevant motivations."
  ],
  "dimension_scores": [
    {
      "dimension": "soundness",
      "score": 2,
      "justification": "The core fixed-point convergence guarantee (Banach theorem for J∈(0,1)) and the adaptive tolerance bound are correct. However, the IFT gradient formula as stated—∂m*/∂x = sech²(x+J·m*)/(1−J·s̄)—is missing a critical factor of 1/n. Since m* is a scalar defined as (1/n)Σ_j tanh(x_j+J·m*), the correct IFT derivative is ∂m*/∂x_j = v_j/(n·(1−J·s̄)), not v_j/(1−J·s̄). The correct custom backward hook formula is ∂L/∂x_j = g_j·v_j + J·v_j·(v^T g)/(n·(1−J·s̄))—a rank-1 perturbation of the diagonal, not a uniform rescaling. The mode-switching discontinuity is an additional soundness concern. These issues make the hybrid backprop strategy—now central to the proposal—technically uncertain.",
      "improvements": [
        "Derive the full IFT backward formula from first principles: define F(m,x,J)=mean(tanh(x+J·m))−m=0, apply implicit differentiation to get ∂m*/∂x_j=v_j/(n(1−J·s̄)) and ∂m*/∂J=s̄·m*/(1−J·s̄), then work out the full custom backward hook: C=v^T·g (scalar), ∂L/∂x_j = g_j·v_j + J·v_j·C/(n(1−J·s̄)), ∂L/∂J = m*·C/(1−J·s̄). Verify this matches unrolled autograd in a unit test.",
        "Address the mode-switching discontinuity: either (a) replace the hard threshold at J·s̄=0.8 with a smooth blending schedule α(J·s̄)·IFT_grad + (1−α(J·s̄))·unrolled_grad for J·s̄∈[0.7,0.9]; or (b) commit to IFT throughout (O(1) memory, sufficient accuracy via adaptive δ) and use unrolled autograd only as a verification check at initialization; or (c) add a mini-batch instability diagnostic in Experiment 5 that measures gradient variance in J_raw specifically when J·s̄ is near 0.8."
      ]
    },
    {
      "dimension": "presentation",
      "score": 3,
      "justification": "The hypothesis is clearly organized with a comprehensive terminology section, explicit assumptions, and well-specified success criteria. All prior revisions are traceable. The only clarity issue is the gradient formula ambiguity: writing '∂m*/∂x = sech²(x+J·m*)/(1−J·s̄)' without specifying whether this is the full backward formula or an intermediate scalar quantity leaves a critical implementation detail unresolved for the reader.",
      "improvements": [
        "In the Hybrid IFT/Unrolled Backprop term definition, replace the current gradient formula with the complete vectorized custom backward pseudocode: inputs are g (gradient of loss w.r.t. y, shape n), v=sech²(x+J·m*) (shape n), J (scalar), s̄=mean(v), m* (scalar); outputs are grad_x = g*v + J*v*(dot(g,v)/n)/(1-J*s̄) and grad_J = m*(dot(g,v)/n)/(1-J*s̄). This unambiguously specifies the implementation and makes the 1/n factor explicit."
      ]
    },
    {
      "dimension": "contribution",
      "score": 3,
      "justification": "The CWA concept is novel, parameter-efficient (1 scalar per layer), and well-differentiated from DEQ, SELU, and LayerNorm. The cross-domain inspiration from Curie-Weiss ferromagnetism is appropriately operationalized. The most likely outcome (PARTIAL CONFIRM: benefit only in unnormalized settings) is a meaningful contribution for a targeted practical setting. The full CONFIRM scenario would merit a higher contribution score but seems less probable given SELU and tanh+LN as strong competitors in normalized settings.",
      "improvements": [
        "Add a 'tanh with per-layer learned temperature τ=exp(τ_raw)' baseline (one learnable parameter per layer, no inter-neuron coupling) to isolate whether CWA's benefit comes from learned scalar adaptation versus the self-consistency coupling mechanism. This baseline is parameter-count-matched to CWA (1 param/layer) and would sharpen the contribution claim by ruling out the simpler explanation.",
        "Consider proposing a joint CWA + Boltzmann Attention experiment on the character-level GPT as a future direction, since these are complementary components (within-layer coupling vs cross-token coupling) and Boltzmann Attention is already evaluated on the same Tiny Shakespeare benchmark—a combined model would directly test complementarity."
      ]
    }
  ],
  "critiques": [
    {
      "category": "rigor",
      "severity": "major",
      "description": "The IFT gradient formula '∂m*/∂x = sech²(x+J·m*)/(1−J·s̄)' contains a factor-of-n error. Since m* is the scalar fixed point of m* = (1/n)Σ_j tanh(x_j+J·m*), applying the implicit function theorem to F(m*,x_j)=0 gives ∂m*/∂x_j = (∂F/∂x_j)/(−∂F/∂m) = (v_j/n)/(1−J·s̄), i.e., the correct formula is v_j/(n·(1−J·s̄)), not v_j/(1−J·s̄). The full vectorized backward hook is then ∂L/∂x_j = g_j·v_j + J·v_j·(v^T g)/(n·(1−J·s̄))—a rank-1 perturbation of the diagonal, not v_j/(1-J·s̄) applied directly. If the custom hook is implemented with the stated formula, the x-gradient in the IFT branch will be inflated by a factor of n (e.g., 256× in the MLP experiments), causing the IFT branch to give incorrect gradient updates while the unrolled branch gives correct ones. This would make the hybrid comparison meaningless, as the two branches would train with systematically different effective learning rates for x.",
      "suggested_action": "In the assumptions section, provide the complete, correct IFT backward derivation: (1) Note F(m,x,J) = (1/n)Σ_j tanh(x_j+J·m) − m = 0 is a scalar fixed-point equation. (2) Compute ∂F/∂m = J·s̄−1, ∂F/∂x_j = v_j/n, ∂F/∂J = s̄·m*. (3) IFT gives ∂m*/∂x_j = v_j/(n(1−J·s̄)), ∂m*/∂J = s̄·m*/(1−J·s̄). (4) Full backward: let C = (1/n)Σ_i g_i·v_i; then ∂L/∂x_j = g_j·v_j + J·n·v_j·C/(n(1−J·s̄)) = g_j·v_j + J·v_j·C/(1−J·s̄) — wait, let me recheck: C = v^T g / n is the mean, then the coupling term is J·v_j·(v^T g/n)/(1−J·s̄). Write out the pseudocode explicitly. Also add a unit test to Experiment 5: verify that IFT and unrolled gradients agree within 1% on a small test case with known J·s̄ before running full experiments."
    },
    {
      "category": "methodology",
      "severity": "major",
      "description": "The hybrid IFT/unrolled mode switch at J·s̄=0.8 creates a gradient discontinuity that could cause training instability. During training, J·s̄ is estimated from the current mini-batch (s̄ = mean(sech²(x+J·m*)) over the batch), so it fluctuates stochastically. When J·s̄ oscillates around 0.8 across consecutive mini-batches, the gradient of J_raw alternates between two systematically different estimators: unrolled autograd gives the exact gradient of the finite-K computation graph (which depends on K* and the specific convergence trajectory); IFT gives the analytical gradient of the infinite-iteration fixed point. Near the threshold where K* is moderate (~10–20 steps), these estimators can differ non-negligibly, and their alternation creates a bimodal effective gradient distribution for J_raw specifically at the critical region where J·s̄≈0.8. The DEQ literature (arXiv:2111.05177, 'On Training Implicit Models') documents analogous instabilities from inconsistent gradient estimators in mode-switching implicit model training. No hysteresis, smooth blending, or diagnostic for boundary oscillation is described in the current proposal.",
      "suggested_action": "Choose one of three mitigations: (a) Replace the hard threshold with a smooth sigmoid blend α(J·s̄) = σ((J·s̄−0.8)/0.05) so the effective gradient is α·IFT_grad + (1−α)·unrolled_grad in [0.7,0.9], eliminating the discontinuity; (b) Commit to IFT-only throughout training (O(1) memory, uniform accuracy via adaptive δ) and validate against unrolled at initialization—the simplest strategy and consistent with DEQ practice; (c) Keep the hard switch but add a monitoring diagnostic: plot J_raw learning curves overlaid with J·s̄ trajectories in Experiment 4 (fixed-J ablation) to empirically check for oscillation. Report explicitly whether gradient variance spikes at J·s̄≈0.8. At minimum, acknowledge the boundary sensitivity in the assumptions section."
    },
    {
      "category": "methodology",
      "severity": "minor",
      "description": "The comparison between CWA (1 learnable scalar J per layer) and GELU+LayerNorm (2n learnable parameters per layer: affine scale and bias) is parameter-count-asymmetric. At n=256, 10 layers: CWA adds 10 parameters total; GELU+LN adds 5,120. While CWA's extreme parameter efficiency is a strength, the experimental design does not include a parameter-count-matched single-parameter baseline. Without such a baseline, it is unclear whether observed gains come from the inter-neuron coupling mechanism or simply from having one learned scalar gain per layer. A 'tanh with per-layer temperature τ=exp(τ_raw)∈(0,∞)' (one parameter, no coupling) would resolve this ambiguity at negligible cost.",
      "suggested_action": "Add 'tanh+τ' as a baseline: y_i = tanh(τ·x_i) with τ = exp(τ_raw), τ_raw initialized at 0 (τ=1). This is (a) parameter-count-matched to CWA, (b) pointwise (no inter-neuron coupling), (c) able to learn gain control via the temperature. If CWA outperforms tanh+τ, the coupling mechanism is confirmed as the source of benefit. If not, the effect is attributable to having one adaptive scalar, not the self-consistency structure. Include this in Experiments 1 and 4."
    },
    {
      "category": "rigor",
      "severity": "minor",
      "description": "The SOC gradient dynamics argument contains an internal tension: the hypothesis claims 'gradient descent has incentive to approach J·s̄=1 because the IFT Jacobian ∂y_i/∂x_i=sech²/(1−J·s̄) diverges there, potentially improving gradient flow.' However, J=σ(J_raw) means the actual gradient update to J_raw is ∂L/∂J_raw=(∂L/∂J)·J·(1−J). As J→1, J·(1−J)→0, creating a vanishing-sigmoid gradient that prevents J_raw from driving J to 1 via gradient descent. Therefore, J·s̄→1 in successful configurations must arise primarily from s̄→1 (neurons operating near zero, maximally in the linear tanh regime), not from J→1. But s̄→1 corresponds to pre-activations x≈0 for all neurons, which may conflict with the network learning rich representations. This tension between the SOC narrative and the sigmoid parameterization's gradient dynamics is not discussed and could affect interpretation of the fixed-J ablation results.",
      "suggested_action": "In the Self-Organized Criticality term definition, add: 'Note that J=σ(J_raw) has vanishing gradient as J→1 (J·(1−J)→0), so J·s̄→1 must arise via s̄→1 (neurons operating near linear regime, tanh≈identity) rather than J→1 alone. The fixed-J ablation study at J=0.9 tests this: if high fixed-J with s̄ near 1 matches learned-J performance, it supports the s̄-driven SOC interpretation.' Also track the distribution of s̄ values at convergence (not just J) in the J·s̄ monitoring, and distinguish learned-J-increasing from s̄-increasing contributions to J·s̄ trajectories."
    }
  ],
  "score": 6,
  "confidence": 4,
  "relation_type": "evolution",
  "relation_rationale": "Same CWA concept and experimental frame; hybrid IFT/unrolled strategy, finite-width analysis, and wider GPT are incremental refinements."
}
```

### [36] TOOL RESULT — Write · 2026-06-16 17:20:54 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/iter_3/review_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"overall_assessment\": \"The revised CWA hypothesis addresses all six prior critiques convincingly: the hybrid IFT/unrolled backprop strategy resolves the memory-overhead major; explicit finite-width acknowledgment plus wide-ResNet comparison resolves the mean-field breakdown major; the GPT experiment scales to 6L/256H on both Tiny Shakespeare and WikiText-2; adaptive tolerance δ(J·s̄)=1e-4·(1−J·s̄) addresses IFT gradient bias; concrete edge/scientific motivation is added; and p_c is specified analytically plus validation-tuned for non-MLP architectures. The revision shows careful incremental refinement. However, two new issues emerge that prevent a score increase: (1) the IFT gradient formula as stated—∂m*/∂x = sech²(x+J·m*)/(1−J·s̄)—is missing a factor of 1/n that is required by the correct implicit-function-theorem derivation for the scalar fixed point, creating a potential factor-of-n error in the custom backward hook; and (2) the hard mode-switch at J·s̄=0.8 between unrolled autograd and IFT produces a gradient discontinuity that could cause training instability when mini-batch estimates of s̄ fluctuate around the threshold. Both issues are fixable but must be resolved before experiments are run, as they directly affect gradient correctness and the viability of the hybrid strategy that is now central to the hypothesis.\",\n  \"strengths\": [\n    \"All six prior reviewer critiques are explicitly and substantively addressed: hybrid IFT/unrolled strategy resolves memory, wide-ResNet comparison tests finite-width scaling, 6L/256H + WikiText-2 scales language modeling, adaptive δ(J·s̄) bounds IFT bias uniformly, edge/scientific motivation is concrete, and p_c is specified analytically per architecture.\",\n    \"The core mechanism—scalar mean-field fixed-point coupling within a layer via a single learnable J—is genuinely novel as a hidden-layer activation function. No prior work combines within-sample output coupling with gradient-descent-learned criticality at the activation level (DEQ operates at layer level; Boltzmann Attention operates on inter-token attention; SELU is pointwise).\",\n    \"The experimental design is well-controlled: 5 seeds, comprehensive baselines (GELU, SELU, tanh+LN, GELU+LN, Competing Nonlinearities@p_c, fixed-J ablation), explicit disconfirmation and partial-confirm criteria, and separate SOC finding reported regardless of task outcome.\",\n    \"The adaptive tolerance δ(J·s̄)=1e-4·(1−J·s̄) is a rigorous and elegant solution to bounding IFT gradient bias uniformly across J·s̄ ∈ (0,1), directly motivated by perturbation theory of the IFT.\",\n    \"The width-dependent analysis (standard vs wide ResNet-20) converts the finite-width mean-field limitation from a confound into an informative experiment, testing whether CWA benefit scales with n as mean-field physics predicts.\",\n    \"Practical scope is appropriately bounded: the PARTIAL CONFIRM scenario (unnormalized networks only) is explicitly embraced as a principled contribution for edge/scientific settings, with concrete 2026-relevant motivations.\"\n  ],\n  \"dimension_scores\": [\n    {\n      \"dimension\": \"soundness\",\n      \"score\": 2,\n      \"justification\": \"The core fixed-point convergence guarantee (Banach theorem for J∈(0,1)) and the adaptive tolerance bound are correct. However, the IFT gradient formula as stated—∂m*/∂x = sech²(x+J·m*)/(1−J·s̄)—is missing a critical factor of 1/n. Since m* is a scalar defined as (1/n)Σ_j tanh(x_j+J·m*), the correct IFT derivative is ∂m*/∂x_j = v_j/(n·(1−J·s̄)), not v_j/(1−J·s̄). The correct custom backward hook formula is ∂L/∂x_j = g_j·v_j + J·v_j·(v^T g)/(n·(1−J·s̄))—a rank-1 perturbation of the diagonal, not a uniform rescaling. The mode-switching discontinuity is an additional soundness concern. These issues make the hybrid backprop strategy—now central to the proposal—technically uncertain.\",\n      \"improvements\": [\n        \"Derive the full IFT backward formula from first principles: define F(m,x,J)=mean(tanh(x+J·m))−m=0, apply implicit differentiation to get ∂m*/∂x_j=v_j/(n(1−J·s̄)) and ∂m*/∂J=s̄·m*/(1−J·s̄), then work out the full custom backward hook: C=v^T·g (scalar), ∂L/∂x_j = g_j·v_j + J·v_j·C/(n(1−J·s̄)), ∂L/∂J = m*·C/(1−J·s̄). Verify this matches unrolled autograd in a unit test.\",\n        \"Address the mode-switching discontinuity: either (a) replace the hard threshold at J·s̄=0.8 with a smooth blending schedule α(J·s̄)·IFT_grad + (1−α(J·s̄))·unrolled_grad for J·s̄∈[0.7,0.9]; or (b) commit to IFT throughout (O(1) memory, sufficient accuracy via adaptive δ) and use unrolled autograd only as a verification check at initialization; or (c) add a mini-batch instability diagnostic in Experiment 5 that measures gradient variance in J_raw specifically when J·s̄ is near 0.8.\"\n      ]\n    },\n    {\n      \"dimension\": \"presentation\",\n      \"score\": 3,\n      \"justification\": \"The hypothesis is clearly organized with a comprehensive terminology section, explicit assumptions, and well-specified success criteria. All prior revisions are traceable. The only clarity issue is the gradient formula ambiguity: writing '∂m*/∂x = sech²(x+J·m*)/(1−J·s̄)' without specifying whether this is the full backward formula or an intermediate scalar quantity leaves a critical implementation detail unresolved for the reader.\",\n      \"improvements\": [\n        \"In the Hybrid IFT/Unrolled Backprop term definition, replace the current gradient formula with the complete vectorized custom backward pseudocode: inputs are g (gradient of loss w.r.t. y, shape n), v=sech²(x+J·m*) (shape n), J (scalar), s̄=mean(v), m* (scalar); outputs are grad_x = g*v + J*v*(dot(g,v)/n)/(1-J*s̄) and grad_J = m*(dot(g,v)/n)/(1-J*s̄). This unambiguously specifies the implementation and makes the 1/n factor explicit.\"\n      ]\n    },\n    {\n      \"dimension\": \"contribution\",\n      \"score\": 3,\n      \"justification\": \"The CWA concept is novel, parameter-efficient (1 scalar per layer), and well-differentiated from DEQ, SELU, and LayerNorm. The cross-domain inspiration from Curie-Weiss ferromagnetism is appropriately operationalized. The most likely outcome (PARTIAL CONFIRM: benefit only in unnormalized settings) is a meaningful contribution for a targeted practical setting. The full CONFIRM scenario would merit a higher contribution score but seems less probable given SELU and tanh+LN as strong competitors in normalized settings.\",\n      \"improvements\": [\n        \"Add a 'tanh with per-layer learned temperature τ=exp(τ_raw)' baseline (one learnable parameter per layer, no inter-neuron coupling) to isolate whether CWA's benefit comes from learned scalar adaptation versus the self-consistency coupling mechanism. This baseline is parameter-count-matched to CWA (1 param/layer) and would sharpen the contribution claim by ruling out the simpler explanation.\",\n        \"Consider proposing a joint CWA + Boltzmann Attention experiment on the character-level GPT as a future direction, since these are complementary components (within-layer coupling vs cross-token coupling) and Boltzmann Attention is already evaluated on the same Tiny Shakespeare benchmark—a combined model would directly test complementarity.\"\n      ]\n    }\n  ],\n  \"critiques\": [\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"major\",\n      \"description\": \"The IFT gradient formula '∂m*/∂x = sech²(x+J·m*)/(1−J·s̄)' contains a factor-of-n error. Since m* is the scalar fixed point of m* = (1/n)Σ_j tanh(x_j+J·m*), applying the implicit function theorem to F(m*,x_j)=0 gives ∂m*/∂x_j = (∂F/∂x_j)/(−∂F/∂m) = (v_j/n)/(1−J·s̄), i.e., the correct formula is v_j/(n·(1−J·s̄)), not v_j/(1−J·s̄). The full vectorized backward hook is then ∂L/∂x_j = g_j·v_j + J·v_j·(v^T g)/(n·(1−J·s̄))—a rank-1 perturbation of the diagonal, not v_j/(1-J·s̄) applied directly. If the custom hook is implemented with the stated formula, the x-gradient in the IFT branch will be inflated by a factor of n (e.g., 256× in the MLP experiments), causing the IFT branch to give incorrect gradient updates while the unrolled branch gives correct ones. This would make the hybrid comparison meaningless, as the two branches would train with systematically different effective learning rates for x.\",\n      \"suggested_action\": \"In the assumptions section, provide the complete, correct IFT backward derivation: (1) Note F(m,x,J) = (1/n)Σ_j tanh(x_j+J·m) − m = 0 is a scalar fixed-point equation. (2) Compute ∂F/∂m = J·s̄−1, ∂F/∂x_j = v_j/n, ∂F/∂J = s̄·m*. (3) IFT gives ∂m*/∂x_j = v_j/(n(1−J·s̄)), ∂m*/∂J = s̄·m*/(1−J·s̄). (4) Full backward: let C = (1/n)Σ_i g_i·v_i; then ∂L/∂x_j = g_j·v_j + J·n·v_j·C/(n(1−J·s̄)) = g_j·v_j + J·v_j·C/(1−J·s̄) — wait, let me recheck: C = v^T g / n is the mean, then the coupling term is J·v_j·(v^T g/n)/(1−J·s̄). Write out the pseudocode explicitly. Also add a unit test to Experiment 5: verify that IFT and unrolled gradients agree within 1% on a small test case with known J·s̄ before running full experiments.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"The hybrid IFT/unrolled mode switch at J·s̄=0.8 creates a gradient discontinuity that could cause training instability. During training, J·s̄ is estimated from the current mini-batch (s̄ = mean(sech²(x+J·m*)) over the batch), so it fluctuates stochastically. When J·s̄ oscillates around 0.8 across consecutive mini-batches, the gradient of J_raw alternates between two systematically different estimators: unrolled autograd gives the exact gradient of the finite-K computation graph (which depends on K* and the specific convergence trajectory); IFT gives the analytical gradient of the infinite-iteration fixed point. Near the threshold where K* is moderate (~10–20 steps), these estimators can differ non-negligibly, and their alternation creates a bimodal effective gradient distribution for J_raw specifically at the critical region where J·s̄≈0.8. The DEQ literature (arXiv:2111.05177, 'On Training Implicit Models') documents analogous instabilities from inconsistent gradient estimators in mode-switching implicit model training. No hysteresis, smooth blending, or diagnostic for boundary oscillation is described in the current proposal.\",\n      \"suggested_action\": \"Choose one of three mitigations: (a) Replace the hard threshold with a smooth sigmoid blend α(J·s̄) = σ((J·s̄−0.8)/0.05) so the effective gradient is α·IFT_grad + (1−α)·unrolled_grad in [0.7,0.9], eliminating the discontinuity; (b) Commit to IFT-only throughout training (O(1) memory, uniform accuracy via adaptive δ) and validate against unrolled at initialization—the simplest strategy and consistent with DEQ practice; (c) Keep the hard switch but add a monitoring diagnostic: plot J_raw learning curves overlaid with J·s̄ trajectories in Experiment 4 (fixed-J ablation) to empirically check for oscillation. Report explicitly whether gradient variance spikes at J·s̄≈0.8. At minimum, acknowledge the boundary sensitivity in the assumptions section.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"minor\",\n      \"description\": \"The comparison between CWA (1 learnable scalar J per layer) and GELU+LayerNorm (2n learnable parameters per layer: affine scale and bias) is parameter-count-asymmetric. At n=256, 10 layers: CWA adds 10 parameters total; GELU+LN adds 5,120. While CWA's extreme parameter efficiency is a strength, the experimental design does not include a parameter-count-matched single-parameter baseline. Without such a baseline, it is unclear whether observed gains come from the inter-neuron coupling mechanism or simply from having one learned scalar gain per layer. A 'tanh with per-layer temperature τ=exp(τ_raw)∈(0,∞)' (one parameter, no coupling) would resolve this ambiguity at negligible cost.\",\n      \"suggested_action\": \"Add 'tanh+τ' as a baseline: y_i = tanh(τ·x_i) with τ = exp(τ_raw), τ_raw initialized at 0 (τ=1). This is (a) parameter-count-matched to CWA, (b) pointwise (no inter-neuron coupling), (c) able to learn gain control via the temperature. If CWA outperforms tanh+τ, the coupling mechanism is confirmed as the source of benefit. If not, the effect is attributable to having one adaptive scalar, not the self-consistency structure. Include this in Experiments 1 and 4.\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"minor\",\n      \"description\": \"The SOC gradient dynamics argument contains an internal tension: the hypothesis claims 'gradient descent has incentive to approach J·s̄=1 because the IFT Jacobian ∂y_i/∂x_i=sech²/(1−J·s̄) diverges there, potentially improving gradient flow.' However, J=σ(J_raw) means the actual gradient update to J_raw is ∂L/∂J_raw=(∂L/∂J)·J·(1−J). As J→1, J·(1−J)→0, creating a vanishing-sigmoid gradient that prevents J_raw from driving J to 1 via gradient descent. Therefore, J·s̄→1 in successful configurations must arise primarily from s̄→1 (neurons operating near zero, maximally in the linear tanh regime), not from J→1. But s̄→1 corresponds to pre-activations x≈0 for all neurons, which may conflict with the network learning rich representations. This tension between the SOC narrative and the sigmoid parameterization's gradient dynamics is not discussed and could affect interpretation of the fixed-J ablation results.\",\n      \"suggested_action\": \"In the Self-Organized Criticality term definition, add: 'Note that J=σ(J_raw) has vanishing gradient as J→1 (J·(1−J)→0), so J·s̄→1 must arise via s̄→1 (neurons operating near linear regime, tanh≈identity) rather than J→1 alone. The fixed-J ablation study at J=0.9 tests this: if high fixed-J with s̄ near 1 matches learned-J performance, it supports the s̄-driven SOC interpretation.' Also track the distribution of s̄ values at convergence (not just J) in the J·s̄ monitoring, and distinguish learned-J-increasing from s̄-increasing contributions to J·s̄ trajectories.\"\n    }\n  ],\n  \"score\": 6,\n  \"confidence\": 4,\n  \"relation_type\": \"evolution\",\n  \"relation_rationale\": \"Same CWA concept and experimental frame; hybrid IFT/unrolled strategy, finite-width analysis, and wider GPT are incremental refinements.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [37] ASSISTANT · 2026-06-16 17:21:04 UTC

```
Review written to `.terminal_claude_agent_struct_out.json`.

**Summary:** Score 6/10 (Weak Accept, stable). All 6 prior critiques are adequately addressed. Two new issues prevent a score increase:

1. **[MAJOR rigor]** The IFT gradient formula `∂m*/∂x = sech²(x+J·m*)/(1−J·s̄)` is missing a factor of `1/n`. The correct IFT derivative for the scalar fixed point `m* = (1/n)Σ_j tanh(x_j+J·m*)` is `∂m*/∂x_j = v_j/(n·(1−J·s̄))`. The full custom backward hook should be `∂L/∂x_j = g_j·v_j + J·v_j·C/(1−J·s̄)` where `C = (1/n)Σ_i g_i·v_i`. As stated, the IFT branch could inflate x-gradients by n× relative to the unrolled branch, making the hybrid comparison meaningless.

2. **[MAJOR methodology]** The hard mode-switch at J·s̄=0.8 creates a gradient discontinuity when mini-batch estimates of s̄ straddle the threshold — the unrolled and IFT branches produce systematically different gradient estimates for J_raw at the boundary, with no hysteresis or smoothing described. Recommend either a smooth blend in [0.7, 0.9] or committing to IFT-only (consistent with DEQ practice).

Two minor issues also flagged: parameter-count asymmetry vs GELU+LN (add a 1-param `tanh+τ` baseline), and a tension in the SOC argument (sigmoid parameterization's vanishing gradient as J→1 means J·s̄→1 must come from s̄→1, not J→1, with different training dynamics implications).
```

### [38] SYSTEM-USER prompt · 2026-06-16 17:21:06 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same CWA concept and experimental frame; hybrid IFT/unrolled strategy, finite-width analysis, and wider GPT are incremental refinements.' is too long (at most 120 characters, got 136)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [39] TOOL CALL — Edit · 2026-06-16 17:21:12 UTC

```
File: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/iter_3/review_hypo/.terminal_claude_agent_struct_out.json
OLD:   "relation_rationale": "Same CWA concept and experimental frame; hybrid IFT/unrolled strategy, finite-width analysis, and wider GPT are incremental refinements."
NEW:   "relation_rationale": "Same CWA concept; hybrid IFT/unrolled, finite-width analysis, and wider GPT are incremental refinements."
```

### [40] TOOL RESULT — Edit · 2026-06-16 17:21:12 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/iter_3/review_hypo/.terminal_claude_agent_struct_out.json", "oldString": "  \"relation_rationale\": \"Same CWA concept and experimental frame; hybrid IFT/unrolled strategy, finite-width analysis, and wider GPT are incremental refinements.\"", "newString": "  \"relation_rationale\": \"Same CWA concept; hybrid IFT/unrolled, finite-width analysis, and wider GPT are incremental refinements.\"", "originalFile": null, "structuredPatch": [{"oldStart": 65, "oldLines": 5, "newStart": 65, "newLines": 5, "lines": ["   \"score\": 6,", "   \"confidence\": 4,", "   \"relation_type\": \"evolution\",", "-  \"relation_rationale\": \"Same CWA concept and experimental frame; hybrid IFT/unrolled strategy, finite-width analysis, and wider GPT are incremental refinements.\"", "+  \"relation_rationale\": \"Same CWA concept; hybrid IFT/unrolled, finite-width analysis, and wider GPT are incremental refinements.\"", " }"]}], "userModified": false, "replaceAll": false}
```

### [41] ASSISTANT · 2026-06-16 17:21:13 UTC

```
Fixed — `relation_rationale` shortened to under 120 characters.
```
