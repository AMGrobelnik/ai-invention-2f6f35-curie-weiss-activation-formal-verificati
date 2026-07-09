# gen_plan_experiment_3 — test_idea

> Phase: `invention_loop` · round 1 · `gen_plan`
> Run: `run_6gT5lHFn8559` — Novel Activation Function
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_experiment_3` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-06-16 17:23:32 UTC

```
model: claude-sonnet-4-6 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_3
```

### [2] SYSTEM-USER prompt · 2026-06-16 17:23:41 UTC

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

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter1_dir4
type: experiment
objective: >-
  Run Experiment 3: Replace GELU in MLP sublayers of a 6-layer/256-hidden character-level GPT with CWA, test on Tiny Shakespeare
  and WikiText-2. Measure test BPC (character) and perplexity (word) vs GELU, GELU+LN, SELU, tanh+Swish@p_c baselines. Track
  J, J·s̄, K, backprop mode, peak GPU memory per epoch.
approach: >-
  Implement minimal GPT (6 layers, 256 hidden, 8 heads, MLP expansion 4×) in PyTorch from scratch. Replace GELU in FFN block
  with CWA. Train character-level on Tiny Shakespeare (download raw txt from GitHub): seq_len=256, batch=64, 10K steps, AdamW
  lr=3e-4. Train word-level on WikiText-2 (download via datasets library): seq_len=128, batch=32, 20K steps. Baselines: same
  GPT with GELU, GELU+LN (LayerNorm in FFN), SELU, tanh+Swish@p_c (p_c=0.5 tuned on val). Eval: test BPC (Shakespeare), test
  perplexity (WikiText-2). Track per-layer J*s_bar and K* across training. Run 3 seeds for Shakespeare, 2 seeds for WikiText-2.
  Output method_out.json with shakespeare_bpc, wikitext2_ppl, baseline_comparison, J_s_bar_trajectory_per_layer, K_per_layer_per_epoch,
  peak_gpu_memory.
depends_on: []
</artifact_direction>



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

### [3] HUMAN-USER prompt · 2026-06-16 17:23:41 UTC

```
Role: You are an expert Deep Learning Research Scientist specializing in neural network architecture and mathematical optimization.Objective: Given a supervised learning dataset, design, implement, and validate an optimal, novel activation function $f(x)$ for a neural network. Your goal is to discover an activation function that empirically outperforms traditional baselines (ReLU, Swish, GELU, Tanh) in terms of final validation metrics, convergence speed, and gradient stability.Search Space & Constraints:The solution may be a parameterized function (with learnable parameters), a dynamic/gated composition of existing functions, or an entirely novel mathematical formulation.The function must be differentiable (or sub-differentiable) to allow for backpropagation.Consider computational efficiency; the function should not introduce prohibitive computational overhead compared to standard functions.
```

### [4] ASSISTANT · 2026-06-16 17:25:11 UTC

```
I'll research the key technical components before writing the plan.
```

### [5] TOOL CALL — Skill · 2026-06-16 17:25:11 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-06-16 17:25:11 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — ToolSearch · 2026-06-16 17:25:33 UTC

```
{'query': 'select:WebSearch,WebFetch'}
```

### [8] TOOL RESULT — ToolSearch · 2026-06-16 17:25:33 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [9] ASSISTANT · 2026-06-16 17:26:11 UTC

```
Now let me do parallel research on key components for the plan.
```

### [10] TOOL CALL — WebSearch · 2026-06-16 17:26:11 UTC

```
karpathy nanoGPT minimal GPT PyTorch character level language model implementation 2024
```

### [11] TOOL CALL — WebSearch · 2026-06-16 17:26:11 UTC

```
DEQ deep equilibrium model implicit function theorem gradient custom autograd PyTorch backward 2024
```

### [12] TOOL CALL — WebSearch · 2026-06-16 17:26:11 UTC

```
WikiText-2 dataset HuggingFace datasets word-level GPT perplexity PyTorch 2024
```

### [13] TOOL RESULT — WebSearch · 2026-06-16 17:26:26 UTC

```
{"query": "karpathy nanoGPT minimal GPT PyTorch character level language model implementation 2024", "results": [{"tool_use_id": "srvtoolu_01Muta58o1oAzdmEJV7iaP6i", "content": [{"title": "GitHub - karpathy/minGPT: A minimal PyTorch re-implementation of the OpenAI GPT (Generative Pretrained Transformer) training · GitHub", "url": "https://github.com/karpathy/minGPT"}, {"title": "karpathy (Andrej) / Repositories · GitHub", "url": "https://github.com/karpathy?tab=repositories"}, {"title": "Andrej Karpathy’s NanoGPT", "url": "https://medium.com/predict/andrej-karpathys-nanogpt-4dbcb00fb97f"}, {"title": "GitHub - jbxamora/reversenanogpt: A minimal character-level language model using Transformer architecture in PyTorch · GitHub", "url": "https://github.com/jbxamora/reversenanogpt"}, {"title": "GitHub - gs-101/nanoGPT-from-scratch: Model created by following the \"Let's build GPT: from scratch, in code, spelled out.\" lecture by Andrej Karpathy, in Org Mode. · GitHub", "url": "https://github.com/gs-101/nanoGPT-from-scratch"}, {"title": "Training NanoGPT on Modal - AI Engineering Academy", "url": "https://aiengineering.academy/LLM/ServerLessFinetuning/TrainNanoGPTModalTutorial/"}, {"title": "nanoGPT/model.py at master · karpathy/nanoGPT", "url": "https://github.com/karpathy/nanoGPT/blob/master/model.py"}, {"title": "nano-gpt · PyPI", "url": "https://pypi.org/project/nano-gpt/"}, {"title": "GitHub - karpathy/nanoGPT: The simplest, fastest repository for training/finetuning medium-sized GPTs. · GitHub", "url": "https://github.com/karpathy/nanoGPT"}]}, "I've performed the web search on \"karpathy nanoGPT minimal GPT PyTorch character level language model implementation 2024\". Here are the key findings:\n\n## Overview\n\nNanoGPT, created by Andrej Karpathy, is an open-source project designed to simplify and democratize the training of GPT-like language models. It's only ~300 lines of clean PyTorch code.\n\n## Purpose and Design\n\nnanoGPT is Karpathy's rewrite that aimed to change direction from a sole focus on education to something that is still simple and hackable but has teeth (reproduces medium-sized industry benchmarks, accepts some tradeoffs to gain runtime efficiency, etc).\n\n## Architecture and Components\n\nIts streamlined codebase, built in PyTorch with minimal dependencies, centers on a few key files: model.py for defining the transformer architecture, train.py for managing the training process, and sample.py for generating text outputs.\n\n## Character-Level Implementation\n\nThe model can be trained on a character-level GPT on Shakespeare's collected works. The model starts by converting the input characters into embeddings using a token embedding table and utilizes positional embeddings for each token, which allows the model to understand the order of the input characters.\n\n## Educational Value\n\nAndrej Karpathy built this as an educational implementation that's simple enough to understand but powerful enough to actually train real models, and if you've ever wondered how GPT actually works under the hood, this is the best place to start."], "durationSeconds": 19.270285618000024, "searchCount": 1}
```

### [14] TOOL RESULT — WebSearch · 2026-06-16 17:26:36 UTC

```
{"query": "DEQ deep equilibrium model implicit function theorem gradient custom autograd PyTorch backward 2024", "results": [{"tool_use_id": "srvtoolu_01Ahh8EhwTpWPWJ7MMYWZurT", "content": [{"title": "Deep Equilibrium Models: Neural Networks Without Layers | by Void | Medium", "url": "https://medium.com/@atulit23/deep-equilibrium-models-neural-networks-without-layers-4dd1b1095503"}, {"title": "GitHub - locuslab/deq: [NeurIPS'19] Deep Equilibrium Models · GitHub", "url": "https://github.com/locuslab/deq"}, {"title": "Equivariant Deep Equilibrium Models for Imaging Inverse Problems", "url": "https://arxiv.org/pdf/2511.18667"}, {"title": "TorchDEQ: A Library for Deep Equilibrium Models Zhengyang Geng1", "url": "https://arxiv.org/pdf/2310.18605"}, {"title": "Deep Equilibrium Models", "url": "https://arxiv.org/pdf/1909.01377"}, {"title": "Deep Equilibrium Models - GeeksforGeeks", "url": "https://www.geeksforgeeks.org/deep-learning/deep-equilibrium-models/"}, {"title": "The Deep Equilibrium Algorithmic Reasoner", "url": "https://arxiv.org/pdf/2402.06445"}, {"title": "Solving Differential Equations using Physics-Informed Deep Equilibrium   Models", "url": "https://arxiv.org/pdf/2406.03472"}, {"title": "Efficient Training of Deep Equilibrium Models", "url": "https://arxiv.org/pdf/2304.11663"}, {"title": "Gradient descent for deep equilibrium single-index models", "url": "https://arxiv.org/pdf/2511.16976"}]}, "I found comprehensive information about DEQ (Deep Equilibrium) models and their gradient computation. Here's a summary of the key findings:\n\n## Core Concept\n\nDeep equilibrium models (DEQs) are a class of implicit neural networks where functions are modeled as z* = f_θ(z*, x), with x as input, f_θ as a parameterized function, and z* as the output.\n\n## Implicit Function Theorem & Gradient Computation\n\nDEQs use the implicit function theorem to compute gradients with respect to parameters efficiently and save memory because the intermediate states of the solver don't need to be stored. One of the core benefits of the DEQ approach comes from its analytical backward gradient at equilibrium.\n\nUsing the implicit function theorem, gradients with respect to model parameters θ can be computed as ∂ℓ/∂θ = (∂f/∂θ)A(∂ℓ/∂z*), where A = (I - ∂f/∂z*)^(-1).\n\n## Custom Autograd Implementation in PyTorch\n\nA PyTorch implementation uses a custom `DEQFunction` class extending `torch.autograd.Function` with a forward method that iteratively solves for the equilibrium z*, and a backward method that computes gradients by solving a linear system involving the Jacobian.\n\nThe backward pass relies on implicit function theorem and uses PyTorch's register_hook function to register a backward hook, solving for the fixed point of a linear system involving the Jacobian at the equilibrium.\n\n## Recent Libraries (2024)\n\nThe TorchDEQ library supports two types of backward passes: implicit differentiation (IFT) and phantom gradients (PG)."], "durationSeconds": 27.988959455000003, "searchCount": 1}
```

### [15] TOOL RESULT — WebSearch · 2026-06-16 17:26:38 UTC

```
{"query": "WikiText-2 dataset HuggingFace datasets word-level GPT perplexity PyTorch 2024", "results": [{"tool_use_id": "srvtoolu_01AkWsFaTrjPCXFUYbVN9Z2r", "content": [{"title": "Is perplexity correctly computed? · Issue #560 · huggingface/evaluate", "url": "https://github.com/huggingface/evaluate/issues/560"}, {"title": "Intel/distilgpt2-wikitext2 · Hugging Face", "url": "https://huggingface.co/Intel/distilgpt2-wikitext2"}, {"title": "Extremely high perplexity on openai/gpt-oss-20b with WikiText-2 (raw) · Issue #40990 · huggingface/transformers", "url": "https://github.com/huggingface/transformers/issues/40990"}, {"title": "evaluate-measurement/perplexity · Results on Wikitext-2 with GPT2 don't match paper", "url": "https://huggingface.co/spaces/evaluate-measurement/perplexity/discussions/1"}, {"title": "perplexity very high on wikitext for GPT2XL - PyTorch Forums", "url": "https://discuss.pytorch.org/t/perplexity-very-high-on-wikitext-for-gpt2xl/212273"}, {"title": "transformers/examples/pytorch/language-modeling/README.md at main · huggingface/transformers", "url": "https://github.com/huggingface/transformers/blob/main/examples/pytorch/language-modeling/README.md"}, {"title": "perplexity too big for gpt2 wikitext evaluation · Issue #6 · NVIDIA/Megatron-LM", "url": "https://github.com/NVIDIA/Megatron-LM/issues/6"}, {"title": "Warm-Start Flow Matching for Guaranteed Fast Text/Image Generation", "url": "https://arxiv.org/pdf/2603.19360"}, {"title": "OATS: Outlier-Aware Pruning Through Sparse and Low Rank Decomposition", "url": "https://arxiv.org/pdf/2409.13652"}]}, "I've performed the web search for your query about WikiText-2 dataset, HuggingFace datasets, word-level GPT perplexity, and PyTorch 2024. Here are the relevant results:\n\n## Key Findings:\n\n**WikiText-2 Dataset Access and Usage:**\nWikiText-2 can be loaded from HuggingFace's datasets library using `datasets.load_dataset(\"wikitext\", \"wikitext-2-raw-v1\", split=\"test\")`.\n\n**Perplexity Evaluation with GPT Models:**\nFine-tuning GPT-2 on WikiText-2-raw-v1 can reach approximately 20 perplexity. A distilled GPT-2 model fine-tuned on WikiText-2-raw-v1 achieved a perplexity of 27.8235.\n\n**PyTorch Integration:**\nPyTorch 1.12.1 has been used in conjunction with the HuggingFace transformers library for model evaluation on WikiText-2.\n\n**Common Challenges (2024):**\nUsers have reported difficulties replicating reported perplexity values when evaluating models like LLaMa-2-7b on WikiText-2 using the HuggingFace evaluate library, highlighting that perplexity computation methodologies can significantly impact results.\n\nThe search results show active discussion and implementation of WikiText-2 evaluation with various GPT-class models throughout 2024, with perplexity scores varying based on the specific model and computation methodology used."], "durationSeconds": 25.303330183999993, "searchCount": 1}
```

### [16] ASSISTANT · 2026-06-16 17:27:29 UTC

```
Good. Now let me fetch the nanoGPT architecture details and DEQ IFT implementation details in parallel.
```

### [17] TOOL CALL — WebFetch · 2026-06-16 17:27:29 UTC

```
URL: https://github.com/karpathy/nanoGPT/blob/master/model.py
Prompt: Extract the exact GPT architecture: Block, CausalSelfAttention, MLP/FFN class definitions, forward pass shapes, and how GELU is used in the MLP. Include key hyperparameters.
```

### [18] TOOL CALL — WebFetch · 2026-06-16 17:27:29 UTC

```
URL: https://github.com/locuslab/deq
Prompt: How does DEQ implement the implicit function theorem backward pass in PyTorch? What is the exact custom autograd Function structure? What tensors are saved in forward for use in backward?
```

### [19] TOOL RESULT — WebFetch · 2026-06-16 17:27:29 UTC

````
{"bytes": 329263, "code": 200, "codeText": "OK", "result": "# DEQ Backward Pass Implementation\n\nBased on the repository documentation, DEQ implements the implicit function theorem backward pass using **PyTorch's backward hook mechanism** rather than a custom autograd Function.\n\n## Key Implementation Details\n\n**Forward Pass:**\nThe forward pass solves for the fixed point without storing intermediate states:\n```\nwith torch.no_grad():\n    z_star = solver(lambda z: f(z, x, *args), z0)['result']\n```\n\n**Backward Pass Strategy:**\nInstead of a custom autograd Function, DEQ registers a backward hook on the equilibrium state. The documentation states:\n\n> \"we can use the `register_hook` function in PyTorch that registers a backward hook function to be executed in the backward pass.\"\n\n**Saved Tensors:**\nFor backward computation, the framework saves:\n- `z_star`: The equilibrium fixed point\n- `new_z_star`: The transformation output at equilibrium (requires gradients during training)\n- `x`: The input injection\n\n**Hook Computation:**\nThe backward hook solves another fixed-point problem involving the Jacobian:\n\n> \"Compute the fixed point of yJ + grad, where J=J_f is the Jacobian of f at z_star\"\n\nThis avoids materializing the full Jacobian matrix explicitly, using only vector-Jacobian products via `autograd.grad()`.\n\nThis design enables O(1) memory complexity despite arbitrarily deep implicit depth.", "durationMs": 11657, "url": "https://github.com/locuslab/deq"}
````

### [20] TOOL RESULT — WebFetch · 2026-06-16 17:27:31 UTC

```
{"bytes": 369852, "code": 200, "codeText": "OK", "result": "# nanoGPT Architecture Summary\n\n## Core Components\n\n**Block Structure**: The foundational transformer block combines residual connections with layer normalization. Each block applies:\n1. Layer norm → Causal self-attention → residual add\n2. Layer norm → MLP → residual add\n\n**CausalSelfAttention**: Implements multi-head attention with Flash Attention support (PyTorch 2.0+). Key aspects:\n- Projects input to query/key/value: `nn.Linear(n_embd, 3 * n_embd)`\n- Splits into `n_head` heads with dimension `n_embd // n_head`\n- Applies causal masking via lower triangular bias matrix\n- Uses `scaled_dot_product_attention` or manual attention computation\n- Output projection: `nn.Linear(n_embd, n_embd)`\n\n**MLP (Feed-Forward Network)**: Implements the typical two-layer FFN:\n- Expansion: `nn.Linear(n_embd, 4 * n_embd)` \n- Activation: \"GELU activation function\"\n- Projection: `nn.Linear(4 * n_embd, n_embd)`\n- Dropout applied post-projection\n\n## Forward Pass Shapes\n\nToken embeddings shape: `(batch, sequence_length, n_embd)`\n\nAfter multi-head split: `(batch, n_head, sequence_length, head_size)`\n\nAttention output: recombined to `(batch, sequence_length, n_embd)`\n\n## Key Hyperparameters\n\nDefault GPTConfig values:\n- `block_size`: 1024 (context window)\n- `vocab_size`: 50,304\n- `n_layer`: 12 (transformer blocks)\n- `n_head`: 12 (attention heads)\n- `n_embd`: 768 (embedding dimension)\n- `dropout`: 0.0", "durationMs": 13997, "url": "https://github.com/karpathy/nanoGPT/blob/master/model.py"}
```

### [21] ASSISTANT · 2026-06-16 17:31:39 UTC

```
Now I have all I need. Let me write the detailed plan.
```

### [22] TOOL CALL — Read · 2026-06-16 17:31:39 UTC

```
/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_3
```

### [23] TOOL RESULT — Read [ERROR] · 2026-06-16 17:31:39 UTC

```
Error: EISDIR: illegal operation on a directory, read '/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_3'
```

### [24] TOOL CALL — Glob · 2026-06-16 17:31:41 UTC

```
Pattern: "*"
```

### [25] TOOL RESULT — Glob · 2026-06-16 17:31:41 UTC

```
{"filenames": [".repl_agent.ptylog"], "durationMs": 26, "numFiles": 1, "truncated": false}
```

### [26] ASSISTANT · 2026-06-16 17:34:25 UTC

```
Now I'll write the complete plan.
```

### [27] TOOL CALL — Write · 2026-06-16 17:34:25 UTC

````
File: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_3/.terminal_claude_agent_struct_out.json

{
  "title": "CWA Language Model Experiment: 6-Layer/256-Hidden GPT on Tiny Shakespeare and WikiText-2",
  "summary": "Implement a minimal GPT in PyTorch (6 layers, 256 hidden, 8 heads, 4x MLP expansion) with a custom Curie-Weiss Activation (CWA) replacing GELU in FFN blocks. Train character-level on Tiny Shakespeare (3 seeds, 10K steps) and word-level (tiktoken BPE) on WikiText-2 (2 seeds, 20K steps). Compare test BPC and perplexity against GELU, GELU+LN, SELU, and tanh+Swish@0.5 baselines. Track per-layer J, J·s̄, K, backprop mode, and peak GPU memory throughout training. Output method_out.json.",
  "runpod_compute_profile": "gpu",
  "implementation_pseudocode": "# ============================================================\n# FILE STRUCTURE\n# ============================================================\n# method.py        — main orchestrator (run this)\n# cwa_activation.py — CWAActivation + CWAIFTFunction\n# gpt_model.py     — GPT, Block, CausalSelfAttention, MLP, baselines\n# data_utils.py    — Shakespeare + WikiText-2 loaders\n# train_utils.py   — train loop, eval, memory measurement\n\n# ============================================================\n# cwa_activation.py\n# ============================================================\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\n\n\nclass CWAIFTFunction(torch.autograd.Function):\n    \"\"\"IFT backward for CWA when J·s̄ >= 0.8 (O(1) activation memory).\"\"\"\n    @staticmethod\n    def forward(ctx, x, J, m_star):\n        # m_star: [B, T, 1] — already converged fixed point (detached)\n        y_star = torch.tanh(x + J * m_star)\n        s_bar = 1.0 - y_star.pow(2)          # sech² per element [B, T, H]\n        s_bar_mean = s_bar.mean(dim=-1, keepdim=True)  # [B, T, 1]\n        ctx.save_for_backward(J, m_star, s_bar, s_bar_mean)\n        return y_star\n\n    @staticmethod\n    def backward(ctx, grad_y):\n        J, m_star, s_bar, s_bar_mean = ctx.saved_tensors\n        J_val = J.item()\n        n = grad_y.shape[-1]  # hidden dim = 4 * n_embd\n        denom = (1.0 - J_val * s_bar_mean).clamp(min=1e-4)  # [B, T, 1]\n\n        # IFT gradient for x:\n        # ∂L/∂x_i = sech²_i * [grad_y_i + (J/n) * Σ_j(grad_y_j * sech²_j) / denom]\n        weighted_sum = (grad_y * s_bar).sum(dim=-1, keepdim=True)  # [B, T, 1]\n        grad_x = s_bar * (grad_y + J_val * weighted_sum / (n * denom))\n\n        # IFT gradient for J (scalar):\n        # ∂L/∂J = Σ_{i,b,t} grad_y_i * sech²_i * m*_i / denom_i\n        grad_J = (grad_y * s_bar * m_star / denom).sum().unsqueeze(0)\n\n        return grad_x, grad_J, None  # no grad for m_star\n\n\nclass CWAActivation(nn.Module):\n    \"\"\"Curie-Weiss Activation: fixed point of y = tanh(x + J * mean_h(y)).\n\n    J = sigmoid(J_raw) in (0, 1). init J_raw=0 so J starts at 0.5.\n    Hybrid backward: unrolled autograd if J·s̄ < 0.8, IFT if J·s̄ >= 0.8.\n    \"\"\"\n    def __init__(self):\n        super().__init__()\n        self.J_raw = nn.Parameter(torch.zeros(1))\n        # Internal stats for logging (updated in-place each forward call)\n        self._last_J = 0.5\n        self._last_J_s_bar = 0.5\n        self._last_K = 0\n        self._last_mode = 'unrolled'\n\n    def forward(self, x):\n        # x: [B, T, H] where H = 4 * n_embd (MLP expanded dimension)\n        J = torch.sigmoid(self.J_raw)   # scalar in (0,1)\n        J_val = J.item()\n\n        # --- Step 1: Find m* without gradient tracking ---\n        with torch.no_grad():\n            m = torch.zeros(*x.shape[:-1], 1, device=x.device, dtype=x.dtype)  # [B, T, 1]\n            K_used = 0\n            J_s_bar_final = J_val * 1.0  # upper bound before first step\n            for k in range(50):          # K_max = 50\n                y_tmp = torch.tanh(x + J_val * m)\n                m_new = y_tmp.mean(dim=-1, keepdim=True)\n                # Compute s̄ and adaptive tolerance\n                s_bar_tmp = (1.0 - y_tmp.pow(2)).mean().item()   # scalar mean\n                J_s_bar_cur = J_val * s_bar_tmp\n                delta = 1e-4 * max(1.0 - J_s_bar_cur, 1e-2) + 1e-8\n                diff = (m_new - m).abs().max().item()\n                m = m_new\n                K_used = k + 1\n                J_s_bar_final = J_s_bar_cur\n                if diff < delta:\n                    break\n            m_star = m.clone()   # [B, T, 1], detached\n\n        # --- Step 2: Decide backprop mode based on J·s̄ ---\n        if J_s_bar_final < 0.8:\n            # Unrolled autograd: warm-start from m_star (detached), run 3 tracked steps\n            # This is accurate because m_star is close to the true fixed point\n            m_tracked = m_star.detach()\n            for _ in range(3):\n                m_tracked = torch.tanh(x + J * m_tracked).mean(dim=-1, keepdim=True)\n            y_out = torch.tanh(x + J * m_tracked)\n            mode = 'unrolled'\n        else:\n            # IFT mode: O(1) activation memory, analytic gradient\n            y_out = CWAIFTFunction.apply(x, J, m_star)\n            mode = 'ift'\n\n        # Update logging stats (no autograd side effects)\n        with torch.no_grad():\n            y_check = torch.tanh(x + J_val * m_star)\n            s_bar_check = (1.0 - y_check.pow(2)).mean().item()\n            J_s_bar_final = J_val * s_bar_check\n        self._last_J = J_val\n        self._last_J_s_bar = J_s_bar_final\n        self._last_K = K_used\n        self._last_mode = mode\n\n        return y_out\n\n\n# ============================================================\n# gpt_model.py\n# ============================================================\n\nimport math\nimport torch, torch.nn as nn, torch.nn.functional as F\nfrom cwa_activation import CWAActivation\n\n\nclass TanhSwishMixture(nn.Module):\n    \"\"\"p * tanh(x) + (1-p) * swish(x); p_c=0.5 as default.\"\"\"\n    def __init__(self, p=0.5):\n        super().__init__()\n        self.p = p\n    def forward(self, x):\n        return self.p * torch.tanh(x) + (1.0 - self.p) * F.silu(x)\n\n\ndef make_activation(name, n_embd):\n    \"\"\"Return the activation module for use inside MLP.\"\"\"\n    mlp_dim = 4 * n_embd\n    if name == 'gelu':\n        return nn.GELU()\n    elif name == 'gelu+ln':\n        # LayerNorm applied after GELU inside the FFN expansion\n        return nn.Sequential(nn.GELU(), nn.LayerNorm(mlp_dim))\n    elif name == 'selu':\n        return nn.SELU()\n    elif name == 'tanh_swish':\n        return TanhSwishMixture(p=0.5)\n    elif name == 'cwa':\n        return CWAActivation()\n    else:\n        raise ValueError(f'Unknown activation: {name}')\n\n\nclass MLP(nn.Module):\n    def __init__(self, n_embd, activation_name='gelu', dropout=0.1):\n        super().__init__()\n        self.c_fc   = nn.Linear(n_embd, 4 * n_embd)\n        self.act    = make_activation(activation_name, n_embd)\n        self.c_proj = nn.Linear(4 * n_embd, n_embd)\n        self.drop   = nn.Dropout(dropout)\n\n    def forward(self, x):\n        x = self.c_fc(x)\n        x = self.act(x)\n        x = self.c_proj(x)\n        return self.drop(x)\n\n\nclass CausalSelfAttention(nn.Module):\n    def __init__(self, n_embd, n_head, dropout=0.1, block_size=2048):\n        super().__init__()\n        assert n_embd % n_head == 0\n        self.c_attn  = nn.Linear(n_embd, 3 * n_embd)\n        self.c_proj  = nn.Linear(n_embd, n_embd)\n        self.attn_drop  = nn.Dropout(dropout)\n        self.resid_drop = nn.Dropout(dropout)\n        self.n_head = n_head\n        self.n_embd = n_embd\n        # Causal mask buffer (not a parameter)\n        self.register_buffer('bias',\n            torch.tril(torch.ones(block_size, block_size)).view(1, 1, block_size, block_size))\n\n    def forward(self, x):\n        B, T, C = x.shape\n        q, k, v = self.c_attn(x).split(self.n_embd, dim=2)\n        k = k.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)\n        q = q.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)\n        v = v.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)\n        # Use flash attention when available (PyTorch 2.0+)\n        use_flash = hasattr(F, 'scaled_dot_product_attention')\n        if use_flash:\n            y = F.scaled_dot_product_attention(q, k, v, attn_mask=None,\n                                                dropout_p=0.0, is_causal=True)\n        else:\n            att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(k.size(-1)))\n            att = att.masked_fill(self.bias[:, :, :T, :T] == 0, float('-inf'))\n            att = F.softmax(att, dim=-1)\n            att = self.attn_drop(att)\n            y = att @ v\n        y = y.transpose(1, 2).contiguous().view(B, T, C)\n        return self.resid_drop(self.c_proj(y))\n\n\nclass Block(nn.Module):\n    def __init__(self, n_embd, n_head, activation_name='gelu', dropout=0.1, block_size=2048):\n        super().__init__()\n        self.ln_1 = nn.LayerNorm(n_embd)\n        self.attn = CausalSelfAttention(n_embd, n_head, dropout, block_size)\n        self.ln_2 = nn.LayerNorm(n_embd)\n        self.mlp  = MLP(n_embd, activation_name, dropout)\n\n    def forward(self, x):\n        x = x + self.attn(self.ln_1(x))\n        x = x + self.mlp(self.ln_2(x))\n        return x\n\n\nclass GPT(nn.Module):\n    def __init__(self, vocab_size, n_layer=6, n_head=8, n_embd=256,\n                 block_size=256, dropout=0.1, activation_name='gelu'):\n        super().__init__()\n        self.tok_emb = nn.Embedding(vocab_size, n_embd)\n        self.pos_emb = nn.Embedding(block_size, n_embd)\n        self.drop    = nn.Dropout(dropout)\n        self.blocks  = nn.ModuleList([\n            Block(n_embd, n_head, activation_name, dropout, block_size)\n            for _ in range(n_layer)\n        ])\n        self.ln_f    = nn.LayerNorm(n_embd)\n        self.lm_head = nn.Linear(n_embd, vocab_size, bias=False)\n        self.block_size = block_size\n        # Init weights\n        self.apply(self._init_weights)\n\n    def _init_weights(self, module):\n        if isinstance(module, nn.Linear):\n            nn.init.normal_(module.weight, mean=0.0, std=0.02)\n            if module.bias is not None:\n                nn.init.zeros_(module.bias)\n        elif isinstance(module, nn.Embedding):\n            nn.init.normal_(module.weight, mean=0.0, std=0.02)\n        # J_raw in CWAActivation is initialized to 0.0 by nn.Parameter default\n\n    def forward(self, idx, targets=None):\n        B, T = idx.shape\n        assert T <= self.block_size\n        pos = torch.arange(T, device=idx.device, dtype=torch.long)\n        x = self.drop(self.tok_emb(idx) + self.pos_emb(pos))\n        for block in self.blocks:\n            x = block(x)\n        x = self.ln_f(x)\n        logits = self.lm_head(x)   # [B, T, vocab_size]\n        loss = None\n        if targets is not None:\n            loss = F.cross_entropy(\n                logits.view(-1, logits.size(-1)), targets.view(-1)\n            )\n        return logits, loss\n\n    def get_cwa_stats(self):\n        \"\"\"Collect CWA diagnostics from all layers (if activation is CWA).\"\"\"\n        stats = {}\n        for i, block in enumerate(self.blocks):\n            act = block.mlp.act\n            # For gelu+ln, act is Sequential — no CWA stats\n            if isinstance(act, CWAActivation):\n                stats[f'layer_{i}'] = {\n                    'J':       act._last_J,\n                    'J_s_bar': act._last_J_s_bar,\n                    'K':       act._last_K,\n                    'mode':    act._last_mode,\n                }\n        return stats\n\n\n# ============================================================\n# data_utils.py\n# ============================================================\n\nimport os, requests, math\nimport torch\n\n\ndef load_shakespeare(seq_len, batch_size, device):\n    \"\"\"Download and tokenize Tiny Shakespeare. Returns (train, val, test, vocab_size, decode_fn).\"\"\"\n    url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'\n    os.makedirs('data', exist_ok=True)\n    path = 'data/shakespeare.txt'\n    if not os.path.exists(path):\n        r = requests.get(url)\n        with open(path, 'w') as f:\n            f.write(r.text)\n    text = open(path).read()\n    chars = sorted(set(text))\n    vocab_size = len(chars)\n    stoi = {ch: i for i, ch in enumerate(chars)}\n    itos = {i: ch for ch, i in stoi.items()}\n    data = torch.tensor([stoi[c] for c in text], dtype=torch.long)\n    n = len(data)\n    train_data = data[:int(0.90 * n)]\n    val_data   = data[int(0.90 * n):int(0.95 * n)]\n    test_data  = data[int(0.95 * n):]\n    decode = lambda ids: ''.join(itos[i] for i in ids)\n\n    def get_batch(split):\n        d = {'train': train_data, 'val': val_data, 'test': test_data}[split]\n        ix = torch.randint(len(d) - seq_len, (batch_size,))\n        x  = torch.stack([d[i:i+seq_len] for i in ix]).to(device)\n        y  = torch.stack([d[i+1:i+seq_len+1] for i in ix]).to(device)\n        return x, y\n\n    return get_batch, vocab_size, decode\n\n\ndef load_wikitext2(seq_len, batch_size, device):\n    \"\"\"Load WikiText-2 with tiktoken BPE. Returns (get_batch_fn, vocab_size).\"\"\"\n    from datasets import load_dataset\n    import tiktoken\n    enc = tiktoken.get_encoding('gpt2')  # vocab_size = 50257\n    vocab_size = enc.n_vocab\n\n    ds = load_dataset('wikitext', 'wikitext-2-raw-v1')\n\n    def tokenize_split(split_name):\n        texts = ds[split_name]['text']\n        tokens = []\n        for t in texts:\n            t = t.strip()\n            if t:\n                # encode_ordinary avoids adding BOS/EOS special tokens\n                tokens.extend(enc.encode_ordinary(t))\n        return torch.tensor(tokens, dtype=torch.long)\n\n    train_data = tokenize_split('train')\n    val_data   = tokenize_split('validation')\n    test_data  = tokenize_split('test')\n\n    def get_batch(split):\n        d = {'train': train_data, 'val': val_data, 'test': test_data}[split]\n        ix = torch.randint(len(d) - seq_len, (batch_size,))\n        x  = torch.stack([d[i:i+seq_len] for i in ix]).to(device)\n        y  = torch.stack([d[i+1:i+seq_len+1] for i in ix]).to(device)\n        return x, y\n\n    return get_batch, vocab_size\n\n\n# ============================================================\n# train_utils.py\n# ============================================================\n\nimport math, time\nimport torch, torch.nn as nn\nfrom collections import defaultdict\n\n\ndef get_cosine_lr(step, max_steps, lr, warmup_steps):\n    if step < warmup_steps:\n        return lr * step / max(warmup_steps, 1)\n    t = (step - warmup_steps) / max(max_steps - warmup_steps, 1)\n    return lr * 0.5 * (1.0 + math.cos(math.pi * t))\n\n\ndef evaluate(model, get_batch, n_batches=50):\n    \"\"\"Return mean cross-entropy loss over n_batches random batches.\"\"\"\n    model.eval()\n    losses = []\n    with torch.no_grad():\n        for _ in range(n_batches):\n            x, y = get_batch('val')\n            _, loss = model(x, y)\n            losses.append(loss.item())\n    model.train()\n    return sum(losses) / len(losses)\n\n\ndef evaluate_test(model, get_batch, n_batches=100):\n    model.eval()\n    losses = []\n    with torch.no_grad():\n        for _ in range(n_batches):\n            x, y = get_batch('test')\n            _, loss = model(x, y)\n            losses.append(loss.item())\n    model.train()\n    return sum(losses) / len(losses)\n\n\ndef measure_peak_memory_mb(model, get_batch, device):\n    \"\"\"Measure peak GPU memory over one forward+backward pass.\"\"\"\n    if not torch.cuda.is_available():\n        return 0.0\n    torch.cuda.reset_peak_memory_stats(device)\n    model.train()\n    x, y = get_batch('train')\n    _, loss = model(x, y)\n    loss.backward()\n    model.zero_grad()\n    return torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n\n\ndef train_model(model, get_batch, config, activation_name):\n    \"\"\"\n    Train model for config.max_steps steps.\n    config fields: max_steps, lr, warmup_steps, grad_clip, eval_every, log_every\n    Returns: (final_val_loss, cwa_trajectory dict)\n    \"\"\"\n    optimizer = torch.optim.AdamW(\n        model.parameters(), lr=config['lr'],\n        weight_decay=0.1, betas=(0.9, 0.95)\n    )\n    cwa_traj = defaultdict(list)   # layer_id -> list of stat dicts\n    backprop_counts = {'unrolled': 0, 'ift': 0}\n    t0 = time.time()\n\n    for step in range(config['max_steps']):\n        # LR schedule\n        lr = get_cosine_lr(step, config['max_steps'], config['lr'], config['warmup_steps'])\n        for g in optimizer.param_groups:\n            g['lr'] = lr\n\n        # Forward + backward\n        x, y = get_batch('train')\n        logits, loss = model(x, y)\n        optimizer.zero_grad(set_to_none=True)\n        loss.backward()\n        nn.utils.clip_grad_norm_(model.parameters(), config['grad_clip'])\n        optimizer.step()\n\n        # Collect CWA stats every log_every steps\n        if activation_name == 'cwa' and step % config.get('log_every', 500) == 0:\n            stats = model.get_cwa_stats()\n            for layer_key, s in stats.items():\n                cwa_traj[layer_key].append({'step': step, **s})\n                if s['mode'] == 'unrolled':\n                    backprop_counts['unrolled'] += 1\n                else:\n                    backprop_counts['ift'] += 1\n\n        # Print progress\n        if step % config.get('eval_every', 500) == 0:\n            val_loss = evaluate(model, get_batch, n_batches=50)\n            elapsed = time.time() - t0\n            print(f'  step {step}/{config[\"max_steps\"]}: '\n                  f'train_loss={loss.item():.4f} val_loss={val_loss:.4f} '\n                  f'lr={lr:.2e} elapsed={elapsed:.1f}s')\n\n    final_val = evaluate(model, get_batch, n_batches=50)\n    total = backprop_counts['unrolled'] + backprop_counts['ift']\n    bp_stats = {\n        'unrolled_count': backprop_counts['unrolled'],\n        'ift_count': backprop_counts['ift'],\n        'unrolled_fraction': backprop_counts['unrolled'] / max(total, 1),\n        'ift_fraction':  backprop_counts['ift'] / max(total, 1),\n    }\n    return final_val, dict(cwa_traj), bp_stats\n\n\n# ============================================================\n# method.py — MAIN ORCHESTRATOR\n# ============================================================\n\nimport json, math, random, os, time\nimport numpy as np\nimport torch\nfrom collections import defaultdict\n\nfrom cwa_activation import CWAActivation\nfrom gpt_model import GPT\nfrom data_utils import load_shakespeare, load_wikitext2\nfrom train_utils import train_model, evaluate_test, measure_peak_memory_mb\n\n\n# -------- reproducibility --------\ndef set_seed(seed):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n    torch.backends.cudnn.deterministic = True\n\n\n# -------- configs --------\nSHAKES_CONFIG = {\n    'seq_len': 256, 'batch_size': 64, 'max_steps': 10_000,\n    'lr': 3e-4, 'warmup_steps': 200, 'grad_clip': 1.0,\n    'eval_every': 500, 'log_every': 500,\n}\nWT2_CONFIG = {\n    'seq_len': 128, 'batch_size': 32, 'max_steps': 20_000,\n    'lr': 3e-4, 'warmup_steps': 400, 'grad_clip': 1.0,\n    'eval_every': 1000, 'log_every': 1000,\n}\n\nGPT_COMMON = dict(n_layer=6, n_head=8, n_embd=256, dropout=0.1)\n\nACTIVATIONS = ['gelu', 'gelu+ln', 'selu', 'tanh_swish', 'cwa']\nSHAKES_SEEDS  = [42, 123, 7]\nWT2_SEEDS     = [42, 123]\n\ndevice = 'cuda' if torch.cuda.is_available() else 'cpu'\nprint(f'Using device: {device}')\n\n\n# -------- SHAKESPEARE --------\nprint('\\n===== SHAKESPEARE =====')\nresults_shakes = {}\ncwa_traj_shakes = {}\nmemory_shakes = {}\nbp_stats_shakes = {}\n\nfor act in ACTIVATIONS:\n    print(f'\\n--- Activation: {act} ---')\n    bpcs_per_seed = []\n    for si, seed in enumerate(SHAKES_SEEDS):\n        set_seed(seed)\n        # Load data (re-create get_batch with same shuffle seed)\n        get_batch, vocab_size, decode = load_shakespeare(\n            SHAKES_CONFIG['seq_len'], SHAKES_CONFIG['batch_size'], device\n        )\n        model = GPT(vocab_size=vocab_size, block_size=256,\n                    activation_name=act, **GPT_COMMON).to(device)\n        n_params = sum(p.numel() for p in model.parameters())\n        print(f'  seed={seed}, params={n_params/1e6:.2f}M')\n\n        # Measure peak memory for first activation + first seed only\n        if si == 0:\n            mem_mb = measure_peak_memory_mb(model, get_batch, device)\n            memory_shakes[act] = mem_mb\n            print(f'  Peak GPU memory: {mem_mb:.1f} MB')\n            # Reinit model and optimizer state after memory measurement\n            model = GPT(vocab_size=vocab_size, block_size=256,\n                        activation_name=act, **GPT_COMMON).to(device)\n            set_seed(seed)  # re-seed after measurement\n\n        final_val, cwa_traj, bp_stats = train_model(\n            model, get_batch, SHAKES_CONFIG, act\n        )\n        test_loss = evaluate_test(model, get_batch, n_batches=100)\n        bpc = test_loss / math.log(2.0)   # nats -> bits per character\n        bpcs_per_seed.append(bpc)\n        print(f'  seed={seed}: test_loss={test_loss:.4f}, BPC={bpc:.4f}')\n\n        if act == 'cwa':\n            cwa_traj_shakes[f'seed_{seed}'] = cwa_traj\n            bp_stats_shakes[f'seed_{seed}'] = bp_stats\n\n    results_shakes[act] = {\n        'mean': float(np.mean(bpcs_per_seed)),\n        'std':  float(np.std(bpcs_per_seed)),\n        'per_seed': [float(v) for v in bpcs_per_seed],\n    }\n\n\n# -------- WIKITEXT-2 --------\nprint('\\n===== WIKITEXT-2 =====')\nresults_wt2 = {}\ncwa_traj_wt2 = {}\nmemory_wt2 = {}\nbp_stats_wt2 = {}\n\nfor act in ACTIVATIONS:\n    print(f'\\n--- Activation: {act} ---')\n    ppls_per_seed = []\n    for si, seed in enumerate(WT2_SEEDS):\n        set_seed(seed)\n        get_batch_wt2, vocab_size_wt2 = load_wikitext2(\n            WT2_CONFIG['seq_len'], WT2_CONFIG['batch_size'], device\n        )\n        model = GPT(vocab_size=vocab_size_wt2, block_size=128,\n                    activation_name=act, **GPT_COMMON).to(device)\n        n_params = sum(p.numel() for p in model.parameters())\n        print(f'  seed={seed}, params={n_params/1e6:.2f}M')\n\n        if si == 0:\n            mem_mb = measure_peak_memory_mb(model, get_batch_wt2, device)\n            memory_wt2[act] = mem_mb\n            print(f'  Peak GPU memory: {mem_mb:.1f} MB')\n            model = GPT(vocab_size=vocab_size_wt2, block_size=128,\n                        activation_name=act, **GPT_COMMON).to(device)\n            set_seed(seed)\n\n        final_val, cwa_traj, bp_stats = train_model(\n            model, get_batch_wt2, WT2_CONFIG, act\n        )\n        test_loss = evaluate_test(model, get_batch_wt2, n_batches=100)\n        ppl = math.exp(min(test_loss, 20.0))  # clamp to avoid inf\n        ppls_per_seed.append(ppl)\n        print(f'  seed={seed}: test_loss={test_loss:.4f}, PPL={ppl:.2f}')\n\n        if act == 'cwa':\n            cwa_traj_wt2[f'seed_{seed}'] = cwa_traj\n            bp_stats_wt2[f'seed_{seed}'] = bp_stats\n\n    results_wt2[act] = {\n        'mean': float(np.mean(ppls_per_seed)),\n        'std':  float(np.std(ppls_per_seed)),\n        'per_seed': [float(v) for v in ppls_per_seed],\n    }\n\n\n# -------- Assemble baseline comparison --------\ndef pct_improvement(cwa_mean, base_mean, lower_is_better=True):\n    if lower_is_better:\n        return float((base_mean - cwa_mean) / base_mean * 100.0)\n    return float((cwa_mean - base_mean) / base_mean * 100.0)\n\nbaseline_comparison = {\n    'shakespeare_bpc_vs_gelu_pct': pct_improvement(\n        results_shakes['cwa']['mean'], results_shakes['gelu']['mean']),\n    'wikitext2_ppl_vs_gelu_pct': pct_improvement(\n        results_wt2['cwa']['mean'], results_wt2['gelu']['mean']),\n    'shakespeare_cwa_better_than_all': all(\n        results_shakes['cwa']['mean'] < results_shakes[a]['mean']\n        for a in ACTIVATIONS if a != 'cwa'\n    ),\n    'wikitext2_cwa_better_than_all': all(\n        results_wt2['cwa']['mean'] < results_wt2[a]['mean']\n        for a in ACTIVATIONS if a != 'cwa'\n    ),\n}\n\n# Peak memory ratio CWA / GELU\nmemory_ratio_shakes = (\n    memory_shakes.get('cwa', 0) / memory_shakes.get('gelu', 1)\n    if memory_shakes.get('gelu', 0) > 0 else None\n)\nmemory_ratio_wt2 = (\n    memory_wt2.get('cwa', 0) / memory_wt2.get('gelu', 1)\n    if memory_wt2.get('gelu', 0) > 0 else None\n)\n\n# Serialize CWA trajectory (convert to plain lists)\ndef serialize_traj(traj):\n    out = {}\n    for layer_k, steps in traj.items():\n        out[layer_k] = [\n            {k: (v if not isinstance(v, float) else round(v, 6)) for k, v in s.items()}\n            for s in steps\n        ]\n    return out\n\n\n# -------- Write method_out.json --------\nmethod_out = {\n    'shakespeare_bpc': results_shakes,\n    'wikitext2_ppl': results_wt2,\n    'baseline_comparison': baseline_comparison,\n    'J_s_bar_trajectory_per_layer': {\n        'shakespeare': {s: serialize_traj(t) for s, t in cwa_traj_shakes.items()},\n        'wikitext2':   {s: serialize_traj(t) for s, t in cwa_traj_wt2.items()},\n    },\n    'K_per_layer_per_epoch': {\n        'shakespeare': {\n            s: {\n                layer_k: {\n                    'mean_K': float(np.mean([x['K'] for x in steps])),\n                    'max_K':  int(max(x['K'] for x in steps)),\n                    'steps':  [x['step'] for x in steps],\n                    'K_values': [x['K'] for x in steps],\n                }\n                for layer_k, steps in cwa_traj_shakes.get(s, {}).items()\n            }\n            for s in [f'seed_{sd}' for sd in SHAKES_SEEDS]\n        },\n        'wikitext2': {\n            s: {\n                layer_k: {\n                    'mean_K': float(np.mean([x['K'] for x in steps])),\n                    'max_K':  int(max(x['K'] for x in steps)),\n                }\n                for layer_k, steps in cwa_traj_wt2.get(s, {}).items()\n            }\n            for s in [f'seed_{sd}' for sd in WT2_SEEDS]\n        },\n    },\n    'backprop_mode_statistics': {\n        'shakespeare': bp_stats_shakes,\n        'wikitext2':   bp_stats_wt2,\n    },\n    'peak_gpu_memory_mb': {\n        'shakespeare': memory_shakes,\n        'wikitext2':   memory_wt2,\n        'ratio_cwa_over_gelu': {\n            'shakespeare': memory_ratio_shakes,\n            'wikitext2':   memory_ratio_wt2,\n        },\n    },\n    'J_per_layer_at_convergence': {\n        'shakespeare': {\n            s: {\n                layer_k: {\n                    'final_J': round(steps[-1]['J'], 6) if steps else None,\n                    'final_J_s_bar': round(steps[-1]['J_s_bar'], 6) if steps else None,\n                }\n                for layer_k, steps in cwa_traj_shakes.get(s, {}).items()\n            }\n            for s in [f'seed_{sd}' for sd in SHAKES_SEEDS]\n        },\n        'wikitext2': {\n            s: {\n                layer_k: {\n                    'final_J': round(steps[-1]['J'], 6) if steps else None,\n                    'final_J_s_bar': round(steps[-1]['J_s_bar'], 6) if steps else None,\n                }\n                for layer_k, steps in cwa_traj_wt2.get(s, {}).items()\n            }\n            for s in [f'seed_{sd}' for sd in WT2_SEEDS]\n        },\n    },\n    'success_criteria_evaluation': {\n        'note': 'Experiment 3 tests a normalized GPT architecture; gradient stability criterion '\n                'applies to Exp 1 (unnormalized MLP). Here we report BPC/PPL vs baselines.',\n        'bpc_improvement_over_gelu_pct': baseline_comparison['shakespeare_bpc_vs_gelu_pct'],\n        'ppl_improvement_over_gelu_pct': baseline_comparison['wikitext2_ppl_vs_gelu_pct'],\n        'memory_criterion_met_shakespeare': (\n            memory_ratio_shakes is not None and memory_ratio_shakes <= 2.0\n        ),\n        'memory_criterion_met_wikitext2': (\n            memory_ratio_wt2 is not None and memory_ratio_wt2 <= 2.0\n        ),\n        'verdict': (\n            'CONFIRM (LM)' if (\n                baseline_comparison['shakespeare_bpc_vs_gelu_pct'] >= 0 and\n                baseline_comparison['wikitext2_ppl_vs_gelu_pct'] >= 0\n            ) else 'DISCONFIRM'\n        ),\n    },\n    'hyperparameters': {\n        'gpt': GPT_COMMON,\n        'shakespeare': {**SHAKES_CONFIG, 'seeds': SHAKES_SEEDS},\n        'wikitext2':   {**WT2_CONFIG,    'seeds': WT2_SEEDS},\n        'cwa': {\n            'J_raw_init': 0.0,\n            'J_init': 0.5,\n            'K_max': 50,\n            'unrolled_warm_steps': 3,\n            'ift_threshold': 0.8,\n            'delta_base': 1e-4,\n            'denom_clamp': 1e-4,\n        },\n        'tanh_swish_p_c': 0.5,\n    },\n    'total_llm_api_cost_usd': 0.0,\n}\n\nwith open('method_out.json', 'w') as f:\n    json.dump(method_out, f, indent=2)\n\nprint('\\nDone! Results saved to method_out.json')\nprint(f\"Shakespeare BPC: {results_shakes}\")\nprint(f\"WikiText-2 PPL: {results_wt2}\")",
  "fallback_plan": "## Fallback Strategies (in order of severity)\n\n### F1: CWA diverges or produces NaN\n- Reduce J_raw init to -1.0 (J≈0.27) so J starts farther from criticality.\n- Reduce lr to 1e-4 for CWA runs only.\n- Add `torch.nan_to_num(grad, nan=0.0)` after loss.backward().\n- If still failing, cap K_max=10 and always use unrolled mode (remove IFT branch entirely).\n\n### F2: GPU OOM on WikiText-2 (vocab_size=50257, large embedding)\n- Reduce batch_size from 32 to 16.\n- Reduce seq_len from 128 to 64.\n- Use gradient checkpointing: `model = torch.utils.checkpoint.checkpoint_sequential(model.blocks, segments=2, input=x)`.\n- If still OOM, use a smaller BPE vocab: build a word-level vocabulary of 10K most frequent words from the WikiText-2 training set instead of tiktoken.\n\n### F3: WikiText-2 20K steps too slow to fit in 6h budget\n- Reduce to 10K steps and clearly note this in method_out.json under a 'training_note' field.\n- Report extrapolated estimate if loss curve has clearly plateaued.\n- Alternatively run 3 activations (GELU, CWA, best baseline) at full 20K, and 2 less critical baselines at 10K.\n\n### F4: tiktoken/datasets unavailable\n- Fall back to a simple word tokenizer: `text.lower().split()` → build vocab from training set, keep top 10K words + `<unk>` token.\n- This gives a smaller, interpretable vocab and lower perplexity numbers; note the vocab change in output.\n\n### F5: Shakespeare download fails\n- Bundle the text inline as a raw string or use a local copy from `/ai-inventor` data directories.\n- Alternative source: `https://www.gutenberg.org/files/100/100-0.txt` (Shakespeare complete works).\n\n### F6: IFT gradient correctness issue (backward NaN)\n- Debug by comparing IFT gradient vs finite-differences on a tiny example (n=4, B=2, T=2).\n- If IFT gradient is wrong, fall back to pure unrolled mode (K=10 iterations from scratch, no warm start) for ALL coupling strengths.\n- This is slower but correct.\n\n### F7: Complete experiment too slow (all 25 runs)\n- Drop WikiText-2 entirely; report Shakespeare only with confidence intervals across 3 seeds.\n- Or: run 1 seed per activation × 2 datasets; acknowledge single-seed limitation.\n\n### F8: SELU NaN in deep untrained network\n- SELU requires lecun_normal init. Add a flag: for SELU, override `_init_weights` to use `nn.init.kaiming_normal_` with mode='fan_in'.\n- Alternatively replace SELU with nn.ELU() if initialization cannot be fixed quickly.",
  "testing_plan": "## Testing Plan: Fast Verification Before Full Scale\n\n### T1: CWA forward pass correctness (run first, ~30 seconds)\n```python\n# Quick sanity check: verify fixed-point iteration converges\nimport torch\nfrom cwa_activation import CWAActivation\ncwa = CWAActivation()\nx = torch.randn(2, 4, 16)   # tiny: batch=2, seq=4, hidden=16\ny = cwa(x)\nassert y.shape == x.shape\nassert not torch.isnan(y).any()\nprint(f'Forward OK. J={cwa._last_J:.3f}, J_s_bar={cwa._last_J_s_bar:.3f}, K={cwa._last_K}')\n```\n\n### T2: CWA backward pass + IFT correctness (numerical gradient check, ~2 minutes)\n```python\n# Force IFT mode by setting J_raw to a large value (J -> 0.99)\nfrom torch.autograd import gradcheck\ncwa = CWAActivation()\ncwa.J_raw.data.fill_(4.6)  # sigmoid(4.6) ~= 0.99 -> IFT mode\nx = torch.randn(1, 2, 8, dtype=torch.float64, requires_grad=True)\ncwa.J_raw = torch.nn.Parameter(cwa.J_raw.double())\n# Note: gradcheck requires float64\ntry:\n    result = gradcheck(lambda inp: cwa(inp), (x,), eps=1e-4, atol=1e-3)\n    print('IFT gradcheck PASSED')\nexcept Exception as e:\n    print(f'IFT gradcheck FAILED: {e}')  # fallback: remove IFT, use unrolled only\n```\n\n### T3: Tiny GPT sanity run (all activations, 10 steps each, ~1 minute)\n```python\n# Verify all 5 activations compile and take a gradient step without error\nfor act in ['gelu', 'gelu+ln', 'selu', 'tanh_swish', 'cwa']:\n    model = GPT(vocab_size=65, block_size=32, n_layer=2, n_head=4,\n                n_embd=32, activation_name=act)\n    x = torch.randint(0, 65, (4, 32))\n    y = torch.randint(0, 65, (4, 32))\n    _, loss = model(x, y)\n    loss.backward()\n    print(f'{act}: loss={loss.item():.4f} OK')\n```\n\n### T4: Mini-scale Shakespeare run (50 steps, 1 seed, ~2 minutes)\n```python\n# Confirm training loop works end-to-end with real data\nget_batch, vocab_size, _ = load_shakespeare(seq_len=64, batch_size=8, device='cpu')\nmodel = GPT(vocab_size=vocab_size, block_size=64, n_layer=2, n_head=2,\n            n_embd=32, activation_name='cwa')\nconfig = {'max_steps': 50, 'lr': 3e-4, 'warmup_steps': 5, 'grad_clip': 1.0,\n          'eval_every': 25, 'log_every': 25}\ntrain_model(model, get_batch, config, 'cwa')\nprint('Mini Shakespeare run OK')\n```\n\n### T5: WikiText-2 data loading check (~30 seconds)\n```python\n# Verify dataset loads and tokenizes without errors\nget_batch_wt2, vocab_size_wt2 = load_wikitext2(seq_len=32, batch_size=4, device='cpu')\nx, y = get_batch_wt2('train')\nprint(f'WikiText-2 batch shape: x={x.shape}, y={y.shape}, vocab={vocab_size_wt2}')\nassert x.shape == (4, 32)\nassert vocab_size_wt2 == 50257\n```\n\n### T6: GPU memory check (if GPU available, ~1 minute)\n```python\n# Verify memory measurement and CWA doesn't OOM vs GELU\nfor act in ['gelu', 'cwa']:\n    model = GPT(vocab_size=65, block_size=256, n_layer=6, n_head=8,\n                n_embd=256, activation_name=act).cuda()\n    get_batch, _, _ = load_shakespeare(256, 64, 'cuda')\n    mb = measure_peak_memory_mb(model, get_batch, 'cuda')\n    print(f'{act}: {mb:.1f} MB')\n```\n\n### Confirmation signals before full run\n- T1-T3 pass: proceed to T4\n- T4 shows decreasing loss: proceed to full Shakespeare runs\n- T5 passes: proceed to WikiText-2 runs\n- If T6 shows CWA > 2x GELU memory: reduce batch_size by 2x before full run\n- Full run ETA: monitor after first 500 steps and estimate total; abort early if >5h projected\n\n### Install commands (at top of method.py)\n```python\nimport subprocess, sys\nsubprocess.run([sys.executable, '-m', 'pip', 'install', '-q',\n    'tiktoken', 'datasets', 'numpy', 'torch'], check=True)\n```"
}
````

### [28] TOOL RESULT — Write · 2026-06-16 17:34:25 UTC

````
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_3/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"CWA Language Model Experiment: 6-Layer/256-Hidden GPT on Tiny Shakespeare and WikiText-2\",\n  \"summary\": \"Implement a minimal GPT in PyTorch (6 layers, 256 hidden, 8 heads, 4x MLP expansion) with a custom Curie-Weiss Activation (CWA) replacing GELU in FFN blocks. Train character-level on Tiny Shakespeare (3 seeds, 10K steps) and word-level (tiktoken BPE) on WikiText-2 (2 seeds, 20K steps). Compare test BPC and perplexity against GELU, GELU+LN, SELU, and tanh+Swish@0.5 baselines. Track per-layer J, J·s̄, K, backprop mode, and peak GPU memory throughout training. Output method_out.json.\",\n  \"runpod_compute_profile\": \"gpu\",\n  \"implementation_pseudocode\": \"# ============================================================\\n# FILE STRUCTURE\\n# ============================================================\\n# method.py        — main orchestrator (run this)\\n# cwa_activation.py — CWAActivation + CWAIFTFunction\\n# gpt_model.py     — GPT, Block, CausalSelfAttention, MLP, baselines\\n# data_utils.py    — Shakespeare + WikiText-2 loaders\\n# train_utils.py   — train loop, eval, memory measurement\\n\\n# ============================================================\\n# cwa_activation.py\\n# ============================================================\\n\\nimport torch\\nimport torch.nn as nn\\nimport torch.nn.functional as F\\n\\n\\nclass CWAIFTFunction(torch.autograd.Function):\\n    \\\"\\\"\\\"IFT backward for CWA when J·s̄ >= 0.8 (O(1) activation memory).\\\"\\\"\\\"\\n    @staticmethod\\n    def forward(ctx, x, J, m_star):\\n        # m_star: [B, T, 1] — already converged fixed point (detached)\\n        y_star = torch.tanh(x + J * m_star)\\n        s_bar = 1.0 - y_star.pow(2)          # sech² per element [B, T, H]\\n        s_bar_mean = s_bar.mean(dim=-1, keepdim=True)  # [B, T, 1]\\n        ctx.save_for_backward(J, m_star, s_bar, s_bar_mean)\\n        return y_star\\n\\n    @staticmethod\\n    def backward(ctx, grad_y):\\n        J, m_star, s_bar, s_bar_mean = ctx.saved_tensors\\n        J_val = J.item()\\n        n = grad_y.shape[-1]  # hidden dim = 4 * n_embd\\n        denom = (1.0 - J_val * s_bar_mean).clamp(min=1e-4)  # [B, T, 1]\\n\\n        # IFT gradient for x:\\n        # ∂L/∂x_i = sech²_i * [grad_y_i + (J/n) * Σ_j(grad_y_j * sech²_j) / denom]\\n        weighted_sum = (grad_y * s_bar).sum(dim=-1, keepdim=True)  # [B, T, 1]\\n        grad_x = s_bar * (grad_y + J_val * weighted_sum / (n * denom))\\n\\n        # IFT gradient for J (scalar):\\n        # ∂L/∂J = Σ_{i,b,t} grad_y_i * sech²_i * m*_i / denom_i\\n        grad_J = (grad_y * s_bar * m_star / denom).sum().unsqueeze(0)\\n\\n        return grad_x, grad_J, None  # no grad for m_star\\n\\n\\nclass CWAActivation(nn.Module):\\n    \\\"\\\"\\\"Curie-Weiss Activation: fixed point of y = tanh(x + J * mean_h(y)).\\n\\n    J = sigmoid(J_raw) in (0, 1). init J_raw=0 so J starts at 0.5.\\n    Hybrid backward: unrolled autograd if J·s̄ < 0.8, IFT if J·s̄ >= 0.8.\\n    \\\"\\\"\\\"\\n    def __init__(self):\\n        super().__init__()\\n        self.J_raw = nn.Parameter(torch.zeros(1))\\n        # Internal stats for logging (updated in-place each forward call)\\n        self._last_J = 0.5\\n        self._last_J_s_bar = 0.5\\n        self._last_K = 0\\n        self._last_mode = 'unrolled'\\n\\n    def forward(self, x):\\n        # x: [B, T, H] where H = 4 * n_embd (MLP expanded dimension)\\n        J = torch.sigmoid(self.J_raw)   # scalar in (0,1)\\n        J_val = J.item()\\n\\n        # --- Step 1: Find m* without gradient tracking ---\\n        with torch.no_grad():\\n            m = torch.zeros(*x.shape[:-1], 1, device=x.device, dtype=x.dtype)  # [B, T, 1]\\n            K_used = 0\\n            J_s_bar_final = J_val * 1.0  # upper bound before first step\\n            for k in range(50):          # K_max = 50\\n                y_tmp = torch.tanh(x + J_val * m)\\n                m_new = y_tmp.mean(dim=-1, keepdim=True)\\n                # Compute s̄ and adaptive tolerance\\n                s_bar_tmp = (1.0 - y_tmp.pow(2)).mean().item()   # scalar mean\\n                J_s_bar_cur = J_val * s_bar_tmp\\n                delta = 1e-4 * max(1.0 - J_s_bar_cur, 1e-2) + 1e-8\\n                diff = (m_new - m).abs().max().item()\\n                m = m_new\\n                K_used = k + 1\\n                J_s_bar_final = J_s_bar_cur\\n                if diff < delta:\\n                    break\\n            m_star = m.clone()   # [B, T, 1], detached\\n\\n        # --- Step 2: Decide backprop mode based on J·s̄ ---\\n        if J_s_bar_final < 0.8:\\n            # Unrolled autograd: warm-start from m_star (detached), run 3 tracked steps\\n            # This is accurate because m_star is close to the true fixed point\\n            m_tracked = m_star.detach()\\n            for _ in range(3):\\n                m_tracked = torch.tanh(x + J * m_tracked).mean(dim=-1, keepdim=True)\\n            y_out = torch.tanh(x + J * m_tracked)\\n            mode = 'unrolled'\\n        else:\\n            # IFT mode: O(1) activation memory, analytic gradient\\n            y_out = CWAIFTFunction.apply(x, J, m_star)\\n            mode = 'ift'\\n\\n        # Update logging stats (no autograd side effects)\\n        with torch.no_grad():\\n            y_check = torch.tanh(x + J_val * m_star)\\n            s_bar_check = (1.0 - y_check.pow(2)).mean().item()\\n            J_s_bar_final = J_val * s_bar_check\\n        self._last_J = J_val\\n        self._last_J_s_bar = J_s_bar_final\\n        self._last_K = K_used\\n        self._last_mode = mode\\n\\n        return y_out\\n\\n\\n# ============================================================\\n# gpt_model.py\\n# ============================================================\\n\\nimport math\\nimport torch, torch.nn as nn, torch.nn.functional as F\\nfrom cwa_activation import CWAActivation\\n\\n\\nclass TanhSwishMixture(nn.Module):\\n    \\\"\\\"\\\"p * tanh(x) + (1-p) * swish(x); p_c=0.5 as default.\\\"\\\"\\\"\\n    def __init__(self, p=0.5):\\n        super().__init__()\\n        self.p = p\\n    def forward(self, x):\\n        return self.p * torch.tanh(x) + (1.0 - self.p) * F.silu(x)\\n\\n\\ndef make_activation(name, n_embd):\\n    \\\"\\\"\\\"Return the activation module for use inside MLP.\\\"\\\"\\\"\\n    mlp_dim = 4 * n_embd\\n    if name == 'gelu':\\n        return nn.GELU()\\n    elif name == 'gelu+ln':\\n        # LayerNorm applied after GELU inside the FFN expansion\\n        return nn.Sequential(nn.GELU(), nn.LayerNorm(mlp_dim))\\n    elif name == 'selu':\\n        return nn.SELU()\\n    elif name == 'tanh_swish':\\n        return TanhSwishMixture(p=0.5)\\n    elif name == 'cwa':\\n        return CWAActivation()\\n    else:\\n        raise ValueError(f'Unknown activation: {name}')\\n\\n\\nclass MLP(nn.Module):\\n    def __init__(self, n_embd, activation_name='gelu', dropout=0.1):\\n        super().__init__()\\n        self.c_fc   = nn.Linear(n_embd, 4 * n_embd)\\n        self.act    = make_activation(activation_name, n_embd)\\n        self.c_proj = nn.Linear(4 * n_embd, n_embd)\\n        self.drop   = nn.Dropout(dropout)\\n\\n    def forward(self, x):\\n        x = self.c_fc(x)\\n        x = self.act(x)\\n        x = self.c_proj(x)\\n        return self.drop(x)\\n\\n\\nclass CausalSelfAttention(nn.Module):\\n    def __init__(self, n_embd, n_head, dropout=0.1, block_size=2048):\\n        super().__init__()\\n        assert n_embd % n_head == 0\\n        self.c_attn  = nn.Linear(n_embd, 3 * n_embd)\\n        self.c_proj  = nn.Linear(n_embd, n_embd)\\n        self.attn_drop  = nn.Dropout(dropout)\\n        self.resid_drop = nn.Dropout(dropout)\\n        self.n_head = n_head\\n        self.n_embd = n_embd\\n        # Causal mask buffer (not a parameter)\\n        self.register_buffer('bias',\\n            torch.tril(torch.ones(block_size, block_size)).view(1, 1, block_size, block_size))\\n\\n    def forward(self, x):\\n        B, T, C = x.shape\\n        q, k, v = self.c_attn(x).split(self.n_embd, dim=2)\\n        k = k.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)\\n        q = q.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)\\n        v = v.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)\\n        # Use flash attention when available (PyTorch 2.0+)\\n        use_flash = hasattr(F, 'scaled_dot_product_attention')\\n        if use_flash:\\n            y = F.scaled_dot_product_attention(q, k, v, attn_mask=None,\\n                                                dropout_p=0.0, is_causal=True)\\n        else:\\n            att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(k.size(-1)))\\n            att = att.masked_fill(self.bias[:, :, :T, :T] == 0, float('-inf'))\\n            att = F.softmax(att, dim=-1)\\n            att = self.attn_drop(att)\\n            y = att @ v\\n        y = y.transpose(1, 2).contiguous().view(B, T, C)\\n        return self.resid_drop(self.c_proj(y))\\n\\n\\nclass Block(nn.Module):\\n    def __init__(self, n_embd, n_head, activation_name='gelu', dropout=0.1, block_size=2048):\\n        super().__init__()\\n        self.ln_1 = nn.LayerNorm(n_embd)\\n        self.attn = CausalSelfAttention(n_embd, n_head, dropout, block_size)\\n        self.ln_2 = nn.LayerNorm(n_embd)\\n        self.mlp  = MLP(n_embd, activation_name, dropout)\\n\\n    def forward(self, x):\\n        x = x + self.attn(self.ln_1(x))\\n        x = x + self.mlp(self.ln_2(x))\\n        return x\\n\\n\\nclass GPT(nn.Module):\\n    def __init__(self, vocab_size, n_layer=6, n_head=8, n_embd=256,\\n                 block_size=256, dropout=0.1, activation_name='gelu'):\\n        super().__init__()\\n        self.tok_emb = nn.Embedding(vocab_size, n_embd)\\n        self.pos_emb = nn.Embedding(block_size, n_embd)\\n        self.drop    = nn.Dropout(dropout)\\n        self.blocks  = nn.ModuleList([\\n            Block(n_embd, n_head, activation_name, dropout, block_size)\\n            for _ in range(n_layer)\\n        ])\\n        self.ln_f    = nn.LayerNorm(n_embd)\\n        self.lm_head = nn.Linear(n_embd, vocab_size, bias=False)\\n        self.block_size = block_size\\n        # Init weights\\n        self.apply(self._init_weights)\\n\\n    def _init_weights(self, module):\\n        if isinstance(module, nn.Linear):\\n            nn.init.normal_(module.weight, mean=0.0, std=0.02)\\n            if module.bias is not None:\\n                nn.init.zeros_(module.bias)\\n        elif isinstance(module, nn.Embedding):\\n            nn.init.normal_(module.weight, mean=0.0, std=0.02)\\n        # J_raw in CWAActivation is initialized to 0.0 by nn.Parameter default\\n\\n    def forward(self, idx, targets=None):\\n        B, T = idx.shape\\n        assert T <= self.block_size\\n        pos = torch.arange(T, device=idx.device, dtype=torch.long)\\n        x = self.drop(self.tok_emb(idx) + self.pos_emb(pos))\\n        for block in self.blocks:\\n            x = block(x)\\n        x = self.ln_f(x)\\n        logits = self.lm_head(x)   # [B, T, vocab_size]\\n        loss = None\\n        if targets is not None:\\n            loss = F.cross_entropy(\\n                logits.view(-1, logits.size(-1)), targets.view(-1)\\n            )\\n        return logits, loss\\n\\n    def get_cwa_stats(self):\\n        \\\"\\\"\\\"Collect CWA diagnostics from all layers (if activation is CWA).\\\"\\\"\\\"\\n        stats = {}\\n        for i, block in enumerate(self.blocks):\\n            act = block.mlp.act\\n            # For gelu+ln, act is Sequential — no CWA stats\\n            if isinstance(act, CWAActivation):\\n                stats[f'layer_{i}'] = {\\n                    'J':       act._last_J,\\n                    'J_s_bar': act._last_J_s_bar,\\n                    'K':       act._last_K,\\n                    'mode':    act._last_mode,\\n                }\\n        return stats\\n\\n\\n# ============================================================\\n# data_utils.py\\n# ============================================================\\n\\nimport os, requests, math\\nimport torch\\n\\n\\ndef load_shakespeare(seq_len, batch_size, device):\\n    \\\"\\\"\\\"Download and tokenize Tiny Shakespeare. Returns (train, val, test, vocab_size, decode_fn).\\\"\\\"\\\"\\n    url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'\\n    os.makedirs('data', exist_ok=True)\\n    path = 'data/shakespeare.txt'\\n    if not os.path.exists(path):\\n        r = requests.get(url)\\n        with open(path, 'w') as f:\\n            f.write(r.text)\\n    text = open(path).read()\\n    chars = sorted(set(text))\\n    vocab_size = len(chars)\\n    stoi = {ch: i for i, ch in enumerate(chars)}\\n    itos = {i: ch for ch, i in stoi.items()}\\n    data = torch.tensor([stoi[c] for c in text], dtype=torch.long)\\n    n = len(data)\\n    train_data = data[:int(0.90 * n)]\\n    val_data   = data[int(0.90 * n):int(0.95 * n)]\\n    test_data  = data[int(0.95 * n):]\\n    decode = lambda ids: ''.join(itos[i] for i in ids)\\n\\n    def get_batch(split):\\n        d = {'train': train_data, 'val': val_data, 'test': test_data}[split]\\n        ix = torch.randint(len(d) - seq_len, (batch_size,))\\n        x  = torch.stack([d[i:i+seq_len] for i in ix]).to(device)\\n        y  = torch.stack([d[i+1:i+seq_len+1] for i in ix]).to(device)\\n        return x, y\\n\\n    return get_batch, vocab_size, decode\\n\\n\\ndef load_wikitext2(seq_len, batch_size, device):\\n    \\\"\\\"\\\"Load WikiText-2 with tiktoken BPE. Returns (get_batch_fn, vocab_size).\\\"\\\"\\\"\\n    from datasets import load_dataset\\n    import tiktoken\\n    enc = tiktoken.get_encoding('gpt2')  # vocab_size = 50257\\n    vocab_size = enc.n_vocab\\n\\n    ds = load_dataset('wikitext', 'wikitext-2-raw-v1')\\n\\n    def tokenize_split(split_name):\\n        texts = ds[split_name]['text']\\n        tokens = []\\n        for t in texts:\\n            t = t.strip()\\n            if t:\\n                # encode_ordinary avoids adding BOS/EOS special tokens\\n                tokens.extend(enc.encode_ordinary(t))\\n        return torch.tensor(tokens, dtype=torch.long)\\n\\n    train_data = tokenize_split('train')\\n    val_data   = tokenize_split('validation')\\n    test_data  = tokenize_split('test')\\n\\n    def get_batch(split):\\n        d = {'train': train_data, 'val': val_data, 'test': test_data}[split]\\n        ix = torch.randint(len(d) - seq_len, (batch_size,))\\n        x  = torch.stack([d[i:i+seq_len] for i in ix]).to(device)\\n        y  = torch.stack([d[i+1:i+seq_len+1] for i in ix]).to(device)\\n        return x, y\\n\\n    return get_batch, vocab_size\\n\\n\\n# ============================================================\\n# train_utils.py\\n# ============================================================\\n\\nimport math, time\\nimport torch, torch.nn as nn\\nfrom collections import defaultdict\\n\\n\\ndef get_cosine_lr(step, max_steps, lr, warmup_steps):\\n    if step < warmup_steps:\\n        return lr * step / max(warmup_steps, 1)\\n    t = (step - warmup_steps) / max(max_steps - warmup_steps, 1)\\n    return lr * 0.5 * (1.0 + math.cos(math.pi * t))\\n\\n\\ndef evaluate(model, get_batch, n_batches=50):\\n    \\\"\\\"\\\"Return mean cross-entropy loss over n_batches random batches.\\\"\\\"\\\"\\n    model.eval()\\n    losses = []\\n    with torch.no_grad():\\n        for _ in range(n_batches):\\n            x, y = get_batch('val')\\n            _, loss = model(x, y)\\n            losses.append(loss.item())\\n    model.train()\\n    return sum(losses) / len(losses)\\n\\n\\ndef evaluate_test(model, get_batch, n_batches=100):\\n    model.eval()\\n    losses = []\\n    with torch.no_grad():\\n        for _ in range(n_batches):\\n            x, y = get_batch('test')\\n            _, loss = model(x, y)\\n            losses.append(loss.item())\\n    model.train()\\n    return sum(losses) / len(losses)\\n\\n\\ndef measure_peak_memory_mb(model, get_batch, device):\\n    \\\"\\\"\\\"Measure peak GPU memory over one forward+backward pass.\\\"\\\"\\\"\\n    if not torch.cuda.is_available():\\n        return 0.0\\n    torch.cuda.reset_peak_memory_stats(device)\\n    model.train()\\n    x, y = get_batch('train')\\n    _, loss = model(x, y)\\n    loss.backward()\\n    model.zero_grad()\\n    return torch.cuda.max_memory_allocated(device) / (1024 ** 2)\\n\\n\\ndef train_model(model, get_batch, config, activation_name):\\n    \\\"\\\"\\\"\\n    Train model for config.max_steps steps.\\n    config fields: max_steps, lr, warmup_steps, grad_clip, eval_every, log_every\\n    Returns: (final_val_loss, cwa_trajectory dict)\\n    \\\"\\\"\\\"\\n    optimizer = torch.optim.AdamW(\\n        model.parameters(), lr=config['lr'],\\n        weight_decay=0.1, betas=(0.9, 0.95)\\n    )\\n    cwa_traj = defaultdict(list)   # layer_id -> list of stat dicts\\n    backprop_counts = {'unrolled': 0, 'ift': 0}\\n    t0 = time.time()\\n\\n    for step in range(config['max_steps']):\\n        # LR schedule\\n        lr = get_cosine_lr(step, config['max_steps'], config['lr'], config['warmup_steps'])\\n        for g in optimizer.param_groups:\\n            g['lr'] = lr\\n\\n        # Forward + backward\\n        x, y = get_batch('train')\\n        logits, loss = model(x, y)\\n        optimizer.zero_grad(set_to_none=True)\\n        loss.backward()\\n        nn.utils.clip_grad_norm_(model.parameters(), config['grad_clip'])\\n        optimizer.step()\\n\\n        # Collect CWA stats every log_every steps\\n        if activation_name == 'cwa' and step % config.get('log_every', 500) == 0:\\n            stats = model.get_cwa_stats()\\n            for layer_key, s in stats.items():\\n                cwa_traj[layer_key].append({'step': step, **s})\\n                if s['mode'] == 'unrolled':\\n                    backprop_counts['unrolled'] += 1\\n                else:\\n                    backprop_counts['ift'] += 1\\n\\n        # Print progress\\n        if step % config.get('eval_every', 500) == 0:\\n            val_loss = evaluate(model, get_batch, n_batches=50)\\n            elapsed = time.time() - t0\\n            print(f'  step {step}/{config[\\\"max_steps\\\"]}: '\\n                  f'train_loss={loss.item():.4f} val_loss={val_loss:.4f} '\\n                  f'lr={lr:.2e} elapsed={elapsed:.1f}s')\\n\\n    final_val = evaluate(model, get_batch, n_batches=50)\\n    total = backprop_counts['unrolled'] + backprop_counts['ift']\\n    bp_stats = {\\n        'unrolled_count': backprop_counts['unrolled'],\\n        'ift_count': backprop_counts['ift'],\\n        'unrolled_fraction': backprop_counts['unrolled'] / max(total, 1),\\n        'ift_fraction':  backprop_counts['ift'] / max(total, 1),\\n    }\\n    return final_val, dict(cwa_traj), bp_stats\\n\\n\\n# ============================================================\\n# method.py — MAIN ORCHESTRATOR\\n# ============================================================\\n\\nimport json, math, random, os, time\\nimport numpy as np\\nimport torch\\nfrom collections import defaultdict\\n\\nfrom cwa_activation import CWAActivation\\nfrom gpt_model import GPT\\nfrom data_utils import load_shakespeare, load_wikitext2\\nfrom train_utils import train_model, evaluate_test, measure_peak_memory_mb\\n\\n\\n# -------- reproducibility --------\\ndef set_seed(seed):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n    torch.backends.cudnn.deterministic = True\\n\\n\\n# -------- configs --------\\nSHAKES_CONFIG = {\\n    'seq_len': 256, 'batch_size': 64, 'max_steps': 10_000,\\n    'lr': 3e-4, 'warmup_steps': 200, 'grad_clip': 1.0,\\n    'eval_every': 500, 'log_every': 500,\\n}\\nWT2_CONFIG = {\\n    'seq_len': 128, 'batch_size': 32, 'max_steps': 20_000,\\n    'lr': 3e-4, 'warmup_steps': 400, 'grad_clip': 1.0,\\n    'eval_every': 1000, 'log_every': 1000,\\n}\\n\\nGPT_COMMON = dict(n_layer=6, n_head=8, n_embd=256, dropout=0.1)\\n\\nACTIVATIONS = ['gelu', 'gelu+ln', 'selu', 'tanh_swish', 'cwa']\\nSHAKES_SEEDS  = [42, 123, 7]\\nWT2_SEEDS     = [42, 123]\\n\\ndevice = 'cuda' if torch.cuda.is_available() else 'cpu'\\nprint(f'Using device: {device}')\\n\\n\\n# -------- SHAKESPEARE --------\\nprint('\\\\n===== SHAKESPEARE =====')\\nresults_shakes = {}\\ncwa_traj_shakes = {}\\nmemory_shakes = {}\\nbp_stats_shakes = {}\\n\\nfor act in ACTIVATIONS:\\n    print(f'\\\\n--- Activation: {act} ---')\\n    bpcs_per_seed = []\\n    for si, seed in enumerate(SHAKES_SEEDS):\\n        set_seed(seed)\\n        # Load data (re-create get_batch with same shuffle seed)\\n        get_batch, vocab_size, decode = load_shakespeare(\\n            SHAKES_CONFIG['seq_len'], SHAKES_CONFIG['batch_size'], device\\n        )\\n        model = GPT(vocab_size=vocab_size, block_size=256,\\n                    activation_name=act, **GPT_COMMON).to(device)\\n        n_params = sum(p.numel() for p in model.parameters())\\n        print(f'  seed={seed}, params={n_params/1e6:.2f}M')\\n\\n        # Measure peak memory for first activation + first seed only\\n        if si == 0:\\n            mem_mb = measure_peak_memory_mb(model, get_batch, device)\\n            memory_shakes[act] = mem_mb\\n            print(f'  Peak GPU memory: {mem_mb:.1f} MB')\\n            # Reinit model and optimizer state after memory measurement\\n            model = GPT(vocab_size=vocab_size, block_size=256,\\n                        activation_name=act, **GPT_COMMON).to(device)\\n            set_seed(seed)  # re-seed after measurement\\n\\n        final_val, cwa_traj, bp_stats = train_model(\\n            model, get_batch, SHAKES_CONFIG, act\\n        )\\n        test_loss = evaluate_test(model, get_batch, n_batches=100)\\n        bpc = test_loss / math.log(2.0)   # nats -> bits per character\\n        bpcs_per_seed.append(bpc)\\n        print(f'  seed={seed}: test_loss={test_loss:.4f}, BPC={bpc:.4f}')\\n\\n        if act == 'cwa':\\n            cwa_traj_shakes[f'seed_{seed}'] = cwa_traj\\n            bp_stats_shakes[f'seed_{seed}'] = bp_stats\\n\\n    results_shakes[act] = {\\n        'mean': float(np.mean(bpcs_per_seed)),\\n        'std':  float(np.std(bpcs_per_seed)),\\n        'per_seed': [float(v) for v in bpcs_per_seed],\\n    }\\n\\n\\n# -------- WIKITEXT-2 --------\\nprint('\\\\n===== WIKITEXT-2 =====')\\nresults_wt2 = {}\\ncwa_traj_wt2 = {}\\nmemory_wt2 = {}\\nbp_stats_wt2 = {}\\n\\nfor act in ACTIVATIONS:\\n    print(f'\\\\n--- Activation: {act} ---')\\n    ppls_per_seed = []\\n    for si, seed in enumerate(WT2_SEEDS):\\n        set_seed(seed)\\n        get_batch_wt2, vocab_size_wt2 = load_wikitext2(\\n            WT2_CONFIG['seq_len'], WT2_CONFIG['batch_size'], device\\n        )\\n        model = GPT(vocab_size=vocab_size_wt2, block_size=128,\\n                    activation_name=act, **GPT_COMMON).to(device)\\n        n_params = sum(p.numel() for p in model.parameters())\\n        print(f'  seed={seed}, params={n_params/1e6:.2f}M')\\n\\n        if si == 0:\\n            mem_mb = measure_peak_memory_mb(model, get_batch_wt2, device)\\n            memory_wt2[act] = mem_mb\\n            print(f'  Peak GPU memory: {mem_mb:.1f} MB')\\n            model = GPT(vocab_size=vocab_size_wt2, block_size=128,\\n                        activation_name=act, **GPT_COMMON).to(device)\\n            set_seed(seed)\\n\\n        final_val, cwa_traj, bp_stats = train_model(\\n            model, get_batch_wt2, WT2_CONFIG, act\\n        )\\n        test_loss = evaluate_test(model, get_batch_wt2, n_batches=100)\\n        ppl = math.exp(min(test_loss, 20.0))  # clamp to avoid inf\\n        ppls_per_seed.append(ppl)\\n        print(f'  seed={seed}: test_loss={test_loss:.4f}, PPL={ppl:.2f}')\\n\\n        if act == 'cwa':\\n            cwa_traj_wt2[f'seed_{seed}'] = cwa_traj\\n            bp_stats_wt2[f'seed_{seed}'] = bp_stats\\n\\n    results_wt2[act] = {\\n        'mean': float(np.mean(ppls_per_seed)),\\n        'std':  float(np.std(ppls_per_seed)),\\n        'per_seed': [float(v) for v in ppls_per_seed],\\n    }\\n\\n\\n# -------- Assemble baseline comparison --------\\ndef pct_improvement(cwa_mean, base_mean, lower_is_better=True):\\n    if lower_is_better:\\n        return float((base_mean - cwa_mean) / base_mean * 100.0)\\n    return float((cwa_mean - base_mean) / base_mean * 100.0)\\n\\nbaseline_comparison = {\\n    'shakespeare_bpc_vs_gelu_pct': pct_improvement(\\n        results_shakes['cwa']['mean'], results_shakes['gelu']['mean']),\\n    'wikitext2_ppl_vs_gelu_pct': pct_improvement(\\n        results_wt2['cwa']['mean'], results_wt2['gelu']['mean']),\\n    'shakespeare_cwa_better_than_all': all(\\n        results_shakes['cwa']['mean'] < results_shakes[a]['mean']\\n        for a in ACTIVATIONS if a != 'cwa'\\n    ),\\n    'wikitext2_cwa_better_than_all': all(\\n        results_wt2['cwa']['mean'] < results_wt2[a]['mean']\\n        for a in ACTIVATIONS if a != 'cwa'\\n    ),\\n}\\n\\n# Peak memory ratio CWA / GELU\\nmemory_ratio_shakes = (\\n    memory_shakes.get('cwa', 0) / memory_shakes.get('gelu', 1)\\n    if memory_shakes.get('gelu', 0) > 0 else None\\n)\\nmemory_ratio_wt2 = (\\n    memory_wt2.get('cwa', 0) / memory_wt2.get('gelu', 1)\\n    if memory_wt2.get('gelu', 0) > 0 else None\\n)\\n\\n# Serialize CWA trajectory (convert to plain lists)\\ndef serialize_traj(traj):\\n    out = {}\\n    for layer_k, steps in traj.items():\\n        out[layer_k] = [\\n            {k: (v if not isinstance(v, float) else round(v, 6)) for k, v in s.items()}\\n            for s in steps\\n        ]\\n    return out\\n\\n\\n# -------- Write method_out.json --------\\nmethod_out = {\\n    'shakespeare_bpc': results_shakes,\\n    'wikitext2_ppl': results_wt2,\\n    'baseline_comparison': baseline_comparison,\\n    'J_s_bar_trajectory_per_layer': {\\n        'shakespeare': {s: serialize_traj(t) for s, t in cwa_traj_shakes.items()},\\n        'wikitext2':   {s: serialize_traj(t) for s, t in cwa_traj_wt2.items()},\\n    },\\n    'K_per_layer_per_epoch': {\\n        'shakespeare': {\\n            s: {\\n                layer_k: {\\n                    'mean_K': float(np.mean([x['K'] for x in steps])),\\n                    'max_K':  int(max(x['K'] for x in steps)),\\n                    'steps':  [x['step'] for x in steps],\\n                    'K_values': [x['K'] for x in steps],\\n                }\\n                for layer_k, steps in cwa_traj_shakes.get(s, {}).items()\\n            }\\n            for s in [f'seed_{sd}' for sd in SHAKES_SEEDS]\\n        },\\n        'wikitext2': {\\n            s: {\\n                layer_k: {\\n                    'mean_K': float(np.mean([x['K'] for x in steps])),\\n                    'max_K':  int(max(x['K'] for x in steps)),\\n                }\\n                for layer_k, steps in cwa_traj_wt2.get(s, {}).items()\\n            }\\n            for s in [f'seed_{sd}' for sd in WT2_SEEDS]\\n        },\\n    },\\n    'backprop_mode_statistics': {\\n        'shakespeare': bp_stats_shakes,\\n        'wikitext2':   bp_stats_wt2,\\n    },\\n    'peak_gpu_memory_mb': {\\n        'shakespeare': memory_shakes,\\n        'wikitext2':   memory_wt2,\\n        'ratio_cwa_over_gelu': {\\n            'shakespeare': memory_ratio_shakes,\\n            'wikitext2':   memory_ratio_wt2,\\n        },\\n    },\\n    'J_per_layer_at_convergence': {\\n        'shakespeare': {\\n            s: {\\n                layer_k: {\\n                    'final_J': round(steps[-1]['J'], 6) if steps else None,\\n                    'final_J_s_bar': round(steps[-1]['J_s_bar'], 6) if steps else None,\\n                }\\n                for layer_k, steps in cwa_traj_shakes.get(s, {}).items()\\n            }\\n            for s in [f'seed_{sd}' for sd in SHAKES_SEEDS]\\n        },\\n        'wikitext2': {\\n            s: {\\n                layer_k: {\\n                    'final_J': round(steps[-1]['J'], 6) if steps else None,\\n                    'final_J_s_bar': round(steps[-1]['J_s_bar'], 6) if steps else None,\\n                }\\n                for layer_k, steps in cwa_traj_wt2.get(s, {}).items()\\n            }\\n            for s in [f'seed_{sd}' for sd in WT2_SEEDS]\\n        },\\n    },\\n    'success_criteria_evaluation': {\\n        'note': 'Experiment 3 tests a normalized GPT architecture; gradient stability criterion '\\n                'applies to Exp 1 (unnormalized MLP). Here we report BPC/PPL vs baselines.',\\n        'bpc_improvement_over_gelu_pct': baseline_comparison['shakespeare_bpc_vs_gelu_pct'],\\n        'ppl_improvement_over_gelu_pct': baseline_comparison['wikitext2_ppl_vs_gelu_pct'],\\n        'memory_criterion_met_shakespeare': (\\n            memory_ratio_shakes is not None and memory_ratio_shakes <= 2.0\\n        ),\\n        'memory_criterion_met_wikitext2': (\\n            memory_ratio_wt2 is not None and memory_ratio_wt2 <= 2.0\\n        ),\\n        'verdict': (\\n            'CONFIRM (LM)' if (\\n                baseline_comparison['shakespeare_bpc_vs_gelu_pct'] >= 0 and\\n                baseline_comparison['wikitext2_ppl_vs_gelu_pct'] >= 0\\n            ) else 'DISCONFIRM'\\n        ),\\n    },\\n    'hyperparameters': {\\n        'gpt': GPT_COMMON,\\n        'shakespeare': {**SHAKES_CONFIG, 'seeds': SHAKES_SEEDS},\\n        'wikitext2':   {**WT2_CONFIG,    'seeds': WT2_SEEDS},\\n        'cwa': {\\n            'J_raw_init': 0.0,\\n            'J_init': 0.5,\\n            'K_max': 50,\\n            'unrolled_warm_steps': 3,\\n            'ift_threshold': 0.8,\\n            'delta_base': 1e-4,\\n            'denom_clamp': 1e-4,\\n        },\\n        'tanh_swish_p_c': 0.5,\\n    },\\n    'total_llm_api_cost_usd': 0.0,\\n}\\n\\nwith open('method_out.json', 'w') as f:\\n    json.dump(method_out, f, indent=2)\\n\\nprint('\\\\nDone! Results saved to method_out.json')\\nprint(f\\\"Shakespeare BPC: {results_shakes}\\\")\\nprint(f\\\"WikiText-2 PPL: {results_wt2}\\\")\",\n  \"fallback_plan\": \"## Fallback Strategies (in order of severity)\\n\\n### F1: CWA diverges or produces NaN\\n- Reduce J_raw init to -1.0 (J≈0.27) so J starts farther from criticality.\\n- Reduce lr to 1e-4 for CWA runs only.\\n- Add `torch.nan_to_num(grad, nan=0.0)` after loss.backward().\\n- If still failing, cap K_max=10 and always use unrolled mode (remove IFT branch entirely).\\n\\n### F2: GPU OOM on WikiText-2 (vocab_size=50257, large embedding)\\n- Reduce batch_size from 32 to 16.\\n- Reduce seq_len from 128 to 64.\\n- Use gradient checkpointing: `model = torch.utils.checkpoint.checkpoint_sequential(model.blocks, segments=2, input=x)`.\\n- If still OOM, use a smaller BPE vocab: build a word-level vocabulary of 10K most frequent words from the WikiText-2 training set instead of tiktoken.\\n\\n### F3: WikiText-2 20K steps too slow to fit in 6h budget\\n- Reduce to 10K steps and clearly note this in method_out.json under a 'training_note' field.\\n- Report extrapolated estimate if loss curve has clearly plateaued.\\n- Alternatively run 3 activations (GELU, CWA, best baseline) at full 20K, and 2 less critical baselines at 10K.\\n\\n### F4: tiktoken/datasets unavailable\\n- Fall back to a simple word tokenizer: `text.lower().split()` → build vocab from training set, keep top 10K words + `<unk>` token.\\n- This gives a smaller, interpretable vocab and lower perplexity numbers; note the vocab change in output.\\n\\n### F5: Shakespeare download fails\\n- Bundle the text inline as a raw string or use a local copy from `/ai-inventor` data directories.\\n- Alternative source: `https://www.gutenberg.org/files/100/100-0.txt` (Shakespeare complete works).\\n\\n### F6: IFT gradient correctness issue (backward NaN)\\n- Debug by comparing IFT gradient vs finite-differences on a tiny example (n=4, B=2, T=2).\\n- If IFT gradient is wrong, fall back to pure unrolled mode (K=10 iterations from scratch, no warm start) for ALL coupling strengths.\\n- This is slower but correct.\\n\\n### F7: Complete experiment too slow (all 25 runs)\\n- Drop WikiText-2 entirely; report Shakespeare only with confidence intervals across 3 seeds.\\n- Or: run 1 seed per activation × 2 datasets; acknowledge single-seed limitation.\\n\\n### F8: SELU NaN in deep untrained network\\n- SELU requires lecun_normal init. Add a flag: for SELU, override `_init_weights` to use `nn.init.kaiming_normal_` with mode='fan_in'.\\n- Alternatively replace SELU with nn.ELU() if initialization cannot be fixed quickly.\",\n  \"testing_plan\": \"## Testing Plan: Fast Verification Before Full Scale\\n\\n### T1: CWA forward pass correctness (run first, ~30 seconds)\\n```python\\n# Quick sanity check: verify fixed-point iteration converges\\nimport torch\\nfrom cwa_activation import CWAActivation\\ncwa = CWAActivation()\\nx = torch.randn(2, 4, 16)   # tiny: batch=2, seq=4, hidden=16\\ny = cwa(x)\\nassert y.shape == x.shape\\nassert not torch.isnan(y).any()\\nprint(f'Forward OK. J={cwa._last_J:.3f}, J_s_bar={cwa._last_J_s_bar:.3f}, K={cwa._last_K}')\\n```\\n\\n### T2: CWA backward pass + IFT correctness (numerical gradient check, ~2 minutes)\\n```python\\n# Force IFT mode by setting J_raw to a large value (J -> 0.99)\\nfrom torch.autograd import gradcheck\\ncwa = CWAActivation()\\ncwa.J_raw.data.fill_(4.6)  # sigmoid(4.6) ~= 0.99 -> IFT mode\\nx = torch.randn(1, 2, 8, dtype=torch.float64, requires_grad=True)\\ncwa.J_raw = torch.nn.Parameter(cwa.J_raw.double())\\n# Note: gradcheck requires float64\\ntry:\\n    result = gradcheck(lambda inp: cwa(inp), (x,), eps=1e-4, atol=1e-3)\\n    print('IFT gradcheck PASSED')\\nexcept Exception as e:\\n    print(f'IFT gradcheck FAILED: {e}')  # fallback: remove IFT, use unrolled only\\n```\\n\\n### T3: Tiny GPT sanity run (all activations, 10 steps each, ~1 minute)\\n```python\\n# Verify all 5 activations compile and take a gradient step without error\\nfor act in ['gelu', 'gelu+ln', 'selu', 'tanh_swish', 'cwa']:\\n    model = GPT(vocab_size=65, block_size=32, n_layer=2, n_head=4,\\n                n_embd=32, activation_name=act)\\n    x = torch.randint(0, 65, (4, 32))\\n    y = torch.randint(0, 65, (4, 32))\\n    _, loss = model(x, y)\\n    loss.backward()\\n    print(f'{act}: loss={loss.item():.4f} OK')\\n```\\n\\n### T4: Mini-scale Shakespeare run (50 steps, 1 seed, ~2 minutes)\\n```python\\n# Confirm training loop works end-to-end with real data\\nget_batch, vocab_size, _ = load_shakespeare(seq_len=64, batch_size=8, device='cpu')\\nmodel = GPT(vocab_size=vocab_size, block_size=64, n_layer=2, n_head=2,\\n            n_embd=32, activation_name='cwa')\\nconfig = {'max_steps': 50, 'lr': 3e-4, 'warmup_steps': 5, 'grad_clip': 1.0,\\n          'eval_every': 25, 'log_every': 25}\\ntrain_model(model, get_batch, config, 'cwa')\\nprint('Mini Shakespeare run OK')\\n```\\n\\n### T5: WikiText-2 data loading check (~30 seconds)\\n```python\\n# Verify dataset loads and tokenizes without errors\\nget_batch_wt2, vocab_size_wt2 = load_wikitext2(seq_len=32, batch_size=4, device='cpu')\\nx, y = get_batch_wt2('train')\\nprint(f'WikiText-2 batch shape: x={x.shape}, y={y.shape}, vocab={vocab_size_wt2}')\\nassert x.shape == (4, 32)\\nassert vocab_size_wt2 == 50257\\n```\\n\\n### T6: GPU memory check (if GPU available, ~1 minute)\\n```python\\n# Verify memory measurement and CWA doesn't OOM vs GELU\\nfor act in ['gelu', 'cwa']:\\n    model = GPT(vocab_size=65, block_size=256, n_layer=6, n_head=8,\\n                n_embd=256, activation_name=act).cuda()\\n    get_batch, _, _ = load_shakespeare(256, 64, 'cuda')\\n    mb = measure_peak_memory_mb(model, get_batch, 'cuda')\\n    print(f'{act}: {mb:.1f} MB')\\n```\\n\\n### Confirmation signals before full run\\n- T1-T3 pass: proceed to T4\\n- T4 shows decreasing loss: proceed to full Shakespeare runs\\n- T5 passes: proceed to WikiText-2 runs\\n- If T6 shows CWA > 2x GELU memory: reduce batch_size by 2x before full run\\n- Full run ETA: monitor after first 500 steps and estimate total; abort early if >5h projected\\n\\n### Install commands (at top of method.py)\\n```python\\nimport subprocess, sys\\nsubprocess.run([sys.executable, '-m', 'pip', 'install', '-q',\\n    'tiktoken', 'datasets', 'numpy', 'torch'], check=True)\\n```\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
````

### [29] ASSISTANT · 2026-06-16 17:35:04 UTC

```
The plan has been written to `.terminal_claude_agent_struct_out.json`. Here's what it covers:

**Architecture**: Minimal nanoGPT-style transformer (6L, 256H, 8 heads, 4× MLP expansion) with all 5 activations swapped only into the FFN block — the rest (LayerNorm pre-norm, causal attention) stays standard.

**CWA key design decisions**:
- Forward: no-grad fixed-point iteration to find m* (K_max=50, adaptive δ = 1e-4·(1−J·s̄)), then decide backprop mode
- Unrolled mode (J·s̄ < 0.8): 3 gradient-tracked warm-start steps from m* (keeps graph short while staying accurate)
- IFT mode (J·s̄ ≥ 0.8): custom `torch.autograd.Function` with analytic ∂L/∂x and ∂L/∂J, denom clamped at 1e-4 to prevent explosion near criticality
- Per-layer stats (J, J·s̄, K, mode) logged every 500 steps

**Data**: Shakespeare via raw txt download + char tokenization; WikiText-2 via HuggingFace `datasets` + tiktoken gpt2 BPE (vocab=50257)

**Testing plan**: 6 incremental sanity checks (gradcheck for IFT backward, tiny GPT smoke test, mini 50-step Shakespeare run, data loading) before committing to full 25-run sweep

**Fallbacks**: Ordered from mild (lr reduction, J_raw init change) to severe (remove IFT entirely, drop WikiText-2, word-vocab fallback for tokenization failures)
```
