# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 4 · `gen_plan`
> Run: `run_6gT5lHFn8559` — Novel Activation Function
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_experiment_1` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-06-16 22:29:59 UTC

```
model: claude-sonnet-4-6 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_4/gen_plan/gen_plan_experiment_1
```

### [2] SYSTEM-USER prompt · 2026-06-16 22:30:05 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A plan generator (Step 3.2: GEN_PLAN in the invention loop)

You received the hypothesis, an artifact direction to elaborate, and dependency artifacts relevant to the plan.
Your job: elaborate this direction into a detailed, actionable plan for the executor agent.

Specific, actionable plan → valuable artifact. Vague plan → wasted execution.
</your_role>
</ai_inventor_context>

<artifact_type_info>
You are expanding an artifact direction of type: EXPERIMENT

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance
</artifact_type_info>

<available_resources>
<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
- aii-handbook-multi-llm-agents: Multi-LLM agent orchestration patterns
</skills>

<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>
</available_resources>

<time_budget>

The experiment executor has 6h total (including writing code, debugging, testing, and fixing errors).

</time_budget>

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

<plan_guidelines>
You are expanding an artifact direction from the strategy into a detailed plan.
The artifact direction specifies what to do at a high level (type, objective, approach, dependencies).
Your job is to make it concrete and actionable as a detailed plan.
Use web research to look up technical details, verify feasibility, and find reference materials
that will make your plan more concrete and actionable for the executor.

GOOD PLANS:
- Make each component SPECIFIC and actionable (not vague platitudes)
- Consider both success AND failure scenarios
- Build on the approach in the artifact direction
- Add concrete details the executor needs

BAD PLANS:
- Vague hand-waving ("do research on X")
- Ignoring the approach in the artifact direction
- Missing critical details the executor needs
</plan_guidelines>

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

<hypothesis>
kind: hypothesis
title: >-
  Curie-Weiss Activation Fails as a Drop-In Activation: Mechanistic Account of Gradient Underflow, Bias-Dominance, and the
  sech² Saturation Barrier
hypothesis: >-
  The Curie-Weiss Activation (CWA) — defined by the within-sample mean-field self-consistency equation y_i = tanh(x_i + J·mean_neurons(y))
  with learnable scalar J = σ(J_raw) ∈ (0,1) per layer — provides no measurable benefit over standard pointwise activations
  in unnormalized deep MLPs (depths 6–20) or small character-level GPT models, and exhibits three precisely characterized
  failure modes: (1) GRADIENT UNDERFLOW, not balance: using the correct distance-to-ideal metric |ratio−1|, CWA ranks last
  among six activations at all tested depths (|ratio−1| = 0.695, 0.653, 10.017 at depths 6, 10, 20), with raw gradient ratios
  of 0.305–0.347 at shallow depths indicating gradient underflow (factor 2.4× worse than GELU, 7.8× worse than SELU) rather
  than stability. At depth 20, CWA collapses catastrophically (ratio = 11.02). SELU achieves the best gradient stability at
  all tested depths and the best accuracy at depth 20 (0.535 vs CWA 0.141). (2) BIAS-DOMINANT MECHANISM: a shift ablation
  experiment establishes that the self-consistent fixed-point coupling adds zero benefit over a simple detached mean shift
  (CWA-Full=0.4685 vs CWA-ShiftOnly=0.4686, paired t p=0.984). Critically, CWA provides no statistically significant accuracy
  gain over pure pointwise Tanh with no shift (CWA-Full 0.4685 vs Pure-Tanh 0.4731, p=0.126). There is no confirmed accuracy
  effect of CWA to attribute to any mechanism. (3) sech² SATURATION BARRIER PREVENTS CRITICALITY: the product J·s̄ = J·mean(sech²(x+J·m*))
  remains at 0.20–0.41 under all tested training configurations because sech²(x) ≈ 0.07 at typical activation magnitudes |x|
  ∼ 2.0, capping J·s̄ far below the critical threshold J·s̄ = 1 even when J → 0.85 via 100× dedicated learning rate. Reaching
  J·s̄ = 0.9 would require mean(sech²) ≥ 0.9, corresponding to |x| < 0.48 — impractically small for trained networks processing
  natural data. Small-weight initialization (σ=0.01) raises maximum J·s̄ from 0.374 to 0.412 but still falls far short of
  near-criticality. The IFT branch (J·s̄ ≥ 0.8) is never triggered in normal training. The IFT memory overhead in the synthetic
  micro-benchmark is 5.57× GELU (1.047 MB IFT vs. 0.188 MB GELU), violating the stated 2× criterion; this micro-benchmark
  baseline is anomalously small, and the IFT-vs-unrolled comparison shows 1.0× ratio (no savings vs K=50 unrolled in the micro-benchmark),
  suggesting the benchmark is dominated by model parameter memory rather than activation memory. A dedicated large-scale memory
  benchmark (n=4096, K=50) is required to demonstrate the theoretical O(K·n) vs. O(n) IFT advantage empirically. Five Lean
  4 theorems without sorry establish the mathematical foundation including a new Corollary 4b (J ≤ 0.55, bias ≤ 16.7%·ε) covering
  the experimentally observed J ∈ [0.515, 0.521]. The GELU+LayerNorm anomaly at depth 20 (ratio=9.661 AND accuracy=0.139 despite
  explicit per-layer normalization) establishes that the gradient ratio metric |log‖∇W₁‖/log‖∇W_L‖| conflates LayerNorm's
  internal re-scaling with true inter-layer gradient magnitudes at ANY depth (abs_dev: 0.630 at depth 6, 0.642 at depth 10,
  8.661 at depth 20, all second-worst after CWA), making cross-class comparisons between normalized and unnormalized architectures
  unreliable. The net finding is a mechanistic negative result: within-layer mean-field coupling via Curie-Weiss physics is
  computationally well-defined (convergence in K_mean≈7.4 iterations, formal proofs verified), but it cannot self-organize
  to the critical regime, and provides no benefit over a simple mean-shift correction or over standard pointwise baselines
  in the tested settings. This constitutes a publishable mechanistic contribution: a precise identification of the sech² saturation
  barrier as the root cause of CWA's failure to reach criticality, the bias-dominance of the mean-shift term as the only observed
  mechanism, and the superiority of distributional fixed-point design (SELU) over mean-field output coupling for unnormalized
  deep networks. These conclusions are explicitly scoped to unnormalized MLPs at depths 6–20 and a 6-layer character-level
  GPT; whether normalized or residual architectures exhibit the same pathologies remains untested. The one remaining positive
  avenue requiring investigation is whether explicit pre-activation regularization (auxiliary loss penalizing mean(|x+J·m*|)
  > τ for small τ ≈0.4) can overcome the sech² saturation barrier and allow J·s̄ to reach near-critical values where the self-consistent
  coupling would qualitatively differ from the mean-shift approximation.
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
  Same CWA frame; IFT ratio corrected (5.57×), bias-dominance confirmed, negative-results framing.
_confidence_delta: decreased
_key_changes:
- >-
  IFT memory overhead corrected: actual ratio is 5.57× GELU (not 1.05×); the 2× criterion is NOT met in the micro-benchmark;
  IFT-vs-unrolled ratio is 1.0× (no savings in micro-benchmark, model-parameter-dominated); large-scale n=4096 K=50 benchmark
  required to demonstrate theoretical advantage.
- >-
  Shift ablation finding elevated as decisive: CWA provides NO statistically significant accuracy gain over Pure-Tanh (p=0.126);
  the coupling adds zero over detached mean-shift (p=0.984); there is no confirmed accuracy effect of CWA to attribute to
  any mechanism.
- >-
  Gradient underflow framing strengthened: CWA ranks last at ALL depths using corrected |ratio-1| metric; shallow-depth ratio
  of 0.305-0.347 is underflow not balance (7.8× worse than SELU, 2.4× worse than GELU); depth-20 collapse (ratio=11.02) established.
- >-
  GELU+LN anomaly extended to all depths: abs_dev 0.630/0.642/8.661 at depths 6/10/20 (second-worst after CWA at all depths),
  supporting conclusion that gradient ratio metric is unreliable for normalized architectures at ANY depth, not just depth
  20.
- >-
  Paper framing revised to explicit mechanistic negative-results study: title/abstract needed, contributions reordered to
  lead with negative findings, conclusion explicitly states whether CWA is worth pursuing.
- >-
  sech² saturation root cause confirmed as the primary barrier: max J·s̄ = 0.412 even with small-weight init; IFT branch never
  triggered in normal training; sech² ≈0.07 at |x|−2.0 caps J·s̄ regardless of J magnitude.
- >-
  Scope explicitly bounded to unnormalized MLPs depths 6-20 and 6-layer character-level GPT; conclusions about 'general failure'
  of CWA retracted in favor of scoped empirical claims.
- >-
  Remaining positive avenue identified: pre-activation regularization (auxiliary loss constraining |x+J·m*| < 0.48) to overcome
  sech² saturation barrier and enable near-critical J·s̄.
relation_type: evolution
</hypothesis>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter4_dir1
type: experiment
objective: >-
  Run a dedicated large-scale CWA memory benchmark at layer widths n in {256, 1024, 4096} with K_max=50, directly comparing:
  (A) IFT backward (stores only scalar m*, O(n) activation memory), (B) unrolled K=50 autograd (stores K intermediate activation
  tensors, O(K*n)), and (C) GELU baseline. The primary question: at what n does IFT begin saving meaningful memory over unrolled,
  and what is the IFT/GELU ratio at n=4096?
approach: >-
  Implement a standalone memory benchmark script. For each (n, backprop_mode) in the grid: (1) Construct a single CWA layer
  with width n; (2) Generate random input batch (batch=64, n neurons); (3) Force J_raw=+4.0 (J~0.98) and small-magnitude inputs
  (x_scale=0.1) to trigger J*s_bar > 0.8 and activate IFT path; (4) torch.cuda.reset_peak_memory_stats() before each run,
  3 warm-up passes discarded, 5 measurement runs averaged; (5) Unrolled mode: K=50 iterations with full grad tracking; (6)
  IFT mode: K=50 iterations without grad, then IFT custom backward storing only m* (closed-form scalar: dL/dx_k = s_k * [g_k
  + J * sum(g_i*s_i) / (n*(1-J*s_bar))], per art_Lj-xi6yJR_yy); (7) GELU baseline: single forward+backward of equivalent GELU
  layer. Also run x_scale=1.0 to show J*s_bar drop and confirm saturation effect at standard activation magnitudes. Report
  peak_MB_ift[n], peak_MB_unrolled[n], peak_MB_gelu[n], ratio_ift_over_gelu[n], ratio_ift_over_unrolled[n] for each (n, x_scale).
  Output method_out.json with one example per (n, x_scale, mode) configuration in exp_gen_sol_out schema.
depends_on:
- id: art_Lj-xi6yJR_yy
  label: ift-formulas
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
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
out_dependency_files:
  file_list:
  - research_out.json
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results
</artifact_executor_scope>

<artifact_planning_rules>
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for experiment artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
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
  "description": "Plan for an EXPERIMENT artifact.",
  "properties": {
    "title": {
      "description": "Short title for the plan",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "implementation_pseudocode": {
      "description": "High-level pseudocode for the experiment implementation",
      "title": "Implementation Pseudocode",
      "type": "string"
    },
    "fallback_plan": {
      "description": "What to do if the primary approach fails - alternative methods, simplified versions",
      "title": "Fallback Plan",
      "type": "string"
    },
    "testing_plan": {
      "description": "How to validate the experiment works: start with small/fast tests, look for confirmation signals before running full-scale experiments",
      "title": "Testing Plan",
      "type": "string"
    }
  },
  "required": [
    "title",
    "implementation_pseudocode",
    "fallback_plan",
    "testing_plan"
  ],
  "title": "ExperimentPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-06-16 22:30:05 UTC

```
Role: You are an expert Deep Learning Research Scientist specializing in neural network architecture and mathematical optimization.Objective: Given a supervised learning dataset, design, implement, and validate an optimal, novel activation function $f(x)$ for a neural network. Your goal is to discover an activation function that empirically outperforms traditional baselines (ReLU, Swish, GELU, Tanh) in terms of final validation metrics, convergence speed, and gradient stability.Search Space & Constraints:The solution may be a parameterized function (with learnable parameters), a dynamic/gated composition of existing functions, or an entirely novel mathematical formulation.The function must be differentiable (or sub-differentiable) to allow for backpropagation.Consider computational efficiency; the function should not introduce prohibitive computational overhead compared to standard functions.
```

### [4] ASSISTANT · 2026-06-16 22:30:52 UTC

```
I'll plan the CWA memory benchmark experiment. Let me read the dependency research artifact first to get the exact IFT gradient formulas.
```

### [5] TOOL CALL — Read · 2026-06-16 22:30:52 UTC

```
/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_research_1/research_out.json
```

### [6] TOOL RESULT — Read · 2026-06-16 22:30:52 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_research_1/research_out.json", "content": "{\n  \"title\": \"CWA Implementation Details: DEQ IFT Backward, Competing Nonlinearities p_c, SELU Derivation, and 2025-2026 Related Work Survey\",\n  \"summary\": \"Verified technical foundations for the Curie-Weiss Activation (CWA) experiment across four components: (1) DEQ IFT backward formulas and PyTorch hook pattern — CWA's scalar fixed point allows closed-form O(n) gradients without an iterative solver; (2) Competing Nonlinearities p_c = 32/35 ≈ 0.914 analytically and ≈0.83 empirically at K₀=1, with p = Swish fraction convention confirmed; (3) SELU α₀₁≈1.6733, λ₀₁≈1.0507 from Banach fixed-point theorem on N(0,1/n)-initialized networks; (4) 2025-2026 novelty survey of 5 papers confirms no existing work introduces a learnable scalar coupling between within-sample neuron mean and individual pre-activations in an activation function.\",\n  \"answer\": \"## 1. DEQ IFT Backward Hook\\n\\nThe DEQ forward pass finds fixed point z* = f_θ(z*, x) via Anderson acceleration running inside torch.no_grad() — only z* is stored, achieving O(1) memory w.r.t. solver depth and an 88% memory reduction vs. unrolled backprop on WikiText-103 [1]. After convergence, one forward call with grad re-engages the autograd tape, and a backward hook is registered [2,3].\\n\\nBy the Implicit Function Theorem (Theorem 2.1 of [2]): ∂L/∂θ = (∂L/∂z*)(I − ∂f_θ/∂z*)^{-1}(∂f_θ/∂θ). The inverse is computed via the backward linear fixed-point: g = (∂f/∂z*)^T g + ∂L/∂z*, iterated as g_{t+1} = autograd.grad(f0, z0, g_t, retain_graph=True)[0] + grad [3]. This uses VJPs only — never materializes the full n×n Jacobian.\\n\\n**CWA closed-form IFT:** Because CWA's fixed point m* = (1/n)Σ_i tanh(x_i + J·m*) is SCALAR (dim=1), the system (I−J_f^T)g = y collapses to the scalar equation (1 − J·s̄)g = y, giving the closed-form g = y/(1−J·s̄) where s̄ = (1/n)Σ_i sech²(x_i+J·m*) [1,2,3]. No iterative backward solver is needed.\\n\\nExact CWA gradient formulas:\\n- ∂m*/∂x_i = sech²(x_i+J·m*) / (n·(1−J·s̄))\\n- ∂m*/∂J   = m*·s̄ / (1−J·s̄)\\n- ∂y_i/∂x_i = sech²(x_i+J·m*)·[1 + J·sech²(x_i+J·m*)/(n(1−J·s̄))]\\n- ∂y_i/∂J   = sech²(x_i+J·m*)·m*/(1−J·s̄)\\n- Full ∂L/∂x_i = (∂L/∂y_i)·s_i·(1+scale·s_i) + scale·s_i·Σ_k(∂L/∂y_k)·s_k where scale=J/(n(1−J·s̄))\\n\\nGradient amplification factor 1/(1−J·s̄) is well-defined as long as J·s̄ < 1 (forward convergence condition).\\n\\n## 2. Competing Nonlinearities p_c\\n\\nThe variance recursion is K^(l+1) = C_W·g(K^(l))+C_b where g(K) = E_{z~N(0,K)}[σ²(z)] [4]. For a statistical (incoherent) mixture where each neuron independently draws from {Swish, Tanh}: g^(mix)(K) = p·g^(Swish)(K) + (1−p)·g^(Tanh)(K), with p = Swish fraction (p=0 pure Tanh, p=1 pure Swish) [4].\\n\\nTaylor coefficients of the kernel function near K=0: g₂^(Tanh) = −2, g₂^(Swish) = 3/16. The stability coefficients satisfy a₁^(Tanh)=−2 (stable class, variance collapses K^(l)∼1/l) and a₁^(Swish)=3/4 (half-stable class, variance inflates) [4].\\n\\nCritical point from a₁^(mix)(p_c)=0, Eq. 17 of [4]:\\n  p_c = g₂^(Tanh)/(g₂^(Tanh) − g₂^(Swish)) = (−2)/((−2)−(3/16)) = (−2)/(−35/16) = 32/35 ≈ 0.914\\n\\nNumerical values [4]:\\n- p_c = 32/35 ≈ 0.914 (analytic, K₀→0 small-variance limit)\\n- p_c ≈ 0.83 (empirical simulation at K₀=1)\\n- Perturbative correction: p_c(K₀) = 32/35 − (384/1225)·K₀ + O(K₀²)\\n\\nFor non-standard architectures (ResNet, GPT, C_W≠1): the paper [4] restricts analysis to infinite-width MLPs with C_W=1, C_b=0, and explicitly defers convolutional/attention/layer-norm extensions to future work. Practical recommendation: empirical forward-pass calibration — sweep p over a grid, find the mixing fraction where the depth profile K^(l) is flattest on unlabeled data.\\n\\n## 3. SELU Fixed-Point Derivation\\n\\nSELU(x) = λ·{x if x>0; α(e^x−1) if x≤0}, with exact parameters from Eq. 14 of [5]:\\n- α₀₁ = −√(2/π)/(erfc(1/√2)·exp(1/2)−1) ≈ 1.6732632423543772\\n- λ₀₁ ≈ 1.0507009873554805\\n\\nThese solve the fixed-point equations at (μ,ν)=(0,1): E_{z~N(0,1)}[SELU(z)]=0 and Var[SELU(z)]=1, for LeCun-initialized weights w_i~N(0,1/n) [5].\\n\\nThe Banach fixed-point theorem is applied to the layer-to-layer distributional mapping g:(μ,ν)→(E[SELU(z)], Var[SELU(z)]) on the domain Ω = {μ∈[−0.1,0.1], ω∈[−0.1,0.1], ν∈[0.8,1.5], τ∈[0.95,1.1]}. Two conditions are proven: (1) spectral norm of Jacobian J(g)<1 (contraction, via computer-assisted proof); (2) g(Ω)⊆Ω (domain invariance). Unique attracting fixed point follows [5].\\n\\nMechanistic contrast with CWA: SELU is POINTWISE — y_i=SELU(x_i), no inter-neuron coupling, self-normalization via marginal distribution statistics. CWA is COUPLED — y_i=tanh(x_i+J·m*) where m*=(1/n)Σ_j tanh(x_j+J·m*) involves all neurons simultaneously. SELU's fixed point is distributional; CWA's is a sample-level equation solved per forward pass.\\n\\n## 4. 2025-2026 Survey: Learnable Neuron Coupling\\n\\nFive papers assessed for novelty threat to CWA:\\n\\n**Boltzmann Attention [6]** (arXiv:2606.12478, Jun 2026): Introduces learnable Ising couplings J_{ij} between ATTENTION POSITIONS (sequence/token dimension) in transformer attention. Not an activation function; not in the hidden neuron dimension. Novelty threat: NONE.\\n\\n**Competing Nonlinearities [4]** (arXiv:2605.05294, May 2026): Statistical mixture of activations with fixed (unlearnable) quenched disorder p set at initialization. No inter-neuron coupling at inference time; p is a hyperparameter, not trained. Novelty threat: NONE.\\n\\n**AlphaEvolve Activations [7]** (arXiv:2602.05688, Feb 2026): Evolutionary discovery of activation functions. The 'Turbulent' activation uses BATCH statistics (jnp.mean(x, axis=0) — cross-data axis, not cross-neuron). Batch-statistics functions fail on image tasks (OOM, poor transfer). No learnable inter-neuron coupling J. Novelty threat: PARTIAL (non-pointwise but different axis).\\n\\n**Tuning Universality [8]** (arXiv:2512.00168, Nov 2025): Stochastic theory with 4 effective couplings (r,h,D₁,D₂) characterizing collective dynamics in random DNNs — purely theoretical, no learnable parameters, no new activation function. Novelty threat: NONE.\\n\\n**Mean Field Feature Learning [9]** (arXiv:2510.15174, Oct 2025): Self-consistent MF theory for Bayesian posterior of two-layer networks trained with SGLD. Self-reinforcing feature selection is a training-dynamics property, not an activation-level coupling. No learnable scalar J. Novelty threat: NONE.\\n\\n**Novelty verdict:** No 2025-2026 paper introduces a learnable scalar J coupling the within-sample hidden-neuron mean to individual pre-activations in an activation function. CWA's architecture y_i=σ(x_i+J·m*) with J∈R learnable and m* solved as a per-example fixed point is confirmed novel [4,6,7,8,9].\",\n  \"sources\": [\n    {\n      \"index\": 1,\n      \"url\": \"https://arxiv.org/pdf/1909.01377\",\n      \"title\": \"Deep Equilibrium Models (Bai et al., NeurIPS 2019)\",\n      \"summary\": \"Original DEQ paper: IFT gradient theorem, backward via Broyden/Anderson fixed-point iteration on (I−J_f^T)g=∂L/∂z*, 88% memory reduction on WikiText-103, O(1) activation memory.\"\n    },\n    {\n      \"index\": 2,\n      \"url\": \"https://arxiv.org/pdf/2310.18605\",\n      \"title\": \"TorchDEQ: A Library for Deep Equilibrium Models (Geng & Kolter, 2023)\",\n      \"summary\": \"Theorem 2.1: ∂L/∂θ=(∂L/∂z*)(I−∂f/∂z*)^{-1}(∂f/∂θ). Backward linear fixed-point g^T=g^T(∂f/∂z*)+∂L/∂z*. Supports IFT and Phantom Gradient; backward solvers: anderson, broyden, fixed_point_iter.\"\n    },\n    {\n      \"index\": 3,\n      \"url\": \"http://implicit-layers-tutorial.org/deep_equilibrium_models/\",\n      \"title\": \"Deep Implicit Layers Tutorial Chapter 4 (Kolter, Duvenaud, Johnson)\",\n      \"summary\": \"Concrete PyTorch DEQ backward via register_hook: forward solve under no_grad(), re-engage tape, hook iterates g_{t+1}=autograd.grad(f0,z0,g_t,retain_graph=True)[0]+grad. Full Anderson acceleration code.\"\n    },\n    {\n      \"index\": 4,\n      \"url\": \"https://arxiv.org/pdf/2605.05294\",\n      \"title\": \"Competing Nonlinearities, Criticality, and Order-to-Chaos Transition (Lesser & Chowdhury, May 2026)\",\n      \"summary\": \"p_c=32/35≈0.914 analytically (K₀→0); ≈0.83 empirically (K₀=1). p=Swish fraction. g₂^Tanh=−2, g₂^Swish=3/16. Perturbative correction p_c(K₀)=32/35−(384/1225)K₀. Non-MLP: empirical calibration only.\"\n    },\n    {\n      \"index\": 5,\n      \"url\": \"https://arxiv.org/pdf/1706.02515\",\n      \"title\": \"Self-Normalizing Neural Networks / SELU (Klambauer et al., NeurIPS 2017)\",\n      \"summary\": \"α₀₁≈1.6733, λ₀₁≈1.0507 from Eq.14. Fixed point (μ,ν)=(0,1) for LeCun init w_i~N(0,1/n). Banach theorem on domain Ω proves contraction. SELU is pointwise — no inter-neuron coupling.\"\n    },\n    {\n      \"index\": 6,\n      \"url\": \"https://arxiv.org/abs/2606.12478\",\n      \"title\": \"Boltzmann Attention: Learnable Ising Couplings for Cooperative Attention (Kim & Park, Jun 2026)\",\n      \"summary\": \"Learnable Ising J_{ij} between sequence positions in transformer attention. Not an activation function; operates in sequence/token dimension not hidden neuron dimension. Novelty threat to CWA: none.\"\n    },\n    {\n      \"index\": 7,\n      \"url\": \"https://arxiv.org/pdf/2602.05688\",\n      \"title\": \"Mining Generalizable Activation Functions via AlphaEvolve (Vitvitskyi et al., Feb 2026)\",\n      \"summary\": \"Evolutionary discovery of activations. Turbulent activation uses batch statistics (cross-data axis), not within-sample hidden statistics. Batch-stats functions fail on image tasks. No learnable inter-neuron coupling J.\"\n    },\n    {\n      \"index\": 8,\n      \"url\": \"https://arxiv.org/abs/2512.00168\",\n      \"title\": \"Tuning Universality in Deep Neural Networks (Ghavasieh, Nov 2025)\",\n      \"summary\": \"Stochastic theory with 4 effective couplings (r,h,D₁,D₂) derived from activation/weight choice. Purely theoretical; no learnable coupling parameters and no proposed activation function.\"\n    },\n    {\n      \"index\": 9,\n      \"url\": \"https://arxiv.org/abs/2510.15174\",\n      \"title\": \"A Simple Mean Field Model of Feature Learning (Göring et al., Oct 2025)\",\n      \"summary\": \"Self-consistent MF theory for Bayesian posterior of two-layer networks trained with SGLD. Self-reinforcing feature selection is a training-dynamics property, not a within-sample activation coupling. No learnable J.\"\n    }\n  ],\n  \"follow_up_questions\": [\n    \"For J·s̄ approaching 1 during CWA training (ferromagnetic instability), should a regularization term penalizing J·s̄ or a hard clip on J be applied, and what is the practical effect on the accuracy-stability tradeoff?\",\n    \"The Competing Nonlinearities p_c formula assumes C_W=1 and MLP architectures. For GPT-style transformer MLPs with pre-LN (which normalizes activations before the nonlinearity), does p_c shift significantly from 0.83, or does the normalization effectively enforce the C_W=1 condition?\",\n    \"Is there any paper using a learnable scalar coupling between the within-sample hidden-dimension mean and individual pre-activations — y_i = σ(x_i + J·m*) with J trained by gradient descent — in any domain outside standard neural networks (e.g., physics-inspired ML, mean-field games, energy-based models)?\"\n  ]\n}\n", "numLines": 67, "startLine": 1, "totalLines": 67}}
```

### [7] ASSISTANT · 2026-06-16 22:32:37 UTC

```
Now I have all the key formulas. Let me write the complete plan.
```

### [8] TOOL CALL — Write · 2026-06-16 22:32:37 UTC

```
File: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_4/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json

{
  "title": "CWA Large-Scale IFT vs Unrolled Memory Benchmark",
  "summary": "Dedicated memory benchmark comparing IFT backward, unrolled K=50 autograd, and GELU baseline at layer widths n∈{256,1024,4096} with batch=64, testing both near-critical (x_scale=0.1, J*s_bar≈0.97) and saturated (x_scale=1.0, J*s_bar≈0.07) regimes. Primary output: ratio_ift_over_gelu[n] and ratio_ift_over_unrolled[n] to determine at what n IFT delivers meaningful memory savings over unrolled K=50 autograd.",
  "runpod_compute_profile": "gpu",
  "implementation_pseudocode": "# method.py — CWA Memory Benchmark\n# Measures peak GPU memory for IFT vs Unrolled vs GELU at n in {256,1024,4096}\n\n## DEPENDENCIES:\n# torch, numpy, json (stdlib only — no pip installs needed)\n\n## KEY PARAMETERS:\n# WIDTHS = [256, 1024, 4096]\n# X_SCALES = [0.1, 1.0]       # 0.1 → J*s_bar≈0.97 (near-critical); 1.0 → J*s_bar≈0.07 (saturated)\n# BATCH = 64\n# K_MAX = 50\n# J_RAW_FIXED = 4.0           # sigmoid(4.0) ≈ 0.982 → forces IFT path when x_scale=0.1\n# N_WARMUP = 3\n# N_MEASURE = 5\n\n## STEP 1: Implement CWA_IFT_Function (torch.autograd.Function)\n\nclass CWA_IFT_Function(torch.autograd.Function):\n    @staticmethod\n    def forward(ctx, x, J, K_max, tol):\n        # x: (B, n), J: scalar tensor\n        # Run fixed-point iteration UNDER no_grad() — stores NO intermediate tensors\n        with torch.no_grad():\n            B, n = x.shape\n            m = torch.zeros(B, 1, device=x.device, dtype=x.dtype)\n            for _ in range(K_max):\n                m_new = torch.mean(torch.tanh(x + J * m), dim=1, keepdim=True)  # (B,1)\n                if torch.max(torch.abs(m_new - m)).item() < tol:\n                    m = m_new\n                    break\n                m = m_new\n        # y computed WITH grad engagement for output (needed for loss.backward())\n        # But we'll handle this in backward manually\n        y = torch.tanh(x + J * m)          # (B, n)  — this tensor IS kept for loss\n        s_bar = torch.mean(1.0 - y**2, dim=1, keepdim=True)  # (B,1) = mean(sech²)\n        K_actual = _  # approximate, track convergence iterations\n        # Store only what backward needs: m (B,1), y (B,n), s_bar (B,1), J (scalar)\n        ctx.save_for_backward(x, J, m, y, s_bar)\n        ctx.B = B\n        ctx.n = n\n        return y\n\n    @staticmethod\n    def backward(ctx, grad_output):\n        # grad_output: (B, n)\n        x, J, m, y, s_bar = ctx.saved_tensors\n        B, n = ctx.B, ctx.n\n        # s_k = sech²(x_k + J*m*) = 1 - y_k²  (B, n)\n        s = 1.0 - y**2\n        # IFT gradient from research art_Lj-xi6yJR_yy:\n        # dL/dx_k = s_k * [g_k + J * sum_i(g_i*s_i) / (n*(1-J*s_bar))]\n        # where g_k = grad_output_k\n        one_minus_Jsbar = 1.0 - J * s_bar          # (B, 1)\n        sum_gs = torch.sum(grad_output * s, dim=1, keepdim=True)  # (B, 1)\n        grad_x = s * (grad_output + J * sum_gs / (n * one_minus_Jsbar))  # (B, n)\n        # dL/dJ via chain rule: ∂m*/∂J = m*·s̄/(1-J·s̄)\n        # dL/dJ = sum_k(grad_output_k * sech²(x_k+J*m*) * m*/(1-J*s_bar))\n        # = sum_k(grad_output_k * s_k) * m* / (1 - J*s_bar)   summed over batch too\n        # But J is a scalar — sum over all batch and neuron dims\n        grad_J = torch.sum(sum_gs * m / one_minus_Jsbar)  # scalar\n        return grad_x, grad_J, None, None\n\n## STEP 2: Implement CWA_Unrolled_Forward\n\ndef cwa_unrolled_forward(x, J, K_max=50):\n    # Runs ALL K iterations through autograd tape — stores K intermediate tensors\n    B, n = x.shape\n    m = torch.zeros(B, 1, device=x.device, dtype=x.dtype, requires_grad=False)\n    for k in range(K_max):\n        # Each tanh call adds (B,n) tensor to the autograd graph\n        m = torch.mean(torch.tanh(x + J * m), dim=1, keepdim=True)  # (B,1)\n    y = torch.tanh(x + J * m)\n    return y\n\n## STEP 3: Implement measurement harness\n\ndef measure_peak_memory_MB(fn, *args, n_warmup=3, n_measure=5):\n    # Warmup to avoid cold-start artifacts\n    for _ in range(n_warmup):\n        out = fn(*args)\n        loss = out.sum()\n        loss.backward()\n        # Zero grads but keep tensors alive\n        for a in args:\n            if isinstance(a, torch.Tensor) and a.grad is not None:\n                a.grad = None\n        del out, loss\n        torch.cuda.empty_cache()\n    # Measure\n    peak_mbs = []\n    for _ in range(n_measure):\n        torch.cuda.reset_peak_memory_stats()\n        gc.collect()\n        torch.cuda.empty_cache()\n        out = fn(*args)\n        loss = out.sum()\n        loss.backward()\n        peak_mb = torch.cuda.max_memory_allocated() / 1e6\n        peak_mbs.append(peak_mb)\n        for a in args:\n            if isinstance(a, torch.Tensor) and a.grad is not None:\n                a.grad = None\n        del out, loss\n    return float(np.mean(peak_mbs)), float(np.std(peak_mbs))\n\n## STEP 4: Grid sweep\n\nresults = []\nfor n in [256, 1024, 4096]:\n    for x_scale in [0.1, 1.0]:\n        # Shared input: fresh for each (n, x_scale)\n        x_data = (torch.randn(64, n, device='cuda') * x_scale)\n\n        ## --- MODE: GELU ---\n        linear = nn.Linear(n, n, bias=False).cuda()\n        gelu = nn.GELU()\n        def gelu_fn():\n            x_in = x_data.clone().requires_grad_(True)\n            return gelu(linear(x_in))\n        mem_gelu, std_gelu = measure_peak_memory_MB(gelu_fn)\n\n        ## --- MODE: IFT ---\n        J_raw = torch.tensor(4.0, device='cuda', requires_grad=True)  # J≈0.982\n        J = torch.sigmoid(J_raw)\n        # Compute actual J*s_bar at this x_scale for reporting\n        with torch.no_grad():\n            m_test = torch.zeros(64, 1, device='cuda')\n            for _ in range(50):\n                m_new = torch.mean(torch.tanh(x_data + J * m_test), dim=1, keepdim=True)\n                if torch.max(torch.abs(m_new - m_test)).item() < 1e-6:\n                    m_test = m_new; break\n                m_test = m_new\n            y_test = torch.tanh(x_data + J * m_test)\n            s_bar_test = float(torch.mean(1.0 - y_test**2).item())\n            Jsbar = float(J.item()) * s_bar_test\n\n        def ift_fn():\n            x_in = x_data.clone().requires_grad_(True)\n            J_param = torch.tensor(4.0, device='cuda', requires_grad=True)\n            J_val = torch.sigmoid(J_param)\n            return CWA_IFT_Function.apply(x_in, J_val, 50, 1e-6)\n        mem_ift, std_ift = measure_peak_memory_MB(ift_fn)\n\n        ## --- MODE: UNROLLED K=50 ---\n        def unrolled_fn():\n            x_in = x_data.clone().requires_grad_(True)\n            J_param = torch.tensor(4.0, device='cuda', requires_grad=True)\n            J_val = torch.sigmoid(J_param)\n            return cwa_unrolled_forward(x_in, J_val, K_max=50)\n        mem_unrolled, std_unrolled = measure_peak_memory_MB(unrolled_fn)\n\n        # Compute ratios\n        ratio_ift_gelu = mem_ift / mem_gelu if mem_gelu > 0 else float('inf')\n        ratio_ift_unrolled = mem_ift / mem_unrolled if mem_unrolled > 0 else float('inf')\n        ratio_unrolled_gelu = mem_unrolled / mem_gelu if mem_gelu > 0 else float('inf')\n\n        # Log results\n        print(f'n={n}, x_scale={x_scale}, J*s_bar={Jsbar:.3f}')\n        print(f'  GELU: {mem_gelu:.1f} MB  IFT: {mem_ift:.1f} MB  Unrolled: {mem_unrolled:.1f} MB')\n        print(f'  IFT/GELU={ratio_ift_gelu:.2f}x  IFT/Unrolled={ratio_ift_unrolled:.2f}x  Unrolled/GELU={ratio_unrolled_gelu:.2f}x')\n\n        results.append({\n            'n': n,\n            'x_scale': x_scale,\n            'J': float(torch.sigmoid(torch.tensor(4.0)).item()),\n            'Jsbar': Jsbar,\n            'sbar': s_bar_test,\n            'peak_MB_gelu': mem_gelu,\n            'peak_MB_ift': mem_ift,\n            'peak_MB_unrolled': mem_unrolled,\n            'ratio_ift_over_gelu': ratio_ift_gelu,\n            'ratio_ift_over_unrolled': ratio_ift_unrolled,\n            'ratio_unrolled_over_gelu': ratio_unrolled_gelu,\n            'std_gelu': std_gelu,\n            'std_ift': std_ift,\n            'std_unrolled': std_unrolled\n        })\n\n## STEP 5: Output method_out.json in exp_gen_sol_out schema\n# Each benchmark run = one 'example' with input config and output metrics\nexamples = []\nfor r in results:\n    for mode, mem_key, ratio_key in [\n        ('gelu', 'peak_MB_gelu', None),\n        ('ift', 'peak_MB_ift', 'ratio_ift_over_gelu'),\n        ('unrolled', 'peak_MB_unrolled', 'ratio_unrolled_over_gelu')\n    ]:\n        ex = {\n            'id': f'n{r[\"n\"]}_xscale{r[\"x_scale\"]}_{mode}',\n            'input': {\n                'n': r['n'],\n                'x_scale': r['x_scale'],\n                'mode': mode,\n                'batch': 64,\n                'K_max': 50,\n                'J_raw': 4.0,\n                'J': r['J'],\n                'Jsbar': r['Jsbar'],\n                'sbar': r['sbar']\n            },\n            'output': {\n                'peak_MB': r[mem_key],\n                'peak_MB_std': r[f'std_{mode}'],\n                'ratio_over_gelu': r[ratio_key] if ratio_key else 1.0,\n                'ratio_ift_over_unrolled': r['ratio_ift_over_unrolled'] if mode == 'ift' else None,\n                'ratio_unrolled_over_gelu': r['ratio_unrolled_over_gelu'] if mode == 'unrolled' else None\n            },\n            'prediction': {\n                'expected_ratio_theory': (\n                    1.0 if mode == 'gelu' else\n                    (1.0 if mode == 'ift' else 50.0)  # IFT≈GELU; Unrolled=50×GELU\n                ),\n                'hypothesis_claim': (\n                    'IFT stores only m* (B,1) + output y (B,n) → O(n)' if mode == 'ift' else\n                    ('Unrolled stores K=50 intermediate (B,1) tanh outputs → O(K)' if mode == 'unrolled' else\n                     'GELU baseline: stores input activations (B,n) → O(n)')\n                )\n            },\n            'label': {\n                'confirms_ift_advantage': (\n                    r['ratio_ift_over_unrolled'] < 0.5 if mode == 'ift' else None\n                ),\n                'ift_within_2x_gelu': (\n                    r['ratio_ift_over_gelu'] <= 2.0 if mode == 'ift' else None\n                )\n            }\n        }\n        examples.append(ex)\n\nmethod_out = {\n    'schema': 'exp_gen_sol_out',\n    'experiment': 'cwa_memory_benchmark',\n    'description': 'Peak GPU memory comparison: IFT vs Unrolled K=50 vs GELU at n in {256,1024,4096}',\n    'examples': examples,\n    'summary': {\n        'finding': <filled at runtime>,\n        'ift_2x_criterion_met_at_n': <list of n where ratio_ift_gelu <= 2.0>,\n        'ift_meaningful_savings_vs_unrolled_at_n': <list of n where ratio_ift_unrolled < 0.5>,\n        'peak_jsbar_near_critical': <Jsbar at x_scale=0.1>,\n        'peak_jsbar_saturated': <Jsbar at x_scale=1.0>\n    }\n}\nwith open('method_out.json', 'w') as f:\n    json.dump(method_out, f, indent=2)",
  "fallback_plan": "## Primary Failure Scenarios\n\n### Failure 1: CUDA OOM at n=4096 with unrolled K=50\nK=50 iterations at n=4096, batch=64: 50 × 64 × 4096 × 4 bytes ≈ 52MB for intermediate tanh outputs, plus gradients → ~104MB; well within 20GB VRAM. OOM is unlikely. But if it occurs: reduce K to K=20 for unrolled, report at K=20 and note in summary.\n\n### Failure 2: IFT backward produces NaN gradients\nRoot cause: J*s_bar → 1 causes 1/(1-J*s_bar) to blow up. Fix: check that with J_raw=4.0 (J≈0.982) and x_scale=0.1, J*s_bar is verified to stay < 1. At x_scale=0.1, inputs to tanh are small, sech²≈1, so J*s_bar ≈ 0.982 × 1.0 = 0.982 — stable but high. If NaN appears, reduce J_raw to 3.0 (J≈0.952) or add clamping: one_minus_Jsbar = max(one_minus_Jsbar, 0.01).\n\n### Failure 3: Fixed-point iteration diverges (no convergence in K=50)\nAt J*s_bar < 1 convergence is guaranteed by Banach theorem. Geometric rate ρ=J*s_bar. At J*s_bar=0.97: residual after 50 steps = 0.97^50 × |m_0 - m*| ≈ 0.22 × initial error — may not fully converge. Fix: increase tol to 1e-4 (which is the adaptive tolerance from the hypothesis) or increase K_max to 200 for x_scale=0.1. Log actual K_actual for all runs.\n\n### Failure 4: Memory measurement unreliable (GPU running other processes)\nFix: add torch.cuda.synchronize() before and after the measured forward+backward pass. Use the minimum over N_MEASURE=5 runs (not mean) as the peak memory estimate, since other processes can inflate but not deflate readings.\n\n### Fallback simplified version:\nIf CUDA memory APIs are unavailable (CPU fallback): use tracemalloc Python memory tracking instead. Switch torch.cuda.max_memory_allocated() to tracemalloc snapshot comparison. This gives RAM not VRAM but still demonstrates the O(K*n) vs O(n) scaling difference.\n\n### Fallback output if GPU unavailable:\nRun on CPU with n in {64, 256, 1024} only (skip n=4096 for time), measuring Python process RSS memory via psutil.Process().memory_info().rss before and after each call. Report memory_overhead_bytes instead of peak_MB_gpu.",
  "testing_plan": "## Validation Strategy\n\n### Step 0: Smoke test at n=64, K=10 (< 5 seconds)\n- Run IFT backward on tiny (batch=4, n=64) input, check:\n  - Forward output matches unrolled output to tolerance 1e-4\n  - IFT gradient matches unrolled gradient to tolerance 1e-3 (they should be close since K=50 unrolled is near-converged)\n  - No NaN in gradients\n  - Memory APIs return nonzero values\n- Print J, J*s_bar at x_scale=0.1 and x_scale=1.0 to confirm near-critical vs saturated regime\n\n### Step 1: Gradient correctness check via torch.autograd.gradcheck\n- Run torch.autograd.gradcheck(CWA_IFT_Function.apply, inputs=(x_small, J_val, 50, 1e-7)) with x_small shape (4, 16)\n- Expect gradcheck to pass (default rtol=1e-3, atol=1e-5 is sufficient for the IFT approximation)\n- If gradcheck fails: add eps=1e-4 argument (larger finite difference step for numerical stability)\n\n### Step 2: Quick memory scaling check at n=256 only\n- Run 3 warmup + 3 measure passes for all 3 modes at n=256\n- Confirm: unrolled memory > ift memory (this must hold; if not, there's an implementation bug where unrolled isn't actually tracking grads)\n- Check that ratios are in plausible range: unrolled/gelu should be >> 1 at n=256, K=50\n\n### Step 3: Verify J*s_bar diagnostic\n- At x_scale=0.1, n=256: print J*s_bar, confirm it is > 0.8 (IFT path active)\n- At x_scale=1.0, n=256: print J*s_bar, confirm it is < 0.5 (deep saturation, matching the hypothesis's claim that J*s_bar ≈ 0.07 at |x|≈2.0)\n- This is a critical sanity check: if x_scale=0.1 gives J*s_bar < 0.8, the IFT regime is not being tested\n\n### Step 4: Full benchmark n∈{256,1024,4096}\n- Run all 3×2×3=18 configurations\n- Expected pattern to confirm:\n  - ratio_unrolled_gelu should scale roughly as K=50 (50×) regardless of n (O(K) overhead)\n  - ratio_ift_gelu should stay near 1.0-2.0 regardless of n (O(1) overhead w.r.t. K)\n  - The 'crossover' where IFT clearly beats unrolled should be visible at all n\n- If ratio_ift_gelu >> 5.57 (the prior micro-benchmark result), investigate: check that forward pass is actually running under no_grad()\n\n### Step 5: Output validation\n- Confirm method_out.json is valid JSON with 'examples' array of 18 entries\n- Each entry has id, input, output, prediction, label fields\n- Report the IFT/GELU ratio at n=4096, x_scale=0.1 as the PRIMARY finding\n- Explicitly state whether the 2× memory criterion from the hypothesis is met at any n"
}
```

### [9] TOOL RESULT — Write · 2026-06-16 22:32:37 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_4/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"CWA Large-Scale IFT vs Unrolled Memory Benchmark\",\n  \"summary\": \"Dedicated memory benchmark comparing IFT backward, unrolled K=50 autograd, and GELU baseline at layer widths n∈{256,1024,4096} with batch=64, testing both near-critical (x_scale=0.1, J*s_bar≈0.97) and saturated (x_scale=1.0, J*s_bar≈0.07) regimes. Primary output: ratio_ift_over_gelu[n] and ratio_ift_over_unrolled[n] to determine at what n IFT delivers meaningful memory savings over unrolled K=50 autograd.\",\n  \"runpod_compute_profile\": \"gpu\",\n  \"implementation_pseudocode\": \"# method.py — CWA Memory Benchmark\\n# Measures peak GPU memory for IFT vs Unrolled vs GELU at n in {256,1024,4096}\\n\\n## DEPENDENCIES:\\n# torch, numpy, json (stdlib only — no pip installs needed)\\n\\n## KEY PARAMETERS:\\n# WIDTHS = [256, 1024, 4096]\\n# X_SCALES = [0.1, 1.0]       # 0.1 → J*s_bar≈0.97 (near-critical); 1.0 → J*s_bar≈0.07 (saturated)\\n# BATCH = 64\\n# K_MAX = 50\\n# J_RAW_FIXED = 4.0           # sigmoid(4.0) ≈ 0.982 → forces IFT path when x_scale=0.1\\n# N_WARMUP = 3\\n# N_MEASURE = 5\\n\\n## STEP 1: Implement CWA_IFT_Function (torch.autograd.Function)\\n\\nclass CWA_IFT_Function(torch.autograd.Function):\\n    @staticmethod\\n    def forward(ctx, x, J, K_max, tol):\\n        # x: (B, n), J: scalar tensor\\n        # Run fixed-point iteration UNDER no_grad() — stores NO intermediate tensors\\n        with torch.no_grad():\\n            B, n = x.shape\\n            m = torch.zeros(B, 1, device=x.device, dtype=x.dtype)\\n            for _ in range(K_max):\\n                m_new = torch.mean(torch.tanh(x + J * m), dim=1, keepdim=True)  # (B,1)\\n                if torch.max(torch.abs(m_new - m)).item() < tol:\\n                    m = m_new\\n                    break\\n                m = m_new\\n        # y computed WITH grad engagement for output (needed for loss.backward())\\n        # But we'll handle this in backward manually\\n        y = torch.tanh(x + J * m)          # (B, n)  — this tensor IS kept for loss\\n        s_bar = torch.mean(1.0 - y**2, dim=1, keepdim=True)  # (B,1) = mean(sech²)\\n        K_actual = _  # approximate, track convergence iterations\\n        # Store only what backward needs: m (B,1), y (B,n), s_bar (B,1), J (scalar)\\n        ctx.save_for_backward(x, J, m, y, s_bar)\\n        ctx.B = B\\n        ctx.n = n\\n        return y\\n\\n    @staticmethod\\n    def backward(ctx, grad_output):\\n        # grad_output: (B, n)\\n        x, J, m, y, s_bar = ctx.saved_tensors\\n        B, n = ctx.B, ctx.n\\n        # s_k = sech²(x_k + J*m*) = 1 - y_k²  (B, n)\\n        s = 1.0 - y**2\\n        # IFT gradient from research art_Lj-xi6yJR_yy:\\n        # dL/dx_k = s_k * [g_k + J * sum_i(g_i*s_i) / (n*(1-J*s_bar))]\\n        # where g_k = grad_output_k\\n        one_minus_Jsbar = 1.0 - J * s_bar          # (B, 1)\\n        sum_gs = torch.sum(grad_output * s, dim=1, keepdim=True)  # (B, 1)\\n        grad_x = s * (grad_output + J * sum_gs / (n * one_minus_Jsbar))  # (B, n)\\n        # dL/dJ via chain rule: ∂m*/∂J = m*·s̄/(1-J·s̄)\\n        # dL/dJ = sum_k(grad_output_k * sech²(x_k+J*m*) * m*/(1-J*s_bar))\\n        # = sum_k(grad_output_k * s_k) * m* / (1 - J*s_bar)   summed over batch too\\n        # But J is a scalar — sum over all batch and neuron dims\\n        grad_J = torch.sum(sum_gs * m / one_minus_Jsbar)  # scalar\\n        return grad_x, grad_J, None, None\\n\\n## STEP 2: Implement CWA_Unrolled_Forward\\n\\ndef cwa_unrolled_forward(x, J, K_max=50):\\n    # Runs ALL K iterations through autograd tape — stores K intermediate tensors\\n    B, n = x.shape\\n    m = torch.zeros(B, 1, device=x.device, dtype=x.dtype, requires_grad=False)\\n    for k in range(K_max):\\n        # Each tanh call adds (B,n) tensor to the autograd graph\\n        m = torch.mean(torch.tanh(x + J * m), dim=1, keepdim=True)  # (B,1)\\n    y = torch.tanh(x + J * m)\\n    return y\\n\\n## STEP 3: Implement measurement harness\\n\\ndef measure_peak_memory_MB(fn, *args, n_warmup=3, n_measure=5):\\n    # Warmup to avoid cold-start artifacts\\n    for _ in range(n_warmup):\\n        out = fn(*args)\\n        loss = out.sum()\\n        loss.backward()\\n        # Zero grads but keep tensors alive\\n        for a in args:\\n            if isinstance(a, torch.Tensor) and a.grad is not None:\\n                a.grad = None\\n        del out, loss\\n        torch.cuda.empty_cache()\\n    # Measure\\n    peak_mbs = []\\n    for _ in range(n_measure):\\n        torch.cuda.reset_peak_memory_stats()\\n        gc.collect()\\n        torch.cuda.empty_cache()\\n        out = fn(*args)\\n        loss = out.sum()\\n        loss.backward()\\n        peak_mb = torch.cuda.max_memory_allocated() / 1e6\\n        peak_mbs.append(peak_mb)\\n        for a in args:\\n            if isinstance(a, torch.Tensor) and a.grad is not None:\\n                a.grad = None\\n        del out, loss\\n    return float(np.mean(peak_mbs)), float(np.std(peak_mbs))\\n\\n## STEP 4: Grid sweep\\n\\nresults = []\\nfor n in [256, 1024, 4096]:\\n    for x_scale in [0.1, 1.0]:\\n        # Shared input: fresh for each (n, x_scale)\\n        x_data = (torch.randn(64, n, device='cuda') * x_scale)\\n\\n        ## --- MODE: GELU ---\\n        linear = nn.Linear(n, n, bias=False).cuda()\\n        gelu = nn.GELU()\\n        def gelu_fn():\\n            x_in = x_data.clone().requires_grad_(True)\\n            return gelu(linear(x_in))\\n        mem_gelu, std_gelu = measure_peak_memory_MB(gelu_fn)\\n\\n        ## --- MODE: IFT ---\\n        J_raw = torch.tensor(4.0, device='cuda', requires_grad=True)  # J≈0.982\\n        J = torch.sigmoid(J_raw)\\n        # Compute actual J*s_bar at this x_scale for reporting\\n        with torch.no_grad():\\n            m_test = torch.zeros(64, 1, device='cuda')\\n            for _ in range(50):\\n                m_new = torch.mean(torch.tanh(x_data + J * m_test), dim=1, keepdim=True)\\n                if torch.max(torch.abs(m_new - m_test)).item() < 1e-6:\\n                    m_test = m_new; break\\n                m_test = m_new\\n            y_test = torch.tanh(x_data + J * m_test)\\n            s_bar_test = float(torch.mean(1.0 - y_test**2).item())\\n            Jsbar = float(J.item()) * s_bar_test\\n\\n        def ift_fn():\\n            x_in = x_data.clone().requires_grad_(True)\\n            J_param = torch.tensor(4.0, device='cuda', requires_grad=True)\\n            J_val = torch.sigmoid(J_param)\\n            return CWA_IFT_Function.apply(x_in, J_val, 50, 1e-6)\\n        mem_ift, std_ift = measure_peak_memory_MB(ift_fn)\\n\\n        ## --- MODE: UNROLLED K=50 ---\\n        def unrolled_fn():\\n            x_in = x_data.clone().requires_grad_(True)\\n            J_param = torch.tensor(4.0, device='cuda', requires_grad=True)\\n            J_val = torch.sigmoid(J_param)\\n            return cwa_unrolled_forward(x_in, J_val, K_max=50)\\n        mem_unrolled, std_unrolled = measure_peak_memory_MB(unrolled_fn)\\n\\n        # Compute ratios\\n        ratio_ift_gelu = mem_ift / mem_gelu if mem_gelu > 0 else float('inf')\\n        ratio_ift_unrolled = mem_ift / mem_unrolled if mem_unrolled > 0 else float('inf')\\n        ratio_unrolled_gelu = mem_unrolled / mem_gelu if mem_gelu > 0 else float('inf')\\n\\n        # Log results\\n        print(f'n={n}, x_scale={x_scale}, J*s_bar={Jsbar:.3f}')\\n        print(f'  GELU: {mem_gelu:.1f} MB  IFT: {mem_ift:.1f} MB  Unrolled: {mem_unrolled:.1f} MB')\\n        print(f'  IFT/GELU={ratio_ift_gelu:.2f}x  IFT/Unrolled={ratio_ift_unrolled:.2f}x  Unrolled/GELU={ratio_unrolled_gelu:.2f}x')\\n\\n        results.append({\\n            'n': n,\\n            'x_scale': x_scale,\\n            'J': float(torch.sigmoid(torch.tensor(4.0)).item()),\\n            'Jsbar': Jsbar,\\n            'sbar': s_bar_test,\\n            'peak_MB_gelu': mem_gelu,\\n            'peak_MB_ift': mem_ift,\\n            'peak_MB_unrolled': mem_unrolled,\\n            'ratio_ift_over_gelu': ratio_ift_gelu,\\n            'ratio_ift_over_unrolled': ratio_ift_unrolled,\\n            'ratio_unrolled_over_gelu': ratio_unrolled_gelu,\\n            'std_gelu': std_gelu,\\n            'std_ift': std_ift,\\n            'std_unrolled': std_unrolled\\n        })\\n\\n## STEP 5: Output method_out.json in exp_gen_sol_out schema\\n# Each benchmark run = one 'example' with input config and output metrics\\nexamples = []\\nfor r in results:\\n    for mode, mem_key, ratio_key in [\\n        ('gelu', 'peak_MB_gelu', None),\\n        ('ift', 'peak_MB_ift', 'ratio_ift_over_gelu'),\\n        ('unrolled', 'peak_MB_unrolled', 'ratio_unrolled_over_gelu')\\n    ]:\\n        ex = {\\n            'id': f'n{r[\\\"n\\\"]}_xscale{r[\\\"x_scale\\\"]}_{mode}',\\n            'input': {\\n                'n': r['n'],\\n                'x_scale': r['x_scale'],\\n                'mode': mode,\\n                'batch': 64,\\n                'K_max': 50,\\n                'J_raw': 4.0,\\n                'J': r['J'],\\n                'Jsbar': r['Jsbar'],\\n                'sbar': r['sbar']\\n            },\\n            'output': {\\n                'peak_MB': r[mem_key],\\n                'peak_MB_std': r[f'std_{mode}'],\\n                'ratio_over_gelu': r[ratio_key] if ratio_key else 1.0,\\n                'ratio_ift_over_unrolled': r['ratio_ift_over_unrolled'] if mode == 'ift' else None,\\n                'ratio_unrolled_over_gelu': r['ratio_unrolled_over_gelu'] if mode == 'unrolled' else None\\n            },\\n            'prediction': {\\n                'expected_ratio_theory': (\\n                    1.0 if mode == 'gelu' else\\n                    (1.0 if mode == 'ift' else 50.0)  # IFT≈GELU; Unrolled=50×GELU\\n                ),\\n                'hypothesis_claim': (\\n                    'IFT stores only m* (B,1) + output y (B,n) → O(n)' if mode == 'ift' else\\n                    ('Unrolled stores K=50 intermediate (B,1) tanh outputs → O(K)' if mode == 'unrolled' else\\n                     'GELU baseline: stores input activations (B,n) → O(n)')\\n                )\\n            },\\n            'label': {\\n                'confirms_ift_advantage': (\\n                    r['ratio_ift_over_unrolled'] < 0.5 if mode == 'ift' else None\\n                ),\\n                'ift_within_2x_gelu': (\\n                    r['ratio_ift_over_gelu'] <= 2.0 if mode == 'ift' else None\\n                )\\n            }\\n        }\\n        examples.append(ex)\\n\\nmethod_out = {\\n    'schema': 'exp_gen_sol_out',\\n    'experiment': 'cwa_memory_benchmark',\\n    'description': 'Peak GPU memory comparison: IFT vs Unrolled K=50 vs GELU at n in {256,1024,4096}',\\n    'examples': examples,\\n    'summary': {\\n        'finding': <filled at runtime>,\\n        'ift_2x_criterion_met_at_n': <list of n where ratio_ift_gelu <= 2.0>,\\n        'ift_meaningful_savings_vs_unrolled_at_n': <list of n where ratio_ift_unrolled < 0.5>,\\n        'peak_jsbar_near_critical': <Jsbar at x_scale=0.1>,\\n        'peak_jsbar_saturated': <Jsbar at x_scale=1.0>\\n    }\\n}\\nwith open('method_out.json', 'w') as f:\\n    json.dump(method_out, f, indent=2)\",\n  \"fallback_plan\": \"## Primary Failure Scenarios\\n\\n### Failure 1: CUDA OOM at n=4096 with unrolled K=50\\nK=50 iterations at n=4096, batch=64: 50 × 64 × 4096 × 4 bytes ≈ 52MB for intermediate tanh outputs, plus gradients → ~104MB; well within 20GB VRAM. OOM is unlikely. But if it occurs: reduce K to K=20 for unrolled, report at K=20 and note in summary.\\n\\n### Failure 2: IFT backward produces NaN gradients\\nRoot cause: J*s_bar → 1 causes 1/(1-J*s_bar) to blow up. Fix: check that with J_raw=4.0 (J≈0.982) and x_scale=0.1, J*s_bar is verified to stay < 1. At x_scale=0.1, inputs to tanh are small, sech²≈1, so J*s_bar ≈ 0.982 × 1.0 = 0.982 — stable but high. If NaN appears, reduce J_raw to 3.0 (J≈0.952) or add clamping: one_minus_Jsbar = max(one_minus_Jsbar, 0.01).\\n\\n### Failure 3: Fixed-point iteration diverges (no convergence in K=50)\\nAt J*s_bar < 1 convergence is guaranteed by Banach theorem. Geometric rate ρ=J*s_bar. At J*s_bar=0.97: residual after 50 steps = 0.97^50 × |m_0 - m*| ≈ 0.22 × initial error — may not fully converge. Fix: increase tol to 1e-4 (which is the adaptive tolerance from the hypothesis) or increase K_max to 200 for x_scale=0.1. Log actual K_actual for all runs.\\n\\n### Failure 4: Memory measurement unreliable (GPU running other processes)\\nFix: add torch.cuda.synchronize() before and after the measured forward+backward pass. Use the minimum over N_MEASURE=5 runs (not mean) as the peak memory estimate, since other processes can inflate but not deflate readings.\\n\\n### Fallback simplified version:\\nIf CUDA memory APIs are unavailable (CPU fallback): use tracemalloc Python memory tracking instead. Switch torch.cuda.max_memory_allocated() to tracemalloc snapshot comparison. This gives RAM not VRAM but still demonstrates the O(K*n) vs O(n) scaling difference.\\n\\n### Fallback output if GPU unavailable:\\nRun on CPU with n in {64, 256, 1024} only (skip n=4096 for time), measuring Python process RSS memory via psutil.Process().memory_info().rss before and after each call. Report memory_overhead_bytes instead of peak_MB_gpu.\",\n  \"testing_plan\": \"## Validation Strategy\\n\\n### Step 0: Smoke test at n=64, K=10 (< 5 seconds)\\n- Run IFT backward on tiny (batch=4, n=64) input, check:\\n  - Forward output matches unrolled output to tolerance 1e-4\\n  - IFT gradient matches unrolled gradient to tolerance 1e-3 (they should be close since K=50 unrolled is near-converged)\\n  - No NaN in gradients\\n  - Memory APIs return nonzero values\\n- Print J, J*s_bar at x_scale=0.1 and x_scale=1.0 to confirm near-critical vs saturated regime\\n\\n### Step 1: Gradient correctness check via torch.autograd.gradcheck\\n- Run torch.autograd.gradcheck(CWA_IFT_Function.apply, inputs=(x_small, J_val, 50, 1e-7)) with x_small shape (4, 16)\\n- Expect gradcheck to pass (default rtol=1e-3, atol=1e-5 is sufficient for the IFT approximation)\\n- If gradcheck fails: add eps=1e-4 argument (larger finite difference step for numerical stability)\\n\\n### Step 2: Quick memory scaling check at n=256 only\\n- Run 3 warmup + 3 measure passes for all 3 modes at n=256\\n- Confirm: unrolled memory > ift memory (this must hold; if not, there's an implementation bug where unrolled isn't actually tracking grads)\\n- Check that ratios are in plausible range: unrolled/gelu should be >> 1 at n=256, K=50\\n\\n### Step 3: Verify J*s_bar diagnostic\\n- At x_scale=0.1, n=256: print J*s_bar, confirm it is > 0.8 (IFT path active)\\n- At x_scale=1.0, n=256: print J*s_bar, confirm it is < 0.5 (deep saturation, matching the hypothesis's claim that J*s_bar ≈ 0.07 at |x|≈2.0)\\n- This is a critical sanity check: if x_scale=0.1 gives J*s_bar < 0.8, the IFT regime is not being tested\\n\\n### Step 4: Full benchmark n∈{256,1024,4096}\\n- Run all 3×2×3=18 configurations\\n- Expected pattern to confirm:\\n  - ratio_unrolled_gelu should scale roughly as K=50 (50×) regardless of n (O(K) overhead)\\n  - ratio_ift_gelu should stay near 1.0-2.0 regardless of n (O(1) overhead w.r.t. K)\\n  - The 'crossover' where IFT clearly beats unrolled should be visible at all n\\n- If ratio_ift_gelu >> 5.57 (the prior micro-benchmark result), investigate: check that forward pass is actually running under no_grad()\\n\\n### Step 5: Output validation\\n- Confirm method_out.json is valid JSON with 'examples' array of 18 entries\\n- Each entry has id, input, output, prediction, label fields\\n- Report the IFT/GELU ratio at n=4096, x_scale=0.1 as the PRIMARY finding\\n- Explicitly state whether the 2× memory criterion from the hypothesis is met at any n\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [10] ASSISTANT · 2026-06-16 22:32:47 UTC

```
The plan is written. Here's what it covers:

**Experiment goal**: Benchmark peak GPU memory for CWA-IFT vs CWA-Unrolled-K50 vs GELU at n∈{256,1024,4096}, batch=64, to determine where IFT delivers meaningful memory savings over unrolled autograd.

**Key implementation decisions in the plan**:
- `CWA_IFT_Function` as a `torch.autograd.Function` — forward runs K=50 iterations under `torch.no_grad()` storing only `m*` and `y`; backward uses the closed-form IFT formula from the dependency: `dL/dx_k = s_k * [g_k + J * Σ(g_i·s_i) / (n·(1-J·s̄))]`
- J_raw=4.0 (J≈0.982) forces the near-critical regime; x_scale=0.1 yields J·s̄≈0.97, x_scale=1.0 yields J·s̄≈0.07 (the saturation regime from the hypothesis)
- Memory measured via `torch.cuda.reset_peak_memory_stats()` + `torch.cuda.max_memory_allocated()`, 3 warmup + 5 measured passes

**Output**: 18 examples (3n × 2x_scale × 3modes) in `method_out.json`, with ratios `ratio_ift_over_gelu` and `ratio_ift_over_unrolled` as the primary metrics. The plan explicitly checks whether the 2× GELU criterion (the hypothesis's stated boundary) is met at any n.

**Compute profile**: `gpu` — CUDA memory APIs are required for meaningful measurement.
```
