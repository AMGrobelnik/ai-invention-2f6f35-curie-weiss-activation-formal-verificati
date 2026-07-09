# review_paper — test_idea

> Phase: `invention_loop` · round 1 · `review_paper`
> Run: `run_6gT5lHFn8559` — Novel Activation Function
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 19:06:44 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An adversarial paper reviewer (Step 3.5: REVIEW_PAPER in the invention loop)

You received a paper draft written by a DIFFERENT model. Review it with fresh eyes.
Provide constructive but rigorous critique that will improve the next iteration.

Specific critiques → better paper. Vague praise → no improvement.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the paper under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of the paper.

FIGURES: The paper contains figure specifications with captions and descriptions but the
actual images have not been generated yet. Assume each figure shows exactly what its
caption describes — do not penalize for missing images.

ARTIFACTS: The paper references code artifacts via [ARTIFACT:id] markers. The correct
URLs to the artifact folders will be added later — do not penalize for missing links.

GOAL: Your review feeds directly back to the paper author. The objective is to maximize
the overall review score in subsequent rounds. Every piece of feedback you give should
be written with this goal in mind — prioritize the critiques and suggestions that would
produce the largest score improvement if addressed. Don't waste the author's iteration
budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the tasks or methods new? Novel combination of known techniques?
    Clear differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the submission technically sound? Are claims well supported by theoretical
    analysis or experimental results? Is the methodology appropriate? Is this a complete
    piece of work? Are the authors honest about limitations?
(c) Clarity: Is the submission clearly written and well organized? Does it provide enough
    information for an expert to reproduce its results?
(d) Significance: Are the results important? Would others build on them? Does it address
    a meaningful problem better than prior work? Does it advance the state of the art?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims, experimental and research methodology,
and whether central claims are adequately supported with evidence:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas and execution, value to the broader research community:
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
- Distinguish major issues (would cause rejection) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Check if figures are well-specified and would effectively communicate the results
- Verify that claims are supported by the artifacts described

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

<paper>
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
</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

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
</supplementary_materials>



<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
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
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
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
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-16 19:06:44 UTC

```
Role: You are an expert Deep Learning Research Scientist specializing in neural network architecture and mathematical optimization.Objective: Given a supervised learning dataset, design, implement, and validate an optimal, novel activation function $f(x)$ for a neural network. Your goal is to discover an activation function that empirically outperforms traditional baselines (ReLU, Swish, GELU, Tanh) in terms of final validation metrics, convergence speed, and gradient stability.Search Space & Constraints:The solution may be a parameterized function (with learnable parameters), a dynamic/gated composition of existing functions, or an entirely novel mathematical formulation.The function must be differentiable (or sub-differentiable) to allow for backpropagation.Consider computational efficiency; the function should not introduce prohibitive computational overhead compared to standard functions.
```
