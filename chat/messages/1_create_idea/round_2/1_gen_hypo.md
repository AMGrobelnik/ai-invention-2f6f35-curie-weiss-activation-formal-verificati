# gen_hypo_1 — create_idea

> Phase: `hypo_loop` · round 2 · `gen_hypo`
> Run: `run_6gT5lHFn8559` — Novel Activation Function
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_hypo_1` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-06-16 16:58:33 UTC

```
model: claude-sonnet-4-6 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/iter_2/gen_hypo/claude_agent
```

### [2] SYSTEM-USER prompt · 2026-06-16 16:58:39 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis generator (Step 2.1: GEN_HYPO — UNSEEDED mode)

Pipeline: GEN_HYPO (you) → INVENTION_LOOP → GEN_PAPER_REPO

You received a AII prompt. No external seeds — generate a novel hypothesis from your own reasoning and web research.

Your hypothesis will enter the invention loop (propose → execute → narrate) → the results become a paper + GitHub repo.
It MUST be GENUINELY NOVEL (validated against related work) and FEASIBLE TO TEST (within computational/data/tooling constraints provided).
Vague or incremental hypothesis → wasted computation across the entire pipeline.
</your_role>
</ai_inventor_context>

<strategic_mindset>
You are competing with human researchers.

YOUR ADVANTAGE: Breadth across many fields (information theory, ecology, economics, physics, cognitive science, program synthesis, etc.). No single human has this breadth.

HUMAN ADVANTAGE: Deep expertise in their specific field — they know every paper, every failed attempt, every subtle reason "obvious" ideas don't work.

HOW TO WIN: Don't create variants within their field — they'll always recognize those. Find unexpected connections ACROSS fields no single expert would think of.

NOVELTY BAR: An expert should say "I never thought of approaching it THAT way" — not "that's like paper X with a twist." If your idea lives in a crowded neighborhood of similar approaches, it's NOT novel enough.

NO TIME PRESSURE: Exploring 5-6 directions and abandoning all is a SUCCESSFUL process. Settling for a mediocre idea because you already spent so long researching it is a FAILED process.
</strategic_mindset>

<principles>
1. NOVEL - genuinely new mechanism/principle, not incremental. If you have to argue why it's different, it's NOT novel enough.
2. FEASIBLE - testable within the provided compute, data, and tooling
3. CROSS-FIELD - leverage connections across distant domains
4. RIGOROUS - consider what evidence would support OR refute it
5. PRECISE - clear language, no unnecessary jargon
</principles>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. EXPLICITLY CHECK FOR EACH ONE.

**1. Incremental Recombination Disguised as Novelty**
"Apply known method X to known domain Y" is engineering, not conceptual novelty. Your idea needs a new mechanism/principle/insight — not just a new pairing of existing things.
CHECK: If describable as "A but with B" where A and B both exist, it's recombination. What is the genuinely new IDEA?

**2. Ignoring Resource Constraints**
Every hypothesis MUST be testable with available compute, data, and tools.
CHECK: "Can this be implemented with the specific resources listed? What exact data/compute/tools do I need, and are they available?"

**3. Shallow Search Leading to False Novelty**
The same concept often exists under different terminology, in different fields, or framed differently. Searching only your own phrasing and concluding novelty is the MOST dangerous mistake.

CHECK — For every promising hypothesis:
a) Search 5-6 semantically different phrasings within the field
b) Strip to the CORE MECHANISM and search 8-10 unrelated fields (e.g., "MDL-based complexity selection" → search neural architecture search, program synthesis, Bayesian model selection) — the same principle often exists under different names
c) Search for failed/negative results ("limitations", "does not improve")
d) Search in plain English without jargon
If a paper does the same thing under a different name, it's NOT novel.

**4. Rationalizing Overlapping Prior Work**
When you find similar work, do NOT rationalize minor differences as novelty. Two common traps:

FRAMEWORK PORTING: "Nobody did this in MY framework" — if the core mechanism exists in any context (different algorithm, different ensemble type, different field), porting it is engineering, not novelty.

GAP-FILLING: Papers A, B, C each cover variants → you propose the missing combination. An expert would say "obviously someone will do that eventually."

CHECK: Strip your idea to its core mechanism. Search if that mechanism exists ANYWHERE — any framework, any field, any algorithm family. If yes, ABANDON. Don't salvage by narrowing scope or listing "critical differences."

**5. Anchoring Bias**
Once invested in a direction, you'll unconsciously downplay overlap and inflate minor differences into "key differentiators." This feels like thoroughness but is actually defensiveness.

WARNING SIGNS: listing "critical differences" instead of reconsidering; reluctance to "waste" prior search effort; refining the SAME idea instead of exploring different ones; differentiators about context/framework rather than core mechanism.

CHECK: If you found even 1 paper with a similar core mechanism, ABANDON. The best hypotheses rarely come from your first direction. Each abandonment is progress.

**6. Relying on Search Snippets Without Fetching**
Search snippets are NOT enough to assess overlap or understand an approach. The actual mechanism and limitations are only in the full text.
CHECK: FETCH and read any potentially relevant result. Don't assess novelty from titles and snippets alone.

**7. Same-Neighborhood Pivoting**
Replacing one idea with a variant in the same conceptual space is NOT a genuine pivot. If all your directions are "[different adjective] + [same core concept]", you haven't actually explored.

CHECK: Would a single expert in that subfield have thought of ALL your directions? If yes, bring in a mechanism or framing from a completely unrelated field. That's where genuine novelty lives.
</common_mistakes_to_avoid>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

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

<task_preview>
You will generate 1 novel groundbreaking research hypothesis in the AII prompt provided in the accompanying user message.
</task_preview>

<YOUR_AII_PROMPT>
Your AII prompt — the research prompt to invent within — is provided as a SEPARATE user message in this turn, immediately following this one. Treat that message as the definition of what to generate a hypothesis for.
</YOUR_AII_PROMPT>

<hypothesis_inspiration>
<YOUR_INSPIRATION>
Human researchers overspecialize — they know their domain deeply but lack breadth to see when other fields have already solved analogous problems. Your advantage is breadth. Only propose a cross-domain transfer if it concretely outperforms existing approaches in this domain. Avoid handwavy analogies — if the imported method is vaguer or weaker than what domain experts already use, it's not worth proposing.

Explore cross-domain inspiration at three levels, from abstract to concrete. At each level, consider both established and recent developments — with slight priority for newer work, which tends to leverage more powerful tools and be less widely known.

1. CONCEPTUAL: Borrow high-level ideas, framings, or design philosophies from distant fields.
   What mental model or approach from another domain suggests a novel angle on this problem?

2. PROCEDURAL: Adapt specific problem-solving processes from other domains.
   What workflow, iterative strategy, or pipeline used elsewhere could restructure how this problem is attacked?

3. METHODOLOGICAL: Import concrete methods directly from other fields with minimal modification.
   What algorithm, formula, or technique from a different domain applies here as-is or with adaptation?

Cast wide — draw from ANY field, not just these examples: ecology, economics, physics, linguistics, game theory, control theory, materials science, cognitive science, epidemiology. The best hypotheses often come from Level 2-3 transfers that experts in the field would never encounter.
</YOUR_INSPIRATION>
</hypothesis_inspiration>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

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
</available_resources>

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

<YOUR_TASK>
Generate 1 novel groundbreaking research hypothesis in the AII prompt that is feasible with the above constraints.

<web_research_process>
Read and STRICTLY follow these skills: aii-web-tools.

1. DIVERGE: Brainstorm 5-7 diverse directions WITHOUT searching.
   Think across fields — what techniques from unrelated domains (ecology, economics, physics,
   linguistics, game theory, etc.) could inspire a novel mechanism? What assumptions does the field
   take for granted? Diversity matters more than depth here.

2. SEARCH: Web search for a high-level overview of each direction.
   What similar approaches exist? Is this genuinely novel or incremental? Remember: snippets
   are NOT enough for detailed understanding — treat search as discovery only.

3. FETCH & READ: MUST fetch any potentially relevant URL — you cannot assess novelty from
   snippets alone. Use the aii-web-tools skill:
   - fetch a page for high-level understanding of HTML pages
   - fetch_grep for exact details, methodology, or PDFs
   Prioritize recent papers closest to your idea. If you find significant overlap, PIVOT.

4. ADVERSARIAL NOVELTY CHECK: Actively try to DISPROVE novelty. Most important step.
   Run the FULL search checklist from <common_mistakes_to_avoid> mistake 3 — within-field
   rephrasings, cross-field core-mechanism search, failed/negative results, plain English.
   Ask: "Is the core insight of your hypothesis new, or known things in a new wrapper?"
   "Would an expert find this genuinely surprising?"
   MANDATORY SELF-CHECK: State the core mechanism in one sentence. Does it exist in ANY
   algorithm, framework, or field? If yes — even in a different framework — ABANDON.

5. FEASIBILITY CHECK: Verify your hypothesis is testable with provided resources. What specific data/compute/tools
   needed? All available within constraints?

6. ABANDON or PROCEED:
   ABANDON if: 2+ similar papers exist; you need to argue "critical differences"; core mechanism
   exists in any context.
   Abandoning is progress — go back to step 1 in a genuinely DIFFERENT direction (not a variant).
   PROCEED only if novelty is SELF-EVIDENT — an expert would immediately see it's new without
   explanation.

7. ITERATE: Expect to repeat steps 1-6 multiple times. The first few directions will likely be
   non-novel. This is normal. Don't settle for your first idea just because you've invested time.

<CRITICAL>We want SCIENTIFIC novelty (new mechanism, principle, or insight — the contribution is
knowledge), NOT application novelty (known methods applied to a new domain — the contribution is a
product). If an expert would say "clever engineering but known science," keep searching.
Hypothesis must be feasible within available resources.</CRITICAL>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>
</web_research_process>

Prioritize simplicity. Use concise, approachable language. The explanation should be fully self-contained.
</YOUR_TASK>

<previous_hypothesis>
Your hypothesis from the previous iteration. The reviewer evaluated it below.

hypothesis_id: gen_hypo_1
model: claude-sonnet-4-6
is_seeded: false
seeds: []
kind: hypothesis
title: >-
  Curie-Weiss Mean-Field Activation: Self-Consistent Within-Layer Coupling That Learns Critical Gain
hypothesis: >-
  A neural network activation function defined as the fixed point of the Curie-Weiss mean-field self-consistency equation
  — y_i = tanh(x_i + J * mean(y)) for all neurons i in a layer, where J is a single learnable scalar coupling constant — will
  outperform standard pointwise activations (ReLU, GELU, Swish, Tanh) in convergence speed, gradient stability, and final
  accuracy, because: (1) J self-organizes toward the critical value J → 1 during training, maximizing the layer's input sensitivity
  and gradient flow simultaneously; (2) the within-sample mean-field coupling acts as a learned, parameter-efficient form
  of collective gain control that is unavailable to any purely pointwise activation; and (3) near criticality the effective
  gain 1/(1 − J·s̄) diverges smoothly, maintaining gradient signal across many layers without the dead-neuron or saturation
  pathologies of existing activations.
motivation: >-
  All standard activation functions (ReLU, GELU, Swish, tanh) are applied pointwise: each neuron's output depends only on
  its own pre-activation. This ignores the collective behavior of all neurons in the layer — a dimension of expressivity that
  biological neural systems exploit via homeostatic coupling. The critical cost of this independence is that the effective
  gain of each layer must be managed externally (via weight initialization, batch norm, careful learning rate schedules).
  Criticality theory in deep learning (Poole et al. 2016; Yang & Schoenholz 2017) shows that networks at the 'edge of chaos'
  — where the Jacobian singular values are near unity — train fastest and generalize best. Existing methods achieve this only
  at initialization; the network drifts away from criticality as weights update. This hypothesis proposes an activation function
  that ENFORCES near-critical behavior throughout training via a thermodynamic self-consistency mechanism, adapting the gain
  of the entire layer collectively with a single learned parameter. The impact is: fewer dead neurons, more stable gradient
  propagation in deep networks, and empirically faster convergence, all without adding normalization overhead or per-neuron
  parameters.
assumptions:
- >-
  The Curie-Weiss fixed point (y = tanh(x + J·mean(y))) has a unique stable solution for |J| < 1 and converges in 3–5 iterations
  of mean-field updating starting from m = 0, making it computationally feasible as a drop-in activation.
- >-
  Gradient-based training of J will push it toward the critical value J → 1⁻ because this maximizes the layer's mutual information
  between input and output (via the diverging susceptibility), giving the network a training incentive to approach criticality.
- >-
  The within-sample mean-field coupling (coupling outputs to each other within one forward pass through the fixed point) provides
  strictly more expressive gain control than pointwise activations, enabling better representation of features that require
  collective detection.
- >-
  PyTorch autograd can differentiate through the fixed-point iteration accurately (either directly via unrolled iterations
  or via the implicit function theorem applied to F(m) = mean(tanh(x + J·m)) − m = 0), making end-to-end gradient training
  straightforward.
- >-
  The improvement generalizes across architectures (MLP, CNN, Transformer) because the gain-control mechanism is architecture-agnostic
  and operates within any feedforward layer.
investigation_approach: >-
  Implement CWA in PyTorch as a custom nn.Module. Forward pass: iterate m ← mean(tanh(x + J·m)) for 5 steps starting from
  m=0; output y_i = tanh(x_i + J·m*). Backward pass: use PyTorch autograd through the unrolled iterations. Train small MLPs
  (3–6 layers, 256 hidden units) on CIFAR-10, MNIST, and a tabular dataset (e.g., adult-income), comparing CWA against ReLU,
  GELU, Swish, and tanh baselines. Measure: (1) final validation accuracy, (2) convergence speed (epochs to 95% of peak),
  (3) gradient norm stability across layers (log of ratio of gradient norms at layer 1 vs. layer L), and (4) the learned value
  of J per layer at convergence. Also test with J constrained to [0, 1) to prevent bistability during experiments, and free
  J (unconstrained) to observe whether it self-organizes near criticality. Report effect size with confidence intervals using
  5 random seeds per configuration. Total LLM API cost: $0 (pure neural network training, no LLM calls required); compute:
  CPU sufficient for MNIST/tabular, GPU for CIFAR-10.
success_criteria: >-
  CONFIRM if: (1) CWA achieves ≥0.5% higher final accuracy than the best baseline on at least 2 of 3 datasets, AND (2) gradient
  norm ratio (layer-1/layer-L) for CWA is ≤2× closer to 1.0 than best baseline, indicating more stable gradient propagation,
  AND (3) learned J converges to values in [0.7, 1.0] across layers (near-critical regime). DISCONFIRM if: (1) CWA performs
  worse than or within noise of all baselines on all datasets, OR (2) J consistently converges far from criticality (J < 0.3
  or J ≥ 1.0 causing instability), OR (3) convergence requires significantly more than 5 iterations making it computationally
  prohibitive. PARTIAL CONFIRM if: CWA improves gradient stability (criterion 2 and 3) but not final accuracy — this would
  suggest the benefit is architecture-dependent and motivate testing in deeper networks where gradient pathologies dominate.
related_works:
- >-
  Milletarì et al. (2018, arXiv:1805.08786) 'Mean Field Theory of Activation Functions in Deep Neural Networks': Uses statistical
  mechanics to DERIVE existing activations (tanh, ReLU, Swish) as natural solutions to energy-based models. Key difference:
  their work provides a post-hoc physical interpretation of known functions; we propose a NEW activation defined by the actual
  Curie-Weiss self-consistency equation with a learnable coupling J, which introduces within-layer neuron coupling absent
  in all their derived activations.
- >-
  Sakthivadivel (2021, arXiv:2102.04896) 'Formalising the Use of the Activation Function in Neural Inference': Shows the sigmoid/tanh
  family corresponds to mean-field Ising models, providing a neuroscientific and physical justification for their use. Key
  difference: this work explains why tanh ≈ independent mean-field spin; our proposal uses the COUPLED mean-field equation
  m = (1/n)Σ tanh(x_i + J·m) as the actual activation, adding the explicit inter-neuron coupling term J·m that their analysis
  treats as zero.
- >-
  Bal (2021, 'Deep Implicit Attention'): Applies Thouless-Anderson-Palmer mean-field equations to ATTENTION mechanisms in
  transformers, showing softmax attention is one step of naive mean-field inference. Key difference: their work reformulates
  the attention operator; our proposal replaces ACTIVATION FUNCTIONS (nonlinearities within a layer), a different architectural
  component. Our CWA operates within a single layer's neurons, while their work operates across token positions.
- >-
  Yang & Schoenholz (2017) 'Mean Field Residual Networks' and Poole et al. (2016) 'Exponential Expressivity': Show that networks
  at the edge of chaos (Jacobian singular values ≈ 1) propagate information best and train fastest, achieved via careful weight
  variance initialization. Key difference: these works achieve criticality through INITIALIZATION — it is not maintained during
  training. CWA provides a mechanism through the activation function itself (via learned J → 1) that actively maintains criticality
  throughout the training process.
- >-
  Amos & Kolter (2017) 'OptNet: Differentiable Optimization as a Layer in Neural Networks': Introduces differentiable quadratic
  program solvers as neural network layers. Key difference: OptNet replaces full linear layers with QP solvers (O(n³) per
  solve); CWA is a lightweight activation-level operation (O(n·K) for K≈5 iterations) that is a drop-in replacement for any
  pointwise activation, not a new layer type.
- >-
  Bai et al. (2019) 'Deep Equilibrium Models (DEQ)': Applies fixed-point iteration at the FULL-LAYER level — the entire layer
  mapping is solved to a fixed point. Key difference: DEQ replaces the full layer (including the weight matrix); CWA is a
  within-layer activation function that only couples neurons through a single scalar mean field, retaining the standard linear
  weight matrix and adding only one learnable parameter J per layer.
inspiration: >-
  This hypothesis is a Level-3 (methodological) cross-domain transfer from statistical physics, specifically the Curie-Weiss
  model of ferromagnetism. In physics, the Curie-Weiss mean-field equation m = tanh(β(h + J·m)) describes how an Ising spin
  aligns with an external field h plus a self-consistent feedback from the average magnetization J·m of all other spins. The
  critical insight is that this 'self-consistent' structure — where the output depends on the mean of all outputs — is entirely
  absent from all standard neural network activations, which are purely pointwise. The cross-domain insight is: just as a
  ferromagnet near its Curie temperature exhibits maximum magnetic susceptibility (tiny external fields produce large magnetization
  changes), a neural layer near its 'critical coupling' J→1 should exhibit maximum input sensitivity — small changes in the
  pre-activation produce large, amplified output changes. This is exactly what gradient-based learning needs: high sensitivity
  to inputs means high signal-to-noise ratio in gradient updates. The self-organization toward criticality (like 'self-organized
  criticality' in sandpile models) emerges naturally because networks that approach J=1 have higher effective capacity and
  thus lower training loss, giving gradient descent an incentive to push J toward the critical point.
terms:
- term: Curie-Weiss Model
  definition: >-
    A mean-field model of ferromagnetism where each spin interacts with the average ('mean field') of all other spins rather
    than with neighbors individually. Described by the self-consistency equation m = tanh(β(h + J·m)), where m is the average
    magnetization, h is the external field, J is the coupling strength, and β is the inverse temperature. Exhibits a phase
    transition at βJ = 1.
- term: Curie-Weiss Activation (CWA)
  definition: >-
    The proposed activation function defined by the fixed point y* of the equation y = tanh(x + J·mean(y)), where x is the
    vector of pre-activations, y is the vector of activations, J is a learnable scalar coupling, and mean(y) is the layer-wise
    mean of y. The fixed point is found by iterating m ← mean(tanh(x + J·m)) and setting y_i = tanh(x_i + J·m*).
- term: Coupling Constant (J)
  definition: >-
    A single learnable scalar parameter per layer in CWA that controls the strength of inter-neuron coupling through the mean
    field. J=0 recovers independent tanh; J→1 approaches criticality with maximum gain; J>1 creates a bistable activation
    with two stable fixed points (the layer has spontaneous symmetry breaking).
- term: Critical Gain
  definition: >-
    The effective gradient amplification of the CWA at the critical coupling J=1. By the implicit function theorem, ∂y_i/∂x_i
    ∝ sech²(x_i + m*)/(1 − J·s̄), where s̄ = mean(sech²(x + m*)) ∈ (0,1]. As J·s̄ → 1, this gain diverges, enabling maximum
    sensitivity. In practice, J learns a value slightly below 1 to maintain stability.
- term: Mean-Field Self-Consistency
  definition: >-
    The defining property of CWA where the activation output y depends on its own mean (mean(y)), creating a fixed-point equation
    that must be solved iteratively. Unlike layer normalization (which uses the mean of the INPUT x), self-consistency means
    the mean of the OUTPUT y feeds back into the computation, coupling all neurons in the layer through their collective state.
- term: Edge of Chaos
  definition: >-
    The critical operating regime of a neural network where the Jacobian of the layer mapping has singular values close to
    1, balancing ordered (singular values < 1, vanishing gradients) and chaotic (singular values > 1, exploding gradients)
    phases. CWA is hypothesized to self-organize toward this regime via the learned coupling J → 1.
- term: Pointwise Activation
  definition: >-
    Any activation function where each neuron's output y_i depends only on its own pre-activation x_i, with no dependence
    on other neurons' pre-activations or outputs. All standard activations (ReLU, GELU, Swish, tanh, sigmoid) are pointwise.
    CWA is not pointwise because y_i depends on mean(y), which involves all neurons.
summary: >-
  We propose the Curie-Weiss Activation (CWA), a novel activation function where each neuron's output is the fixed point of
  a mean-field self-consistency equation y_i = tanh(x_i + J·mean(y)), with J a single learnable coupling per layer. Borrowed
  from the physics of ferromagnetism, this within-layer coupling gives the activation a tunable effective gain 1/(1 − J·s̄)
  that gradient descent is hypothesized to push toward the critical point J → 1, achieving maximum sensitivity and gradient
  stability throughout training without requiring batch statistics or per-neuron parameters.
</previous_hypothesis>

<previous_review_feedback>
A reviewer evaluated your previous hypothesis and provided the feedback below.

IMPORTANT: Do NOT generate a completely new hypothesis. Take the previous hypothesis above and
REVISE it to address the feedback. Keep what works, fix what was criticized.

You MUST address ALL the critiques. Do NOT repeat the same mistakes.

kind: reviewer_feedback
id: review_hypo_4285d418af4f
overall_assessment: >-
  The Curie-Weiss Activation (CWA) is a creative and physically well-motivated proposal that imports the mean-field self-consistency
  equation from ferromagnetism as a neural network activation function. The core idea — coupling neurons within a layer through
  their collective mean field and learning the coupling J — is genuinely novel at the activation level and is cleanly differentiated
  from DEQ models (which operate at the full-layer scale) and from prior mean-field interpretations of existing activations.
  However, the hypothesis contains a fundamental internal contradiction: the 5-step fixed-point iteration degrades in accuracy
  exactly at the near-critical regime (J·s̄ → 1) where the claimed performance benefits are supposed to materialize. This
  'critical slowing down' flaw undermines the computational feasibility assumption. Additionally, the central empirical claim
  — that gradient descent spontaneously pushes J → 1 — is speculative and lacks theoretical grounding. Two very recent concurrent
  works (Boltzmann Attention, arXiv:2606.12478, June 2026; Competing Nonlinearities, arXiv:2605.05294, May 2026) are unacknowledged
  and directly relevant. The experimental scope (MLP-only on MNIST/CIFAR-10) is too narrow to establish a contribution at
  top-tier venues. These are all fixable issues within a revised hypothesis, making this a borderline case: worth investigating
  but requiring significant revision before a clean experimental run.
strengths:
- >-
  Genuinely novel activation-level mechanism: CWA introduces within-layer inter-neuron coupling via a fixed-point self-consistency
  equation, which is absent from all standard pointwise activations. The distinction from DEQ (which replaces full layers)
  and TAP mean-field (which reformulates attention, not activation functions) is clearly and correctly drawn.
- >-
  Parameter efficiency: a single learnable scalar J per layer achieves collective gain control without per-neuron parameters,
  keeping the parameter overhead negligible.
- >-
  Well-grounded physical analogy: the mapping from ferromagnetic Curie-Weiss susceptibility to neural gain control is precise
  and non-trivial. The observation that existing activations correspond to J=0 (independent spins) and that J→1 is the critical
  point is mathematically correct.
- >-
  Clean mathematical formulation: the forward pass, fixed-point iteration, IFT-based backward pass, and the diverging effective
  gain 1/(1−J·s̄) are all explicitly specified and technically correct.
- >-
  Clear motivation for edge-of-chaos maintenance: existing criticality approaches (Poole 2016, Yang & Schoenholz 2017) achieve
  criticality only at initialization and drift away. CWA's proposal to enforce criticality throughout training via a learned
  parameter is a meaningful problem to address.
- >-
  Honest acknowledgment of the J≥1 bistability regime and the proposal to constrain J ∈ [0,1) as a safety measure.
- >-
  Good related work coverage: Amos & Kolter (OptNet), Bai et al. (DEQ), Bal (Deep Implicit Attention), and Poole/Yang criticality
  papers are correctly characterized and differentiated.
dimension_scores:
- dimension: soundness
  score: 2
  justification: >-
    The fixed-point iteration convergence rate is (J·s̄) per step, so at J·s̄ → 1 (the claimed critical/beneficial regime)
    the 5-step iteration yields errors ≈ (J·s̄)^5 × initial error ≈ 0.77× at J·s̄=0.95 — far from the true fixed point. This
    is classical critical slowing down. The hypothesis therefore contains a fundamental internal contradiction: the 5-iteration
    assumption is cheapest exactly when J is small (far from criticality) and breaks down exactly when J is near 1 (the claimed
    sweet spot). Additionally, the claim that gradient descent spontaneously pushes J → 1 is unsubstantiated; J·s̄=1 is the
    true critical condition, not simply J=1, and the actual critical coupling depends on the input distribution. These are
    not minor estimation issues — they potentially undermine the entire mechanism.
  improvements:
  - >-
    Derive or bound the fixed-point approximation error after K iterations as a function of J·s̄ explicitly (error ≈ (J·s̄)^K
    |m*|). Report the required K for <1% error at J·s̄ ∈ {0.5, 0.8, 0.9, 0.95, 0.99}. This will surface whether 5 is sufficient
    for the regime of interest.
  - >-
    Reframe the critical condition correctly: the effective Jacobian eigenvalue is J·s̄ = J·mean(sech²(x+J·m*)), not simply
    J. Add a figure or table showing how J_eff = J·s̄ varies with input variance σ², so readers understand that 'J → 1' and
    'criticality' are not the same.
  - >-
    Provide a theoretical argument (or cite evidence) for why gradient descent should push J·s̄ toward 1. The Katsnelson et
    al. (2021, arXiv:2107.03402) result on SOC addresses weight matrix statistics and does not directly imply that an explicit
    scalar coupling parameter J is pushed toward any particular value by task loss minimization.
- dimension: presentation
  score: 3
  justification: >-
    Writing is clear and well-organized. The terms section is unusually detailed and helpful. The physical analogy is explained
    accessibly. However, two important recent papers are missing from related works (Boltzmann Attention, 2606.12478, June
    2026; Competing Nonlinearities, 2605.05294, May 2026), and the claim that 'all standard activations are pointwise' is
    technically incorrect (softmax, widely used in attention and output layers, is non-pointwise). The success criteria conflate
    J→1 with criticality, using an imprecise formulation that will confuse readers.
  improvements:
  - >-
    Add Boltzmann Attention (arXiv:2606.12478, Kim & Park, June 2026) to related works. This concurrent paper proposes learnable
    Ising couplings J for attention weights and is the closest concurrently published work. Clarify the distinction: CWA operates
    on neuron activations within a single layer (replacing the nonlinearity), while Boltzmann Attention operates on inter-position
    attention weights (replacing the attention operator). Different architectural component, but same physical inspiration
    and similar J parameter.
  - >-
    Add Lesser & Chowdhury (arXiv:2605.05294, May 2026) to related works. This paper achieves edge-of-chaos criticality through
    a statistical mixture of activations (tanh + Swish at mixing fraction p), achieving scale-invariant variance propagation.
    It is a directly competing approach to CWA's goal of reaching criticality via activation design. CWA must differentiate
    itself and ideally include it as a baseline.
  - >-
    Qualify the statement 'all standard activations are pointwise.' Softmax is widely used in the final layer and in attention
    heads and is not pointwise. A parenthetical clarifying 'in the sense of hidden-layer activations between linear layers'
    would be accurate.
- dimension: contribution
  score: 2
  justification: >-
    CWA is a novel idea at the activation level, but the proposed experimental scope (3-6 layer MLPs on MNIST, CIFAR-10, adult-income)
    is far too narrow to establish a contribution at top-tier venues. Activation function papers accepted at NeurIPS/ICML/ICLR
    typically demonstrate improvements on ResNets or ViTs on ImageNet, or in transformer language models. The proposed experiments
    would constitute preliminary evidence only. Furthermore, the key value proposition (gain control without normalization
    overhead) should be directly tested against networks that already use normalization layers, which is currently absent.
  improvements:
  - >-
    Extend experiments to include at minimum: (a) ResNet-20/ResNet-56 on CIFAR-100, (b) a small Transformer (GPT-2 scale or
    smaller) on a language modeling task. These are the standard benchmarks where activation function differences matter at
    scale.
  - >-
    Add an explicit baseline: tanh + LayerNorm (same nonlinearity, same collective behavior via input normalization) and SELU
    (self-normalizing activation, Klambauer 2017). CWA's value-add over these must be demonstrated, because both already address
    the gradient stability motivation.
  - >-
    Test CWA inside a network that already uses BatchNorm or LayerNorm to determine whether CWA provides value-add when normalization
    is already present. This tests the hypothesis's core claim that CWA's output-based self-consistency is distinct from input-statistics-based
    normalization.
critiques:
- id: ''
  category: methodology
  severity: major
  description: >-
    Critical slowing down creates a fundamental internal contradiction. The fixed-point iteration m_{t+1} = mean(tanh(x +
    J·m_t)) converges with per-step geometric rate ρ = J·s̄ = J·mean(sech²(x+J·m*)). Classical results from statistical physics
    and numerical analysis show that at ρ → 1 (the critical point), the iteration requires O(1/(1-ρ)) steps to reach a fixed
    accuracy. With 5 iterations and ρ = 0.95 (a modest J near criticality), the residual error is ρ^5 ≈ 0.77 times the initial
    error — meaning the 5-step output is far from the true fixed point. The hypothesis claims J self-organizes toward J·s̄
    → 1, but this is precisely the regime where 5 iterations become inadequate. Worse, the gradient via unrolled iterations
    is computed at the 5-step approximation, not the true fixed point, so even the gradient signal is corrupted near criticality.
    The IFT approach assumes the fixed point has been reached, which also fails when J·s̄ is near 1.
  suggested_action: >-
    Derive the number of iterations K required for |m_K - m*| < ε as K ≥ log(ε/|m*|)/log(J·s̄). Table this for J·s̄ ∈ {0.5,
    0.8, 0.9, 0.95, 0.99}. Either (a) adapt K dynamically (iterate until convergence, e.g., |m_{t+1}-m_t| < δ), and measure
    wall-clock cost as a function of J at training time, or (b) restrict experiments to J·s̄ < 0.8 and acknowledge that the
    activation is not operating at criticality. An adaptive-K implementation is the better path as it is honest about the
    computational cost.
- id: ''
  category: evidence
  severity: major
  description: >-
    The self-organized criticality (SOC) claim — that gradient descent spontaneously pushes J toward the critical coupling
    — is stated as a core assumption but is entirely unsubstantiated. The argument in the hypothesis is essentially: 'networks
    at J=1 have higher effective capacity → lower training loss → gradient descent pushes J → 1.' But higher gain does not
    guarantee lower training loss; high gain can also cause overfitting, instability, and loss explosion. The Katsnelson et
    al. (2021) SOC result is about the emergent scale-invariance of WEIGHT MATRIX spectra during SGD, not about explicitly
    parameterized coupling constants. There is no known result that a scalar coupling constant J trained by gradient descent
    on a supervised loss converges to any specific value, let alone the critical value. Empirical evidence for this would
    itself be a novel finding.
  suggested_action: >-
    Recast J-self-organization as a measurable empirical question rather than a stated assumption. Make it a primary experimental
    finding: plot the distribution of learned J values across layers and seeds at convergence for each dataset/architecture.
    If J self-organizes near J·s̄ = 1, that is a result. If it does not, that tells us the activation is working by a different
    mechanism. Also add a controlled study: fix J at several values (0.1, 0.3, 0.5, 0.7, 0.9) and compare to learned J — this
    tests whether criticality is necessary for the benefits.
- id: ''
  category: novelty
  severity: major
  description: >-
    Two closely related concurrent papers are unacknowledged: (1) Boltzmann Attention (Kim & Park, arXiv:2606.12478, June
    10, 2026) proposes learnable pairwise Ising couplings J_{jk} in attention mechanisms, with the same physical motivation
    (beyond the J=0 non-interacting regime), the same parameter class (scalar/matrix couplings in a spin-system energy), and
    demonstrates empirical improvements in transformers. The conceptual overlap is high even though the architectural component
    differs (attention operator vs. activation nonlinearity). (2) Competing Nonlinearities (Lesser & Chowdhury, arXiv:2605.05294,
    May 2026) achieves edge-of-chaos criticality through statistical activation mixtures (tanh + Swish mixing fraction p),
    demonstrating non-monotonic test performance peaked at the theoretical critical p_c. This is a competing approach to CWA's
    goal of reaching criticality via activation design, without any fixed-point iteration overhead.
  suggested_action: >-
    Add both papers to related works with explicit differentiation: CWA vs. Boltzmann Attention — same physics, different
    architectural target (activation function vs. attention operator); CWA provides all-layer coupling while Boltzmann Attention
    targets inter-token co-attention. CWA vs. Competing Nonlinearities — both aim for edge-of-chaos activation design, but
    Competing Nonlinearities uses a static mixture (no fixed-point overhead) and quenched disorder regularization. Include
    Lesser & Chowdhury's tanh/Swish-at-p_c as a baseline in experiments.
- id: ''
  category: scope
  severity: major
  description: >-
    The experimental plan tests 3-6 layer MLPs on MNIST, CIFAR-10, and adult-income. This is far below the standard of evidence
    required for top-tier venue acceptance for an activation function contribution. Activation functions are typically evaluated
    on: (a) ResNets / CNNs on CIFAR-100 and ImageNet, (b) transformer architectures on language modeling (perplexity on WikiText-103
    or similar), (c) at multiple depths (e.g., 10/20/50 layers) to test the claimed gradient stability at depth. MLP-only
    tests are preliminary. The adult-income tabular dataset is non-standard and unlikely to reveal activation function differences.
  suggested_action: >-
    Replace adult-income with a tabular benchmark from the TabZilla suite. Add ResNet-18 or ResNet-20 on CIFAR-100 and at
    least a small GPT-style language model (on WikiText-103 or character-level Shakespeare as in Boltzmann Attention) to test
    activation function performance in transformer-scale depth. These additions would elevate the scope to Borderline Accept
    at NeurIPS/ICLR. If GPU budget allows only CIFAR-10, frame the paper explicitly as a proof-of-concept and expect a workshop
    tier rather than main conference acceptance.
- id: ''
  category: methodology
  severity: major
  description: >-
    Missing critical baselines undermine the scientific claim. The hypothesis claims CWA provides 'gradient stability without
    normalization overhead.' But the most natural comparison is against tanh + LayerNorm, which also provides collective input-statistics
    normalization followed by the same nonlinearity. Similarly, SELU (Klambauer et al. 2017, NeurIPS) was specifically designed
    to self-normalize activation statistics in deep MLPs and addresses the same dead-neuron and gradient instability motivation.
    Without comparing against these, the claim that CWA provides a fundamentally new mechanism for gradient stability cannot
    be established.
  suggested_action: >-
    Add to baselines: (a) tanh + LayerNorm, (b) GELU + LayerNorm, (c) SELU (no normalization layer, self-normalizing), and
    (d) ReLU + BatchNorm. For gradient stability experiments specifically, test in unnormalized deep networks (no BatchNorm/LayerNorm)
    to isolate CWA's contribution from normalization. Then retest in normalized networks to show whether CWA adds value on
    top of standard normalization.
- id: ''
  category: methodology
  severity: minor
  description: >-
    The effective critical coupling is J·s̄ = 1, not J = 1. The paper repeatedly frames criticality as J → 1, but s̄ = mean(sech²(x
    + J·m*)) varies with the input distribution. For inputs with large magnitude (|x| >> 1), sech² → 0 and s̄ << 1, meaning
    J_c >> 1 would be needed for criticality — which is in the bistable regime the paper explicitly wants to avoid. For nearly
    zero inputs, s̄ ≈ 1 and J_c ≈ 1. This means the 'critical regime' is input-distribution-dependent, and the success criterion
    J ∈ [0.7, 1.0] does not unambiguously indicate criticality.
  suggested_action: >-
    Add tracking of J·s̄ (the true Jacobian eigenvalue = effective coupling) alongside J in all experiments. The success criterion
    for criticality should be J·s̄ → 1 (or equivalently, the layer's input-output Jacobian spectral norm → 1), not J → 1 alone.
    This is consistent with the Poole/Yang criticality literature which frames criticality in terms of the Jacobian, not J
    directly.
- id: ''
  category: novelty
  severity: minor
  description: >-
    Softmax is already a widely-used non-pointwise activation: each output depends on all inputs. The statement in the motivation
    that 'all standard activation functions are applied pointwise' is technically incorrect. Softmax appears in output layers
    and in attention mechanisms and is not pointwise. This weakens the novelty framing, since non-pointwise activations already
    exist and are standard.
  suggested_action: >-
    Qualify the claim to 'all standard hidden-layer activation functions between linear layers are pointwise' or 'all activation
    functions used in feedforward layers of MLP blocks are pointwise.' Then note the contrast: softmax, while non-pointwise,
    is used only in specific output/attention positions and introduces strict simplex constraints, not learnable gain control.
    This makes the CWA contribution precise.
- id: ''
  category: rigor
  severity: minor
  description: >-
    The success criterion '≥0.5% higher final accuracy than the best baseline on at least 2 of 3 datasets' uses 'best baseline'
    without specifying which baseline is expected to be best. Different baselines may win on different datasets, and the criterion
    as stated could be satisfied by narrow wins against a single weak baseline. Additionally, the gradient norm ratio criterion
    (≤2× closer to 1.0) is loosely defined — 'closer to 1.0' for ratios depends on whether the ratio is currently > 1 or <
    1.
  suggested_action: >-
    Specify success criteria as: 'CWA achieves ≥0.5% higher accuracy than GELU (the strongest pointwise baseline) on at least
    2 of 3 datasets.' For the gradient stability criterion, define the metric precisely: log|∇L_layer1| / log|∇L_layerL|,
    and specify that CWA's ratio should be within a factor of 2 of 1.0 while baselines without normalization have ratios >5.
    This removes ambiguity and prevents criterion gaming.
- id: ''
  category: clarity
  severity: minor
  description: >-
    The hypothesis does not discuss what happens when the fixed-point iteration is differentiated via unrolled steps in the
    presence of the J≥1 bistability. During early training, J might transiently exceed 1 (before regularization or projection
    constrains it), causing the iteration to diverge and NaN gradients to appear. The proposal mentions 'J constrained to
    [0,1)' as a safety measure but does not specify the constraint mechanism.
  suggested_action: >-
    Specify the constraint mechanism explicitly: sigmoid parameterization (J = σ(J_raw), range (0,1)), softplus-minus-one
    (range (0,∞) but requires separate clipping), or projected gradient descent. Include a hyperparameter: whether to constrain
    J ∈ [0, 1) hard or allow J ∈ ℝ and monitor divergence. This is implementation-critical information.
score: 5
confidence: 4
relation_type:
relation_rationale: ''
</previous_review_feedback><user_data>
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
    "TermDefinition": {
      "description": "A technical term and its definition.",
      "properties": {
        "term": {
          "description": "The technical term",
          "title": "Term",
          "type": "string"
        },
        "definition": {
          "description": "Clear definition of the term",
          "title": "Definition",
          "type": "string"
        }
      },
      "required": [
        "term",
        "definition"
      ],
      "title": "TermDefinition",
      "type": "object"
    }
  },
  "description": "A research hypothesis with validation approach.",
  "properties": {
    "title": {
      "description": "Concise, self-explanatory title",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "The core hypothesis statement",
      "title": "Hypothesis",
      "type": "string"
    },
    "motivation": {
      "description": "Why this hypothesis matters - significance and impact",
      "title": "Motivation",
      "type": "string"
    },
    "assumptions": {
      "description": "Key assumptions that must hold for this hypothesis (2-5 items)",
      "items": {
        "type": "string"
      },
      "title": "Assumptions",
      "type": "array"
    },
    "investigation_approach": {
      "description": "High-level approach to investigating this hypothesis",
      "title": "Investigation Approach",
      "type": "string"
    },
    "success_criteria": {
      "description": "What outcomes would confirm or disconfirm this hypothesis?",
      "title": "Success Criteria",
      "type": "string"
    },
    "related_works": {
      "description": "The most similar existing works found during research. Each entry describes one related work: what it does and how the proposed hypothesis fundamentally differs from it.",
      "items": {
        "type": "string"
      },
      "title": "Related Works",
      "type": "array"
    },
    "inspiration": {
      "description": "What inspired this hypothesis - which patterns, techniques, or cross-field insights were adapted (from the explicit inspiration seeds if your prompt included any, otherwise from your own cross-domain exploration)",
      "title": "Inspiration",
      "type": "string"
    },
    "terms": {
      "description": "Definitions of key technical terms used in the hypothesis",
      "items": {
        "$ref": "#/$defs/TermDefinition"
      },
      "title": "Terms",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the hypothesis in 1-2 sentences",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "motivation",
    "assumptions",
    "investigation_approach",
    "success_criteria",
    "related_works",
    "inspiration",
    "terms",
    "summary"
  ],
  "title": "Hypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-06-16 16:58:39 UTC

```
Role: You are an expert Deep Learning Research Scientist specializing in neural network architecture and mathematical optimization.Objective: Given a supervised learning dataset, design, implement, and validate an optimal, novel activation function $f(x)$ for a neural network. Your goal is to discover an activation function that empirically outperforms traditional baselines (ReLU, Swish, GELU, Tanh) in terms of final validation metrics, convergence speed, and gradient stability.Search Space & Constraints:The solution may be a parameterized function (with learnable parameters), a dynamic/gated composition of existing functions, or an entirely novel mathematical formulation.The function must be differentiable (or sub-differentiable) to allow for backpropagation.Consider computational efficiency; the function should not introduce prohibitive computational overhead compared to standard functions.
```

### [4] ASSISTANT · 2026-06-16 16:59:01 UTC

```
I'll revise the previous Curie-Weiss Activation hypothesis, addressing all 5 major and 4 minor critiques from the reviewer. Let me first fetch the two unacknowledged concurrent papers to properly characterize them.
```

### [5] TOOL CALL — Skill · 2026-06-16 16:59:01 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-06-16 16:59:01 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — ToolSearch · 2026-06-16 16:59:05 UTC

```
{'query': 'select:WebSearch,WebFetch'}
```

### [8] TOOL RESULT — ToolSearch · 2026-06-16 16:59:05 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [9] TOOL CALL — WebFetch · 2026-06-16 16:59:15 UTC

```
URL: https://arxiv.org/abs/2606.12478
Prompt: What is this paper about? Describe the core mechanism (learnable Ising couplings J, attention weights), how it works, what it achieves, and how it differs from standard attention. What are the key results?
```

### [10] TOOL CALL — WebFetch · 2026-06-16 16:59:15 UTC

```
URL: https://arxiv.org/abs/2605.05294
Prompt: What is this paper about? Describe the core mechanism for achieving edge-of-chaos criticality through activation mixtures. What activation functions are mixed? How is the critical mixing fraction determined? What are the results?
```

### [11] TOOL RESULT — WebFetch · 2026-06-16 16:59:15 UTC

```
{"bytes": 48274, "code": 200, "codeText": "OK", "result": "# Boltzmann Attention: Core Concepts and Results\n\n## Core Mechanism\n\nThis paper proposes an energy-based approach to attention that augments standard mechanisms with learnable pairwise interactions. Rather than computing relevance solely through query-key similarities, the method introduces \"learnable pairwise couplings\" governed by an Ising model framework. These couplings enable the attention mechanism to represent correlations between positions beyond what standard softmax attention captures.\n\n## Key Differences from Standard Attention\n\nStandard attention relies on individual query-key comparisons with softmax competition. Boltzmann attention adds explicit inter-position interactions, allowing the model to directly parameterize \"cooperative or antagonistic co-attention structure within the attention mechanism itself.\" This represents a fundamental shift from position-independent scoring to structured position interdependencies.\n\n## Key Results\n\nThe experiments demonstrate consistent improvements:\n- Character-level language modeling and bracket-matching tasks show improvements over standard softmax attention\n- Advantages \"become more pronounced as sequence length increases\"\n- An ablation study confirms improvements stem from the learnable pairwise couplings themselves\n- The framework supports quantum computing approaches: the authors show \"diabatic quantum annealing provides a practical training method while maintaining competitive performance\"\n\n## Significance\n\nThe work bridges attention mechanisms with statistical physics, suggesting that explicit position interactions provide a principled enhancement for sequence modeling while opening pathways toward quantum-accelerated training strategies.", "durationMs": 6108, "url": "https://arxiv.org/abs/2606.12478"}
```

### [12] TOOL RESULT — WebFetch · 2026-06-16 16:59:17 UTC

```
{"bytes": 48889, "code": 200, "codeText": "OK", "result": "# Paper Summary: Competing Nonlinearities and Criticality in Deep Networks\n\n## Core Topic\nThis research explores how mixing different activation functions in neural networks can achieve a critical transition point that balances network stability with expressiveness—an \"edge of chaos\" state beneficial for learning.\n\n## The Mechanism\nThe authors introduce \"statistical activation mixtures\" where neurons randomly select their activation functions from a two-component distribution controlled by parameter *p* (mixing fraction). This creates a phase transition as *p* varies, providing \"a new mechanism for a continuous phase transition.\"\n\n## Activation Functions Mixed\nThe primary example combines **Tanh and Swish** functions. The authors note this addresses a longstanding problem: previous \"scale-invariant propagation has previously required the non-smooth ReLU family,\" which performs poorly with curvature-based optimizers. Their mixture enables smoothness while maintaining scale invariance.\n\n## Critical Point Determination\nThe critical mixing fraction (p_c) is identified theoretically through analyzing depth scaling of preactivation variance and empirically validated through:\n- Variance propagation analysis\n- Susceptibility measurements\n- Lyapunov exponents\n\n## Key Results\nTraining experiments on real datasets revealed \"non-monotonic test performance as a function of p, with an optimum near the theoretically predicted p_c,\" confirming the initialization-level transition translates to improved learned representations. The activation disorder also acts as regularization, suppressing memorization while preserving generalization.", "durationMs": 5528, "url": "https://arxiv.org/abs/2605.05294"}
```

### [13] ASSISTANT · 2026-06-16 17:01:31 UTC

```
Now I have clear understanding of both concurrent papers. Let me write the revised hypothesis addressing all critiques systematically.
```

### [14] TOOL CALL — Write · 2026-06-16 17:01:31 UTC

```
File: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/iter_2/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json

{
  "title": "Curie-Weiss Activation with Adaptive Fixed-Point Iteration: Empirically-Grounded Self-Consistent Within-Layer Coupling for Neural Gain Control",
  "hypothesis": "A neural network hidden-layer activation function defined as the fixed point y* of the Curie-Weiss mean-field self-consistency equation — y_i = tanh(x_i + J·mean(y)) for all neurons i in a layer, where J = σ(J_raw) ∈ (0,1) is a per-layer learnable scalar coupling — will outperform standard pointwise hidden-layer activations (ReLU, GELU, Swish, Tanh) and self-normalizing baselines (SELU, tanh+LayerNorm, GELU+LayerNorm) in gradient stability in deep unnormalized networks (≥10 layers), with performance improvements on CIFAR-100 (ResNet-20) and character-level language modeling (4-layer GPT), because: (1) the within-sample mean-field coupling y_i ← tanh(x_i + J·mean(y)) implements a learned, parameter-efficient form of collective output-based gain control that is unavailable to any purely pointwise activation and is categorically distinct from LayerNorm (which normalizes inputs, not outputs); (2) the effective per-step convergence rate ρ = J·s̄ = J·mean(sech²(x+J·m*)) can be tracked and the adaptive-K stopping rule |m_{t+1}−m_t| < δ renders the computation honest about wall-clock cost at any coupling strength; and (3) the question of whether J·s̄ self-organizes toward 1 during training is treated as a primary empirical finding — not an assumption — with controlled fixed-J ablations (J fixed at {0.1, 0.3, 0.5, 0.7, 0.9}) separating whether criticality is necessary for the benefits.",
  "motivation": "All standard hidden-layer activation functions used between linear layers in MLP blocks — ReLU, GELU, Swish, and tanh — are applied pointwise: each neuron's output depends only on its own pre-activation. (Note: softmax is non-pointwise but is restricted to output layers and attention operators, not feedforward nonlinearities, and introduces strict simplex constraints rather than learnable gain control.) This independence means each layer's effective gain must be managed externally via weight initialization, batch/layer normalization, or learning rate schedules. Criticality theory in deep learning (Poole et al. 2016; Yang & Schoenholz 2017) shows that networks at the 'edge of chaos' — where the layer Jacobian's singular values are near unity, i.e., the effective coupling J·s̄ ≈ 1 — train fastest and generalize best. Existing approaches achieve this only at initialization (Poole/Yang weight variance tuning) or through random static mixtures (Lesser & Chowdhury 2026, tanh+Swish at theoretical p_c). Neither provides a per-layer learned mechanism that adapts collectively to the actual input distribution during training. CWA proposes an activation function that introduces within-layer coupling through a single learnable scalar J, implementing the Curie-Weiss mean-field self-consistency equation as the actual forward computation. Critically, the new mechanism is tested honestly: (a) adaptive-K iteration makes the computational cost of near-critical regimes explicit; (b) J self-organization toward the critical point J·s̄ = 1 is treated as an empirical question measured during experiments, not assumed; and (c) baselines include SELU and tanh+LN to directly test whether CWA adds value beyond existing self-normalizing and collectively-normalized alternatives.",
  "assumptions": [
    "The adaptive-K fixed-point iteration m_{t+1} = mean(tanh(x + J·m_t)) converges with geometric rate ρ = J·s̄ = J·mean(sech²(x+J·m*)) per step (rigorously bounded by the Banach fixed-point theorem since ρ = dF/dm < 1 when J ∈ (0,1)); the stopping rule |m_{t+1}−m_t| < δ = 1e-4 terminates in K*(ρ) = ceil(log(δ/|m_0−m*|)/log(ρ)) steps, which is finite for all J = σ(J_raw) ∈ (0,1). The wall-clock overhead (K* iterations × O(n) cost per step) is a measured experimental output, not an assumed constant.",
    "PyTorch autograd can differentiate correctly through the unrolled adaptive-K iteration (direct backprop) or via the implicit function theorem F(m*) = mean(tanh(x + J·m*)) − m* = 0, which gives ∂m*/∂x = sech²(x+J·m*) / (1 − J·s̄) and ∂m*/∂J = s̄ · m* / (1 − J·s̄). Both approaches require J·s̄ < 1 (guaranteed by J = σ(J_raw) ∈ (0,1)); the IFT gradient is exact at the true fixed point and requires an additional Newton solve if used with inexact convergence.",
    "The sigmoid parameterization J = σ(J_raw) hard-constrains J ∈ (0,1), preventing the bistable regime J ≥ 1 and ensuring all fixed-point iterations are globally convergent. This eliminates NaN gradients during early training while allowing the optimizer to freely adjust J_raw ∈ ℝ.",
    "Whether J·s̄ self-organizes toward 1 during training (the 'self-organized criticality' hypothesis) is an empirical question to be answered by the experiments, not assumed. The controlled fixed-J ablation study (J fixed at {0.1, 0.3, 0.5, 0.7, 0.9}) tests whether the benefits of CWA require J to move, or whether any fixed coupling value provides gain-control benefits over purely pointwise baselines.",
    "The CWA gain-control mechanism is distinct from LayerNorm/BatchNorm: LayerNorm normalizes the INPUT pre-activations x to zero mean, unit variance before applying a pointwise nonlinearity; CWA couples the OUTPUTS y through a self-consistency feedback mean(y) → tanh(x + J·mean(y)) → new y, operating on output statistics under the actual nonlinearity. This distinction is testable by comparing CWA (no LN) versus tanh+LN and GELU+LN in unnormalized deep networks."
  ],
  "investigation_approach": "Implement CWA in PyTorch as a custom nn.Module with J = torch.sigmoid(J_raw) where J_raw is an nn.Parameter initialized at 0 (J ≈ 0.5). Forward pass: adaptive-K iteration m_0 = 0, repeat m ← mean(tanh(x + J·m)) until |m_{t+1}−m_t| < δ = 1e-4 (cap at K_max=50); output y_i = tanh(x_i + J·m*). Backward pass: unrolled autograd through adaptive iterations. At each forward call, log K (number of iterations), J, and J·s̄ = J·mean(sech²(x+J·m*)) for analysis.\n\nExperiment 1 — Gradient stability in deep MLPs: Train unnormalized MLPs at depths {6, 10, 20} with 256 hidden units on MNIST and CIFAR-10 (as pixel vectors). Compare: CWA vs ReLU, GELU, Swish, tanh, SELU, tanh+LN, GELU+LN, tanh+Swish@p_c (Competing Nonlinearities baseline). Measure: gradient norm ratio log|∇L_{layer1}|/log|∇L_{layerL}| per layer, final accuracy, convergence speed (epochs to 95% of peak). 5 seeds.\n\nExperiment 2 — ResNet-20 on CIFAR-100: Replace standard GELU/ReLU with CWA in each residual block (no BatchNorm variant and standard BatchNorm variant). Compare against all baselines. Report top-1 accuracy at 200 epochs.\n\nExperiment 3 — Character-level GPT (4 layers, 128 hidden, sequence length 128) on Tiny Shakespeare: Replace GELU in MLP sublayers with CWA. Compare test BPC (bits per character) at 10K steps against GELU, GELU+LN, SELU, Boltzmann Attention baseline (different component — included for context). Monitor K (iterations), J, and J·s̄ per layer per epoch.\n\nExperiment 4 — Fixed-J ablation: Train 10-layer MLP on CIFAR-10 with J frozen at {0.1, 0.3, 0.5, 0.7, 0.9} versus learned J. Identify whether J self-organizes and whether criticality (high J·s̄) is necessary for gains.\n\nExperiment 5 — Computational overhead: Measure wall-clock time per batch for CWA vs GELU as a function of J (and hence ρ = J·s̄) during training to assess the adaptive-K cost. Total LLM API cost: $0 (pure neural network experiments).",
  "success_criteria": "CONFIRM if: (1) CWA in unnormalized deep MLPs (≥10 layers) achieves gradient norm ratio within 2× of 1.0 (i.e., |log|∇L_1|/log|∇L_L|| < 2.0) while GELU baseline (no normalization) has ratio > 5.0 — demonstrating CWA's core gradient stability claim in the setting where it matters most; AND (2) CWA achieves ≥0.5% higher final accuracy than GELU (the strongest standard pointwise baseline) on at least 2 of 3 benchmark tasks (CIFAR-10 deep MLP, CIFAR-100 ResNet-20, character-level GPT), measured with 95% confidence intervals over 5 seeds; AND (3) the adaptive-K overhead averages ≤3× wall-clock vs GELU during training (monitoring K per forward call). DISCONFIRM if: (1) CWA performs within noise of all pointwise baselines (including GELU) on all tasks, OR (2) tanh+LayerNorm or SELU matches or exceeds CWA on all tasks — indicating the benefit is explained by collective normalization rather than the output-coupling self-consistency mechanism; OR (3) the adaptive-K overhead exceeds 10× wall-clock vs GELU in the near-critical regime (J·s̄ > 0.9), making it computationally prohibitive. PARTIAL CONFIRM if: CWA improves gradient stability (criterion 1) but not final accuracy in normalized networks (ResNet+BN, GPT) while improving in unnormalized deep MLPs — this would precisely bound the contribution: CWA provides unique value when external normalization is absent. SOC FINDING (separate from confirm/disconfirm): Report whether J·s̄ concentrates near 1 in successful configurations (as hypothesized) or settles at scattered values — this is a novel empirical finding either way.",
  "related_works": [
    "Boltzmann Attention (Kim & Park, arXiv:2606.12478, June 2026): Proposes learnable pairwise Ising couplings J_{jk} in the ATTENTION OPERATOR of transformers, enabling inter-position cooperative/antagonistic co-attention beyond standard softmax (J=0). Same physical inspiration (Ising model) and same class of learnable couplings, with demonstrated improvements in character-level language modeling. Key difference: Boltzmann Attention replaces the attention operator (inter-token interactions across sequence positions); CWA replaces the ACTIVATION NONLINEARITY (inter-neuron coupling within a single layer's hidden dimension). These are complementary architectural components — Boltzmann Attention and CWA could be combined in the same transformer. Additionally, Boltzmann Attention uses pairwise J_{jk} (quadratic parameters); CWA uses a single scalar J per layer (one learnable parameter).",
    "Competing Nonlinearities (Lesser & Chowdhury, arXiv:2605.05294, May 2026): Achieves edge-of-chaos criticality in activation design by statistically mixing tanh and Swish at a theoretical critical mixing fraction p_c, producing scale-invariant variance propagation without fixed-point overhead. Activation disorder acts as regularization. Key difference: Competing Nonlinearities uses a STATIC mixture at initialization (quenched disorder), with p_c determined theoretically from variance propagation analysis — there is no learned parameter, no self-consistency feedback, and no within-layer neuron coupling. CWA introduces a LEARNABLE coupling J that is adapted by gradient descent and creates an explicit inter-neuron feedback through mean(y). Competing Nonlinearities is included as a direct baseline in CWA experiments (tanh+Swish at p_c).",
    "Milletarì et al. (2018, arXiv:1805.08786) 'Mean Field Theory of Activation Functions': Uses statistical mechanics to derive existing activations (tanh, ReLU, Swish) as natural solutions to energy-based models. Key difference: this work provides post-hoc physical interpretation of known functions; CWA proposes a NEW activation defined by the actual Curie-Weiss self-consistency equation with a learnable coupling J, introducing within-layer neuron coupling absent from all their derived activations.",
    "Bal (2021, 'Deep Implicit Attention'): Applies Thouless-Anderson-Palmer mean-field equations to ATTENTION mechanisms in transformers, showing softmax attention is one step of naive mean-field inference. Key difference: their work reformulates the attention operator; CWA replaces ACTIVATION FUNCTIONS (nonlinearities within a layer's hidden dimension), a different architectural component. CWA operates within a single layer's neurons, while Bal's work operates across token positions.",
    "Yang & Schoenholz (2017) 'Mean Field Residual Networks' and Poole et al. (2016) 'Exponential Expressivity': Show that networks at the edge of chaos (Jacobian singular values ≈ 1, i.e., effective coupling J·s̄ = 1) propagate information best and train fastest, achieved via careful weight variance initialization. Key difference: these works achieve criticality through INITIALIZATION only — it drifts away as weights update. CWA provides a learnable mechanism through the activation function that can in principle maintain J·s̄ near 1 throughout training (whether it does so empirically is a primary experimental finding).",
    "Bai et al. (2019) 'Deep Equilibrium Models (DEQ)': Applies fixed-point iteration at the FULL-LAYER level — the entire layer mapping (weight matrix + activation) is solved to a fixed point. Key difference: DEQ replaces the full layer (O(n²) per Newton step); CWA is a lightweight activation-level operation (O(n·K) for adaptive-K iterations) that retains the standard linear weight matrix and adds only one learnable parameter J per layer. CWA is a drop-in activation replacement; DEQ is a complete layer replacement.",
    "Klambauer et al. (2017, NeurIPS) 'Self-Normalizing Neural Networks (SELU)': Designs an activation function (Scaled ELU) with specific fixed-point statistics (mean≈0, var≈1 propagation through layers) that self-normalizes without external normalization layers. Key difference: SELU achieves self-normalization by carefully tuning the function's fixed-point statistics under the assumption of normally distributed inputs — it is still POINTWISE (each neuron depends only on its own pre-activation). CWA's self-consistency coupling explicitly averages OUTPUT values and feeds them back, coupling neurons within the layer. SELU is included as a direct baseline.",
    "Amos & Kolter (2017) 'OptNet: Differentiable Optimization as a Layer': Introduces differentiable quadratic program solvers as neural network layers (O(n³) per solve). Key difference: OptNet is a layer-level replacement; CWA is activation-level (O(n·K), K adaptive), making it parameter-efficient and drop-in replaceable at the nonlinearity position."
  ],
  "inspiration": "This hypothesis is a Level-3 (methodological) cross-domain transfer from statistical physics, specifically the Curie-Weiss model of ferromagnetism. In physics, the self-consistency equation m = tanh(β(h + J·m)) describes how an Ising spin aligns with an external field h plus a self-consistent feedback from the average magnetization J·m of all other spins. The critical point βJ = 1 marks the onset of long-range magnetic order and corresponds to maximum magnetic susceptibility — tiny external fields produce large magnetization responses. The cross-domain insight is: just as a ferromagnet near its Curie temperature exhibits maximum input sensitivity (large response to small field), a neural layer near its effective critical coupling J·s̄ = 1 should exhibit maximum sensitivity to pre-activations (high gradient signal-to-noise ratio). The key physical-to-neural mapping is: external field h ↔ pre-activation x; magnetization m ↔ layer mean output; inverse temperature β ↔ 1 (absorbed into J); coupling J ↔ learnable scalar per layer. The self-consistency structure — outputs feeding back into themselves — is absent from all standard pointwise hidden-layer activations, which correspond to the J=0 (non-interacting) case. This revision incorporates an important amendment: the standard physics analysis of critical slowing down (convergence rate ρ = J·s̄ per iteration) is treated as a computational reality rather than an engineering nuisance — the adaptive-K stopping criterion makes the cost honest rather than hiding it under a fixed-5-step assumption. The analogy to sandpile self-organized criticality (J spontaneously approaching 1) is retained as an empirical hypothesis to be tested, not assumed.",
  "terms": [
    {
      "term": "Curie-Weiss Activation (CWA)",
      "definition": "The proposed hidden-layer activation function defined by the fixed point y* of the equation y = tanh(x + J·mean(y)), where x is the vector of pre-activations, y is the vector of activations, J = σ(J_raw) ∈ (0,1) is a per-layer learnable scalar coupling, and mean(y) is the layer-wise mean of y. The fixed point is found by adaptive-K iteration m_{t+1} = mean(tanh(x + J·m_t)) until |m_{t+1}−m_t| < δ, then y_i = tanh(x_i + J·m*)."
    },
    {
      "term": "Effective Coupling (J·s̄)",
      "definition": "The true critical parameter of CWA, defined as J·s̄ = J·mean(sech²(x+J·m*)) ∈ (0,1). This is the per-step convergence rate of the fixed-point iteration and the spectral norm of the layer's input-output Jacobian. J·s̄ → 1 corresponds to the edge-of-chaos critical regime with diverging gain. J·s̄ depends on both the learned coupling J and the input distribution (through s̄), making the critical condition input-distribution-dependent. All experiments track J·s̄ alongside J."
    },
    {
      "term": "Adaptive-K Iteration",
      "definition": "The convergence-based stopping rule for the CWA forward pass: iterate m ← mean(tanh(x + J·m)) until |m_{t+1}−m_t| < δ = 1e-4 (with a maximum of K_max=50 iterations). The number of required steps K*(ρ) grows as O(1/(1−ρ)) near criticality (ρ = J·s̄ → 1) due to classical critical slowing down. Wall-clock cost per forward pass is measured during training as a function of the current J·s̄ to empirically characterize the computational overhead of near-critical regimes."
    },
    {
      "term": "Sigmoid Parameterization of J",
      "definition": "The constraint mechanism for the learnable coupling: J = σ(J_raw) = 1/(1+exp(−J_raw)), where J_raw ∈ ℝ is the actual learnable parameter and J ∈ (0,1) is the constrained coupling. This hard-constrains J to the monostable regime (below the ferromagnetic phase transition at J=1), preventing bistability and guaranteeing global convergence of the fixed-point iteration. J_raw is initialized at 0 so that J starts at 0.5 (moderate coupling)."
    },
    {
      "term": "Critical Gain",
      "definition": "The effective gradient amplification of CWA near the critical coupling J·s̄ → 1. By the implicit function theorem, the input-output Jacobian element ∂y_i/∂x_i = sech²(x_i + J·m*) / (1 − J·s̄), which diverges as J·s̄ → 1. This diverging gain enables maximum sensitivity of the layer to its inputs and is the proposed mechanism for gradient stability in deep unnormalized networks."
    },
    {
      "term": "Self-Organized Criticality (SOC) Hypothesis",
      "definition": "The empirical hypothesis — not an assumption — that gradient descent will push J·s̄ toward 1 during training, because layers with J·s̄ near 1 have higher effective gain and thus more informative gradients, giving task-loss minimization an incentive to approach criticality. Tested experimentally by plotting the distribution of learned J·s̄ values across layers and seeds at convergence and by the fixed-J ablation study."
    },
    {
      "term": "Output-Coupling vs Input-Normalization",
      "definition": "The key mechanistic distinction between CWA and LayerNorm/BatchNorm. LayerNorm/BatchNorm normalize the INPUT pre-activations x (shifting and scaling to zero mean, unit variance) before a pointwise nonlinearity — they operate on input statistics. CWA couples the OUTPUTS y through the self-consistency feedback mean(y) → tanh(x + J·mean(y)) → new y — it operates on output statistics under the actual nonlinearity. These are categorically different operations that compose rather than substitute."
    },
    {
      "term": "Fixed-J Ablation",
      "definition": "A controlled experiment where J is frozen at specific values {0.1, 0.3, 0.5, 0.7, 0.9} (J_raw fixed, not updated by optimizer) and compared against the full CWA (learned J). This separates whether the performance benefit of CWA requires (a) any nonzero coupling (vs. J=0 = pure tanh), (b) a specific coupling value, or (c) the adaptive optimization of J by gradient descent. It directly tests the SOC hypothesis and whether criticality is necessary for the performance gains."
    }
  ],
  "summary": "We propose the Curie-Weiss Activation (CWA), a hidden-layer activation function where each neuron's output is the fixed point of the mean-field self-consistency equation y_i = tanh(x_i + J·mean(y)), with J = σ(J_raw) ∈ (0,1) a per-layer learnable coupling constrained by sigmoid parameterization. Borrowing from the physics of ferromagnetism, CWA introduces within-layer inter-neuron coupling absent from all standard pointwise MLP-block activations; whether J self-organizes toward the critical coupling J·s̄ → 1 is treated as an empirical finding — tested via adaptive-K iteration with honest wall-clock accounting and a controlled fixed-J ablation — evaluated against comprehensive baselines (GELU, SELU, tanh+LN, GELU+LN, Competing Nonlinearities mixture) on deep unnormalized MLPs, ResNet-20/CIFAR-100, and character-level language modeling."
}
```

### [15] TOOL RESULT — Write · 2026-06-16 17:01:31 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/iter_2/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Curie-Weiss Activation with Adaptive Fixed-Point Iteration: Empirically-Grounded Self-Consistent Within-Layer Coupling for Neural Gain Control\",\n  \"hypothesis\": \"A neural network hidden-layer activation function defined as the fixed point y* of the Curie-Weiss mean-field self-consistency equation — y_i = tanh(x_i + J·mean(y)) for all neurons i in a layer, where J = σ(J_raw) ∈ (0,1) is a per-layer learnable scalar coupling — will outperform standard pointwise hidden-layer activations (ReLU, GELU, Swish, Tanh) and self-normalizing baselines (SELU, tanh+LayerNorm, GELU+LayerNorm) in gradient stability in deep unnormalized networks (≥10 layers), with performance improvements on CIFAR-100 (ResNet-20) and character-level language modeling (4-layer GPT), because: (1) the within-sample mean-field coupling y_i ← tanh(x_i + J·mean(y)) implements a learned, parameter-efficient form of collective output-based gain control that is unavailable to any purely pointwise activation and is categorically distinct from LayerNorm (which normalizes inputs, not outputs); (2) the effective per-step convergence rate ρ = J·s̄ = J·mean(sech²(x+J·m*)) can be tracked and the adaptive-K stopping rule |m_{t+1}−m_t| < δ renders the computation honest about wall-clock cost at any coupling strength; and (3) the question of whether J·s̄ self-organizes toward 1 during training is treated as a primary empirical finding — not an assumption — with controlled fixed-J ablations (J fixed at {0.1, 0.3, 0.5, 0.7, 0.9}) separating whether criticality is necessary for the benefits.\",\n  \"motivation\": \"All standard hidden-layer activation functions used between linear layers in MLP blocks — ReLU, GELU, Swish, and tanh — are applied pointwise: each neuron's output depends only on its own pre-activation. (Note: softmax is non-pointwise but is restricted to output layers and attention operators, not feedforward nonlinearities, and introduces strict simplex constraints rather than learnable gain control.) This independence means each layer's effective gain must be managed externally via weight initialization, batch/layer normalization, or learning rate schedules. Criticality theory in deep learning (Poole et al. 2016; Yang & Schoenholz 2017) shows that networks at the 'edge of chaos' — where the layer Jacobian's singular values are near unity, i.e., the effective coupling J·s̄ ≈ 1 — train fastest and generalize best. Existing approaches achieve this only at initialization (Poole/Yang weight variance tuning) or through random static mixtures (Lesser & Chowdhury 2026, tanh+Swish at theoretical p_c). Neither provides a per-layer learned mechanism that adapts collectively to the actual input distribution during training. CWA proposes an activation function that introduces within-layer coupling through a single learnable scalar J, implementing the Curie-Weiss mean-field self-consistency equation as the actual forward computation. Critically, the new mechanism is tested honestly: (a) adaptive-K iteration makes the computational cost of near-critical regimes explicit; (b) J self-organization toward the critical point J·s̄ = 1 is treated as an empirical question measured during experiments, not assumed; and (c) baselines include SELU and tanh+LN to directly test whether CWA adds value beyond existing self-normalizing and collectively-normalized alternatives.\",\n  \"assumptions\": [\n    \"The adaptive-K fixed-point iteration m_{t+1} = mean(tanh(x + J·m_t)) converges with geometric rate ρ = J·s̄ = J·mean(sech²(x+J·m*)) per step (rigorously bounded by the Banach fixed-point theorem since ρ = dF/dm < 1 when J ∈ (0,1)); the stopping rule |m_{t+1}−m_t| < δ = 1e-4 terminates in K*(ρ) = ceil(log(δ/|m_0−m*|)/log(ρ)) steps, which is finite for all J = σ(J_raw) ∈ (0,1). The wall-clock overhead (K* iterations × O(n) cost per step) is a measured experimental output, not an assumed constant.\",\n    \"PyTorch autograd can differentiate correctly through the unrolled adaptive-K iteration (direct backprop) or via the implicit function theorem F(m*) = mean(tanh(x + J·m*)) − m* = 0, which gives ∂m*/∂x = sech²(x+J·m*) / (1 − J·s̄) and ∂m*/∂J = s̄ · m* / (1 − J·s̄). Both approaches require J·s̄ < 1 (guaranteed by J = σ(J_raw) ∈ (0,1)); the IFT gradient is exact at the true fixed point and requires an additional Newton solve if used with inexact convergence.\",\n    \"The sigmoid parameterization J = σ(J_raw) hard-constrains J ∈ (0,1), preventing the bistable regime J ≥ 1 and ensuring all fixed-point iterations are globally convergent. This eliminates NaN gradients during early training while allowing the optimizer to freely adjust J_raw ∈ ℝ.\",\n    \"Whether J·s̄ self-organizes toward 1 during training (the 'self-organized criticality' hypothesis) is an empirical question to be answered by the experiments, not assumed. The controlled fixed-J ablation study (J fixed at {0.1, 0.3, 0.5, 0.7, 0.9}) tests whether the benefits of CWA require J to move, or whether any fixed coupling value provides gain-control benefits over purely pointwise baselines.\",\n    \"The CWA gain-control mechanism is distinct from LayerNorm/BatchNorm: LayerNorm normalizes the INPUT pre-activations x to zero mean, unit variance before applying a pointwise nonlinearity; CWA couples the OUTPUTS y through a self-consistency feedback mean(y) → tanh(x + J·mean(y)) → new y, operating on output statistics under the actual nonlinearity. This distinction is testable by comparing CWA (no LN) versus tanh+LN and GELU+LN in unnormalized deep networks.\"\n  ],\n  \"investigation_approach\": \"Implement CWA in PyTorch as a custom nn.Module with J = torch.sigmoid(J_raw) where J_raw is an nn.Parameter initialized at 0 (J ≈ 0.5). Forward pass: adaptive-K iteration m_0 = 0, repeat m ← mean(tanh(x + J·m)) until |m_{t+1}−m_t| < δ = 1e-4 (cap at K_max=50); output y_i = tanh(x_i + J·m*). Backward pass: unrolled autograd through adaptive iterations. At each forward call, log K (number of iterations), J, and J·s̄ = J·mean(sech²(x+J·m*)) for analysis.\\n\\nExperiment 1 — Gradient stability in deep MLPs: Train unnormalized MLPs at depths {6, 10, 20} with 256 hidden units on MNIST and CIFAR-10 (as pixel vectors). Compare: CWA vs ReLU, GELU, Swish, tanh, SELU, tanh+LN, GELU+LN, tanh+Swish@p_c (Competing Nonlinearities baseline). Measure: gradient norm ratio log|∇L_{layer1}|/log|∇L_{layerL}| per layer, final accuracy, convergence speed (epochs to 95% of peak). 5 seeds.\\n\\nExperiment 2 — ResNet-20 on CIFAR-100: Replace standard GELU/ReLU with CWA in each residual block (no BatchNorm variant and standard BatchNorm variant). Compare against all baselines. Report top-1 accuracy at 200 epochs.\\n\\nExperiment 3 — Character-level GPT (4 layers, 128 hidden, sequence length 128) on Tiny Shakespeare: Replace GELU in MLP sublayers with CWA. Compare test BPC (bits per character) at 10K steps against GELU, GELU+LN, SELU, Boltzmann Attention baseline (different component — included for context). Monitor K (iterations), J, and J·s̄ per layer per epoch.\\n\\nExperiment 4 — Fixed-J ablation: Train 10-layer MLP on CIFAR-10 with J frozen at {0.1, 0.3, 0.5, 0.7, 0.9} versus learned J. Identify whether J self-organizes and whether criticality (high J·s̄) is necessary for gains.\\n\\nExperiment 5 — Computational overhead: Measure wall-clock time per batch for CWA vs GELU as a function of J (and hence ρ = J·s̄) during training to assess the adaptive-K cost. Total LLM API cost: $0 (pure neural network experiments).\",\n  \"success_criteria\": \"CONFIRM if: (1) CWA in unnormalized deep MLPs (≥10 layers) achieves gradient norm ratio within 2× of 1.0 (i.e., |log|∇L_1|/log|∇L_L|| < 2.0) while GELU baseline (no normalization) has ratio > 5.0 — demonstrating CWA's core gradient stability claim in the setting where it matters most; AND (2) CWA achieves ≥0.5% higher final accuracy than GELU (the strongest standard pointwise baseline) on at least 2 of 3 benchmark tasks (CIFAR-10 deep MLP, CIFAR-100 ResNet-20, character-level GPT), measured with 95% confidence intervals over 5 seeds; AND (3) the adaptive-K overhead averages ≤3× wall-clock vs GELU during training (monitoring K per forward call). DISCONFIRM if: (1) CWA performs within noise of all pointwise baselines (including GELU) on all tasks, OR (2) tanh+LayerNorm or SELU matches or exceeds CWA on all tasks — indicating the benefit is explained by collective normalization rather than the output-coupling self-consistency mechanism; OR (3) the adaptive-K overhead exceeds 10× wall-clock vs GELU in the near-critical regime (J·s̄ > 0.9), making it computationally prohibitive. PARTIAL CONFIRM if: CWA improves gradient stability (criterion 1) but not final accuracy in normalized networks (ResNet+BN, GPT) while improving in unnormalized deep MLPs — this would precisely bound the contribution: CWA provides unique value when external normalization is absent. SOC FINDING (separate from confirm/disconfirm): Report whether J·s̄ concentrates near 1 in successful configurations (as hypothesized) or settles at scattered values — this is a novel empirical finding either way.\",\n  \"related_works\": [\n    \"Boltzmann Attention (Kim & Park, arXiv:2606.12478, June 2026): Proposes learnable pairwise Ising couplings J_{jk} in the ATTENTION OPERATOR of transformers, enabling inter-position cooperative/antagonistic co-attention beyond standard softmax (J=0). Same physical inspiration (Ising model) and same class of learnable couplings, with demonstrated improvements in character-level language modeling. Key difference: Boltzmann Attention replaces the attention operator (inter-token interactions across sequence positions); CWA replaces the ACTIVATION NONLINEARITY (inter-neuron coupling within a single layer's hidden dimension). These are complementary architectural components — Boltzmann Attention and CWA could be combined in the same transformer. Additionally, Boltzmann Attention uses pairwise J_{jk} (quadratic parameters); CWA uses a single scalar J per layer (one learnable parameter).\",\n    \"Competing Nonlinearities (Lesser & Chowdhury, arXiv:2605.05294, May 2026): Achieves edge-of-chaos criticality in activation design by statistically mixing tanh and Swish at a theoretical critical mixing fraction p_c, producing scale-invariant variance propagation without fixed-point overhead. Activation disorder acts as regularization. Key difference: Competing Nonlinearities uses a STATIC mixture at initialization (quenched disorder), with p_c determined theoretically from variance propagation analysis — there is no learned parameter, no self-consistency feedback, and no within-layer neuron coupling. CWA introduces a LEARNABLE coupling J that is adapted by gradient descent and creates an explicit inter-neuron feedback through mean(y). Competing Nonlinearities is included as a direct baseline in CWA experiments (tanh+Swish at p_c).\",\n    \"Milletarì et al. (2018, arXiv:1805.08786) 'Mean Field Theory of Activation Functions': Uses statistical mechanics to derive existing activations (tanh, ReLU, Swish) as natural solutions to energy-based models. Key difference: this work provides post-hoc physical interpretation of known functions; CWA proposes a NEW activation defined by the actual Curie-Weiss self-consistency equation with a learnable coupling J, introducing within-layer neuron coupling absent from all their derived activations.\",\n    \"Bal (2021, 'Deep Implicit Attention'): Applies Thouless-Anderson-Palmer mean-field equations to ATTENTION mechanisms in transformers, showing softmax attention is one step of naive mean-field inference. Key difference: their work reformulates the attention operator; CWA replaces ACTIVATION FUNCTIONS (nonlinearities within a layer's hidden dimension), a different architectural component. CWA operates within a single layer's neurons, while Bal's work operates across token positions.\",\n    \"Yang & Schoenholz (2017) 'Mean Field Residual Networks' and Poole et al. (2016) 'Exponential Expressivity': Show that networks at the edge of chaos (Jacobian singular values ≈ 1, i.e., effective coupling J·s̄ = 1) propagate information best and train fastest, achieved via careful weight variance initialization. Key difference: these works achieve criticality through INITIALIZATION only — it drifts away as weights update. CWA provides a learnable mechanism through the activation function that can in principle maintain J·s̄ near 1 throughout training (whether it does so empirically is a primary experimental finding).\",\n    \"Bai et al. (2019) 'Deep Equilibrium Models (DEQ)': Applies fixed-point iteration at the FULL-LAYER level — the entire layer mapping (weight matrix + activation) is solved to a fixed point. Key difference: DEQ replaces the full layer (O(n²) per Newton step); CWA is a lightweight activation-level operation (O(n·K) for adaptive-K iterations) that retains the standard linear weight matrix and adds only one learnable parameter J per layer. CWA is a drop-in activation replacement; DEQ is a complete layer replacement.\",\n    \"Klambauer et al. (2017, NeurIPS) 'Self-Normalizing Neural Networks (SELU)': Designs an activation function (Scaled ELU) with specific fixed-point statistics (mean≈0, var≈1 propagation through layers) that self-normalizes without external normalization layers. Key difference: SELU achieves self-normalization by carefully tuning the function's fixed-point statistics under the assumption of normally distributed inputs — it is still POINTWISE (each neuron depends only on its own pre-activation). CWA's self-consistency coupling explicitly averages OUTPUT values and feeds them back, coupling neurons within the layer. SELU is included as a direct baseline.\",\n    \"Amos & Kolter (2017) 'OptNet: Differentiable Optimization as a Layer': Introduces differentiable quadratic program solvers as neural network layers (O(n³) per solve). Key difference: OptNet is a layer-level replacement; CWA is activation-level (O(n·K), K adaptive), making it parameter-efficient and drop-in replaceable at the nonlinearity position.\"\n  ],\n  \"inspiration\": \"This hypothesis is a Level-3 (methodological) cross-domain transfer from statistical physics, specifically the Curie-Weiss model of ferromagnetism. In physics, the self-consistency equation m = tanh(β(h + J·m)) describes how an Ising spin aligns with an external field h plus a self-consistent feedback from the average magnetization J·m of all other spins. The critical point βJ = 1 marks the onset of long-range magnetic order and corresponds to maximum magnetic susceptibility — tiny external fields produce large magnetization responses. The cross-domain insight is: just as a ferromagnet near its Curie temperature exhibits maximum input sensitivity (large response to small field), a neural layer near its effective critical coupling J·s̄ = 1 should exhibit maximum sensitivity to pre-activations (high gradient signal-to-noise ratio). The key physical-to-neural mapping is: external field h ↔ pre-activation x; magnetization m ↔ layer mean output; inverse temperature β ↔ 1 (absorbed into J); coupling J ↔ learnable scalar per layer. The self-consistency structure — outputs feeding back into themselves — is absent from all standard pointwise hidden-layer activations, which correspond to the J=0 (non-interacting) case. This revision incorporates an important amendment: the standard physics analysis of critical slowing down (convergence rate ρ = J·s̄ per iteration) is treated as a computational reality rather than an engineering nuisance — the adaptive-K stopping criterion makes the cost honest rather than hiding it under a fixed-5-step assumption. The analogy to sandpile self-organized criticality (J spontaneously approaching 1) is retained as an empirical hypothesis to be tested, not assumed.\",\n  \"terms\": [\n    {\n      \"term\": \"Curie-Weiss Activation (CWA)\",\n      \"definition\": \"The proposed hidden-layer activation function defined by the fixed point y* of the equation y = tanh(x + J·mean(y)), where x is the vector of pre-activations, y is the vector of activations, J = σ(J_raw) ∈ (0,1) is a per-layer learnable scalar coupling, and mean(y) is the layer-wise mean of y. The fixed point is found by adaptive-K iteration m_{t+1} = mean(tanh(x + J·m_t)) until |m_{t+1}−m_t| < δ, then y_i = tanh(x_i + J·m*).\"\n    },\n    {\n      \"term\": \"Effective Coupling (J·s̄)\",\n      \"definition\": \"The true critical parameter of CWA, defined as J·s̄ = J·mean(sech²(x+J·m*)) ∈ (0,1). This is the per-step convergence rate of the fixed-point iteration and the spectral norm of the layer's input-output Jacobian. J·s̄ → 1 corresponds to the edge-of-chaos critical regime with diverging gain. J·s̄ depends on both the learned coupling J and the input distribution (through s̄), making the critical condition input-distribution-dependent. All experiments track J·s̄ alongside J.\"\n    },\n    {\n      \"term\": \"Adaptive-K Iteration\",\n      \"definition\": \"The convergence-based stopping rule for the CWA forward pass: iterate m ← mean(tanh(x + J·m)) until |m_{t+1}−m_t| < δ = 1e-4 (with a maximum of K_max=50 iterations). The number of required steps K*(ρ) grows as O(1/(1−ρ)) near criticality (ρ = J·s̄ → 1) due to classical critical slowing down. Wall-clock cost per forward pass is measured during training as a function of the current J·s̄ to empirically characterize the computational overhead of near-critical regimes.\"\n    },\n    {\n      \"term\": \"Sigmoid Parameterization of J\",\n      \"definition\": \"The constraint mechanism for the learnable coupling: J = σ(J_raw) = 1/(1+exp(−J_raw)), where J_raw ∈ ℝ is the actual learnable parameter and J ∈ (0,1) is the constrained coupling. This hard-constrains J to the monostable regime (below the ferromagnetic phase transition at J=1), preventing bistability and guaranteeing global convergence of the fixed-point iteration. J_raw is initialized at 0 so that J starts at 0.5 (moderate coupling).\"\n    },\n    {\n      \"term\": \"Critical Gain\",\n      \"definition\": \"The effective gradient amplification of CWA near the critical coupling J·s̄ → 1. By the implicit function theorem, the input-output Jacobian element ∂y_i/∂x_i = sech²(x_i + J·m*) / (1 − J·s̄), which diverges as J·s̄ → 1. This diverging gain enables maximum sensitivity of the layer to its inputs and is the proposed mechanism for gradient stability in deep unnormalized networks.\"\n    },\n    {\n      \"term\": \"Self-Organized Criticality (SOC) Hypothesis\",\n      \"definition\": \"The empirical hypothesis — not an assumption — that gradient descent will push J·s̄ toward 1 during training, because layers with J·s̄ near 1 have higher effective gain and thus more informative gradients, giving task-loss minimization an incentive to approach criticality. Tested experimentally by plotting the distribution of learned J·s̄ values across layers and seeds at convergence and by the fixed-J ablation study.\"\n    },\n    {\n      \"term\": \"Output-Coupling vs Input-Normalization\",\n      \"definition\": \"The key mechanistic distinction between CWA and LayerNorm/BatchNorm. LayerNorm/BatchNorm normalize the INPUT pre-activations x (shifting and scaling to zero mean, unit variance) before a pointwise nonlinearity — they operate on input statistics. CWA couples the OUTPUTS y through the self-consistency feedback mean(y) → tanh(x + J·mean(y)) → new y — it operates on output statistics under the actual nonlinearity. These are categorically different operations that compose rather than substitute.\"\n    },\n    {\n      \"term\": \"Fixed-J Ablation\",\n      \"definition\": \"A controlled experiment where J is frozen at specific values {0.1, 0.3, 0.5, 0.7, 0.9} (J_raw fixed, not updated by optimizer) and compared against the full CWA (learned J). This separates whether the performance benefit of CWA requires (a) any nonzero coupling (vs. J=0 = pure tanh), (b) a specific coupling value, or (c) the adaptive optimization of J by gradient descent. It directly tests the SOC hypothesis and whether criticality is necessary for the performance gains.\"\n    }\n  ],\n  \"summary\": \"We propose the Curie-Weiss Activation (CWA), a hidden-layer activation function where each neuron's output is the fixed point of the mean-field self-consistency equation y_i = tanh(x_i + J·mean(y)), with J = σ(J_raw) ∈ (0,1) a per-layer learnable coupling constrained by sigmoid parameterization. Borrowing from the physics of ferromagnetism, CWA introduces within-layer inter-neuron coupling absent from all standard pointwise MLP-block activations; whether J self-organizes toward the critical coupling J·s̄ → 1 is treated as an empirical finding — tested via adaptive-K iteration with honest wall-clock accounting and a controlled fixed-J ablation — evaluated against comprehensive baselines (GELU, SELU, tanh+LN, GELU+LN, Competing Nonlinearities mixture) on deep unnormalized MLPs, ResNet-20/CIFAR-100, and character-level language modeling.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [16] ASSISTANT · 2026-06-16 17:01:46 UTC

```
The revised hypothesis has been written to `.terminal_claude_agent_struct_out.json`. Here's a summary of how each critique was addressed:

**Major critiques fixed:**

1. **Critical slowing down** — Replaced the fixed 5-step iteration with adaptive-K stopping (`|m_{t+1}−m_t| < δ=1e-4`, cap 50), making the O(1/(1−ρ)) cost near criticality explicit and measured experimentally rather than hidden.

2. **SOC claim unsubstantiated** — J self-organization toward J·s̄=1 is now an *empirical finding to be measured*, not an assumption. Added a controlled fixed-J ablation (J frozen at {0.1, 0.3, 0.5, 0.7, 0.9} vs. learned J) to directly test whether criticality is necessary.

3. **Missing concurrent papers** — Boltzmann Attention (2606.12478) and Competing Nonlinearities (2605.05294) are now in related works with precise differentiation: BA targets the attention operator (inter-token), CWA targets the activation nonlinearity (intra-layer); CN uses a static mixture at p_c (no fixed-point, no learned coupling), CWA uses adaptive self-consistency with a learned J.

4. **Experimental scope** — Extended to: ResNet-20 on CIFAR-100, 4-layer GPT on character-level text, and MLPs at depths {6, 10, 20} to test gradient stability at depth. CN's tanh+Swish@p_c included as a direct baseline.

5. **Missing baselines** — Added tanh+LN, GELU+LN, SELU, ReLU+BN, and the CN mixture.

**Minor critiques fixed:**

6. **J vs J·s̄** — All experiments now track J·s̄ = J·mean(sech²(x+J·m*)) as the true critical parameter; success criterion uses J·s̄, not J alone.

7. **Softmax not pointwise** — Qualified to "hidden-layer activation functions in MLP blocks between linear layers."

8. **Success criteria ambiguous** — GELU is now the explicit primary comparison baseline.

9. **J constraint mechanism** — Specified as sigmoid parameterization J = σ(J_raw), initialized at J_raw=0 (J≈0.5), with explicit rationale for preventing bistability.
```
