# gen_paper_text — test_idea

> Phase: `invention_loop` · round 3 · `gen_paper_text`
> Run: `run_6gT5lHFn8559` — Novel Activation Function
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 22:05:23 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A research paper writer (Step 3.4: GEN_PAPER_TEXT in the invention loop)

You received the hypothesis, all artifacts, the previous paper draft (if any), and reviewer feedback.
Write a complete paper draft with figure placeholders.

Publication-quality paper → strong contribution. Weak paper → wasted iteration.
</your_role>
</ai_inventor_context>

<research_methodology>
Write like a researcher drafting a paper, not a chatbot summarizing bullet points.

- Structure as a paper would: research question → methodology → results → analysis → limitations. Not a list of "we did X, then Y."
- Ground every claim in specific artifacts and specific numbers. "Results show improvement" is empty — state effect sizes, baselines, and conditions.
- Be honest about what worked, what didn't, and why. Don't spin failures as "future work."
- The paper's headline contribution should be a positive or surprising finding. Negative results are valuable context but should not be the primary narrative — lead with what works.
- Address reviewer feedback from previous iterations explicitly — show you've thought about each critique.
</research_methodology>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

# Introduction

Standard activation functions in neural networks — ReLU, GELU [10], Swish [11], tanh — are *pointwise*: each neuron's output y_i depends only on its own pre-activation x_i, with no information about the outputs of other neurons in the same layer. This architectural independence is computationally convenient but requires external normalization (BatchNorm [8], LayerNorm [9]) or precise initialization [3, 4] to maintain gradient signal across depth. In three practically important settings this requirement is burdensome: (a) on-device inference, where normalization's running statistics incur memory and quantization distortion; (b) physics-informed neural networks and neural operators, where normalization disrupts physical conservation laws [5]; and (c) fast-inference transformer variants that eliminate LayerNorm to reduce memory bandwidth.

The *edge of chaos* in deep networks — the boundary where the layer Jacobian's singular values are near unity — correlates with fast training and good generalization [3, 4]. Existing approaches achieve criticality only at initialization via weight variance tuning [3, 4] or static random activation mixtures [5]; neither provides a per-layer mechanism that adapts during training. The Curie-Weiss model of ferromagnetism suggests a natural structure for such adaptive criticality: each spin aligns with the mean field of all other spins, m = tanh(β(h + J·m)), with a critical point at βJ = 1 where magnetic susceptibility diverges. Transferring this to neural activations, the equation y_i = tanh(x_i + J·mean_neurons(y)) couples all neurons in a layer through a learnable scalar J.

This paper makes the following contributions, each grounded in empirical evidence from four experiments and four formally verified theorems:

- **Formally verified mathematical foundation** (Section 3): Four Lean 4 theorems without *sorry* — fixed-point existence, IFT gradient correctness, adaptive bias bound matching the code's tolerance δ = 1e-4·(1−J·s̄), and a new warm-start-T gradient bias theorem bounding error at J^T·ε [ARTIFACT:art_a_2QuPkEZxKS].
- **Empirically validated IFT memory efficiency** (Section 4.1): The near-critical IFT branch triggers at J·s̄ = 0.955 under controlled conditions, achieving 1.05× GELU memory overhead within the 2× success criterion [ARTIFACT:art_V46hELP73T_t].
- **Gradient balance at shallow depth, collapse at depth 20** (Section 4.2): CWA achieves 0.30 and 0.35 gradient norm ratios at depths 6 and 10 vs. GELU's 0.71 and 0.73 (3 seeds, Welch t-test p ≤ 0.003), but catastrophically collapses at depth 20 (ratio 11.02) while SELU remains stable (1.47) [ARTIFACT:art_v26XKv4_F1RM].
- **Fixed-J mechanistic diagnosis** (Section 4.3): Any fixed J ∈ {0.1, 0.3, 0.5, 0.7, 0.9} achieves gradient balance at depth 10, but the coupling term's correlated activation bias prevents accuracy gains over GELU [ARTIFACT:art_v26XKv4_F1RM].
- **SOC failure mechanism identified** (Section 5): J·s̄ remains subcritical because sech²(x+J·m*) saturates at realistic activation magnitudes; even with 100× dedicated J learning rate, J·s̄ reaches only ~0.30 despite J → 0.85 [ARTIFACT:art_V46hELP73T_t].

[FIGURE:fig1]

# Background and Related Work

**Edge-of-chaos criticality.** Poole et al. [3] showed that infinite-depth networks initialized at the boundary between order (vanishing gradients) and chaos (exploding gradients) exhibit depth-independent gradient propagation. Yang and Schoenholz [4] extended this to residual networks. Both methods achieve criticality only at initialization; the property drifts during training. CWA aims to track criticality adaptively through a per-layer learnable scalar, but the present experiments reveal that the coupling J cannot reach the critical regime under standard training because of sech² saturation at typical activation magnitudes.

**Self-normalizing networks.** SELU [2] achieves self-normalization without external normalization by designing the activation's distributional fixed point to have mean 0 and variance 1. SELU is strictly pointwise. CWA couples all neurons within a layer via the scalar mean m*, making it categorically distinct. Empirically, SELU achieves better accuracy and gradient stability at depth 20 than CWA (acc 0.535 vs. 0.141, grad_ratio 1.47 vs. 11.02), suggesting distributional fixed-point design is more effective for deep unnormalized networks than mean-field output coupling.

**Static activation mixtures.** Lesser and Chowdhury [5] achieve edge-of-chaos criticality by drawing each neuron's activation independently from a tanh/Swish mixture at analytically derived critical mixing fraction p_c = 32/35 ≈ 0.914 (K₀→0 limit). This requires no learnable parameter and no inter-neuron coupling. CWA provides a learnable J but fails to translate gradient balance into accuracy gains (Section 4), leaving static critical mixtures as a competitive baseline.

**Deep Equilibrium Models.** Bai et al. [1] showed that any infinite-depth weight-tied network can be computed via root-finding at its equilibrium point, with IFT providing O(1) activation memory (88% reduction on WikiText-103). The CWA IFT backward (Section 3.2) is directly inspired by DEQ but reduces to a closed-form scalar formula — because CWA's fixed point m* ∈ ℝ (scalar) rather than ℝⁿ (vector) — eliminating the need for iterative backward solvers [ARTIFACT:art_Lj-xi6yJR_yy].

**Mean-field theory of activations.** Milletarì et al. [7] provided post-hoc physical interpretations of standard pointwise activations as solutions to energy-based models. CWA instead proposes a new activation defined by the Curie-Weiss self-consistency equation with a learnable coupling J, introducing within-layer coupling absent from all prior derived activations.

**Boltzmann Attention.** Kim and Park [6] introduced learnable Ising couplings J_{jk} between sequence positions in the attention operator of transformers. Boltzmann Attention and CWA are complementary: the former operates in the sequence dimension of the attention operator; the latter operates in the hidden dimension of the activation function.

# Method: Curie-Weiss Activation

## Definition and Forward Pass

The Curie-Weiss Activation (CWA) for a layer with pre-activations x ∈ ℝⁿ is defined as the unique fixed point of the scalar mean-field self-consistency equation:

  m* = mean_neurons(tanh(x + J·m*))

where J = sigmoid(J_raw) ∈ (0, 1) is a per-layer learnable scalar and mean_neurons(y) = (1/n)Σᵢ yᵢ is the within-sample neuron mean (not the batch mean). The layer output is y_i = tanh(xᵢ + J·m*) for each neuron i. The effective coupling J·s̄ = J·mean_neurons(sech²(x+J·m*)) quantifies simultaneously: (i) the per-step convergence rate ρ of the fixed-point iteration; (ii) the spectral norm of the layer's input-output Jacobian; and (iii) proximity to the critical point J·s̄ = 1.

The fixed-point iteration m_{t+1} = mean_neurons(tanh(x + J·m_t)) is initialized at m₀ = 0 and terminated when |m_{t+1} − m_t| < δ(J·s̄) = 1e-4·(1 − J·s̄), with K_max = 50. The sigmoid parameterization J = sigmoid(J_raw) hard-constrains J below the ferromagnetic phase transition at J = 1, ensuring global convergence for all inputs.

## Hybrid IFT/Unrolled Backpropagation

CWA uses a hybrid backward strategy switching based on the forward-pass effective coupling J·s̄. When J·s̄ < 0.8, a warm-start approximation is used: K forward iterations run without gradient tracking to find m*, followed by T = 3 tracked iterations from the detached m*, with gradient bias bounded by J^T·ε (Theorem 4, Section 3). When J·s̄ ≥ 0.8, a custom `torch.autograd.Function` applies the closed-form IFT gradient:

- ∂L/∂xᵢ = sᵢ·[gᵢ + J·(Σₖ gₖ·sₖ) / (n·(1 − J·s̄))]
- ∂L/∂J = Σᵢ gᵢ·sᵢ·m* / (1 − J·s̄)

where sᵢ = sech²(xᵢ + J·m*) and gᵢ = ∂L/∂yᵢ. The IFT path requires only O(n) activation memory — storing the converged scalar m* — analogously to DEQ's memory reduction [1]. The adaptive tolerance δ(J·s̄) = 1e-4·(1 − J·s̄) ensures gradient bias from fixed-point approximation is bounded at O(1e-4·(1−J·s̄)/(1−J)) (Theorem 3 below).

## Formal Verification in Lean 4

Four properties of CWA are formally verified in Lean 4 + Mathlib v4.14.0 without *sorry* [ARTIFACT:art_a_2QuPkEZxKS]. The standard Mathlib `DerivHyp` module is broken in v4.14.0; all HasDerivAt results for sinh, cosh, tanh are derived from first principles via `HasDerivAt.inv` and `HasDerivAt.mul`.

**Theorem 1 (Banach Convergence).** For any x ∈ ℝ and J ∈ (0,1), there exists a unique m* satisfying tanh(x + J·m*) = m*. *Proof chain:* tanh is 1-Lipschitz (from `lipschitzWith_of_nnnorm_deriv_le`); composition with the J-Lipschitz affine map gives F J-Lipschitz; `ContractingWith.fixedPoint_isFixedPt` + `fixedPoint_unique` give existence and uniqueness.

**Theorem 2 (IFT Gradient).** With s̄ = 1 − tanh²(x + J·m*) and grad = s̄/(1 − J·s̄), the equation s̄·(1 + J·grad) = grad holds. *Proof:* `field_simp` after establishing 1 − J·s̄ > 0.

**Theorem 3 (Revised Bias Bound).** The code uses tolerance δ = 1e-4·(1−J·s̄), which is looser than the iter-1 tolerance 1e-4·(1−J) since J·s̄ ≤ J. The revised theorem: if |F(m_approx) − m_approx| ≤ 1e-4·(1−J·s̄), then |m_approx − m*| ≤ 1e-4·(1−J·s̄)/(1−J) ≤ 1e-4/(1−J). For J ≈ 0.5, this bound is 2e-4. *Proof:* contraction residual bound + `div_le_div_of_nonneg_right`.

**Theorem 4 (Warm-Start-T Bias).** For the warm-start-T backward (T tracked iterations from detached m̂ with |m̂ − m*| ≤ ε), |F^[T](m̂) − m*| ≤ J^T·ε. Concrete corollary: T=3, J ≤ 0.5 gives ≤ (1/8)·ε. *Proof:* induction on T via `Function.iterate_succ_apply'` + `dist_le_mul` + `mul_le_mul_of_nonneg_left`. For the experimental regime J·s̄ ≈ 0.35 (J ≈ 0.5, J^3 ≈ 0.125), the warm-start bias is ≈12.5% relative to the initial approximation error, which is bounded by the forward-pass convergence tolerance.

# Experiments

All experiments use PyTorch on NVIDIA GPUs. CWA uses K_max = 50 (corrected from the iter-1 K_max = 5 that caused fixed-point saturation), adaptive tolerance δ = 1e-4·(1−J·s̄), and warm-start T=3 unrolled backward. Total experiment cost is $0 (no LLM API calls). Statistical tests use paired Student's t-tests and Welch's t-tests as appropriate.

## Experiment 1: IFT Branch Validation

We confirm the IFT backward branch empirically via a synthetic benchmark initializing J_raw = +4.0 (J ≈ 0.982) with two x-scale conditions [ARTIFACT:art_V46hELP73T_t].

With **small-magnitude inputs** (x_scale = 0.1), J·s̄ = 0.955 > 0.8 threshold, causing the IFT branch to trigger in all 50/50 runs. Peak GPU memory is 1.046× GELU (32.0 MB IFT vs. 30.6 MB GELU), well within the 2× criterion. Gradient numerical check confirms no NaN/inf outputs.

With **standard-magnitude inputs**, J·s̄ drops to 0.591 because sech²(x+J·m*) saturates toward zero at large |x|, reducing the effective coupling even at J ≈ 0.982. This saturation effect is a fundamental constraint: the IFT branch requires not only large J but also small enough pre-activations that sech² remains non-negligible.

[FIGURE:fig4]

## Experiment 2: Gradient Stability in Unnormalized Deep MLPs

We train MLPs at depths {6, 10, 20} with 256 hidden units on CIFAR-10 for 25 epochs with 3 seeds and no normalization, comparing CWA against ReLU, GELU, SELU, CompetingNonlinearities (tanh+Swish@p_c=0.83), and GELU+LayerNorm. The gradient norm ratio |log‖∇W₁‖/log‖∇W_L‖| measures gradient balance: a ratio near 1.0 indicates stable propagation [ARTIFACT:art_v26XKv4_F1RM].

[FIGURE:fig2]

**Gradient ratio results.** At depths 6 and 10, CWA achieves lower gradient norm ratios than GELU (0.305±0.026 vs. 0.712±0.115 at depth 6; 0.347±0.098 vs. 0.735±0.145 at depth 10, both Welch t-test significant at p ≤ 0.05). However, SELU achieves ratios closest to 1.0 at all depths (1.089±0.039 at depth 6; 1.129±0.082 at depth 10), reflecting its design as a distributional fixed-point activatoin. At depth 20, CWA catastrophically collapses (11.02±2.17), performing far worse than GELU (2.76±1.66) and SELU (1.47±0.97). The mean-field coupling, which compresses the gradient ratio at shallow depths, amplifies instability at depth 20 as the correlated shift J·m* compounds across layers.

**Accuracy results.** Despite lower gradient ratios at depths 6-10, CWA accuracy is significantly below GELU at both depths (0.483±0.002 vs. 0.531±0.002 at depth 6, p=0.003; 0.472±0.003 vs. 0.511±0.001 at depth 10, p=0.003). SELU achieves the best accuracy at depth 20 (0.535±0.001) by a wide margin, while CWA obtains 0.141±0.007. These results confirm that CWA's gradient-ratio reduction does not translate to improved task accuracy.

**CWA diagnostics.** J·s̄ follows a consistent declining trajectory across epochs (0.346→0.286 over 25 epochs at depth 6; 0.400→0.353 at depth 10), with J converging to values in [0.515, 0.518] — less than 0.02 from initialization. The iteration count K_mean ≈ 7.4 per step (K_max=50, fraction_converged=1.0), confirming that the fixed-point is now correctly computed (cf. iter-1's K_max=5 saturation which only achieved ~1.87% accuracy in m*).

## Experiment 3: Fixed-J Ablation

To test whether any fixed coupling strength provides gradient stability benefits independent of J-learning dynamics, we train 10-layer unnormalized MLPs on CIFAR-10 with J frozen at {0.1, 0.3, 0.5, 0.7, 0.9} across 3 seeds, compared to learned J and to GELU [ARTIFACT:art_v26XKv4_F1RM].

[FIGURE:fig3]

**Gradient balance is universal.** All fixed-J variants achieve gradient norm ratios below 0.42 (J=0.1: 0.245±0.012; J=0.7: 0.364±0.064; J=0.9: 0.410±0.081), all below the GELU baseline of 0.735±0.145. The Welch t-test is significant for J=0.1 (p=0.040), J=0.3 (p=0.048), and J=0.5 (p=0.027), marginally non-significant for J=0.7 (p=0.051) and J=0.9 (p=0.066) due to higher within-group variance. This confirms that the mean-field coupling mechanism itself, at any strength, systematically affects gradient dynamics.

**Accuracy is uniformly flat.** Accuracy across all fixed-J variants is 0.47–0.48 (J=0.1: 0.471±0.005; J=0.5: 0.477±0.002; J=0.9: 0.472±0.005; learned J: 0.472±0.003), all significantly below GELU (0.511±0.001). The flat accuracy response across J values rules out J-specific tuning as a remedy. The learned-J variant performs identically to fixed-J=0.5, confirming that gradient descent does not meaningfully update J.

**Mechanistic interpretation.** The gradient norm ratio compression from the mean-field coupling appears to reflect the correlated shift J·m* added uniformly to all pre-activations, which reduces the inter-layer gradient variance but simultaneously introduces a bias that reduces the effective capacity of the activation. The fact that accuracy is nearly J-independent while gradient ratios vary modestly with J suggests the dominant accuracy effect is the coupling term's bias, not the coupling strength per se.

## Experiment 4: Extended Language Modeling and J-Learning Dynamics

We extend language model training from 500 to 5000 steps with cosine LR on a character-level GPT (6 layers, 256 hidden, 8 heads) on Tiny Shakespeare, and test a 100× dedicated learning rate for J_raw [ARTIFACT:art_V46hELP73T_t].

**5000-step shared LR (Sub-Exp B).** CWA mean val BPC = 2.210±0.014 vs. GELU = 2.196±0.037 (2 seeds, within noise). J moves from 0.500 to 0.521 over 5000 steps — a rate of ~1.1e-6 per step. Extrapolation: reaching J = 0.9 would require 350,000–590,000 steps under this LR. J·s̄ remains at ~0.20 throughout, confirming deep subcriticality.

**100× J-LR (Sub-Exp C).** With J-dedicated AdamW at LR = 3e-2 (vs. 3e-4 for weights), J moves dramatically to 0.833–0.848 over 5000 steps (|ΔJ| = 0.307–0.351). However, J·s̄ rises only to ~0.30 — not 0.83 — because sech²(x+J·m*) saturates at realistic activation magnitudes (~2.0), where sech²(2) ≈ 0.07. The product J·s̄ ≈ 0.85 × 0.35 ≈ 0.30. CWA 100×J-LR BPC = 2.212±0.011, virtually identical to shared-LR CWA and not better than GELU.

**The saturation barrier.** The key insight from Sub-Exp C is that the barrier to J·s̄ criticality is not the magnitude of the gradient signal on J, but rather the fundamental physics of sech²: at realistic activation scales |x| ~ 1–3, sech²(x) ~ 0.07–0.42. Even with J → 1, J·s̄ = J·mean(sech²(x+J·m*)) is bounded by the activation-scale-dependent sech² mean, which is typically 0.25–0.45 in trained networks. Reaching J·s̄ = 0.9 would require mean sech² ≥ 0.9, corresponding to |x| < 0.48 (extremely small pre-activations), which does not occur after initial training.

# Discussion

## Why Gradient Balance Does Not Imply Accuracy

The fixed-J ablation (Section 4.3) provides the clearest diagnostic: all J values achieve nearly the same accuracy (0.47–0.48) despite producing different gradient ratios (0.245–0.410). This decoupling of gradient ratio from task accuracy suggests that the gradient norm ratio, as defined here, is not the operative quantity determining accuracy. Two mechanisms explain this:

1. **Activation bias.** The mean-field term J·m* adds a correlated shift to all pre-activations in a layer. At convergence, m* ≈ mean_neurons(tanh(x)) (for small J), which is a data-dependent bias injected before every neuron's tanh. This effectively shifts the operating point of the activation, reducing diversity in the layer's feature representations.

2. **Depth-20 instability.** The layer-wise mean m* is sensitive to the distribution of x across layers. At depth 20, without normalization, the distribution of pre-activations compounds across layers, causing m* to become large and the coupling term J·m* to saturate the tanh nonlinearity — producing the observed gradient ratio of 11.02.

## Why SOC Fails — and Why Near-Criticality Is Unreachable

Self-organized criticality would require gradient descent to push J·s̄ toward 1. The experiments provide two independent disconfirmations:

1. **Gradient signal is too weak.** Under shared LR, J moves at 1.1e-6 per step, requiring 350K–590K steps to approach J = 0.9 — far beyond practical training budgets.

2. **sech² saturation.** Even with 100× J-LR causing J → 0.85, J·s̄ reaches only ~0.30 because sech²(x+J·m*) is small at typical activation magnitudes. This is a fundamental physical constraint: the Curie-Weiss model's critical transition at J·s̄ = 1 requires large susceptibility (small sech²), which occurs only near zero-temperature (small inputs), not in trained networks processing natural data.

These two mechanisms together explain why the IFT branch (designed for J·s̄ ≥ 0.8) was never triggered during normal training experiments — the regime it targets is physically inaccessible at realistic activation scales.

## Formal Proofs Remain Valid

All four Lean 4 theorems (Banach convergence, IFT gradient, revised bias bound, warm-start-T bias) remain mathematically valid and relevant to any implementation of CWA. The revised Theorem 3 now accurately reflects the code's tolerance δ = 1e-4·(1−J·s̄), with proven bound 1e-4·(1−J·s̄)/(1−J). The new Theorem 4 provides the first formal proof of the warm-start-T backward's gradient bias, showing the approximation error contracts geometrically at rate J per step. These guarantees support future work on CWA variants that address the saturation barrier.

## Limitations

The present experiments have several limitations. First, the ResNet-20 CIFAR-100 experiment remains at 1 seed; Section 4 prioritizes the MLP experiments where 3-seed statistics and fixed-J ablation are available. Second, the depth-20 collapse dynamics are not fully characterized: it is unclear whether the collapse is due to compound mean shifts, gradient amplification through the IFT denominator 1/(1−J·s̄), or both. Third, the fixed-J ablation uses the same architecture (10-layer MLP, 256 hidden) for all J values; varying width might reveal whether mean-field predictions hold at larger n. Fourth, the activation-scale argument for sech² saturation assumes typical trained distributions; architectures with explicit pre-activation normalization (unnormalized architectures with small weight initialization) might produce smaller |x| and allow higher J·s̄.

## Future Directions

Four directions could address the identified barriers:

- **Small-weight initialization.** Initializing weights with σ² = 0.01 (vs. Kaiming's 2/n) would keep pre-activations small initially, allowing J·s̄ to be near-critical before the network's weight norms grow during training.
- **Constrained activation magnitudes.** An auxiliary loss term penalizing mean(|x+J·m*|) > τ would directly address the sech² saturation barrier.
- **Vector coupling.** Replacing scalar J with a vector J ∈ ℝⁿ (per-neuron coupling) would enable heterogeneous coupling strengths, with some neurons operating in the near-critical regime.
- **CWA + Boltzmann Attention.** Combining CWA's intra-layer (hidden-dim) coupling with Boltzmann Attention's [6] inter-position (sequence-dim) coupling in transformers is a natural extension that might show synergistic effects.

# Conclusion

We introduced the Curie-Weiss Activation (CWA), an activation function defined by a within-sample scalar mean-field self-consistency equation, with a per-layer learnable coupling J. Four Lean 4 theorems without *sorry* establish the mathematical foundation, including a corrected bias bound matching the code's adaptive tolerance and a new warm-start-T gradient bias theorem (error ≤ J^T·ε, so ≤ 12.5% for T=3 with J ≤ 0.5).

Empirical results reveal a nuanced picture. The mean-field coupling mechanism is active and measurable: CWA achieves significantly lower gradient norm ratios than GELU at depths 6 and 10 (p ≤ 0.003), and the IFT branch is validated at J·s̄ = 0.955 with 1.05× GELU memory overhead. However, these gradient-balance benefits do not translate to task accuracy: CWA is outperformed by GELU and decisively by SELU at all depths, with catastrophic collapse at depth 20.

The root cause is identified: the path to the critical regime (J·s̄ → 1) is blocked by sech² saturation at realistic activation scales. Even with 100× dedicated J learning rate causing J → 0.85, the product J·s̄ reaches only ~0.30. The Curie-Weiss activation's mean-field coupling is physically present but operates far from the critical point where its gradient-stability benefits would be expected to emerge. Future work should target the activation-scale constraint directly — either through small-weight initialization or auxiliary pre-activation regularization — to unlock the critical regime that the present experiments confirm is mathematically accessible but practically unreachable under standard training.

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
</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

- [MAJOR] (methodology) The gradient ratio metric |log‖∇W₁‖/log‖∇W_L‖| = 1.0 at stable gradient propagation. CWA achieves 0.305 at depth 6 while GELU achieves 0.712 and SELU achieves 1.089. The paper presents CWA's lower ratio as a positive result ('CWA achieves significantly lower gradient norm ratios than GELU') and reports the Welch t-test significance as support. However, lower is not better: CWA (0.30) is 0.70 units from the ideal, GELU (0.71) is only 0.29 units from the ideal, and SELU (1.09) is only 0.09 units from the ideal. The direction of the effect is inverted in the narrative. Confirmed by the depth-20 result: CWA's ratio jumps to 11.02 (catastrophic), while SELU's 1.47 is still closest to 1.0 and SELU achieves the best accuracy (0.535). The fact that CWA goes from 0.30 (under-unity) at shallow depth to 11.02 (over-unity) at deep depth indicates gradient flow oscillates wildly across depths, not that CWA achieves balance. The paper's claim 'CWA achieves lower gradient norm ratios than GELU (0.305±0.026 vs. 0.712±0.115 at depth 6)... both Welch t-test significant at p ≤ 0.05' is technically correct but systematically misleading without stating that lower is worse.
  Action: In Section 4.2 gradient ratio results, rewrite: 'CWA achieves gradient norm ratios significantly below GELU (0.305 vs. 0.712 at depth 6), but this indicates over-compression rather than balance — CWA deviates 2.4× more from the ideal ratio of 1.0 than GELU. Only SELU (1.089) achieves near-unity ratios, consistent with its self-normalizing design.' Update the Introduction contribution bullet from 'CWA achieves 0.30 and 0.35 gradient norm ratios at depths 6 and 10 vs. GELU's 0.71 and 0.73' to explicitly note that CWA's values are worse (further from 1.0), not better. Add |ratio − 1| as the reported quantity in figures to make the direction unambiguous. This is the single most important fix: the current presentation inverts the paper's own diagnostic.
- [MAJOR] (evidence) GELU+LayerNorm exhibits a depth-20 gradient ratio of 9.661 (from artifact full_method_out.json), which is WORSE than plain GELU's 2.761 at depth 20. This is counter-intuitive: LayerNorm explicitly re-centers and re-scales activations after each layer and is designed to stabilize gradient flow. A normalized baseline performing worse than its unnormalized counterpart on the gradient stability metric calls into question whether the metric captures gradient stability, or whether something is wrong with the GELU+LN implementation at depth 20. This anomaly appears in the raw data (confirmed in artifact art_v26XKv4_F1RM) but is not discussed anywhere in the paper. The paper only reports SELU's depth-20 ratio (1.47) and CWA's (11.02), omitting the GELU+LN result, which is odd if GELU+LN has worse ratio than plain GELU.
  Action: Report GELU+LN's gradient ratio at depth 20 in Section 4.2 and explain the result. Check whether the GELU+LN accuracy at depth 20 also collapses (if ratio=9.66 and accuracy also drops, this suggests LayerNorm at this depth and learning rate causes gradient issues — possibly due to the extra parameter gradient interaction). If GELU+LN gradient ratio is 9.66 but accuracy is still high, then the gradient ratio metric is poorly calibrated for normalized architectures and this caveat should be explicitly stated. Omitting this data point creates an incomplete picture.
- [MINOR] (rigor) Theorem 4's concrete corollary ('T=3, J ≤ 0.5 gives ≤ (1/8)·ε') does not apply to the experimental regime. The artifact data shows final J converging to 0.515–0.521 across all seeds (depth 6/10 experiments). For J=0.52, J^3 = 0.140, not 0.125, so the actual warm-start bias is ≈14.0% of ε, not 12.5%. The paper cites this corollary as supporting the experimental implementation, stating 'For the experimental regime J·s̄ ≈ 0.35 (J ≈ 0.5, J^3 ≈ 0.125)' — but J≈0.5 is an approximation that underestimates the actual bound.
  Action: Either change the concrete corollary threshold from J≤0.5 to J≤0.55 (so the corollary still holds for J≈0.52 in experiments), or add a sentence: 'In practice, J converges to ≈0.515-0.521, giving J^3≈0.136-0.140, so the warm-start bias is bounded at ≈14% of ε — marginally above the T=3,J≤0.5 corollary but still negligible relative to forward-pass convergence error.' This avoids the gap between the stated corollary condition and the actual experimental regime.
- [MINOR] (evidence) The IFT synthetic benchmark (Sub-Exp A) records a gradient numerical check max_err=1.66e-1 in the near-critical regime (J·s̄=0.955). The artifact explicitly notes this is 'larger than target due to finite-diff error at near-critical regime; IFT backward analytically correct.' This 17% gradient error is not mentioned in the paper, which only states 'no NaN/inf outputs.' A gradient error of 0.166 is substantial and would be concerning in a standard gradient check context, even if it can be attributed to finite-difference instability near the 1/(1-J·s̄) denominator singularity.
  Action: In Section 4.1, add: 'The numerical gradient check yields max_err=0.166, which is elevated due to finite-difference instability near J·s̄=0.955 (the 1/(1-J·s̄) denominator amplifies perturbation effects as J·s̄→1). The IFT formula is algebraically exact per Theorem 2; the numerical discrepancy is a property of the finite-difference approximator at near-critical coupling, not of the backward implementation.' Providing this context prevents readers from interpreting the number as a backward implementation error.
- [MINOR] (clarity) The mechanistic claim in Section 5 ('the coupling term's correlated activation bias prevents accuracy gains') is stated without direct experimental support. The paper offers it as an interpretation of the fixed-J ablation results (accuracy flat at 0.47-0.48 across all J values), but this interpretation is not confirmed by an ablation that isolates the bias effect. An alternative interpretation — that the mean-field coupling simply reduces the network's representational capacity by tying activations together — is equally consistent with the data.
  Action: Either (a) add a brief ablation: shift all pre-activations by a constant equal to mean(tanh(x)) for each layer (without the coupling) and measure accuracy — if accuracy drops similarly, this confirms the bias explanation; or (b) acknowledge the alternative interpretation: 'An alternative explanation is that the mean-field shift reduces the per-neuron activation diversity rather than introducing bias per se; distinguishing these requires an ablation we leave for future work.' Clearly labeling the mechanistic interpretation as a hypothesis rather than a confirmed result would strengthen the paper's scientific honesty.
- [MINOR] (methodology) The Competing Nonlinearities baseline uses p_c=0.83 in experiments, but the paper cites Lesser and Chowdhury [5] as deriving p_c=32/35≈0.914 analytically. The paper mentions both values in different places (p_c=32/35≈0.914 in the Related Work section; p_c=0.83 in Section 4.2 experiment description) without explicitly reconciling them. From the research artifact, p_c≈0.83 is the empirical calibration at K₀=1, not the analytical limit. Readers need to understand which value puts the baseline at the critical point for the specific architecture used.
  Action: Add a single sentence in Section 4.2: 'We use p_c=0.83, the empirically calibrated critical mixing fraction at K₀=1 (the theoretical K₀→0 limit gives p_c=32/35≈0.914, per Lesser and Chowdhury [5] Eq. 17), confirmed via forward-pass calibration on the MLP architecture.' This closes the apparent inconsistency without requiring additional experiments.
- [MINOR] (scope) The ResNet-20 CIFAR-100 experiment (artifact art_SVlh9mQatV8y) is referenced in the Limitations section as 'remaining at 1 seed' but appears nowhere in the main experimental results. The experiment exists and produced data (1 seed, 10 epochs, CWA 14.0% vs GELU 18.9%) but is entirely excluded from Section 4. The paper has a 4-experiment structure (IFT benchmark, gradient stability, fixed-J ablation, extended LM) with no ResNet results reported, even as a supplementary single-seed observation.
  Action: Either (a) include the 1-seed ResNet result in a brief paragraph in Section 4 with appropriate caveats ('preliminary, n=1 seed, 10 epochs'), or (b) remove all references to ResNet in the Limitations section to avoid the appearance of withholding data. Given the space, (a) is preferable: the result (CWA 14.0% vs GELU 18.9% no-BN) is consistent with the MLP findings and adds breadth to the negative evidence.
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

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
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 12 research artifacts across all iterations.

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
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

id: art_W-Ea4lflZ84v
title: 'CWA Re-Analysis: Six Reviewer Critiques Fixed via Corrected Metrics'
type: evaluation
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

id: art_5zKSer_FGOKx
title: >-
  CWA Mechanistic Sub-Experiments: Small-Weight Init and Constant-Shift Ablation on CIFAR-10
type: experiment
summary: |-
  Two mechanistic sub-experiments on 10-layer unnormalized MLPs (no BatchNorm/Dropout) trained on CIFAR-10 using the Curie-Weiss Activation (CWA): a novel activation function with a learned coupling J and closed-form IFT backward pass.

  Sub-Exp A (Small-Weight Init, σ=0.01 vs Kaiming): Tests whether reduced init magnitudes allow J·s̄ to reach near-critical values (>0.7). Three conditions × 3 seeds × 25 epochs. Result: max J·s̄ for cwa_small_init=0.412, cwa_kaiming_init=0.374 — neither reaches criticality. Verdict: init_does_not_help. Small init converges slowly (epoch-1 acc ~0.20 vs 0.36 for Kaiming) but closes the gap by epoch 25.

  Sub-Exp B (Shift Ablation — CWA-Full vs CWA-ShiftOnly vs Pure-Tanh): Isolates whether CWA's accuracy comes from inter-neuron coupling (full fixed-point) or just the mean-shift in pre-activations. Three conditions × 3 seeds × 25 epochs. Final test accuracies: cwa_full=0.4685, cwa_shift_only=0.4686, pure_tanh=0.4731. Verdict: bias_dominant — coupling adds nothing beyond the mean shift, and pure-tanh slightly outperforms both CWA variants. Paired t-tests show no significant difference between CWA-Full and CWA-ShiftOnly (the shift alone captures all the effect).

  Key finding: At Kaiming init the mean-field parameter J·s̄ sits at ~0.35–0.45, far from the critical point (J·s̄→1), and small-init does not push it higher. The CWA's inter-neuron coupling mechanism provides no accuracy benefit over a single detached mean-shift in this unnormalized MLP setting. These negative mechanistic results are informative for the hypothesis revision.

  Experiment ran on RTX 5090 (sm_120) with PyTorch 2.7.0+cu128, ~9 minutes total wall-clock time. Schema-validated exp_gen_sol_out JSON with 18 examples (one per sub-exp × condition × seed).

id: art_l4KqMWHu-dCe
title: 'CWA Proof v3: Corollary 4b (J≤0.55) Covering Experimental Regime'
type: proof
summary: |-
  CWA Proof v3 extends the iter-2 verified Lean 4 proof by adding `cwa_warmstart_corollary_j55`, a new concrete warm-start-3 bias bound theorem covering J≤55/100 (bias≤167/1000·ε≈16.7%·ε). This fills a reviewer-visible gap: the existing iter-2 theorem `cwa_warmstart3_concrete` only covers J≤1/2, but the GPU experiments report J∈[0.515,0.521] — strictly above 0.5. The new corollary formally covers the entire observed experimental range with margin.

  The proof reuses the exact same tactic pattern as the existing J≤1/2 corollary: `cwa_warmstart_bias` provides J^T·ε bound, `gcongr` derives J^3≤(55/100)^3 from hJ_55, `norm_num` closes (55/100)^3≤167/1000 (since 166375/1000000≤167000/1000000), and a three-step calc chain applies `mul_le_mul_of_nonneg_right` twice. No existing theorems were modified.

  All 16 lemmas/theorems verified by Lean 4.14.0 with no sorries and no errors: hasDerivAt_sinh, hasDerivAt_cosh, hasDerivAt_tanh, differentiable_tanh, sech_sq_nonneg, sech_sq_le_one, nnnorm_deriv_tanh_le, tanh_lipschitzWith_one, lin_lipschitz, F_lipschitz, F_contracting, cwa_banach, one_sub_J_sbar_pos, ift_gradient_correct, ift_equation_unique_solution, contraction_residual_bound, cwa_ift_bias_code_tolerance, code_tol_bound_finite, warmstart_iteration_bound, cwa_warmstart_bias, cwa_warmstart3_concrete, cwa_warmstart_corollary_j55 (NEW), cwa_main_v2. Output: proof.lean (complete verified file) and proof_out.json (schema-validated).
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison):
  {"id": "fig3", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: latency (seconds, 0-5). Values: PostgreSQL=4.6s (red), Bao=2.8s (blue), RLQOpt=2.0s (green). Error bars +/-0.3-0.8. Sans-serif font, white background.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero):
  {"id": "fig1", "title": "System Architecture", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
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
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Short descriptive figure title",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "Detailed image generation prompt \u2014 axes, labels, ALL numeric values, colors, aspect ratio, layout. The image generator cannot read files; this is its ONLY input.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title - concise, descriptive, captures the main contribution",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-16 22:05:23 UTC

```
Role: You are an expert Deep Learning Research Scientist specializing in neural network architecture and mathematical optimization.Objective: Given a supervised learning dataset, design, implement, and validate an optimal, novel activation function $f(x)$ for a neural network. Your goal is to discover an activation function that empirically outperforms traditional baselines (ReLU, Swish, GELU, Tanh) in terms of final validation metrics, convergence speed, and gradient stability.Search Space & Constraints:The solution may be a parameterized function (with learnable parameters), a dynamic/gated composition of existing functions, or an entirely novel mathematical formulation.The function must be differentiable (or sub-differentiable) to allow for backpropagation.Consider computational efficiency; the function should not introduce prohibitive computational overhead compared to standard functions.
```

### [3] SKILL-INPUT — aii-paper-writing · 2026-06-16 22:05:52 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: Academic paper writing guidance for AI research. Covers paper structure, figure placeholders, bibliography building with Semantic Scholar, and citation rules. Does NOT cover LaTeX compilation or figure file generation — see aii-paper-to-latex for that.
---

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-06-16 22:05:54 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
