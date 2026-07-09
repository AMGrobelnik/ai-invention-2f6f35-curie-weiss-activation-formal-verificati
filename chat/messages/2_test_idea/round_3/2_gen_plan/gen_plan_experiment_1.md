# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 3 · `gen_plan`
> Run: `run_6gT5lHFn8559` — Novel Activation Function
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_experiment_1` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-06-16 21:16:52 UTC

```
model: claude-sonnet-4-6 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_3/gen_plan/gen_plan_experiment_1
```

### [2] SYSTEM-USER prompt · 2026-06-16 21:16:58 UTC

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

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter3_dir2
type: experiment
objective: >-
  Run two targeted mechanistic sub-experiments: (A) Small-weight initialization — train 10-layer CWA MLP with σ²=0.01 weight
  init to test whether smaller pre-activation magnitudes allow J·s̄ to reach the near-critical regime (>0.7), since the saturation
  barrier is caused by large activations; (B) Constant-shift ablation — implement CWA-ShiftOnly (y_i=tanh(x_i+c) where c is
  a frozen per-forward-pass constant equal to J·mean(tanh(x_i)), no fixed-point iteration) to disambiguate whether accuracy
  loss comes from correlated bias or inter-neuron coupling.
approach: |-
  SUB-EXP A (small-weight init, 3 seeds, 25 epochs, 10-layer MLP, hidden=256, CIFAR-10): Initialize all Linear layer weights with N(0, 0.01²) (vs default Kaiming N(0, 2/n)). Train CWA and GELU with identical small-init. Log J·s̄ trajectory every epoch. Primary question: does small init keep |x|<0.5 in early training, enabling J·s̄>0.7? Report max J·s̄ achieved and whether IFT branch triggers (log IFT_triggered counts). Compare accuracy vs standard-init CWA. LR=1e-3 cosine, batch=256, gradient clip=1.0.

  SUB-EXP B (constant-shift ablation, 3 seeds, 25 epochs, 10-layer MLP, CIFAR-10): Three conditions — (i) CWA-Full (learned J, full fixed-point coupling, same as art_v26XKv4_F1RM), (ii) CWA-ShiftOnly (frozen constant shift: y_i=tanh(x_i + J_frozen*mean(tanh(x_i))) computed once per forward pass with no backprop through the shift term, J_frozen=0.5), (iii) pure tanh (no shift). Compare final accuracy and gradient |ratio−1| at depth 10, 3 seeds each. If CWA-ShiftOnly≈CWA-Full in accuracy, the coupling's loss is entirely explainable by the mean shift (bias hypothesis confirmed). If CWA-ShiftOnly>CWA-Full, the iterative feedback actively hurts. If CWA-ShiftOnly≈tanh, the shift has no effect and it is a pure capacity question.

  Implement from scratch using the IFT gradient formulas from art_Lj-xi6yJR_yy: ∂L/∂x_k = s_k·[g_k + J·(Σ g_i·s_i)/(n·(1−J·s̄))], ∂L/∂J = m*·s̄·(Σ g_i·s_i)/(1−J·s̄). K_max=50, tolerance δ=1e-4·(1−J·s̄). Output method_out.json per exp_gen_sol_out schema with one example per (sub-exp, condition, seed). Report: j_s_bar_trajectory_small_init, max_j_s_bar_achieved, ift_triggered_count, accuracy_by_condition, grad_ratio_abs_deviation_by_condition, mechanistic_interpretation (bias_dominant/coupling_harmful/capacity_only).
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

### [3] HUMAN-USER prompt · 2026-06-16 21:16:58 UTC

```
Role: You are an expert Deep Learning Research Scientist specializing in neural network architecture and mathematical optimization.Objective: Given a supervised learning dataset, design, implement, and validate an optimal, novel activation function $f(x)$ for a neural network. Your goal is to discover an activation function that empirically outperforms traditional baselines (ReLU, Swish, GELU, Tanh) in terms of final validation metrics, convergence speed, and gradient stability.Search Space & Constraints:The solution may be a parameterized function (with learnable parameters), a dynamic/gated composition of existing functions, or an entirely novel mathematical formulation.The function must be differentiable (or sub-differentiable) to allow for backpropagation.Consider computational efficiency; the function should not introduce prohibitive computational overhead compared to standard functions.
```

### [4] ASSISTANT · 2026-06-16 21:17:29 UTC

```
I'll read the dependency research artifact and write the detailed plan for this mechanistic sub-experiment.
```

### [5] TOOL CALL — Read · 2026-06-16 21:17:29 UTC

```
/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_research_1/research_out.json
```

### [6] TOOL RESULT — Read · 2026-06-16 21:17:29 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_1/gen_art/gen_art_research_1/research_out.json", "content": "{\n  \"title\": \"CWA Implementation Details: DEQ IFT Backward, Competing Nonlinearities p_c, SELU Derivation, and 2025-2026 Related Work Survey\",\n  \"summary\": \"Verified technical foundations for the Curie-Weiss Activation (CWA) experiment across four components: (1) DEQ IFT backward formulas and PyTorch hook pattern — CWA's scalar fixed point allows closed-form O(n) gradients without an iterative solver; (2) Competing Nonlinearities p_c = 32/35 ≈ 0.914 analytically and ≈0.83 empirically at K₀=1, with p = Swish fraction convention confirmed; (3) SELU α₀₁≈1.6733, λ₀₁≈1.0507 from Banach fixed-point theorem on N(0,1/n)-initialized networks; (4) 2025-2026 novelty survey of 5 papers confirms no existing work introduces a learnable scalar coupling between within-sample neuron mean and individual pre-activations in an activation function.\",\n  \"answer\": \"## 1. DEQ IFT Backward Hook\\n\\nThe DEQ forward pass finds fixed point z* = f_θ(z*, x) via Anderson acceleration running inside torch.no_grad() — only z* is stored, achieving O(1) memory w.r.t. solver depth and an 88% memory reduction vs. unrolled backprop on WikiText-103 [1]. After convergence, one forward call with grad re-engages the autograd tape, and a backward hook is registered [2,3].\\n\\nBy the Implicit Function Theorem (Theorem 2.1 of [2]): ∂L/∂θ = (∂L/∂z*)(I − ∂f_θ/∂z*)^{-1}(∂f_θ/∂θ). The inverse is computed via the backward linear fixed-point: g = (∂f/∂z*)^T g + ∂L/∂z*, iterated as g_{t+1} = autograd.grad(f0, z0, g_t, retain_graph=True)[0] + grad [3]. This uses VJPs only — never materializes the full n×n Jacobian.\\n\\n**CWA closed-form IFT:** Because CWA's fixed point m* = (1/n)Σ_i tanh(x_i + J·m*) is SCALAR (dim=1), the system (I−J_f^T)g = y collapses to the scalar equation (1 − J·s̄)g = y, giving the closed-form g = y/(1−J·s̄) where s̄ = (1/n)Σ_i sech²(x_i+J·m*) [1,2,3]. No iterative backward solver is needed.\\n\\nExact CWA gradient formulas:\\n- ∂m*/∂x_i = sech²(x_i+J·m*) / (n·(1−J·s̄))\\n- ∂m*/∂J   = m*·s̄ / (1−J·s̄)\\n- ∂y_i/∂x_i = sech²(x_i+J·m*)·[1 + J·sech²(x_i+J·m*)/(n(1−J·s̄))]\\n- ∂y_i/∂J   = sech²(x_i+J·m*)·m*/(1−J·s̄)\\n- Full ∂L/∂x_i = (∂L/∂y_i)·s_i·(1+scale·s_i) + scale·s_i·Σ_k(∂L/∂y_k)·s_k where scale=J/(n(1−J·s̄))\\n\\nGradient amplification factor 1/(1−J·s̄) is well-defined as long as J·s̄ < 1 (forward convergence condition).\\n\\n## 2. Competing Nonlinearities p_c\\n\\nThe variance recursion is K^(l+1) = C_W·g(K^(l))+C_b where g(K) = E_{z~N(0,K)}[σ²(z)] [4]. For a statistical (incoherent) mixture where each neuron independently draws from {Swish, Tanh}: g^(mix)(K) = p·g^(Swish)(K) + (1−p)·g^(Tanh)(K), with p = Swish fraction (p=0 pure Tanh, p=1 pure Swish) [4].\\n\\nTaylor coefficients of the kernel function near K=0: g₂^(Tanh) = −2, g₂^(Swish) = 3/16. The stability coefficients satisfy a₁^(Tanh)=−2 (stable class, variance collapses K^(l)∼1/l) and a₁^(Swish)=3/4 (half-stable class, variance inflates) [4].\\n\\nCritical point from a₁^(mix)(p_c)=0, Eq. 17 of [4]:\\n  p_c = g₂^(Tanh)/(g₂^(Tanh) − g₂^(Swish)) = (−2)/((−2)−(3/16)) = (−2)/(−35/16) = 32/35 ≈ 0.914\\n\\nNumerical values [4]:\\n- p_c = 32/35 ≈ 0.914 (analytic, K₀→0 small-variance limit)\\n- p_c ≈ 0.83 (empirical simulation at K₀=1)\\n- Perturbative correction: p_c(K₀) = 32/35 − (384/1225)·K₀ + O(K₀²)\\n\\nFor non-standard architectures (ResNet, GPT, C_W≠1): the paper [4] restricts analysis to infinite-width MLPs with C_W=1, C_b=0, and explicitly defers convolutional/attention/layer-norm extensions to future work. Practical recommendation: empirical forward-pass calibration — sweep p over a grid, find the mixing fraction where the depth profile K^(l) is flattest on unlabeled data.\\n\\n## 3. SELU Fixed-Point Derivation\\n\\nSELU(x) = λ·{x if x>0; α(e^x−1) if x≤0}, with exact parameters from Eq. 14 of [5]:\\n- α₀₁ = −√(2/π)/(erfc(1/√2)·exp(1/2)−1) ≈ 1.6732632423543772\\n- λ₀₁ ≈ 1.0507009873554805\\n\\nThese solve the fixed-point equations at (μ,ν)=(0,1): E_{z~N(0,1)}[SELU(z)]=0 and Var[SELU(z)]=1, for LeCun-initialized weights w_i~N(0,1/n) [5].\\n\\nThe Banach fixed-point theorem is applied to the layer-to-layer distributional mapping g:(μ,ν)→(E[SELU(z)], Var[SELU(z)]) on the domain Ω = {μ∈[−0.1,0.1], ω∈[−0.1,0.1], ν∈[0.8,1.5], τ∈[0.95,1.1]}. Two conditions are proven: (1) spectral norm of Jacobian J(g)<1 (contraction, via computer-assisted proof); (2) g(Ω)⊆Ω (domain invariance). Unique attracting fixed point follows [5].\\n\\nMechanistic contrast with CWA: SELU is POINTWISE — y_i=SELU(x_i), no inter-neuron coupling, self-normalization via marginal distribution statistics. CWA is COUPLED — y_i=tanh(x_i+J·m*) where m*=(1/n)Σ_j tanh(x_j+J·m*) involves all neurons simultaneously. SELU's fixed point is distributional; CWA's is a sample-level equation solved per forward pass.\\n\\n## 4. 2025-2026 Survey: Learnable Neuron Coupling\\n\\nFive papers assessed for novelty threat to CWA:\\n\\n**Boltzmann Attention [6]** (arXiv:2606.12478, Jun 2026): Introduces learnable Ising couplings J_{ij} between ATTENTION POSITIONS (sequence/token dimension) in transformer attention. Not an activation function; not in the hidden neuron dimension. Novelty threat: NONE.\\n\\n**Competing Nonlinearities [4]** (arXiv:2605.05294, May 2026): Statistical mixture of activations with fixed (unlearnable) quenched disorder p set at initialization. No inter-neuron coupling at inference time; p is a hyperparameter, not trained. Novelty threat: NONE.\\n\\n**AlphaEvolve Activations [7]** (arXiv:2602.05688, Feb 2026): Evolutionary discovery of activation functions. The 'Turbulent' activation uses BATCH statistics (jnp.mean(x, axis=0) — cross-data axis, not cross-neuron). Batch-statistics functions fail on image tasks (OOM, poor transfer). No learnable inter-neuron coupling J. Novelty threat: PARTIAL (non-pointwise but different axis).\\n\\n**Tuning Universality [8]** (arXiv:2512.00168, Nov 2025): Stochastic theory with 4 effective couplings (r,h,D₁,D₂) characterizing collective dynamics in random DNNs — purely theoretical, no learnable parameters, no new activation function. Novelty threat: NONE.\\n\\n**Mean Field Feature Learning [9]** (arXiv:2510.15174, Oct 2025): Self-consistent MF theory for Bayesian posterior of two-layer networks trained with SGLD. Self-reinforcing feature selection is a training-dynamics property, not an activation-level coupling. No learnable scalar J. Novelty threat: NONE.\\n\\n**Novelty verdict:** No 2025-2026 paper introduces a learnable scalar J coupling the within-sample hidden-neuron mean to individual pre-activations in an activation function. CWA's architecture y_i=σ(x_i+J·m*) with J∈R learnable and m* solved as a per-example fixed point is confirmed novel [4,6,7,8,9].\",\n  \"sources\": [\n    {\n      \"index\": 1,\n      \"url\": \"https://arxiv.org/pdf/1909.01377\",\n      \"title\": \"Deep Equilibrium Models (Bai et al., NeurIPS 2019)\",\n      \"summary\": \"Original DEQ paper: IFT gradient theorem, backward via Broyden/Anderson fixed-point iteration on (I−J_f^T)g=∂L/∂z*, 88% memory reduction on WikiText-103, O(1) activation memory.\"\n    },\n    {\n      \"index\": 2,\n      \"url\": \"https://arxiv.org/pdf/2310.18605\",\n      \"title\": \"TorchDEQ: A Library for Deep Equilibrium Models (Geng & Kolter, 2023)\",\n      \"summary\": \"Theorem 2.1: ∂L/∂θ=(∂L/∂z*)(I−∂f/∂z*)^{-1}(∂f/∂θ). Backward linear fixed-point g^T=g^T(∂f/∂z*)+∂L/∂z*. Supports IFT and Phantom Gradient; backward solvers: anderson, broyden, fixed_point_iter.\"\n    },\n    {\n      \"index\": 3,\n      \"url\": \"http://implicit-layers-tutorial.org/deep_equilibrium_models/\",\n      \"title\": \"Deep Implicit Layers Tutorial Chapter 4 (Kolter, Duvenaud, Johnson)\",\n      \"summary\": \"Concrete PyTorch DEQ backward via register_hook: forward solve under no_grad(), re-engage tape, hook iterates g_{t+1}=autograd.grad(f0,z0,g_t,retain_graph=True)[0]+grad. Full Anderson acceleration code.\"\n    },\n    {\n      \"index\": 4,\n      \"url\": \"https://arxiv.org/pdf/2605.05294\",\n      \"title\": \"Competing Nonlinearities, Criticality, and Order-to-Chaos Transition (Lesser & Chowdhury, May 2026)\",\n      \"summary\": \"p_c=32/35≈0.914 analytically (K₀→0); ≈0.83 empirically (K₀=1). p=Swish fraction. g₂^Tanh=−2, g₂^Swish=3/16. Perturbative correction p_c(K₀)=32/35−(384/1225)K₀. Non-MLP: empirical calibration only.\"\n    },\n    {\n      \"index\": 5,\n      \"url\": \"https://arxiv.org/pdf/1706.02515\",\n      \"title\": \"Self-Normalizing Neural Networks / SELU (Klambauer et al., NeurIPS 2017)\",\n      \"summary\": \"α₀₁≈1.6733, λ₀₁≈1.0507 from Eq.14. Fixed point (μ,ν)=(0,1) for LeCun init w_i~N(0,1/n). Banach theorem on domain Ω proves contraction. SELU is pointwise — no inter-neuron coupling.\"\n    },\n    {\n      \"index\": 6,\n      \"url\": \"https://arxiv.org/abs/2606.12478\",\n      \"title\": \"Boltzmann Attention: Learnable Ising Couplings for Cooperative Attention (Kim & Park, Jun 2026)\",\n      \"summary\": \"Learnable Ising J_{ij} between sequence positions in transformer attention. Not an activation function; operates in sequence/token dimension not hidden neuron dimension. Novelty threat to CWA: none.\"\n    },\n    {\n      \"index\": 7,\n      \"url\": \"https://arxiv.org/pdf/2602.05688\",\n      \"title\": \"Mining Generalizable Activation Functions via AlphaEvolve (Vitvitskyi et al., Feb 2026)\",\n      \"summary\": \"Evolutionary discovery of activations. Turbulent activation uses batch statistics (cross-data axis), not within-sample hidden statistics. Batch-stats functions fail on image tasks. No learnable inter-neuron coupling J.\"\n    },\n    {\n      \"index\": 8,\n      \"url\": \"https://arxiv.org/abs/2512.00168\",\n      \"title\": \"Tuning Universality in Deep Neural Networks (Ghavasieh, Nov 2025)\",\n      \"summary\": \"Stochastic theory with 4 effective couplings (r,h,D₁,D₂) derived from activation/weight choice. Purely theoretical; no learnable coupling parameters and no proposed activation function.\"\n    },\n    {\n      \"index\": 9,\n      \"url\": \"https://arxiv.org/abs/2510.15174\",\n      \"title\": \"A Simple Mean Field Model of Feature Learning (Göring et al., Oct 2025)\",\n      \"summary\": \"Self-consistent MF theory for Bayesian posterior of two-layer networks trained with SGLD. Self-reinforcing feature selection is a training-dynamics property, not a within-sample activation coupling. No learnable J.\"\n    }\n  ],\n  \"follow_up_questions\": [\n    \"For J·s̄ approaching 1 during CWA training (ferromagnetic instability), should a regularization term penalizing J·s̄ or a hard clip on J be applied, and what is the practical effect on the accuracy-stability tradeoff?\",\n    \"The Competing Nonlinearities p_c formula assumes C_W=1 and MLP architectures. For GPT-style transformer MLPs with pre-LN (which normalizes activations before the nonlinearity), does p_c shift significantly from 0.83, or does the normalization effectively enforce the C_W=1 condition?\",\n    \"Is there any paper using a learnable scalar coupling between the within-sample hidden-dimension mean and individual pre-activations — y_i = σ(x_i + J·m*) with J trained by gradient descent — in any domain outside standard neural networks (e.g., physics-inspired ML, mean-field games, energy-based models)?\"\n  ]\n}\n", "numLines": 67, "startLine": 1, "totalLines": 67}}
```

### [7] ASSISTANT · 2026-06-16 21:21:06 UTC

```
Now I have all the details needed. Let me write the complete plan.
```

### [8] TOOL CALL — Write · 2026-06-16 21:21:06 UTC

````
File: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_3/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json

{
  "title": "CWA Mechanistic Sub-Experiments: Small-Weight Init (J·s̄ Saturation) and Constant-Shift Ablation (Coupling vs Bias)",
  "summary": "Two targeted mechanistic sub-experiments on 10-layer unnormalized MLPs (CIFAR-10): (A) small-weight init (σ=0.01) to test whether reduced pre-activation magnitudes allow J·s̄ to reach near-critical >0.7; (B) three-way ablation (CWA-Full vs CWA-ShiftOnly vs pure-tanh) to isolate whether accuracy differences arise from inter-neuron coupling or merely from the mean shift in pre-activations. Both implemented from scratch with full IFT backward (closed-form, no iterative backward solver needed). Output: method_out.json with one record per (sub-exp, condition, seed) plus aggregated mechanistic verdict.",
  "runpod_compute_profile": "gpu",
  "implementation_pseudocode": "## File layout\n```\nmethod.py          # main script: all sub-exps + output\nrequirements.txt   # torch torchvision numpy scipy\n```\n\n## Requirements\n```\ntorch>=2.1.0\ntorchvision>=0.16.0\nnumpy>=1.24.0\nscipy>=1.11.0\n```\n\n---\n## 1. DATASET: CIFAR-10\n\n```python\nimport torchvision, torchvision.transforms as T, torch\nfrom torch.utils.data import DataLoader\n\ndef get_cifar10_loaders(batch_size=256, root='/tmp/cifar10'):\n    # Flatten to 3072-dim vectors; normalize with CIFAR-10 channel stats\n    tf_train = T.Compose([T.ToTensor(),\n                          T.Normalize((0.4914, 0.4822, 0.4465),\n                                      (0.2470, 0.2435, 0.2616)),\n                          T.Lambda(lambda x: x.view(-1))])  # 3072\n    tf_test  = T.Compose([T.ToTensor(),\n                          T.Normalize((0.4914, 0.4822, 0.4465),\n                                      (0.2470, 0.2435, 0.2616)),\n                          T.Lambda(lambda x: x.view(-1))])\n    train_ds = torchvision.datasets.CIFAR10(root, train=True,  download=True, transform=tf_train)\n    test_ds  = torchvision.datasets.CIFAR10(root, train=False, download=True, transform=tf_test)\n    return (DataLoader(train_ds, batch_size=batch_size, shuffle=True,  num_workers=2, pin_memory=True),\n            DataLoader(test_ds,  batch_size=batch_size, shuffle=False, num_workers=2, pin_memory=True))\n```\n\n---\n## 2. CWA MODULE — IFT BACKWARD (always IFT, no hybrid switching)\n\nKey formulas from art_Lj-xi6yJR_yy:\n- Forward: m_{t+1} = mean_neurons(tanh(x + J·m_t)) until |m_{t+1}−m_t| < δ\n- δ = 1e-4 · (1 − J·s̄)  where s̄ = mean(sech²(x + J·m*))\n- K_max = 50\n- IFT backward (closed-form, O(n)):\n  - s_k = sech²(x_k + J·m*)  for each neuron k\n  - Σ_gs = Σ_k (g_k · s_k)   where g_k = ∂L/∂y_k (upstream gradient)\n  - ∂L/∂x_k = s_k · [g_k + J · Σ_gs / (n · (1 − J·s̄))]\n  - ∂L/∂J   = m* · s̄ · Σ_gs / (1 − J·s̄)\n  - Chain rule J = sigmoid(J_raw): ∂L/∂J_raw = ∂L/∂J · J · (1 − J)\n\n```python\nclass CWAFunction(torch.autograd.Function):\n    @staticmethod\n    def forward(ctx, x, J_raw, K_max=50):\n        # x: (batch, n_hidden) or (n_hidden,) — operate over last dim\n        J = torch.sigmoid(J_raw)  # scalar in (0,1)\n        m = torch.zeros(*x.shape[:-1], 1, device=x.device, dtype=x.dtype)\n        n = x.shape[-1]\n        \n        # Adaptive-K fixed-point iteration\n        iters_used = 0\n        for k in range(K_max):\n            h = x + J * m                        # broadcast scalar m over n neurons\n            m_new = torch.tanh(h).mean(dim=-1, keepdim=True)\n            s_bar = (1.0 / torch.cosh(h)).pow(2).mean(dim=-1, keepdim=True)\n            j_s_bar = J * s_bar\n            delta = 1e-4 * (1.0 - j_s_bar.clamp(max=0.9999))  # prevent delta->0\n            converged = (m_new - m).abs() < delta\n            m = m_new\n            iters_used = k + 1\n            if converged.all():\n                break\n        \n        m_star = m.detach()       # (batch, 1)\n        h_star = x + J * m_star\n        s_k    = (1.0 / torch.cosh(h_star)).pow(2)  # (batch, n)\n        s_bar  = s_k.mean(dim=-1, keepdim=True)      # (batch, 1)\n        j_s_bar = (J * s_bar).squeeze(-1)            # (batch,)\n        y = torch.tanh(h_star)\n        \n        # Track near-critical: J·s̄ >= 0.8 counts as IFT-triggered even though we always use IFT\n        ift_triggered = (j_s_bar >= 0.8).sum().item()\n        \n        ctx.save_for_backward(x, J_raw, m_star, s_k, s_bar)\n        ctx.ift_triggered = ift_triggered\n        ctx.j_s_bar_mean  = j_s_bar.mean().item()\n        ctx.iters_used    = iters_used\n        return y, j_s_bar.mean().detach(), torch.tensor(float(ift_triggered))\n    \n    @staticmethod\n    def backward(ctx, grad_y, grad_jsbar, grad_ift):\n        x, J_raw, m_star, s_k, s_bar = ctx.saved_tensors\n        J   = torch.sigmoid(J_raw)\n        n   = x.shape[-1]\n        j_s_bar = J * s_bar  # (batch, 1)\n        denom = (1.0 - j_s_bar).clamp(min=1e-6)\n        \n        # Σ_gs = Σ_k g_k · s_k  (per sample)\n        sum_gs = (grad_y * s_k).sum(dim=-1, keepdim=True)  # (batch, 1)\n        \n        # ∂L/∂x_k = s_k · [g_k + J · sum_gs / (n · denom)]\n        grad_x = s_k * (grad_y + J * sum_gs / (n * denom))\n        \n        # ∂L/∂J = m* · s̄ · sum_gs / denom  (summed over batch)\n        grad_J_sum = (m_star * s_bar * sum_gs / denom).sum()\n        # Chain rule: J = sigmoid(J_raw), dJ/dJ_raw = J(1-J)\n        grad_J_raw = grad_J_sum * J * (1.0 - J)\n        \n        return grad_x, grad_J_raw, None\n\n\nclass CWALayer(torch.nn.Module):\n    \"\"\"Curie-Weiss Activation with IFT backward.\"\"\"\n    def __init__(self, K_max=50):\n        super().__init__()\n        self.J_raw   = torch.nn.Parameter(torch.zeros(1))  # J = sigmoid(0) = 0.5\n        self.K_max   = K_max\n        # Tracking stats (not parameters, updated per forward)\n        self.last_j_s_bar      = 0.0\n        self.last_ift_triggered = 0\n        self.last_iters        = 0\n    \n    def forward(self, x):\n        y, j_s_bar, ift_trig = CWAFunction.apply(x, self.J_raw, self.K_max)\n        self.last_j_s_bar       = j_s_bar.item()\n        self.last_ift_triggered += int(ift_trig.item())\n        return y\n```\n\n---\n## 3. CWA-ShiftOnly MODULE (SUB-EXP B only)\n\nCWA-ShiftOnly: single non-iterative pass, shift is detached from backward graph.\n- c = J_frozen · mean(tanh(x_i))   [computed once, detached]\n- y_i = tanh(x_i + c)\n- J_frozen = 0.5 (fixed, not a parameter)\n\n```python\nclass CWAShiftOnlyLayer(torch.nn.Module):\n    \"\"\"Constant-shift ablation: y_i = tanh(x_i + c), c = J_frozen * mean(tanh(x)). No backprop through c.\"\"\"\n    def __init__(self, J_frozen=0.5):\n        super().__init__()\n        self.J_frozen = J_frozen\n    \n    def forward(self, x):\n        with torch.no_grad():\n            c = self.J_frozen * torch.tanh(x).mean(dim=-1, keepdim=True)  # (batch, 1)\n        return torch.tanh(x + c.detach())  # stop-grad on shift\n```\n\n---\n## 4. MLP ARCHITECTURE\n\n```python\nimport torch.nn as nn\n\ndef build_mlp(depth=10, hidden=256, in_dim=3072, out_dim=10, act='cwa',\n              weight_init='kaiming', K_max=50):\n    \"\"\"\n    Build an unnormalized MLP (NO BatchNorm, NO LayerNorm, NO Dropout).\n    act: 'cwa' | 'shift_only' | 'tanh' | 'gelu'\n    weight_init: 'kaiming' (default) | 'small' (sigma=0.01)\n    \"\"\"\n    def make_act():\n        if act == 'cwa':        return CWALayer(K_max=K_max)\n        elif act == 'shift_only': return CWAShiftOnlyLayer(J_frozen=0.5)\n        elif act == 'tanh':     return nn.Tanh()\n        elif act == 'gelu':     return nn.GELU()\n        else: raise ValueError(act)\n    \n    layers = []\n    dims = [in_dim] + [hidden] * (depth - 1) + [out_dim]\n    for i in range(len(dims) - 1):\n        linear = nn.Linear(dims[i], dims[i+1])\n        if weight_init == 'small':\n            nn.init.normal_(linear.weight, mean=0.0, std=0.01)\n            nn.init.zeros_(linear.bias)\n        else:  # kaiming (default PyTorch for Linear)\n            nn.init.kaiming_uniform_(linear.weight, a=math.sqrt(5))\n            fan_in, _ = nn.init._calculate_fan_in_and_fan_out(linear.weight)\n            bound = 1 / math.sqrt(fan_in) if fan_in > 0 else 0\n            nn.init.uniform_(linear.bias, -bound, bound)\n        layers.append(linear)\n        if i < len(dims) - 2:  # no activation after output\n            layers.append(make_act())\n    return nn.Sequential(*layers)\n```\n\n---\n## 5. TRAINING LOOP\n\n```python\nimport math, time\n\ndef train_model(model, train_loader, test_loader, n_epochs=25, lr=1e-3,\n                grad_clip=1.0, device='cuda', log_layer_grads=True):\n    \"\"\"\n    Returns dict:\n      - test_acc_per_epoch: list of float\n      - grad_ratio_per_epoch: list of float  (|∇W_layer1| / |∇W_layer10|)\n      - j_s_bar_per_epoch: list of float (mean over CWA layers in last batch)\n      - ift_triggered_total: int\n      - final_test_acc: float\n    \"\"\"\n    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)\n    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=n_epochs)\n    criterion = nn.CrossEntropyLoss()\n    \n    model.to(device)\n    model.train()\n    \n    results = dict(test_acc_per_epoch=[], grad_ratio_per_epoch=[],\n                   j_s_bar_per_epoch=[], ift_triggered_total=0)\n    \n    for epoch in range(n_epochs):\n        model.train()\n        for xb, yb in train_loader:\n            xb, yb = xb.to(device), yb.to(device)\n            optimizer.zero_grad()\n            logits = model(xb)\n            loss = criterion(logits, yb)\n            loss.backward()\n            torch.nn.utils.clip_grad_norm_(model.parameters(), grad_clip)\n            optimizer.step()\n        scheduler.step()\n        \n        # --- Measure gradient ratio at end of epoch (one training batch) ---\n        grad_ratio = _measure_grad_ratio(model, train_loader, criterion, device)\n        \n        # --- Collect CWA stats (last batch j_s_bar) ---\n        cwa_layers = [m for m in model.modules() if isinstance(m, CWALayer)]\n        j_s_bar_epoch = float(np.mean([c.last_j_s_bar for c in cwa_layers])) if cwa_layers else 0.0\n        ift_total_epoch = sum(c.last_ift_triggered for c in cwa_layers)\n        results['ift_triggered_total'] += ift_total_epoch\n        # Reset per-epoch counters\n        for c in cwa_layers:\n            c.last_ift_triggered = 0\n        \n        # --- Test accuracy ---\n        acc = _evaluate(model, test_loader, device)\n        \n        results['test_acc_per_epoch'].append(acc)\n        results['grad_ratio_per_epoch'].append(grad_ratio)\n        results['j_s_bar_per_epoch'].append(j_s_bar_epoch)\n        \n        print(f'Epoch {epoch+1}/{n_epochs}: acc={acc:.4f} grad_ratio={grad_ratio:.3f} '\n              f'j_s_bar={j_s_bar_epoch:.4f} ift={ift_total_epoch}')\n    \n    results['final_test_acc'] = results['test_acc_per_epoch'][-1]\n    results['max_j_s_bar_achieved'] = max(results['j_s_bar_per_epoch']) if results['j_s_bar_per_epoch'] else 0.0\n    return results\n\n\ndef _measure_grad_ratio(model, loader, criterion, device):\n    \"\"\"One-batch gradient ratio: |∇W_layer0| / |∇W_layer_last|.\"\"\"\n    model.train()\n    xb, yb = next(iter(loader))\n    xb, yb = xb.to(device), yb.to(device)\n    logits = model(xb)\n    loss = criterion(logits, yb)\n    loss.backward()\n    \n    # Collect Linear layers in order\n    linear_layers = [m for m in model.modules() if isinstance(m, nn.Linear)]\n    if len(linear_layers) < 2:\n        return 1.0\n    \n    def grad_norm(layer):\n        if layer.weight.grad is None: return 1e-10\n        return layer.weight.grad.norm().item()\n    \n    # Zero grads after measurement (will be recomputed in train step)\n    # IMPORTANT: call this AFTER optimizer.step() and before zero_grad of next step,\n    # OR use a separate no_grad forward. Better: measure at START of epoch for reporting.\n    # Simplified: return ratio of first to last LINEAR layer grad norms\n    g_first = grad_norm(linear_layers[0])  + 1e-12\n    g_last  = grad_norm(linear_layers[-2]) + 1e-12  # -2 = last hidden layer (skip output)\n    return g_first / g_last  # >1 = vanishing grads going backward\n\n\ndef _evaluate(model, loader, device):\n    model.eval()\n    correct, total = 0, 0\n    with torch.no_grad():\n        for xb, yb in loader:\n            xb, yb = xb.to(device), yb.to(device)\n            preds = model(xb).argmax(dim=-1)\n            correct += (preds == yb).sum().item()\n            total   += len(yb)\n    return correct / total\n```\n\n**IMPLEMENTATION NOTE on gradient ratio measurement**: The correct approach is to run a separate one-batch forward+backward purely for measurement (not mixed with the train step). Do:\n```python\n# After scheduler.step(), before eval:\nmodel.zero_grad()\nxb, yb = next(iter(train_loader))\nloss = criterion(model(xb.to(device)), yb.to(device))\nloss.backward()\ngrad_ratio = grad_norm(first_linear) / grad_norm(last_hidden_linear)\nmodel.zero_grad()  # clear again so train step is clean\n```\n\n---\n## 6. SUB-EXP A: SMALL-WEIGHT INIT\n\n```python\nSEEDS_A = [42, 123, 777]\nresults_A = []\n\nfor seed in SEEDS_A:\n    torch.manual_seed(seed)\n    np.random.seed(seed)\n    \n    # CWA with small init\n    model_cwa_small = build_mlp(depth=10, hidden=256, act='cwa',\n                                weight_init='small', K_max=50)\n    res_cwa_small = train_model(model_cwa_small, train_loader, test_loader,\n                                n_epochs=25, lr=1e-3, grad_clip=1.0, device=device)\n    \n    # GELU with small init (control: does small init help GELU too?)\n    torch.manual_seed(seed)\n    model_gelu_small = build_mlp(depth=10, hidden=256, act='gelu',\n                                 weight_init='small', K_max=50)\n    res_gelu_small = train_model(model_gelu_small, train_loader, test_loader,\n                                 n_epochs=25, lr=1e-3, grad_clip=1.0, device=device)\n    \n    # CWA with standard Kaiming init (baseline for comparison)\n    torch.manual_seed(seed)\n    model_cwa_kaiming = build_mlp(depth=10, hidden=256, act='cwa',\n                                  weight_init='kaiming', K_max=50)\n    res_cwa_kaiming = train_model(model_cwa_kaiming, train_loader, test_loader,\n                                  n_epochs=25, lr=1e-3, grad_clip=1.0, device=device)\n    \n    for cond, res in [('cwa_small_init',   res_cwa_small),\n                      ('gelu_small_init',  res_gelu_small),\n                      ('cwa_kaiming_init', res_cwa_kaiming)]:\n        results_A.append({\n            'sub_exp': 'A_small_weight_init',\n            'condition': cond,\n            'seed': seed,\n            'final_test_acc': res['final_test_acc'],\n            'j_s_bar_trajectory': res['j_s_bar_per_epoch'],  # list[25]\n            'max_j_s_bar_achieved': res.get('max_j_s_bar_achieved', 0.0),\n            'ift_triggered_total': res.get('ift_triggered_total', 0),\n            'grad_ratio_trajectory': res['grad_ratio_per_epoch'],\n            'test_acc_trajectory': res['test_acc_per_epoch'],\n        })\n```\n\n**Key diagnostic questions for Sub-Exp A:**\n- Does small init keep |x| small (e.g., check activation magnitudes at layer 1 in epoch 1)?\n- Does max J·s̄ ever exceed 0.7 with small init (vs Kaiming where it sits at 0.44–0.46)?\n- If IFT is triggered (J·s̄ ≥ 0.8), does accuracy improve in those epochs?\n- Does small init help or hurt CWA vs Kaiming CWA?\n\n**Add activation magnitude logging**: After the first forward pass of each epoch, log mean |x| at each layer to confirm the small-init hypothesis:\n```python\nhooks = []\nact_mags = []\nfor layer in model.children():\n    if isinstance(layer, nn.Linear):\n        h = layer.register_forward_hook(\n            lambda mod, inp, out, mags=act_mags: mags.append(out.abs().mean().item())\n        )\n        hooks.append(h)\n# After one forward pass: remove hooks, store act_mags\n```\n\n---\n## 7. SUB-EXP B: CONSTANT-SHIFT ABLATION\n\n```python\nSEEDS_B = [42, 123, 777]\nresults_B = []\n\nfor seed in SEEDS_B:\n    conditions_B = [\n        ('cwa_full',    'cwa'),         # Full CWA with learned J, fixed-point\n        ('cwa_shift_only', 'shift_only'), # CWA-ShiftOnly: single pass, detached shift\n        ('pure_tanh',   'tanh'),         # pure tanh baseline\n    ]\n    for cond_name, act in conditions_B:\n        torch.manual_seed(seed)\n        # Use Kaiming init for all (standard comparison base)\n        model = build_mlp(depth=10, hidden=256, act=act,\n                          weight_init='kaiming', K_max=50)\n        res = train_model(model, train_loader, test_loader,\n                          n_epochs=25, lr=1e-3, grad_clip=1.0, device=device)\n        \n        # Grad ratio deviation = |ratio - 1| (ratio=1 means perfect; ratio>>1 means vanishing)\n        # Use LAST epoch's grad ratio for the summary metric\n        final_grad_ratio = res['grad_ratio_per_epoch'][-1]\n        \n        results_B.append({\n            'sub_exp': 'B_shift_ablation',\n            'condition': cond_name,\n            'seed': seed,\n            'final_test_acc': res['final_test_acc'],\n            'grad_ratio_abs_deviation': abs(final_grad_ratio - 1.0),\n            'grad_ratio_trajectory': res['grad_ratio_per_epoch'],\n            'test_acc_trajectory': res['test_acc_per_epoch'],\n            'j_s_bar_trajectory': res.get('j_s_bar_per_epoch', [0.0]*25),\n            'ift_triggered_total': res.get('ift_triggered_total', 0),\n        })\n```\n\n---\n## 8. STATISTICAL ANALYSIS\n\n```python\nfrom scipy import stats\nimport numpy as np\n\ndef aggregate_results(records, sub_exp_name, metric='final_test_acc'):\n    \"\"\"Group by condition, compute mean/std/CI across seeds.\"\"\"\n    from collections import defaultdict\n    by_cond = defaultdict(list)\n    for r in records:\n        if r['sub_exp'] == sub_exp_name:\n            by_cond[r['condition']].append(r[metric])\n    \n    out = {}\n    for cond, vals in by_cond.items():\n        vals = np.array(vals)\n        n = len(vals)\n        mean = float(np.mean(vals))\n        std  = float(np.std(vals, ddof=1)) if n > 1 else 0.0\n        # 95% CI via t-distribution\n        if n > 1:\n            se = std / np.sqrt(n)\n            t_crit = stats.t.ppf(0.975, df=n-1)\n            ci = (mean - t_crit*se, mean + t_crit*se)\n        else:\n            ci = (mean, mean)\n        out[cond] = {'mean': mean, 'std': std, 'ci_95': list(ci), 'n': n, 'values': list(vals)}\n    return out\n\n# Paired t-test between conditions in Sub-Exp B\ndef paired_ttest(records, sub_exp, cond_a, cond_b, metric='final_test_acc'):\n    a = [r[metric] for r in records if r['sub_exp']==sub_exp and r['condition']==cond_a]\n    b = [r[metric] for r in records if r['sub_exp']==sub_exp and r['condition']==cond_b]\n    # Match by seed order (seeds must be same in both conditions)\n    if len(a) == len(b) and len(a) >= 2:\n        t_stat, p_val = stats.ttest_rel(a, b)\n        return {'t_stat': float(t_stat), 'p_val': float(p_val), 'n_pairs': len(a)}\n    return {'t_stat': None, 'p_val': None, 'n_pairs': len(a)}\n```\n\n---\n## 9. MECHANISTIC INTERPRETATION LOGIC\n\n```python\ndef determine_mechanistic_verdict(agg_B, agg_A):\n    \"\"\"\n    SUB-EXP B verdicts (based on final_test_acc aggregates):\n      - bias_dominant:   cwa_shift_only ≈ cwa_full  (within 0.5% absolute)\n      - coupling_harmful: cwa_shift_only > cwa_full  (shift alone beats full coupling)\n      - capacity_only:   cwa_shift_only ≈ pure_tanh (shift adds nothing)\n    SUB-EXP A verdict:\n      - init_unlocks_criticality: max_j_s_bar_achieved > 0.7 for cwa_small_init\n      - init_does_not_help: max_j_s_bar_achieved ≤ 0.7 for cwa_small_init\n    \"\"\"\n    cwa_full_acc   = agg_B['cwa_full']['mean']\n    shift_only_acc = agg_B['cwa_shift_only']['mean']\n    tanh_acc       = agg_B['pure_tanh']['mean']\n    \n    THRESH = 0.005  # 0.5% absolute accuracy threshold\n    if abs(shift_only_acc - cwa_full_acc) <= THRESH:\n        verdict_B = 'bias_dominant'\n    elif shift_only_acc > cwa_full_acc + THRESH:\n        verdict_B = 'coupling_harmful'\n    elif abs(shift_only_acc - tanh_acc) <= THRESH:\n        verdict_B = 'capacity_only'\n    else:\n        verdict_B = 'ambiguous'\n    \n    # Sub-Exp A: check if small init unlocks J·s̄ > 0.7\n    # Read from summary stats computed in run\n    return {'sub_exp_B_verdict': verdict_B,\n            'sub_exp_B_description': {\n                'bias_dominant': 'Coupling loss is entirely from mean shift; fixed-point adds no value.',\n                'coupling_harmful': 'Iterative feedback actively hurts; one-shot shift is better.',\n                'capacity_only':    'Shift has no effect; accuracy gap is pure capacity/optimization.',\n                'ambiguous': 'No clear verdict; intermediate regime.'\n            }.get(verdict_B, ''),\n            }\n```\n\n---\n## 10. OUTPUT: method_out.json\n\nSchema: exp_gen_sol_out — one `example` per (sub-exp, condition, seed), plus summary.\n\n```python\nimport json\n\nall_records = results_A + results_B\n\nagg_B = aggregate_results(all_records, 'B_shift_ablation', 'final_test_acc')\nagg_A = aggregate_results(all_records, 'A_small_weight_init', 'final_test_acc')\nagg_grad_B = aggregate_results(all_records, 'B_shift_ablation', 'grad_ratio_abs_deviation')\n\n# Max j_s_bar for sub-exp A\nmax_jsbar_by_cond = {}\nfor r in results_A:\n    c = r['condition']\n    max_jsbar_by_cond.setdefault(c, []).append(r['max_j_s_bar_achieved'])\n\n# Pairwise t-tests for sub-exp B\nttest_full_vs_shift = paired_ttest(all_records, 'B_shift_ablation',\n                                   'cwa_full', 'cwa_shift_only')\nttest_shift_vs_tanh = paired_ttest(all_records, 'B_shift_ablation',\n                                   'cwa_shift_only', 'pure_tanh')\n\nverdict = determine_mechanistic_verdict(agg_B, agg_A)\n\noutput = {\n    'title': 'CWA Mechanistic Sub-Experiments: Small-Init and Shift Ablation',\n    'examples': all_records,  # one per (sub-exp, condition, seed)\n    'summary': {\n        'sub_exp_A': {\n            'accuracy_by_condition': agg_A,\n            'max_j_s_bar_by_condition': {\n                k: {'mean': float(np.mean(v)), 'max': float(np.max(v))}\n                for k, v in max_jsbar_by_cond.items()\n            },\n            'ift_triggered_by_condition': {\n                r['condition']: r['ift_triggered_total']\n                for r in results_A\n            },\n            'j_s_bar_trajectory_small_init': [\n                r['j_s_bar_trajectory']\n                for r in results_A if r['condition'] == 'cwa_small_init'\n            ],\n        },\n        'sub_exp_B': {\n            'accuracy_by_condition': agg_B,\n            'grad_ratio_abs_deviation_by_condition': agg_grad_B,\n            'pairwise_ttests': {\n                'cwa_full_vs_shift_only': ttest_full_vs_shift,\n                'cwa_shift_only_vs_pure_tanh': ttest_shift_vs_tanh,\n            },\n        },\n        'mechanistic_interpretation': verdict['sub_exp_B_verdict'],\n        'mechanistic_description': verdict['sub_exp_B_description'],\n    }\n}\n\nwith open('method_out.json', 'w') as f:\n    json.dump(output, f, indent=2)\nprint('Written method_out.json')\n```\n\n---\n## 11. MAIN SCRIPT STRUCTURE\n\n```python\n# method.py\nimport torch, torchvision, torchvision.transforms as T\nimport torch.nn as nn\nimport numpy as np, math, json, time\nfrom scipy import stats\nfrom torch.utils.data import DataLoader\n\n# [All class/function definitions from sections 2–9 above]\n\nif __name__ == '__main__':\n    device = 'cuda' if torch.cuda.is_available() else 'cpu'\n    print(f'Device: {device}')\n    \n    train_loader, test_loader = get_cifar10_loaders(batch_size=256)\n    \n    print('=== SUB-EXP A: Small-weight initialization ===')\n    results_A = run_sub_exp_A(train_loader, test_loader, device)  # seeds [42,123,777]\n    \n    print('=== SUB-EXP B: Constant-shift ablation ===')\n    results_B = run_sub_exp_B(train_loader, test_loader, device)  # seeds [42,123,777]\n    \n    # Aggregate and write output\n    write_method_out(results_A, results_B)\n    print('DONE')\n```\n\n---\n## 12. CRITICAL IMPLEMENTATION DETAILS\n\n### Numerical stability in IFT backward\n- Clamp denom = (1 − J·s̄) to minimum 1e-6 to prevent division by zero if J·s̄ → 1\n- Clamp delta = 1e-4·(1−J·s̄) to minimum 1e-8 to prevent infinite iteration at near-criticality\n- If K_max iterations exhausted without convergence, use last m as m_star (still differentiable)\n\n### Batch dimension handling\n- x has shape (batch_size, n_hidden). Mean is over last dim (neurons within each sample).\n- m_star has shape (batch_size, 1) — different m* per sample, same J per layer.\n- s_k has shape (batch_size, n_hidden).\n- s_bar has shape (batch_size, 1).\n- J is a global scalar for the layer (not per-sample).\n\n### Gradient ratio measurement\n- Use the WEIGHT gradients of Linear layers, NOT bias. This is more stable.\n- Use layers 0 and depth-2 (not depth-1=output layer, since output is often easier to train).\n- Compute as log10(|∇W_0| + 1e-12) − log10(|∇W_{L-1}| + 1e-12), or raw ratio.\n- For sub-exp B, report |ratio−1| (deviation from 1.0 = perfect gradient flow).\n\n### J·s̄ tracking\n- Track J·s̄ over the LAST batch of each epoch (not averaged over all batches — keep it cheap).\n- Store as a list of 25 floats (one per epoch) per (sub-exp, condition, seed).\n\n### CWA-ShiftOnly correctness check\n- Verify in code: CWAShiftOnlyLayer does NOT have any nn.Parameter that receives gradients.\n- The shift c must be computed with no_grad (or detach) so backward does not trace through it.\n- This tests whether even a detached, single-step approximation to the coupling is beneficial.\n\n### IFT triggered count\n- Count: number of forward passes in an epoch where J·s̄ ≥ 0.8\n- This IS informative even though we always use IFT: it tells us how often the model enters the near-critical regime.\n- For sub-exp A with small init, the hypothesis is this count will be higher (J·s̄ stays larger).\n\n### Sub-Exp A — activation magnitude check\n- At epoch 1, batch 1: record mean absolute activation at each of the 10 hidden layers.\n- This validates the small-init hypothesis: with σ=0.01, activations should be near 0 initially.\n- After convergence (epoch 25), record again to see how much activations grow.\n- Store as 'activation_magnitudes_epoch1' and 'activation_magnitudes_epoch25' in each record.\n",
  "fallback_plan": "## Fallback A: Convergence failure in CWA fixed-point\nIf J·s̄ becomes close to 1.0 and fixed-point diverges:\n- Add hard clamp: J = sigma(J_raw).clamp(max=0.95) to prevent J=1\n- Reduce K_max to 20 and set a minimum delta=1e-6\n- If still diverging, fall back to K=3 unrolled autograd (not IFT) for stability check\n\n## Fallback B: Small init causes training instability (loss=NaN)\nWith σ=0.01, gradients may vanish immediately and loss stays at random (ln(10)≈2.3):\n- Try σ=0.05 as an intermediate between 0.01 and Kaiming\n- Add gradient clip at 0.1 (tighter than 1.0) for small-init conditions\n- If still unstable after 5 epochs, declare 'training_failure' and record final_test_acc=0.1 (chance)\n- Continue with available seeds and report the failure mode honestly\n\n## Fallback C: CWA-ShiftOnly backward accidentally trains through the shift\nIf shift gradients inadvertently flow (implementation bug):\n- Verify by checking: c.requires_grad should be False, or c is detached from the graph\n- Add assertion: assert not any(p.is_leaf for p in [c]) or c.grad_fn is None\n- Alternative: implement CWA-ShiftOnly as a plain function (no nn.Module), compute c outside torch.no_grad, then do y = tanh(x + c.detach())\n\n## Fallback D: Out-of-memory on GPU with K_max=50\nIFT backward is O(n) memory regardless of K_max (only m_star is stored), so this should not be an issue.\nBut if batch_size=256 × hidden=256 × depth=10 causes issues:\n- Reduce batch_size to 128\n- Reduce hidden to 128 and re-run (report that architecture changed)\n\n## Fallback E: Runtime exceeds 6h\nOrder of priority:\n1. Sub-Exp B with 3 seeds (highest mechanistic value — isolates coupling vs shift)\n2. Sub-Exp A with 2 seeds (drop seed=777 if time runs out)\n3. If even 1 full seed of Sub-Exp B runs, report partial results with honest caveat\nPrioritize Sub-Exp B over Sub-Exp A since the shift-vs-coupling question is the primary mechanistic test.",
  "testing_plan": "## Phase 1: Smoke test (5 minutes, should pass before full run)\n\n1. **CWA forward correctness**: instantiate CWALayer(K_max=50), pass a random (4, 32) tensor, check:\n   - Output shape is (4, 32)\n   - J starts near 0.5 (sigmoid(0))\n   - J·s̄ printed is in (0, 1)\n   - Calling backward on output.sum() does not error\n   - J_raw.grad is not None and not zero\n\n2. **IFT backward gradient check**: run `torch.autograd.gradcheck` on CWAFunction with a tiny (2, 4) input and double precision. This verifies the analytical IFT gradient matches finite-difference. Accept 1e-4 tolerance (due to fixed-point inexactness). If gradcheck fails, debug the backward formula.\n\n3. **CWA-ShiftOnly no-grad check**: instantiate CWAShiftOnlyLayer, pass (4, 32) input, call .backward() on output.sum(). Check that no parameter in the module has grad (it has no parameters). Check that the input x still gets gradients (backprop flows through tanh(x + c.detach())).\n\n4. **MLP build test**: build_mlp(depth=10, hidden=256, act='cwa') should have 10 CWA layers and 11 Linear layers (including output). build_mlp(act='shift_only') should have 10 CWAShiftOnlyLayer modules and no trainable J_raw. build_mlp(act='tanh') should have 10 nn.Tanh modules.\n\n5. **Small-init check**: build_mlp with weight_init='small'. Check that linear_layers[0].weight.std().item() ≈ 0.01.\n\n## Phase 2: Mini-scale run (10–15 minutes)\n\nRun 1 seed of each condition with n_epochs=3 and batch_size=64 on a subset of CIFAR-10 (first 5000 samples for train, 1000 for test):\n\n```python\nsubset_train = torch.utils.data.Subset(train_ds, range(5000))\nsubset_test  = torch.utils.data.Subset(test_ds,  range(1000))\n```\n\nConfirm:\n- All conditions (cwa_full, shift_only, pure_tanh, gelu) reach > 11% accuracy (above chance) by epoch 3\n- j_s_bar_per_epoch is a list of 3 floats, all in (0, 1)\n- grad_ratio_trajectory contains 3 finite positive values\n- ift_triggered_total is a non-negative integer\n- method_out.json is written and parseable\n- All `examples` have the required keys\n\n## Phase 3: Validate gradient ratio measurement\n\nWith a simple tanh model (depth=10, hidden=256, no-BN), the gradient ratio first-to-last layer should be >> 1 (vanishing gradients are expected without normalization). Confirm:\n- grad_ratio for pure_tanh baseline is noticeably > 1 (e.g., > 2.0)\n- This validates the measurement is working (we know unnormalized deep tanh vanishes)\n\n## Phase 4: Full run confirmation\n\nAfter smoke test and mini-run pass, launch full run:\n- Sub-Exp A: 3 seeds × 3 conditions × 25 epochs ≈ 225 training epochs total\n- Sub-Exp B: 3 seeds × 3 conditions × 25 epochs ≈ 225 training epochs total\nEstimated time on GPU: ~2–3h total (CWA forward pass K_max=50 adds ~5–10× overhead vs GELU)\n\nMonitor: print epoch-by-epoch output including j_s_bar, grad_ratio, accuracy for early failure detection.\n\n## Success signals\n- Sub-Exp A: If max_j_s_bar_achieved > 0.7 for cwa_small_init but ≤ 0.5 for cwa_kaiming_init, sub-exp is informative\n- Sub-Exp B: If |cwa_full_acc - cwa_shift_only_acc| < 0.005, bias_dominant verdict; if > 0.01, investigate direction\n- method_out.json written with no NaN/Inf values in any trajectory"
}
````

### [9] TOOL RESULT — Write · 2026-06-16 21:21:06 UTC

````
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_3/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"CWA Mechanistic Sub-Experiments: Small-Weight Init (J·s̄ Saturation) and Constant-Shift Ablation (Coupling vs Bias)\",\n  \"summary\": \"Two targeted mechanistic sub-experiments on 10-layer unnormalized MLPs (CIFAR-10): (A) small-weight init (σ=0.01) to test whether reduced pre-activation magnitudes allow J·s̄ to reach near-critical >0.7; (B) three-way ablation (CWA-Full vs CWA-ShiftOnly vs pure-tanh) to isolate whether accuracy differences arise from inter-neuron coupling or merely from the mean shift in pre-activations. Both implemented from scratch with full IFT backward (closed-form, no iterative backward solver needed). Output: method_out.json with one record per (sub-exp, condition, seed) plus aggregated mechanistic verdict.\",\n  \"runpod_compute_profile\": \"gpu\",\n  \"implementation_pseudocode\": \"## File layout\\n```\\nmethod.py          # main script: all sub-exps + output\\nrequirements.txt   # torch torchvision numpy scipy\\n```\\n\\n## Requirements\\n```\\ntorch>=2.1.0\\ntorchvision>=0.16.0\\nnumpy>=1.24.0\\nscipy>=1.11.0\\n```\\n\\n---\\n## 1. DATASET: CIFAR-10\\n\\n```python\\nimport torchvision, torchvision.transforms as T, torch\\nfrom torch.utils.data import DataLoader\\n\\ndef get_cifar10_loaders(batch_size=256, root='/tmp/cifar10'):\\n    # Flatten to 3072-dim vectors; normalize with CIFAR-10 channel stats\\n    tf_train = T.Compose([T.ToTensor(),\\n                          T.Normalize((0.4914, 0.4822, 0.4465),\\n                                      (0.2470, 0.2435, 0.2616)),\\n                          T.Lambda(lambda x: x.view(-1))])  # 3072\\n    tf_test  = T.Compose([T.ToTensor(),\\n                          T.Normalize((0.4914, 0.4822, 0.4465),\\n                                      (0.2470, 0.2435, 0.2616)),\\n                          T.Lambda(lambda x: x.view(-1))])\\n    train_ds = torchvision.datasets.CIFAR10(root, train=True,  download=True, transform=tf_train)\\n    test_ds  = torchvision.datasets.CIFAR10(root, train=False, download=True, transform=tf_test)\\n    return (DataLoader(train_ds, batch_size=batch_size, shuffle=True,  num_workers=2, pin_memory=True),\\n            DataLoader(test_ds,  batch_size=batch_size, shuffle=False, num_workers=2, pin_memory=True))\\n```\\n\\n---\\n## 2. CWA MODULE — IFT BACKWARD (always IFT, no hybrid switching)\\n\\nKey formulas from art_Lj-xi6yJR_yy:\\n- Forward: m_{t+1} = mean_neurons(tanh(x + J·m_t)) until |m_{t+1}−m_t| < δ\\n- δ = 1e-4 · (1 − J·s̄)  where s̄ = mean(sech²(x + J·m*))\\n- K_max = 50\\n- IFT backward (closed-form, O(n)):\\n  - s_k = sech²(x_k + J·m*)  for each neuron k\\n  - Σ_gs = Σ_k (g_k · s_k)   where g_k = ∂L/∂y_k (upstream gradient)\\n  - ∂L/∂x_k = s_k · [g_k + J · Σ_gs / (n · (1 − J·s̄))]\\n  - ∂L/∂J   = m* · s̄ · Σ_gs / (1 − J·s̄)\\n  - Chain rule J = sigmoid(J_raw): ∂L/∂J_raw = ∂L/∂J · J · (1 − J)\\n\\n```python\\nclass CWAFunction(torch.autograd.Function):\\n    @staticmethod\\n    def forward(ctx, x, J_raw, K_max=50):\\n        # x: (batch, n_hidden) or (n_hidden,) — operate over last dim\\n        J = torch.sigmoid(J_raw)  # scalar in (0,1)\\n        m = torch.zeros(*x.shape[:-1], 1, device=x.device, dtype=x.dtype)\\n        n = x.shape[-1]\\n        \\n        # Adaptive-K fixed-point iteration\\n        iters_used = 0\\n        for k in range(K_max):\\n            h = x + J * m                        # broadcast scalar m over n neurons\\n            m_new = torch.tanh(h).mean(dim=-1, keepdim=True)\\n            s_bar = (1.0 / torch.cosh(h)).pow(2).mean(dim=-1, keepdim=True)\\n            j_s_bar = J * s_bar\\n            delta = 1e-4 * (1.0 - j_s_bar.clamp(max=0.9999))  # prevent delta->0\\n            converged = (m_new - m).abs() < delta\\n            m = m_new\\n            iters_used = k + 1\\n            if converged.all():\\n                break\\n        \\n        m_star = m.detach()       # (batch, 1)\\n        h_star = x + J * m_star\\n        s_k    = (1.0 / torch.cosh(h_star)).pow(2)  # (batch, n)\\n        s_bar  = s_k.mean(dim=-1, keepdim=True)      # (batch, 1)\\n        j_s_bar = (J * s_bar).squeeze(-1)            # (batch,)\\n        y = torch.tanh(h_star)\\n        \\n        # Track near-critical: J·s̄ >= 0.8 counts as IFT-triggered even though we always use IFT\\n        ift_triggered = (j_s_bar >= 0.8).sum().item()\\n        \\n        ctx.save_for_backward(x, J_raw, m_star, s_k, s_bar)\\n        ctx.ift_triggered = ift_triggered\\n        ctx.j_s_bar_mean  = j_s_bar.mean().item()\\n        ctx.iters_used    = iters_used\\n        return y, j_s_bar.mean().detach(), torch.tensor(float(ift_triggered))\\n    \\n    @staticmethod\\n    def backward(ctx, grad_y, grad_jsbar, grad_ift):\\n        x, J_raw, m_star, s_k, s_bar = ctx.saved_tensors\\n        J   = torch.sigmoid(J_raw)\\n        n   = x.shape[-1]\\n        j_s_bar = J * s_bar  # (batch, 1)\\n        denom = (1.0 - j_s_bar).clamp(min=1e-6)\\n        \\n        # Σ_gs = Σ_k g_k · s_k  (per sample)\\n        sum_gs = (grad_y * s_k).sum(dim=-1, keepdim=True)  # (batch, 1)\\n        \\n        # ∂L/∂x_k = s_k · [g_k + J · sum_gs / (n · denom)]\\n        grad_x = s_k * (grad_y + J * sum_gs / (n * denom))\\n        \\n        # ∂L/∂J = m* · s̄ · sum_gs / denom  (summed over batch)\\n        grad_J_sum = (m_star * s_bar * sum_gs / denom).sum()\\n        # Chain rule: J = sigmoid(J_raw), dJ/dJ_raw = J(1-J)\\n        grad_J_raw = grad_J_sum * J * (1.0 - J)\\n        \\n        return grad_x, grad_J_raw, None\\n\\n\\nclass CWALayer(torch.nn.Module):\\n    \\\"\\\"\\\"Curie-Weiss Activation with IFT backward.\\\"\\\"\\\"\\n    def __init__(self, K_max=50):\\n        super().__init__()\\n        self.J_raw   = torch.nn.Parameter(torch.zeros(1))  # J = sigmoid(0) = 0.5\\n        self.K_max   = K_max\\n        # Tracking stats (not parameters, updated per forward)\\n        self.last_j_s_bar      = 0.0\\n        self.last_ift_triggered = 0\\n        self.last_iters        = 0\\n    \\n    def forward(self, x):\\n        y, j_s_bar, ift_trig = CWAFunction.apply(x, self.J_raw, self.K_max)\\n        self.last_j_s_bar       = j_s_bar.item()\\n        self.last_ift_triggered += int(ift_trig.item())\\n        return y\\n```\\n\\n---\\n## 3. CWA-ShiftOnly MODULE (SUB-EXP B only)\\n\\nCWA-ShiftOnly: single non-iterative pass, shift is detached from backward graph.\\n- c = J_frozen · mean(tanh(x_i))   [computed once, detached]\\n- y_i = tanh(x_i + c)\\n- J_frozen = 0.5 (fixed, not a parameter)\\n\\n```python\\nclass CWAShiftOnlyLayer(torch.nn.Module):\\n    \\\"\\\"\\\"Constant-shift ablation: y_i = tanh(x_i + c), c = J_frozen * mean(tanh(x)). No backprop through c.\\\"\\\"\\\"\\n    def __init__(self, J_frozen=0.5):\\n        super().__init__()\\n        self.J_frozen = J_frozen\\n    \\n    def forward(self, x):\\n        with torch.no_grad():\\n            c = self.J_frozen * torch.tanh(x).mean(dim=-1, keepdim=True)  # (batch, 1)\\n        return torch.tanh(x + c.detach())  # stop-grad on shift\\n```\\n\\n---\\n## 4. MLP ARCHITECTURE\\n\\n```python\\nimport torch.nn as nn\\n\\ndef build_mlp(depth=10, hidden=256, in_dim=3072, out_dim=10, act='cwa',\\n              weight_init='kaiming', K_max=50):\\n    \\\"\\\"\\\"\\n    Build an unnormalized MLP (NO BatchNorm, NO LayerNorm, NO Dropout).\\n    act: 'cwa' | 'shift_only' | 'tanh' | 'gelu'\\n    weight_init: 'kaiming' (default) | 'small' (sigma=0.01)\\n    \\\"\\\"\\\"\\n    def make_act():\\n        if act == 'cwa':        return CWALayer(K_max=K_max)\\n        elif act == 'shift_only': return CWAShiftOnlyLayer(J_frozen=0.5)\\n        elif act == 'tanh':     return nn.Tanh()\\n        elif act == 'gelu':     return nn.GELU()\\n        else: raise ValueError(act)\\n    \\n    layers = []\\n    dims = [in_dim] + [hidden] * (depth - 1) + [out_dim]\\n    for i in range(len(dims) - 1):\\n        linear = nn.Linear(dims[i], dims[i+1])\\n        if weight_init == 'small':\\n            nn.init.normal_(linear.weight, mean=0.0, std=0.01)\\n            nn.init.zeros_(linear.bias)\\n        else:  # kaiming (default PyTorch for Linear)\\n            nn.init.kaiming_uniform_(linear.weight, a=math.sqrt(5))\\n            fan_in, _ = nn.init._calculate_fan_in_and_fan_out(linear.weight)\\n            bound = 1 / math.sqrt(fan_in) if fan_in > 0 else 0\\n            nn.init.uniform_(linear.bias, -bound, bound)\\n        layers.append(linear)\\n        if i < len(dims) - 2:  # no activation after output\\n            layers.append(make_act())\\n    return nn.Sequential(*layers)\\n```\\n\\n---\\n## 5. TRAINING LOOP\\n\\n```python\\nimport math, time\\n\\ndef train_model(model, train_loader, test_loader, n_epochs=25, lr=1e-3,\\n                grad_clip=1.0, device='cuda', log_layer_grads=True):\\n    \\\"\\\"\\\"\\n    Returns dict:\\n      - test_acc_per_epoch: list of float\\n      - grad_ratio_per_epoch: list of float  (|∇W_layer1| / |∇W_layer10|)\\n      - j_s_bar_per_epoch: list of float (mean over CWA layers in last batch)\\n      - ift_triggered_total: int\\n      - final_test_acc: float\\n    \\\"\\\"\\\"\\n    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)\\n    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=n_epochs)\\n    criterion = nn.CrossEntropyLoss()\\n    \\n    model.to(device)\\n    model.train()\\n    \\n    results = dict(test_acc_per_epoch=[], grad_ratio_per_epoch=[],\\n                   j_s_bar_per_epoch=[], ift_triggered_total=0)\\n    \\n    for epoch in range(n_epochs):\\n        model.train()\\n        for xb, yb in train_loader:\\n            xb, yb = xb.to(device), yb.to(device)\\n            optimizer.zero_grad()\\n            logits = model(xb)\\n            loss = criterion(logits, yb)\\n            loss.backward()\\n            torch.nn.utils.clip_grad_norm_(model.parameters(), grad_clip)\\n            optimizer.step()\\n        scheduler.step()\\n        \\n        # --- Measure gradient ratio at end of epoch (one training batch) ---\\n        grad_ratio = _measure_grad_ratio(model, train_loader, criterion, device)\\n        \\n        # --- Collect CWA stats (last batch j_s_bar) ---\\n        cwa_layers = [m for m in model.modules() if isinstance(m, CWALayer)]\\n        j_s_bar_epoch = float(np.mean([c.last_j_s_bar for c in cwa_layers])) if cwa_layers else 0.0\\n        ift_total_epoch = sum(c.last_ift_triggered for c in cwa_layers)\\n        results['ift_triggered_total'] += ift_total_epoch\\n        # Reset per-epoch counters\\n        for c in cwa_layers:\\n            c.last_ift_triggered = 0\\n        \\n        # --- Test accuracy ---\\n        acc = _evaluate(model, test_loader, device)\\n        \\n        results['test_acc_per_epoch'].append(acc)\\n        results['grad_ratio_per_epoch'].append(grad_ratio)\\n        results['j_s_bar_per_epoch'].append(j_s_bar_epoch)\\n        \\n        print(f'Epoch {epoch+1}/{n_epochs}: acc={acc:.4f} grad_ratio={grad_ratio:.3f} '\\n              f'j_s_bar={j_s_bar_epoch:.4f} ift={ift_total_epoch}')\\n    \\n    results['final_test_acc'] = results['test_acc_per_epoch'][-1]\\n    results['max_j_s_bar_achieved'] = max(results['j_s_bar_per_epoch']) if results['j_s_bar_per_epoch'] else 0.0\\n    return results\\n\\n\\ndef _measure_grad_ratio(model, loader, criterion, device):\\n    \\\"\\\"\\\"One-batch gradient ratio: |∇W_layer0| / |∇W_layer_last|.\\\"\\\"\\\"\\n    model.train()\\n    xb, yb = next(iter(loader))\\n    xb, yb = xb.to(device), yb.to(device)\\n    logits = model(xb)\\n    loss = criterion(logits, yb)\\n    loss.backward()\\n    \\n    # Collect Linear layers in order\\n    linear_layers = [m for m in model.modules() if isinstance(m, nn.Linear)]\\n    if len(linear_layers) < 2:\\n        return 1.0\\n    \\n    def grad_norm(layer):\\n        if layer.weight.grad is None: return 1e-10\\n        return layer.weight.grad.norm().item()\\n    \\n    # Zero grads after measurement (will be recomputed in train step)\\n    # IMPORTANT: call this AFTER optimizer.step() and before zero_grad of next step,\\n    # OR use a separate no_grad forward. Better: measure at START of epoch for reporting.\\n    # Simplified: return ratio of first to last LINEAR layer grad norms\\n    g_first = grad_norm(linear_layers[0])  + 1e-12\\n    g_last  = grad_norm(linear_layers[-2]) + 1e-12  # -2 = last hidden layer (skip output)\\n    return g_first / g_last  # >1 = vanishing grads going backward\\n\\n\\ndef _evaluate(model, loader, device):\\n    model.eval()\\n    correct, total = 0, 0\\n    with torch.no_grad():\\n        for xb, yb in loader:\\n            xb, yb = xb.to(device), yb.to(device)\\n            preds = model(xb).argmax(dim=-1)\\n            correct += (preds == yb).sum().item()\\n            total   += len(yb)\\n    return correct / total\\n```\\n\\n**IMPLEMENTATION NOTE on gradient ratio measurement**: The correct approach is to run a separate one-batch forward+backward purely for measurement (not mixed with the train step). Do:\\n```python\\n# After scheduler.step(), before eval:\\nmodel.zero_grad()\\nxb, yb = next(iter(train_loader))\\nloss = criterion(model(xb.to(device)), yb.to(device))\\nloss.backward()\\ngrad_ratio = grad_norm(first_linear) / grad_norm(last_hidden_linear)\\nmodel.zero_grad()  # clear again so train step is clean\\n```\\n\\n---\\n## 6. SUB-EXP A: SMALL-WEIGHT INIT\\n\\n```python\\nSEEDS_A = [42, 123, 777]\\nresults_A = []\\n\\nfor seed in SEEDS_A:\\n    torch.manual_seed(seed)\\n    np.random.seed(seed)\\n    \\n    # CWA with small init\\n    model_cwa_small = build_mlp(depth=10, hidden=256, act='cwa',\\n                                weight_init='small', K_max=50)\\n    res_cwa_small = train_model(model_cwa_small, train_loader, test_loader,\\n                                n_epochs=25, lr=1e-3, grad_clip=1.0, device=device)\\n    \\n    # GELU with small init (control: does small init help GELU too?)\\n    torch.manual_seed(seed)\\n    model_gelu_small = build_mlp(depth=10, hidden=256, act='gelu',\\n                                 weight_init='small', K_max=50)\\n    res_gelu_small = train_model(model_gelu_small, train_loader, test_loader,\\n                                 n_epochs=25, lr=1e-3, grad_clip=1.0, device=device)\\n    \\n    # CWA with standard Kaiming init (baseline for comparison)\\n    torch.manual_seed(seed)\\n    model_cwa_kaiming = build_mlp(depth=10, hidden=256, act='cwa',\\n                                  weight_init='kaiming', K_max=50)\\n    res_cwa_kaiming = train_model(model_cwa_kaiming, train_loader, test_loader,\\n                                  n_epochs=25, lr=1e-3, grad_clip=1.0, device=device)\\n    \\n    for cond, res in [('cwa_small_init',   res_cwa_small),\\n                      ('gelu_small_init',  res_gelu_small),\\n                      ('cwa_kaiming_init', res_cwa_kaiming)]:\\n        results_A.append({\\n            'sub_exp': 'A_small_weight_init',\\n            'condition': cond,\\n            'seed': seed,\\n            'final_test_acc': res['final_test_acc'],\\n            'j_s_bar_trajectory': res['j_s_bar_per_epoch'],  # list[25]\\n            'max_j_s_bar_achieved': res.get('max_j_s_bar_achieved', 0.0),\\n            'ift_triggered_total': res.get('ift_triggered_total', 0),\\n            'grad_ratio_trajectory': res['grad_ratio_per_epoch'],\\n            'test_acc_trajectory': res['test_acc_per_epoch'],\\n        })\\n```\\n\\n**Key diagnostic questions for Sub-Exp A:**\\n- Does small init keep |x| small (e.g., check activation magnitudes at layer 1 in epoch 1)?\\n- Does max J·s̄ ever exceed 0.7 with small init (vs Kaiming where it sits at 0.44–0.46)?\\n- If IFT is triggered (J·s̄ ≥ 0.8), does accuracy improve in those epochs?\\n- Does small init help or hurt CWA vs Kaiming CWA?\\n\\n**Add activation magnitude logging**: After the first forward pass of each epoch, log mean |x| at each layer to confirm the small-init hypothesis:\\n```python\\nhooks = []\\nact_mags = []\\nfor layer in model.children():\\n    if isinstance(layer, nn.Linear):\\n        h = layer.register_forward_hook(\\n            lambda mod, inp, out, mags=act_mags: mags.append(out.abs().mean().item())\\n        )\\n        hooks.append(h)\\n# After one forward pass: remove hooks, store act_mags\\n```\\n\\n---\\n## 7. SUB-EXP B: CONSTANT-SHIFT ABLATION\\n\\n```python\\nSEEDS_B = [42, 123, 777]\\nresults_B = []\\n\\nfor seed in SEEDS_B:\\n    conditions_B = [\\n        ('cwa_full',    'cwa'),         # Full CWA with learned J, fixed-point\\n        ('cwa_shift_only', 'shift_only'), # CWA-ShiftOnly: single pass, detached shift\\n        ('pure_tanh',   'tanh'),         # pure tanh baseline\\n    ]\\n    for cond_name, act in conditions_B:\\n        torch.manual_seed(seed)\\n        # Use Kaiming init for all (standard comparison base)\\n        model = build_mlp(depth=10, hidden=256, act=act,\\n                          weight_init='kaiming', K_max=50)\\n        res = train_model(model, train_loader, test_loader,\\n                          n_epochs=25, lr=1e-3, grad_clip=1.0, device=device)\\n        \\n        # Grad ratio deviation = |ratio - 1| (ratio=1 means perfect; ratio>>1 means vanishing)\\n        # Use LAST epoch's grad ratio for the summary metric\\n        final_grad_ratio = res['grad_ratio_per_epoch'][-1]\\n        \\n        results_B.append({\\n            'sub_exp': 'B_shift_ablation',\\n            'condition': cond_name,\\n            'seed': seed,\\n            'final_test_acc': res['final_test_acc'],\\n            'grad_ratio_abs_deviation': abs(final_grad_ratio - 1.0),\\n            'grad_ratio_trajectory': res['grad_ratio_per_epoch'],\\n            'test_acc_trajectory': res['test_acc_per_epoch'],\\n            'j_s_bar_trajectory': res.get('j_s_bar_per_epoch', [0.0]*25),\\n            'ift_triggered_total': res.get('ift_triggered_total', 0),\\n        })\\n```\\n\\n---\\n## 8. STATISTICAL ANALYSIS\\n\\n```python\\nfrom scipy import stats\\nimport numpy as np\\n\\ndef aggregate_results(records, sub_exp_name, metric='final_test_acc'):\\n    \\\"\\\"\\\"Group by condition, compute mean/std/CI across seeds.\\\"\\\"\\\"\\n    from collections import defaultdict\\n    by_cond = defaultdict(list)\\n    for r in records:\\n        if r['sub_exp'] == sub_exp_name:\\n            by_cond[r['condition']].append(r[metric])\\n    \\n    out = {}\\n    for cond, vals in by_cond.items():\\n        vals = np.array(vals)\\n        n = len(vals)\\n        mean = float(np.mean(vals))\\n        std  = float(np.std(vals, ddof=1)) if n > 1 else 0.0\\n        # 95% CI via t-distribution\\n        if n > 1:\\n            se = std / np.sqrt(n)\\n            t_crit = stats.t.ppf(0.975, df=n-1)\\n            ci = (mean - t_crit*se, mean + t_crit*se)\\n        else:\\n            ci = (mean, mean)\\n        out[cond] = {'mean': mean, 'std': std, 'ci_95': list(ci), 'n': n, 'values': list(vals)}\\n    return out\\n\\n# Paired t-test between conditions in Sub-Exp B\\ndef paired_ttest(records, sub_exp, cond_a, cond_b, metric='final_test_acc'):\\n    a = [r[metric] for r in records if r['sub_exp']==sub_exp and r['condition']==cond_a]\\n    b = [r[metric] for r in records if r['sub_exp']==sub_exp and r['condition']==cond_b]\\n    # Match by seed order (seeds must be same in both conditions)\\n    if len(a) == len(b) and len(a) >= 2:\\n        t_stat, p_val = stats.ttest_rel(a, b)\\n        return {'t_stat': float(t_stat), 'p_val': float(p_val), 'n_pairs': len(a)}\\n    return {'t_stat': None, 'p_val': None, 'n_pairs': len(a)}\\n```\\n\\n---\\n## 9. MECHANISTIC INTERPRETATION LOGIC\\n\\n```python\\ndef determine_mechanistic_verdict(agg_B, agg_A):\\n    \\\"\\\"\\\"\\n    SUB-EXP B verdicts (based on final_test_acc aggregates):\\n      - bias_dominant:   cwa_shift_only ≈ cwa_full  (within 0.5% absolute)\\n      - coupling_harmful: cwa_shift_only > cwa_full  (shift alone beats full coupling)\\n      - capacity_only:   cwa_shift_only ≈ pure_tanh (shift adds nothing)\\n    SUB-EXP A verdict:\\n      - init_unlocks_criticality: max_j_s_bar_achieved > 0.7 for cwa_small_init\\n      - init_does_not_help: max_j_s_bar_achieved ≤ 0.7 for cwa_small_init\\n    \\\"\\\"\\\"\\n    cwa_full_acc   = agg_B['cwa_full']['mean']\\n    shift_only_acc = agg_B['cwa_shift_only']['mean']\\n    tanh_acc       = agg_B['pure_tanh']['mean']\\n    \\n    THRESH = 0.005  # 0.5% absolute accuracy threshold\\n    if abs(shift_only_acc - cwa_full_acc) <= THRESH:\\n        verdict_B = 'bias_dominant'\\n    elif shift_only_acc > cwa_full_acc + THRESH:\\n        verdict_B = 'coupling_harmful'\\n    elif abs(shift_only_acc - tanh_acc) <= THRESH:\\n        verdict_B = 'capacity_only'\\n    else:\\n        verdict_B = 'ambiguous'\\n    \\n    # Sub-Exp A: check if small init unlocks J·s̄ > 0.7\\n    # Read from summary stats computed in run\\n    return {'sub_exp_B_verdict': verdict_B,\\n            'sub_exp_B_description': {\\n                'bias_dominant': 'Coupling loss is entirely from mean shift; fixed-point adds no value.',\\n                'coupling_harmful': 'Iterative feedback actively hurts; one-shot shift is better.',\\n                'capacity_only':    'Shift has no effect; accuracy gap is pure capacity/optimization.',\\n                'ambiguous': 'No clear verdict; intermediate regime.'\\n            }.get(verdict_B, ''),\\n            }\\n```\\n\\n---\\n## 10. OUTPUT: method_out.json\\n\\nSchema: exp_gen_sol_out — one `example` per (sub-exp, condition, seed), plus summary.\\n\\n```python\\nimport json\\n\\nall_records = results_A + results_B\\n\\nagg_B = aggregate_results(all_records, 'B_shift_ablation', 'final_test_acc')\\nagg_A = aggregate_results(all_records, 'A_small_weight_init', 'final_test_acc')\\nagg_grad_B = aggregate_results(all_records, 'B_shift_ablation', 'grad_ratio_abs_deviation')\\n\\n# Max j_s_bar for sub-exp A\\nmax_jsbar_by_cond = {}\\nfor r in results_A:\\n    c = r['condition']\\n    max_jsbar_by_cond.setdefault(c, []).append(r['max_j_s_bar_achieved'])\\n\\n# Pairwise t-tests for sub-exp B\\nttest_full_vs_shift = paired_ttest(all_records, 'B_shift_ablation',\\n                                   'cwa_full', 'cwa_shift_only')\\nttest_shift_vs_tanh = paired_ttest(all_records, 'B_shift_ablation',\\n                                   'cwa_shift_only', 'pure_tanh')\\n\\nverdict = determine_mechanistic_verdict(agg_B, agg_A)\\n\\noutput = {\\n    'title': 'CWA Mechanistic Sub-Experiments: Small-Init and Shift Ablation',\\n    'examples': all_records,  # one per (sub-exp, condition, seed)\\n    'summary': {\\n        'sub_exp_A': {\\n            'accuracy_by_condition': agg_A,\\n            'max_j_s_bar_by_condition': {\\n                k: {'mean': float(np.mean(v)), 'max': float(np.max(v))}\\n                for k, v in max_jsbar_by_cond.items()\\n            },\\n            'ift_triggered_by_condition': {\\n                r['condition']: r['ift_triggered_total']\\n                for r in results_A\\n            },\\n            'j_s_bar_trajectory_small_init': [\\n                r['j_s_bar_trajectory']\\n                for r in results_A if r['condition'] == 'cwa_small_init'\\n            ],\\n        },\\n        'sub_exp_B': {\\n            'accuracy_by_condition': agg_B,\\n            'grad_ratio_abs_deviation_by_condition': agg_grad_B,\\n            'pairwise_ttests': {\\n                'cwa_full_vs_shift_only': ttest_full_vs_shift,\\n                'cwa_shift_only_vs_pure_tanh': ttest_shift_vs_tanh,\\n            },\\n        },\\n        'mechanistic_interpretation': verdict['sub_exp_B_verdict'],\\n        'mechanistic_description': verdict['sub_exp_B_description'],\\n    }\\n}\\n\\nwith open('method_out.json', 'w') as f:\\n    json.dump(output, f, indent=2)\\nprint('Written method_out.json')\\n```\\n\\n---\\n## 11. MAIN SCRIPT STRUCTURE\\n\\n```python\\n# method.py\\nimport torch, torchvision, torchvision.transforms as T\\nimport torch.nn as nn\\nimport numpy as np, math, json, time\\nfrom scipy import stats\\nfrom torch.utils.data import DataLoader\\n\\n# [All class/function definitions from sections 2–9 above]\\n\\nif __name__ == '__main__':\\n    device = 'cuda' if torch.cuda.is_available() else 'cpu'\\n    print(f'Device: {device}')\\n    \\n    train_loader, test_loader = get_cifar10_loaders(batch_size=256)\\n    \\n    print('=== SUB-EXP A: Small-weight initialization ===')\\n    results_A = run_sub_exp_A(train_loader, test_loader, device)  # seeds [42,123,777]\\n    \\n    print('=== SUB-EXP B: Constant-shift ablation ===')\\n    results_B = run_sub_exp_B(train_loader, test_loader, device)  # seeds [42,123,777]\\n    \\n    # Aggregate and write output\\n    write_method_out(results_A, results_B)\\n    print('DONE')\\n```\\n\\n---\\n## 12. CRITICAL IMPLEMENTATION DETAILS\\n\\n### Numerical stability in IFT backward\\n- Clamp denom = (1 − J·s̄) to minimum 1e-6 to prevent division by zero if J·s̄ → 1\\n- Clamp delta = 1e-4·(1−J·s̄) to minimum 1e-8 to prevent infinite iteration at near-criticality\\n- If K_max iterations exhausted without convergence, use last m as m_star (still differentiable)\\n\\n### Batch dimension handling\\n- x has shape (batch_size, n_hidden). Mean is over last dim (neurons within each sample).\\n- m_star has shape (batch_size, 1) — different m* per sample, same J per layer.\\n- s_k has shape (batch_size, n_hidden).\\n- s_bar has shape (batch_size, 1).\\n- J is a global scalar for the layer (not per-sample).\\n\\n### Gradient ratio measurement\\n- Use the WEIGHT gradients of Linear layers, NOT bias. This is more stable.\\n- Use layers 0 and depth-2 (not depth-1=output layer, since output is often easier to train).\\n- Compute as log10(|∇W_0| + 1e-12) − log10(|∇W_{L-1}| + 1e-12), or raw ratio.\\n- For sub-exp B, report |ratio−1| (deviation from 1.0 = perfect gradient flow).\\n\\n### J·s̄ tracking\\n- Track J·s̄ over the LAST batch of each epoch (not averaged over all batches — keep it cheap).\\n- Store as a list of 25 floats (one per epoch) per (sub-exp, condition, seed).\\n\\n### CWA-ShiftOnly correctness check\\n- Verify in code: CWAShiftOnlyLayer does NOT have any nn.Parameter that receives gradients.\\n- The shift c must be computed with no_grad (or detach) so backward does not trace through it.\\n- This tests whether even a detached, single-step approximation to the coupling is beneficial.\\n\\n### IFT triggered count\\n- Count: number of forward passes in an epoch where J·s̄ ≥ 0.8\\n- This IS informative even though we always use IFT: it tells us how often the model enters the near-critical regime.\\n- For sub-exp A with small init, the hypothesis is this count will be higher (J·s̄ stays larger).\\n\\n### Sub-Exp A — activation magnitude check\\n- At epoch 1, batch 1: record mean absolute activation at each of the 10 hidden layers.\\n- This validates the small-init hypothesis: with σ=0.01, activations should be near 0 initially.\\n- After convergence (epoch 25), record again to see how much activations grow.\\n- Store as 'activation_magnitudes_epoch1' and 'activation_magnitudes_epoch25' in each record.\\n\",\n  \"fallback_plan\": \"## Fallback A: Convergence failure in CWA fixed-point\\nIf J·s̄ becomes close to 1.0 and fixed-point diverges:\\n- Add hard clamp: J = sigma(J_raw).clamp(max=0.95) to prevent J=1\\n- Reduce K_max to 20 and set a minimum delta=1e-6\\n- If still diverging, fall back to K=3 unrolled autograd (not IFT) for stability check\\n\\n## Fallback B: Small init causes training instability (loss=NaN)\\nWith σ=0.01, gradients may vanish immediately and loss stays at random (ln(10)≈2.3):\\n- Try σ=0.05 as an intermediate between 0.01 and Kaiming\\n- Add gradient clip at 0.1 (tighter than 1.0) for small-init conditions\\n- If still unstable after 5 epochs, declare 'training_failure' and record final_test_acc=0.1 (chance)\\n- Continue with available seeds and report the failure mode honestly\\n\\n## Fallback C: CWA-ShiftOnly backward accidentally trains through the shift\\nIf shift gradients inadvertently flow (implementation bug):\\n- Verify by checking: c.requires_grad should be False, or c is detached from the graph\\n- Add assertion: assert not any(p.is_leaf for p in [c]) or c.grad_fn is None\\n- Alternative: implement CWA-ShiftOnly as a plain function (no nn.Module), compute c outside torch.no_grad, then do y = tanh(x + c.detach())\\n\\n## Fallback D: Out-of-memory on GPU with K_max=50\\nIFT backward is O(n) memory regardless of K_max (only m_star is stored), so this should not be an issue.\\nBut if batch_size=256 × hidden=256 × depth=10 causes issues:\\n- Reduce batch_size to 128\\n- Reduce hidden to 128 and re-run (report that architecture changed)\\n\\n## Fallback E: Runtime exceeds 6h\\nOrder of priority:\\n1. Sub-Exp B with 3 seeds (highest mechanistic value — isolates coupling vs shift)\\n2. Sub-Exp A with 2 seeds (drop seed=777 if time runs out)\\n3. If even 1 full seed of Sub-Exp B runs, report partial results with honest caveat\\nPrioritize Sub-Exp B over Sub-Exp A since the shift-vs-coupling question is the primary mechanistic test.\",\n  \"testing_plan\": \"## Phase 1: Smoke test (5 minutes, should pass before full run)\\n\\n1. **CWA forward correctness**: instantiate CWALayer(K_max=50), pass a random (4, 32) tensor, check:\\n   - Output shape is (4, 32)\\n   - J starts near 0.5 (sigmoid(0))\\n   - J·s̄ printed is in (0, 1)\\n   - Calling backward on output.sum() does not error\\n   - J_raw.grad is not None and not zero\\n\\n2. **IFT backward gradient check**: run `torch.autograd.gradcheck` on CWAFunction with a tiny (2, 4) input and double precision. This verifies the analytical IFT gradient matches finite-difference. Accept 1e-4 tolerance (due to fixed-point inexactness). If gradcheck fails, debug the backward formula.\\n\\n3. **CWA-ShiftOnly no-grad check**: instantiate CWAShiftOnlyLayer, pass (4, 32) input, call .backward() on output.sum(). Check that no parameter in the module has grad (it has no parameters). Check that the input x still gets gradients (backprop flows through tanh(x + c.detach())).\\n\\n4. **MLP build test**: build_mlp(depth=10, hidden=256, act='cwa') should have 10 CWA layers and 11 Linear layers (including output). build_mlp(act='shift_only') should have 10 CWAShiftOnlyLayer modules and no trainable J_raw. build_mlp(act='tanh') should have 10 nn.Tanh modules.\\n\\n5. **Small-init check**: build_mlp with weight_init='small'. Check that linear_layers[0].weight.std().item() ≈ 0.01.\\n\\n## Phase 2: Mini-scale run (10–15 minutes)\\n\\nRun 1 seed of each condition with n_epochs=3 and batch_size=64 on a subset of CIFAR-10 (first 5000 samples for train, 1000 for test):\\n\\n```python\\nsubset_train = torch.utils.data.Subset(train_ds, range(5000))\\nsubset_test  = torch.utils.data.Subset(test_ds,  range(1000))\\n```\\n\\nConfirm:\\n- All conditions (cwa_full, shift_only, pure_tanh, gelu) reach > 11% accuracy (above chance) by epoch 3\\n- j_s_bar_per_epoch is a list of 3 floats, all in (0, 1)\\n- grad_ratio_trajectory contains 3 finite positive values\\n- ift_triggered_total is a non-negative integer\\n- method_out.json is written and parseable\\n- All `examples` have the required keys\\n\\n## Phase 3: Validate gradient ratio measurement\\n\\nWith a simple tanh model (depth=10, hidden=256, no-BN), the gradient ratio first-to-last layer should be >> 1 (vanishing gradients are expected without normalization). Confirm:\\n- grad_ratio for pure_tanh baseline is noticeably > 1 (e.g., > 2.0)\\n- This validates the measurement is working (we know unnormalized deep tanh vanishes)\\n\\n## Phase 4: Full run confirmation\\n\\nAfter smoke test and mini-run pass, launch full run:\\n- Sub-Exp A: 3 seeds × 3 conditions × 25 epochs ≈ 225 training epochs total\\n- Sub-Exp B: 3 seeds × 3 conditions × 25 epochs ≈ 225 training epochs total\\nEstimated time on GPU: ~2–3h total (CWA forward pass K_max=50 adds ~5–10× overhead vs GELU)\\n\\nMonitor: print epoch-by-epoch output including j_s_bar, grad_ratio, accuracy for early failure detection.\\n\\n## Success signals\\n- Sub-Exp A: If max_j_s_bar_achieved > 0.7 for cwa_small_init but ≤ 0.5 for cwa_kaiming_init, sub-exp is informative\\n- Sub-Exp B: If |cwa_full_acc - cwa_shift_only_acc| < 0.005, bias_dominant verdict; if > 0.01, investigate direction\\n- method_out.json written with no NaN/Inf values in any trajectory\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
````

### [10] ASSISTANT · 2026-06-16 21:21:16 UTC

```
The plan has been written to `.terminal_claude_agent_struct_out.json`. Here's what it covers:

**Sub-Exp A (small-weight init)**: Three conditions (CWA+small init, GELU+small init, CWA+Kaiming init) across 3 seeds × 25 epochs on a 10-layer MLP on CIFAR-10. The key question is whether σ=0.01 initialization keeps pre-activations small enough that J·s̄ can exceed 0.7 (vs the 0.44–0.46 plateau seen with standard Kaiming init). Activation magnitude logging at epoch 1 and 25 validates the saturation hypothesis.

**Sub-Exp B (shift ablation)**: Three conditions (CWA-Full, CWA-ShiftOnly, pure-tanh) across 3 seeds × 25 epochs. CWA-ShiftOnly applies `tanh(x + detach(J_frozen·mean(tanh(x))))` — one forward pass with frozen shift and no backprop through the shift term. Paired t-tests and the 0.5% absolute accuracy threshold determine whether the verdict is `bias_dominant`, `coupling_harmful`, or `capacity_only`.

Both sub-experiments use the closed-form IFT backward from the dependency (`∂L/∂x_k = s_k·[g_k + J·Σ(g_i·s_i)/(n·(1−J·s̄))]`) — always IFT, no hybrid switching needed since CWA's fixed point is scalar. Compute profile: `gpu` (K_max=50 fixed-point iterations make this too slow on CPU for 450 training epochs total).
```
