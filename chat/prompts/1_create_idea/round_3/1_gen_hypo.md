# gen_hypo_1 — create_idea

> Phase: `hypo_loop` · round 3 · `gen_hypo`
> Run: `run_6gT5lHFn8559` — Novel Activation Function
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_hypo_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 17:06:18 UTC

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

<previous_review_feedback>
A reviewer evaluated your previous hypothesis and provided the feedback below.

IMPORTANT: Do NOT generate a completely new hypothesis. Take the previous hypothesis above and
REVISE it to address the feedback. Keep what works, fix what was criticized.

You MUST address ALL the critiques. Do NOT repeat the same mistakes.

kind: reviewer_feedback
id: review_hypo_35a564e14e2c
overall_assessment: >-
  The revised hypothesis has addressed all five major and four minor critiques from the previous review with impressive thoroughness.
  The adaptive-K iteration properly handles critical slowing down; J self-organization is recast as an empirical finding rather
  than an assumption; Boltzmann Attention and Competing Nonlinearities are now cited with clean differentiation; the experimental
  plan includes ResNet-20/CIFAR-100 and character-level GPT; and all requested baselines (SELU, tanh+LN, GELU+LN) are present.
  The hypothesis is now technically sound at its core. Three new issues emerge from this revision: (1) the memory cost of
  unrolled backprop through K* iterations is unacknowledged and non-trivial near criticality; (2) the mean-field approximation
  breaks down at the narrow layer widths present in ResNet-20 (16–64 channels), and this is not discussed; (3) the GPT experiment
  (4-layer, 128-hidden, Tiny Shakespeare) is too small to establish language modeling claims beyond the toy level. The score
  is stable at 6 (Weak Accept); addressing the memory/finite-width issues and scaling the GPT experiment slightly would open
  a clear path to 7.
strengths:
- >-
  All five major prior critiques are cleanly resolved: adaptive-K iteration with honest wall-clock accounting; SOC reframed
  as an empirical finding with fixed-J ablation; Boltzmann Attention and Competing Nonlinearities cited with precise differentiation;
  ResNet-20 and character-level GPT added; SELU/tanh+LN/GELU+LN baselines included.
- >-
  The sigmoid parameterization J = σ(J_raw) ∈ (0,1) is a principled, complete answer to the bistability/constraint problem,
  with initialization at J_raw=0 (J=0.5) giving a sensible starting coupling.
- >-
  The IFT gradient derivation is correctly stated (∂m*/∂x = sech²(x+J·m*)/(1−J·s̄), ∂m*/∂J = s̄·m*/(1−J·s̄)) and is backed
  by the Banach fixed-point theorem guarantee for J ∈ (0,1).
- >-
  Tracking J·s̄ (the true effective Jacobian coupling) alongside J throughout all experiments is the correct operationalization
  of criticality and directly addresses the prior minor critique.
- >-
  The fixed-J ablation study ({0.1, 0.3, 0.5, 0.7, 0.9}) cleanly separates whether any coupling, a specific value, or learned
  adaptation drives performance — this is a high-value minimal experiment.
- >-
  The PARTIAL CONFIRM scenario is explicitly operationalized: CWA contributes uniquely in unnormalized networks and this is
  treated as a precise bound on the contribution rather than a failure.
- >-
  The motivation clearly distinguishes CWA from LayerNorm (output coupling vs. input normalization) in a testable, mechanistically
  precise way.
- >-
  Related work coverage is now comprehensive and differentiated: DEQ (full-layer vs. activation-level), SELU (pointwise self-normalization
  vs. inter-neuron coupling), Boltzmann Attention (inter-token vs. intra-layer), Competing Nonlinearities (static mixture
  vs. learned adaptive coupling).
dimension_scores:
- dimension: soundness
  score: 3
  justification: >-
    The core mathematical formulation is correct and complete. The Banach contraction guarantee, IFT gradient formula, and
    adaptive-K stopping rule are all properly stated. Two technical gaps remain: (1) the memory cost of unrolled backprop
    through adaptive K* iterations is unaddressed — near ρ=0.9, up to K*=50 intermediate activation tensors of shape (batch,
    n) are stored; (2) the mean-field approximation assumes n→∞ but ResNet-20 has layers with 16–64 channels where finite-width
    noise O(1/√n) is substantial, yet this is not discussed.
  improvements:
  - >-
    Add a paragraph on backpropagation memory: with unrolled autograd through K* steps, each layer stores K* intermediate
    tensors of shape (batch_size × n_neurons). Near criticality (ρ=0.9, K*≈50), this is 50× the memory of GELU for the same
    layer. Either (a) switch to IFT backprop for production experiments (O(1) activation memory, as in DEQ), noting that the
    inexact fixed-point error adds a gradient bias of O(δ/(1−ρ)) that should be characterized, or (b) add peak GPU memory
    as a measured output in Experiment 5 alongside wall-clock time.
  - >-
    Add a discussion of finite-width effects: the CWA mean-field equation m* = mean(tanh(x + J·m*)) treats the sample mean
    as a deterministic quantity, valid as n→∞. At n=16 (first ResNet-20 block), the mean has standard deviation O(1/√16) =
    0.25 times the per-neuron standard deviation — a substantial noise source. Acknowledge this as a limitation and test whether
    CWA performance degrades in narrow-width layers (e.g., compare ResNet-20 standard vs. a wider ResNet variant with 4× channels).
- dimension: presentation
  score: 3
  justification: >-
    The hypothesis is clearly structured, well-motivated, and the terminology section provides precise definitions for all
    non-standard terms. The previous review's softmax qualifier and success criterion issues are resolved. The main presentation
    gap is that the IFT vs. unrolled backprop trade-off is described in the assumptions but not resolved in the investigation
    approach — the reader doesn't know which will be used in practice and why.
  improvements:
  - >-
    In the investigation approach, make a definitive choice between IFT and unrolled backprop for the production experiments,
    and justify it. Recommended: use unrolled autograd for J·s̄ < 0.85 (few iterations, manageable memory) and switch to IFT
    for J·s̄ > 0.85 (large K*, IFT is more efficient but requires exact convergence). State the chosen strategy explicitly
    so the experimental setup is reproducible.
  - >-
    Add a brief note clarifying that 'mean' in mean(y) = mean over n_neurons within one sample, not over the mini-batch. This
    avoids confusion with batch statistics (BatchNorm) and is a key point distinguishing CWA from batch-dependent methods.
- dimension: contribution
  score: 3
  justification: >-
    The contribution is technically novel: a learnable within-layer mean-field coupling at the activation level is absent
    from all cited prior work. The honest empirical program (SOC as a finding, not an assumption) and the fixed-J ablation
    are genuinely valuable contributions independent of whether the main hypothesis confirms. The significance ceiling remains:
    the primary use case (unnormalized deep networks) is a setting modern practitioners largely avoid via LayerNorm/BatchNorm,
    limiting the practical impact. The GPT experiment is too small (4-layer, 128-hidden, Tiny Shakespeare) to constitute evidence
    for language model utility.
  improvements:
  - >-
    Scale the character-level GPT experiment to at least 6 layers and 256 hidden units, or switch to word-level PTB/WikiText-2,
    to produce a result that represents more than a toy proof-of-concept. The current scale (128-hidden) is below the hidden
    dimension of a two-year-old GPT-2 small (768), making the result hard to interpret as evidence about language modeling.
  - >-
    Add a motivating paragraph for why unnormalized deep networks matter in 2026 (e.g., fast inference without normalization
    overhead, edge deployment on hardware that penalizes layer statistics computation, specific scientific computing architectures).
    This converts the PARTIAL CONFIRM scenario from 'niche edge case' into 'targeted practical contribution.'
critiques:
- id: ''
  category: methodology
  severity: major
  description: >-
    Unrolled backprop through adaptive-K iterations introduces a non-trivial memory overhead that is not discussed. When ρ
    = J·s̄ → 0.9 and K* reaches 50 (K_max), PyTorch's unrolled autograd must store K* intermediate activation tensors of shape
    (batch_size × n_neurons) per CWA layer. Concretely: batch=512, n=256, K*=50 → 50 × 512 × 256 × 4 bytes = 26MB per layer,
    per forward pass. For a 20-layer network with CWA everywhere, this is ~520MB of additional activation memory vs. ~10MB
    for GELU. Experiment 5 measures wall-clock time but not peak GPU memory, which may be the binding constraint in the near-critical
    regime. Separately, the DEQ literature (Bai et al. 2019; Efficient DEQ 2023) has demonstrated that implicit differentiation
    (IFT) reduces memory to O(1) by not storing intermediate activations — this approach is mentioned in the assumptions but
    not adopted in the investigation plan.
  suggested_action: >-
    Add peak GPU memory utilization as a second tracked output in Experiment 5, alongside wall-clock time, as a function of
    J·s̄. Either (a) adopt IFT backprop for experiments where J·s̄ > 0.8, storing only the converged m* and computing ∂m*/∂x
    analytically — this is O(1) in K*, avoids storing intermediate activations, and has been proven correct in the DEQ literature;
    or (b) keep unrolled autograd but explicitly acknowledge and measure the O(K*) memory overhead and flag it as a practical
    limitation when J·s̄ > 0.85. The investigation approach section should commit to one strategy and justify why. Expected
    score impact: +0.5.
- id: ''
  category: methodology
  severity: major
  description: >-
    The mean-field approximation underlying CWA is exact only as n_neurons → ∞, but ResNet-20 operates at layer widths of
    16–64 channels in early blocks. At n=16, the sample mean m* = (1/n)Σ_i tanh(x_i + J·m*) has a finite-sample noise of O(1/√n)
    = O(0.25) relative to the unit-scale activations — a 25% noise floor. This means the 'self-consistency' equation the iteration
    solves is not the mean-field equation but a noisy, sample-dependent perturbation of it. The fixed-point m* will fluctuate
    substantially across samples at narrow widths, making J·s̄ a noisy quantity and potentially undermining both gradient
    stability and the SOC analysis. The hypothesis never acknowledges this, and attributing CWA results in the narrow-width
    ResNet-20 blocks to the mean-field physics may be incorrect.
  suggested_action: >-
    Add a brief theoretical caveat: CWA's mean-field interpretation holds in the large-n limit; at finite n, the fixed-point
    equation includes O(1/√n) fluctuations. Mitigate or characterize empirically by: (1) comparing CWA performance in the
    first ResNet-20 block (n=16) vs. later blocks (n=64), to test whether narrow-width blocks benefit less; (2) alternatively,
    test a 'wide ResNet-20' variant (4× channels throughout) to see if performance improves at larger n. This analysis would
    convert a potential confound into an informative experiment about the n-dependence of CWA's mechanism. Expected score
    impact: +0.4.
- id: ''
  category: scope
  severity: minor
  description: >-
    The character-level language modeling experiment uses a 4-layer, 128-hidden GPT on Tiny Shakespeare. This is an extremely
    small model by current standards (GPT-2 small has 12 layers, 768 hidden). At this scale, the test BPC differences between
    activation functions may be dominated by optimization noise and are difficult to interpret as evidence about language
    model utility. The Boltzmann Attention paper (cited in related work) uses Tiny Shakespeare as its own benchmark, making
    the CWA result directly comparable to that paper, but not to the broader NeurIPS/ICLR language modeling literature.
  suggested_action: >-
    Scale the GPT experiment to at least 6 layers and 256 hidden units, keeping sequence length 256 and training on Tiny Shakespeare,
    OR switch to WikiText-2 (word-level) which allows comparison to the established SELU/normalization literature. The goal
    is to have at least one language modeling result that isn't a clear toy: the 4-layer 128-hidden model is smaller than
    GPT-2's single attention head output projection. Even 6L/256H on Tiny Shakespeare would be meaningfully larger. Expected
    score impact: +0.3.
- id: ''
  category: rigor
  severity: minor
  description: >-
    The gradient stopping criterion δ = 1e-4 for |m_{t+1} − m_t| < δ bounds the iteration residual, but when IFT is used for
    backprop, the gradient error is not just O(δ) — it is O(δ/(1−J·s̄)), which diverges as J·s̄ → 1. Near criticality (J·s̄
    = 0.9), the effective gradient error is 10× the residual threshold, i.e., ~1e-3. This interplay between the stopping tolerance
    δ and the IFT gradient accuracy in the near-critical regime is not acknowledged. The hypothesis mentions IFT as an alternative
    but doesn't note that IFT's accuracy degrades in the same near-critical regime where adaptive-K is expensive.
  suggested_action: >-
    In the assumptions section, add a note: when using IFT backprop with an inexact fixed point (residual r = |F(m*)|), the
    gradient error is O(r/(1−J·s̄)) by the perturbation theory of the IFT. At J·s̄ = 0.9 and δ = 1e-4, this error is ~1e-3,
    which is small relative to gradient norms but should be verified not to cause systematic bias. Either tighten δ adaptively
    as J·s̄ increases (e.g., δ = 1e-4 × (1 − J·s̄)), or acknowledge the IFT gradient bias as a measured output alongside K*
    and J·s̄ in Experiment 3. Expected score impact: +0.2.
- id: ''
  category: clarity
  severity: minor
  description: >-
    The practical significance of the unnormalized deep network setting is not motivated. The hypothesis's most compelling
    result scenario — PARTIAL CONFIRM, where CWA helps only when normalization is absent — is the most likely outcome given
    that SELU and tanh+LN are strong baselines in normalized settings. However, unnormalized deep MLPs are rare in current
    practice; most practitioners use LayerNorm or BatchNorm as a default. Without motivation for why the unnormalized setting
    matters, the PARTIAL CONFIRM scenario reads as a niche finding rather than a targeted contribution.
  suggested_action: >-
    Add 2-3 sentences to the motivation section explaining why unnormalized deep networks are a relevant practical target:
    e.g., on-device inference where normalization's mean/variance computation is expensive (memory-constrained edge hardware);
    scientific neural operators where normalization distorts physical quantities; architectures that deliberately avoid BatchNorm
    to prevent train/test distribution shift. This converts the PARTIAL CONFIRM from a fallback to a principled targeted claim.
    Expected score impact: +0.2.
- id: ''
  category: evidence
  severity: minor
  description: >-
    The Competing Nonlinearities (Lesser & Chowdhury 2026) baseline requires knowing the theoretical critical mixing fraction
    p_c, which is architecture-specific (it depends on the variance propagation under the specific tanh/Swish mixture). The
    hypothesis includes 'tanh+Swish@p_c' as a baseline without specifying how p_c will be computed for each architecture in
    the experiment. If p_c is copied from Lesser & Chowdhury's derivation without re-deriving it for the specific architectures
    tested, the baseline may not be at its optimal operating point, making the comparison unfair.
  suggested_action: >-
    Specify how p_c will be determined for each tested architecture: either (a) derive p_c analytically from the variance
    propagation equations at depth d (following Lesser & Chowdhury's method) for each network depth tested, or (b) tune p_c
    as a hyperparameter on the validation set for each architecture (ensuring the baseline is at its best), or (c) include
    p_c ∈ {theoretical, tuned} as separate conditions. Clarify this in the investigation approach section. Expected score
    impact: +0.1.
score: 6
confidence: 4
relation_type: evolution
relation_rationale: >-
  Same CWA frame; adds adaptive-K, reframes SOC as empirical, scales experiments — no conceptual replacement.
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

### [2] HUMAN-USER prompt · 2026-06-16 17:06:18 UTC

```
Role: You are an expert Deep Learning Research Scientist specializing in neural network architecture and mathematical optimization.Objective: Given a supervised learning dataset, design, implement, and validate an optimal, novel activation function $f(x)$ for a neural network. Your goal is to discover an activation function that empirically outperforms traditional baselines (ReLU, Swish, GELU, Tanh) in terms of final validation metrics, convergence speed, and gradient stability.Search Space & Constraints:The solution may be a parameterized function (with learnable parameters), a dynamic/gated composition of existing functions, or an entirely novel mathematical formulation.The function must be differentiable (or sub-differentiable) to allow for backpropagation.Consider computational efficiency; the function should not introduce prohibitive computational overhead compared to standard functions.
```

### [3] SYSTEM-USER prompt · 2026-06-16 17:09:16 UTC

```
STOP — your tool log shows you only SEARCHED the web and never opened or read a single full page. Search result snippets (titles, URLs, one-line descriptions) are NOT sufficient evidence: they cannot confirm novelty, and they cannot give you the exact methods, numbers, or claims of prior work.

Before you finalise this hypothesis you MUST now actually fetch and read the most relevant sources in full. Use the built-in `WebFetch` tool (or, for exact quotes/numbers, the aii-web-tools `aii_fast_web_fetch.py fetch`/`grep` script). Open at least the few most relevant URLs, read their real content, and let that evidence revise your conclusions.

Then re-write your structured output file with the corrected, evidence-grounded result. Do not stop until you have fetched at least one full page.
```

### [4] SKILL-INPUT — aii-web-tools · 2026-06-16 17:09:20 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: web search (Serper/Google), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — Serper.dev for search, html2text + PyMuPDF for fetch, and
   regex grep over the full document text. They work without any built-in web
   tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (Serper.dev / Google)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
```

Returns ranked title / URL / snippet lines. Use it first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````
