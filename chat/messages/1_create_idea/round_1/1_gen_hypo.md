# gen_hypo_1 — create_idea

> Phase: `hypo_loop` · round 1 · `gen_hypo`
> Run: `run_6gT5lHFn8559` — Novel Activation Function
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_hypo_1` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-06-16 16:43:43 UTC

```
model: claude-sonnet-4-6 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/iter_1/gen_hypo/claude_agent
```

### [2] SYSTEM-USER prompt · 2026-06-16 16:43:49 UTC

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

<user_data>
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

### [3] HUMAN-USER prompt · 2026-06-16 16:43:49 UTC

```
Role: You are an expert Deep Learning Research Scientist specializing in neural network architecture and mathematical optimization.Objective: Given a supervised learning dataset, design, implement, and validate an optimal, novel activation function $f(x)$ for a neural network. Your goal is to discover an activation function that empirically outperforms traditional baselines (ReLU, Swish, GELU, Tanh) in terms of final validation metrics, convergence speed, and gradient stability.Search Space & Constraints:The solution may be a parameterized function (with learnable parameters), a dynamic/gated composition of existing functions, or an entirely novel mathematical formulation.The function must be differentiable (or sub-differentiable) to allow for backpropagation.Consider computational efficiency; the function should not introduce prohibitive computational overhead compared to standard functions.
```

### [4] ASSISTANT · 2026-06-16 16:44:24 UTC

```
I'll start by reading the web tools skill, then brainstorm and search for novel activation function directions.
```

### [5] TOOL CALL — Skill · 2026-06-16 16:44:24 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-06-16 16:44:24 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] ASSISTANT · 2026-06-16 16:44:42 UTC

```
Setting up the environment, then I'll run parallel searches across 5-7 brainstormed directions.
```

### [8] TOOL CALL — Bash · 2026-06-16 16:44:42 UTC

```
Set up web tools environment:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
echo "PY=$PY"
ls $SKILL_DIR/scripts/
```

### [9] TOOL RESULT — Bash · 2026-06-16 16:44:42 UTC

```
{"stdout": "PY=/ai-inventor/.claude/skills/aii-web-tools/../.ability_client_venv/bin/python\n__pycache__\n_web_cache.py\naii_fast_web_fetch.py\naii_fast_web_search.py\naii_verify_quotes.py\ncheck_env.sh\nserver_requirements.txt", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [10] TOOL CALL — Bash · 2026-06-16 16:44:48 UTC

```
Run 4 parallel searches across brainstormed directions:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "Nash equilibrium activation function neural network game theory" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "reaction diffusion Turing pattern neural network activation" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "fixed point iteration activation function self-consistent neural network" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "novel activation function 2024 beyond ReLU GELU learnable" --max-results 8 2>&1 &
wait
echo "=== ALL SEARCHES DONE ==="
```

### [11] TOOL RESULT — Bash · 2026-06-16 16:44:48 UTC

```
{"stdout": "Search: reaction diffusion Turing pattern neural network activation\nFound: 8 results\n\n1. Exploring potential of Turing pattern classification through ... - Nature\n   https://www.nature.com/articles/s41598-025-32911-0\n   Turing patterns, observed in natural phenomena such as animal coats and fish scales, are generated by reaction-diffusion systems due to their ......\n\n2. Machine learning approaches to the inverse problem of stationary ...\n   https://www.sciencedirect.com/science/article/pii/S2589004224010447\n   The diffusion-driven Turing instability is a potential mechanism for spatial pattern formation in numerous biological and chemical systems....\n\n3. [PDF] Reaction-Diffusion Model as a Framework for Understanding ...\n   https://www.scienceintheclassroom.org/sites/default/files/related/reaction-diffusion_model_as_a_framework_for_understanding_biological_pattern_formation.pdf\n   The Turing, or reaction-diffusion (RD), model is one of the best-known theoretical models used to explain self-regulated pattern formation ......\n\n4. Pattern formation mechanisms of self-organizing reaction-diffusion ...\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC7154499/\n   For the formation of Turing patterns, two key conditions must be satisfied: First, the stability condition requires that the system reaches a stable and ......\n\n5. Turing pattern - Wikipedia\n   https://en.wikipedia.org/wiki/Turing_pattern\n   The pattern arises due to Turing instability, which in turn arises due to the interplay between differential diffusion of chemical species and chemical reaction ......\n\n6. Pattern Control of Neural Networks with Two-Dimensional Diffusion ...\n   https://link.springer.com/article/10.1007/s11063-024-11491-6\n   In this paper, a two-neuron reaction–diffusion neural network with discrete and distributed delays is proposed, and the state feedback control strategy is ......\n\n7. Turing's theory of pattern formation - VisualPDE\n   https://visualpde.com/visual-stories/turing-morphogenesis.html\n   We start with a 'classical' reaction–diffusion Turing model, show a few examples of how the more general principle of local activation and long-range ......\n\n8. A Reaction-Diffusion Model Generating Turing Patterns\n   https://biologicalmodeling.org/prologue/reaction-diffusion\n   Study reaction diffusion equations that link chemistry with diffusion, showing how Turing patterns emerge from simple instabilities....\n\nSearch: Nash equilibrium activation function neural network game theory\nFound: 8 results\n\n1. [PDF] A Recurrent Neural Network for Game Theoretic Decision Making\n   https://www.cmu.edu/dietrich/sds/docs/golman/a-recurrent-neural-network-for-game-theoretic-decision-making-bhatia_golman.pdf\n   The unique Nash equilibrium corresponds to the only stable state of activation here, because it consists of the only rationalizable strategy for each player....\n\n2. Applications of game theory in deep learning: a survey - PMC\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC9039031/\n   Nash equilibrium. It is a stable state where players cannot earn more profits by unilaterally deviating from their strategies. Players can have a pure or mixed ......\n\n3. A game-theoretic perspective of deep neural networks - ScienceDirect\n   https://www.sciencedirect.com/science/article/abs/pii/S0304397522005965\n   In principle, the classic SVM can be viewed as a two-player zero-sum game, for which we want to compute a pure Nash equilibrium, i.e., a ......\n\n4. Can a neural net model a mixed-strategy Nash equilibrium?\n   https://ai.stackexchange.com/questions/50595/can-a-neural-net-model-a-mixed-strategy-nash-equilibrium\n   This would seem to imply that a neural net cannot model a mixed-strategy Nash equilibrium for a game, because such a mixed-strategy inherently ......\n\n5. Deep Learning to Play Games - arXiv\n   https://arxiv.org/html/2409.15197v1\n   Our simulations demonstrate that the joint behavior of the networks converges to strategies close to Nash equilibria in almost all games. For ......\n\n6. Can Game Theory profit from ML or Deep learning? And if so, how?\n   https://www.reddit.com/r/MLQuestions/comments/7g74ec/can_game_theory_profit_from_ml_or_deep_learning/\n   The Nash equilibrium is one of the foundational concepts in game theory. The reality of the Nash equilibrium of a game can be tested using ......\n\n7. Game Theory in GANs: Nash Equilibrium and Mode Collapse\n   https://eureka.patsnap.com/article/game-theory-in-gans-nash-equilibrium-and-mode-collapse\n   In the context of GANs, a Nash Equilibrium would occur when the generator produces samples that are indistinguishable from real data by the ......\n\n8. [PDF] Strategy Learning in Games by Neural Networks\n   https://www.repository.cam.ac.uk/bitstreams/e065cd32-6b58-4214-a5c9-ae78864f29d5/download\n   What we discover is that Nash equilibrium is just too complex a concept for a neural network to use in general in new environments. It is not difficult for the....\n\nSearch: novel activation function 2024 beyond ReLU GELU learnable\nFound: 8 results\n\n1. Leveraging Continuously Differentiable Activation for Learning in ...\n   https://arxiv.org/html/2402.02593v2\n   In this paper, we demonstrate that GELU and SiLU enable robust propagation of gradients in analog hardware because they are continuously differentiable ......\n\n2. Navigating Neural Networks: Exploring State-of-the-Art Activation ...\n   https://sites.gatech.edu/omscs7641/2024/01/31/navigating-neural-networks-exploring-state-of-the-art-activation-functions/\n   This guide delves into the evolution, characteristics, and applications of state-of-the-art activation functions, illustrating their role in enhancing neural ......\n\n3. Beyond ReLU: A Deep Dive into the Evolution of Activation Functions.\n   https://medium.com/@nanda.yugandhar/beyond-relu-a-deep-dive-into-the-evolution-of-activation-functions-fcce7afc4221\n   From simple switches to smart dimmers, let's explore why modern activation functions like Mish and GELU are taking over....\n\n4. I made a new novel activation function for deep learning - Reddit\n   https://www.reddit.com/r/learnmachinelearning/comments/1mvbjwc/i_made_a_new_novel_activation_function_for_deep/\n   Recently, I created BiNLOP, a novel piecewise linear activation function. I believe that this might be a key advancement in deep learning in ......\n\n5. [PDF] Deep Network Approximation: Beyond ReLU to Diverse Activation ...\n   https://jmlr.org/papers/volume25/23-0912/23-0912.pdf\n   This paper explores the expressive power of deep neural networks for a diverse range of activation functions. An activation function set A is defined to ......\n\n6. Why deep learning models still use RELU instead of SELU, as their ...\n   https://datascience.stackexchange.com/questions/102724/why-deep-learning-models-still-use-relu-instead-of-selu-as-their-activation-fun\n   I am a trying to understand the SELU activation function and I was wondering why deep learning practitioners keep using RELU, with all its issues, instead of ......\n\n7. Some recent activation functions mimicking ReLU\n   https://vitalab.github.io/blog/2024/08/20/new_activation_functions.html\n   Below is a description of the relationships between several important activation functions: ReLU, ELU, GELU, GLU, SiLU, Swish, ReGLU, GEGLU, and SwiGLU....\n\n8. Activation Function Strategies in Deep Learning Models - Nature\n   https://www.nature.com/nature-index/topics/l4/activation-function-strategies-in-deep-learning-models\n   Activation functions are fundamental to the representational power of deep neural networks, introducing non-linearity that enables the modelling of complex....\n\n[1]   Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"Nash equilibrium activation function neural network game theory\" --max-results 8 2>&1\n[2]   Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"reaction diffusion Turing pattern neural network activation\" --max-results 8 2>&1\nSearch: fixed point iteration activation function self-consistent neural network\nFound: 8 results\n\n1. Advancing the Understanding of Fixed Point Iterations in Deep ...\n   https://arxiv.org/html/2410.11279v1\n   This study provides an analytical framework for understanding fixed point iterations in deep neural networks. We established theorems for ......\n\n2. [PDF] Deep Learning and Self-Consistent Field Theory - UCSB Math\n   https://web.math.ucsb.edu/~hdc/public/Deep_Learning_and_Self_Consistent_Field_Theory__A_Path_Towards_Accelerating.pdf\n   A new framework that leverages data obtained from self-consistent field theory (SCFT) simulations with deep learning point iterations....\n\n3. Advancing the understanding of fixed point iterations in deep neural ...\n   https://openreview.net/forum?id=YoEFNqMNmG\n   In this study, we conduct a detailed analysis of fixed point iterations in a vector-valued function modeled by neural networks. We establish a ......\n\n4. [PDF] Approximate Fixed-Points in Recurrent Neural Networks\n   https://homepages.inf.ed.ac.uk/htang2/sigml/mlslp2021/MLSLP2021_paper_3.pdf\n   This paper proposed a novel view on history representations obtained from recurrent neural networks (RNN) as fixed- points of non-linear equation systems. The ......\n\n5. Fixed points of nonnegative neural networks - ACM Digital Library\n   https://dl.acm.org/doi/pdf/10.5555/3722577.3722716\n   We use fixed point theory to analyze nonnegative neural networks, which we define as neural networks that map nonnegative vectors to nonnegative vectors....\n\n6. Learning Fixed Points of Recurrent Neural Networks by ...\n   https://direct.mit.edu/neco/article/36/8/1568/123708/Learning-Fixed-Points-of-Recurrent-Neural-Networks\n   fixed points of recurrent neural networks are used to model neural responses to static or slowly changing stimuli, such as visual cortical ......\n\n7. Activation Functions in Neural Networks - GeeksforGeeks\n   https://www.geeksforgeeks.org/machine-learning/activation-functions-neural-networks/\n   An activation function is applied to the weighted sum of inputs before producing the final output of a neuron. It introduces non-linearity, ......\n\n8. Neural Networks From Scratch - Lec 13 - Swish Activation Function\n   https://www.youtube.com/watch?v=zYtn4BR6R2E\n   Building Neural Networks from scratch in python. This is the thirteenth video of the course - \"Neural Networks From Scratch\"....\n\n[3]-  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"fixed point iteration activation function self-consistent neural network\" --max-results 8 2>&1\n[4]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"novel activation function 2024 beyond ReLU GELU learnable\" --max-results 8 2>&1\n=== ALL SEARCHES DONE ===", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [12] TOOL CALL — Bash · 2026-06-16 16:45:22 UTC

```
Search 5 novel directions in parallel:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "implicit activation function neural network fixed point self-referential" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "optimal transport activation function neural network distribution matching" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "mean field theory activation function Ising Boltzmann neural network" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "maximum entropy activation function neural network information theory" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "topological persistence activation function neural network TDA" --max-results 8 2>&1 &
wait
echo "=== DONE ==="
```

### [13] TOOL RESULT — Bash · 2026-06-16 16:45:22 UTC

```
{"stdout": "Search: mean field theory activation function Ising Boltzmann neural network\nFound: 8 results\n\n1. [PDF] Boltzmann Machine Learning Using Mean Field Theory and Linear ...\n   http://papers.neurips.cc/paper/1412-boltzmann-machine-learning-using-mean-field-theory-and-linear-response-correction.pdf\n   We present a new approximate learning algorithm for Boltzmann Machines, using a systematic expansion of the Gibbs free energy to second order in the weights. A ......\n\n2. [PDF] Mean Field Theory and its application to deep learning - Mimee Xu\n   https://mimee.xyz/meanfield.pdf\n   The variational mean field analysis connects statistical physics and Boltzmann machine approximations for neural networks....\n\n3. [PDF] Restricted Boltzmann Machine, recent advances and mean-field ...\n   https://pages.saclay.inria.fr/cyril.furtlehner/files/art_rbm.pdf\n   This review deals with Restricted Boltzmann Machine (RBM) under the light of statistical physics. The. RBM is a classical family of Machine learning (ML) ......\n\n4. Correspondence Between Ising Machines and Neural Networks\n   https://arxiv.org/html/2511.00746v1\n   The correspondence is based on the trivial observation that both tanh-activated neural networks and naive mean field theory contain a hyperbolic ......\n\n5. Foundations: Mean Field Boltzmann Machines 1987\n   https://calculatedcontent.com/2017/01/05/foundations-mean-field-boltzmann-machines-1987/\n   A Mean Field Theory Learning Algorithm for Neural Networks activation function came from. They come from the MFT. There is a deep reason for ......\n\n6. The Physics of Machine Learning\" Michael Toomey (Brown University)\n   https://www.youtube.com/watch?v=7Yt4R8ZLDz8\n   ... field theory. Nowhere is this more apparent than Boltzmann machines which fall into a class of energy-based machine learning algorithms ......\n\n7. [PDF] An examination and analysis of the Boltzmann machine, its mean ...\n   https://ro.ecu.edu.au/cgi/viewcontent.cgi?article=1394&context=theses_hons\n   Simulation results suggest that the mean field theory approximation learns faster than the Boltzmann Machine, and shows better stability....\n\n8. Boltzmann Machine Learning Using Mean Field Theory and Linear ...\n   https://www.researchgate.net/publication/221618347_Boltzmann_Machine_Learning_Using_Mean_Field_Theory_and_Linear_Response_Correction\n   We present a new approximate learning algorithm for Boltzmann Machines, which is based on mean field theory and the linear response theorem. on mean field ......\n\nSearch: topological persistence activation function neural network TDA\nFound: 8 results\n\n1. Topological Data Analysis for Neural Network Analysis - arXiv\n   https://arxiv.org/html/2312.05840v1\n   This survey provides a comprehensive exploration of applications of Topological Data Analysis (TDA) within neural network analysis. Using TDA ......\n\n2. [PDF] Topological Data Analysis for Neural Network Analysis\n   https://www.ub.edu/topologia/casacuberta/articles/TDASurvey.pdf\n   Abstract. This article provides a comprehensive exploration of applications of Topological Data Anal- ysis (TDA) within neural network analysis....\n\n3. [PDF] Activation Landscapes as a Topological Summary of Neural ...\n   https://people.clas.ufl.edu/peterbubenik/files/Activation_Landscapes_as_a_Topological_Summary_of_Neural_Network_Performance.pdf\n   Abstract—We use topological data analysis (TDA) to study how data transforms as it passes through successive layers of a deep neural network (DNN)....\n\n4. Predicting the generalization gap in neural networks using ...\n   https://www.sciencedirect.com/science/article/pii/S0925231224005587\n   In this paper, we study the generalization gap of neural networks using methods from topological data analysis....\n\n5. Deep Topological Data Analysis - Emergent Mind\n   https://www.emergentmind.com/topics/deep-topological-data-analysis-tda\n   Deep TDA is a vital analytical tool for probing learned representations in neural networks. Persistent Homology on Activations: High-dimensional ......\n\n6. [PDF] Experimental Observations of the Topology of Convolutional Neural ...\n   https://www.sci.utah.edu/~beiwang/publications/AAAI_Activation_BeiWang_2023.pdf\n   Topological data analysis (TDA) is a branch of computa- tional mathematics, bridging algebraic topology and data sci- ence, that provides compact, noise-robust ......\n\n7. Topology of deep neural networks - OpenReview\n   https://openreview.net/forum?id=SkgBfaNKPr\n   We show that neural networks operate by changing topologly of a data set and explore how architectural choices effect this change....\n\n8. [PDF] Topology of Deep Neural Networks - CSI Math\n   https://www.math.csi.cuny.edu/~maher/teaching/2023/spring/tda/paper.pdf\n   With tanh activation, reduction in topological complexity is not only much slower but the network fails to reduce Ma to a topological disk, despite having ten ......\n\nSearch: maximum entropy activation function neural network information theory\nFound: 8 results\n\n1. Maximum entropy models provide functional connectivity estimates ...\n   https://www.nature.com/articles/s41598-022-13674-4\n   MaxEnt models provide a potentially powerful new tool to study functional connectivity in neuronal networks....\n\n2. Explosive neural networks via higher-order interactions in curved ...\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC12290047/\n   The maximum entropy principle (MEP) is a general modelling framework based on the principle of adopting the model with maximal entropy ......\n\n3. [PDF] An Information Theoretic Interpretation to Deep Neural Networks\n   https://sia.mit.edu/wp-content/uploads/2022/04/2022-xu-huang-zheng-wornell-entropy.pdf\n   Our investigation naturally leads to a performance metric for evaluating the effectiveness of extracted features, called the H-score, which il-....\n\n4. [PDF] Artificial Neural Networks and Information Theory - The Swiss Bay\n   https://theswissbay.ch/pdf/Gentoomen%20Library/Information%20Theory/Information%20Theory/Neural%20Networks%20And%20Information%20Theory%20-%20Colin%20Fyfe.pdf\n   use a probabilistic network with an nonlinear activation function designed to manage the effect of contextual information on the response of the network to ......\n\n5. Examining the Causal Structures of Deep Neural Networks Using ...\n   https://www.mdpi.com/1099-4300/22/12/1429\n   E I is defined as the mutual information between layer input and output following a maximum-entropy perturbation. We estimate E I first by uniformly subdividing ......\n\n6. [PDF] Optimization of Entropy with Neural Networks - Nic Schraudolph\n   https://nic.schraudolph.org/pubs/intro.pdf\n   This dissertation discusses and applies three methods for mak- ing density information accessible in a neural network: parametric modelling, probabilistic ......\n\n7. Module 3: Information Theory in Neural Networks - YouTube\n   https://www.youtube.com/watch?v=H1qmVoiZn8A\n   What is Activation function in Neural Network ? Types of Activation ... Arrogant Millionaire CEO's Daughter Mocks Judge Judy, Gets Maximum ......\n\n8. Information theory, and an introduction to chapters 4-6\n   http://www.op59.net/thesis/thesis.html\n   A very simple neural network learning rule is described which attempts to make the output of the network have maximum entropy, in accordance with the ideas ......\n\nSearch: implicit activation function neural network fixed point self-referential\nFound: 8 results\n\n1. Chapter 1: Introduction - Deep Implicit Layers\n   http://implicit-layers-tutorial.org/introduction/\n   We will provide you with the tools and background you need to apply implicit layers to a wide variety of problems and settings, with code examples throughout....\n\n2. Implicit Neural Representations with Periodic Activation Functions\n   https://www.reddit.com/r/MachineLearning/comments/hbo98a/r_siren_implicit_neural_representations_with/\n   Neural network activation functions are not basis functions. Even in a neural network with one hidden layer, the representation of a function ......\n\n3. Advancing the Understanding of Fixed Point Iterations in Deep ...\n   https://arxiv.org/html/2410.11279v1\n   In Section 5, We present case analysis results of fixed-point iterations for neural networks using two types of activation functions. In ......\n\n4. Implicit Neural Representations with Periodic Activation Functions\n   https://www.vincentsitzmann.com/siren/\n   We propose to leverage periodic activation functions for implicit neural representations and demonstrate that these networks, dubbed sinusoidal representation ......\n\n5. Implicit Neural Representations with Periodic Activation Functions\n   https://www.youtube.com/watch?v=Q2fLWGBeaiI\n   , current network architectures for such implicit neural ... representation networks or SIRENs, are ideally suited for representing complex ......\n\n6. SIRENs — Implicit Neural Representations with Periodic Activation ...\n   https://medium.com/@sallyrobotics.blog/sirens-implicit-neural-representations-with-periodic-activation-functions-f425c7f710fa\n   It is used to enable the network to learn non-linear relationships that exist in the dataset. Commonly used activation function include the ......\n\n7. [PDF] Implicit Layers for Implicit Representations - NIPS\n   https://papers.neurips.cc/paper/2021/file/4ffbd5c8221d7c147f8363ccdc9a2a37-Paper.pdf\n   In particular, we show that by exploiting fixed-point implicit layer to model implicit representations, we can substantially improve upon the performance of the....\n\n8. Neural nets with implicit layers - Dan MacKinlay\n   https://danmackinlay.name/notebook/nn_implicit.html\n   These are all networks where the layers are not explicit forward operators, but whose outputs are defined implicitly as the fixed point of some iteration, such ......\n\nSearch: optimal transport activation function neural network distribution matching\nFound: 8 results\n\n1. Distribution matching with discrete optimal transport flows\n   https://www.sciencedirect.com/science/article/pii/S2666990026000200\n   We propose a novel medical image-to-image translation method combining optimal transport (OT) with Normalizing Flows (NF). This extends NF's ability to ......\n\n2. Optimal and Diffusion Transports in Machine Learning - arXiv\n   https://arxiv.org/html/2512.06797v1\n   This includes sampling via diffusion methods, optimizing the weights of neural networks, and analyzing the evolution of token distributions ......\n\n3. [D] Optimal Transport for ML : r/MachineLearning - Reddit\n   https://www.reddit.com/r/MachineLearning/comments/1qufx6b/d_optimal_transport_for_ml/\n   Sinkhorn distances and entropic regularization are often a more approachable entry point since they show up directly in code and experiments....\n\n4. Optimal Transport Theory the New Math for Deep Learning - Medium\n   https://medium.com/intuitionmachine/optimal-transport-theory-the-new-math-for-deep-learning-2520395fc183\n   The key to understanding DL networks is through understand them as generative models and not as descriptive models. The difference is that ......\n\n5. Controlling Language and Diffusion Models by Transporting ...\n   https://machinelearning.apple.com/research/transporting-activations\n   AcT learns the Optimal Transport (OT) map between the source and target activation distributions. This ensures that an activation ......\n\n6. Efficient Neural Network Approaches for Conditional Optimal ...\n   https://epubs.siam.org/doi/10.1137/24M1678659\n   We present two neural network approaches that approximate the solutions of static and dynamic conditional optimal transport (COT) problems....\n\n7. [PDF] Learning to Match via Inverse Optimal Transport\n   https://jmlr.csail.mit.edu/papers/volume20/18-700/18-700.pdf\n   We propose a unified data-driven framework based on inverse optimal transport that can learn adaptive, nonlinear interaction cost function from noisy and ......\n\n8. Optimal-Transport Flow Matching - Emergent Mind\n   https://www.emergentmind.com/topics/optimal-transport-based-flow-matching\n   Optimal-Transport-Based Flow Matching is a computational framework that integrates optimal transport theory with continuous-time flow modeling, ......\n\n[1]   Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"implicit activation function neural network fixed point self-referential\" --max-results 8 2>&1\n[3]   Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"mean field theory activation function Ising Boltzmann neural network\" --max-results 8 2>&1\n[4]-  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"maximum entropy activation function neural network information theory\" --max-results 8 2>&1\n[5]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"topological persistence activation function neural network TDA\" --max-results 8 2>&1\n[2]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"optimal transport activation function neural network distribution matching\" --max-results 8 2>&1\n=== DONE ===", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [14] ASSISTANT · 2026-06-16 16:46:24 UTC

```
Let me search more specific directions to assess novelty carefully.
```

### [15] TOOL CALL — Bash · 2026-06-16 16:46:25 UTC

```
Search Lotka-Volterra, critical point, competitive exclusion activation directions:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "Lotka-Volterra competition equilibrium neural network activation sparse" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "critical point phase transition activation function neural network susceptibility" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "competitive exclusion lateral inhibition activation function deep learning sparse" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "implicit activation function deep learning 2024 forward equation" --max-results 8 2>&1 &
wait
echo "=== DONE ==="
```

### [16] TOOL RESULT — Bash · 2026-06-16 16:46:25 UTC

```
{"stdout": "Search: Lotka-Volterra competition equilibrium neural network activation sparse\nFound: 8 results\n\n1. Non-Gaussian Effects and Topological Multiple-Equilibria Phase\n   https://link.aps.org/doi/10.1103/8hrf-twxb\n   We study the equilibrium phases of a generalized Lotka-Volterra model characterized by a species interaction matrix which is random, sparse, ......\n\n2. Hybrid Physics-Informed Neural Network Correction of the Lotka ...\n   https://www.mdpi.com/2076-3417/15/22/12316\n   This study investigates a hybrid Lotka–Volterra population dynamics model augmented with a neural correction term, aiming to analyze how the strength of the ......\n\n3. Generalized Lotka-Volterra model with sparse interactions - arXiv\n   https://arxiv.org/html/2503.20887v1\n   We study the equilibrium phases of a generalized Lotka-Volterra model characterized by a species interaction matrix which is random, sparse and ......\n\n4. [PDF] Data Driven Modeling of Dynamics - OhioLINK ETD Center\n   https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1618835986278106&disposition=inline\n   The goal that we will take on is to introduce using deep neural networks, in particular residual networks, to discover underlying Lotka-Volterra equations using ......\n\n5. Lotka–Volterra equations - Wikipedia\n   https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations\n   The Lotka–Volterra equations, also known as the Lotka–Volterra predator–prey model, are a pair of first-order nonlinear differential equations...\n\n6. Feasibility of sparse large Lotka-Volterra ecosystems - ADS\n   https://ui.adsabs.harvard.edu/abs/arXiv:2111.11247\n   We address the question of feasibility of the foodweb, that is the existence of an equilibrium solution of the Lotka-Volterra system with no vanishing species....\n\n7. Approximate Message Passing for sparse matrices with application ...\n   https://www.sciencedirect.com/science/article/abs/pii/S030441492300248X\n   The Lotka–Volterra (LV) model is the standard model for studying the dynamical behavior of large dimensional ecological food chains. The second part of this ......\n\n8. ADS : Vol 2 : Chapter 7.2 : Competitive Lotka-Volterra Model\n   https://www.youtube.com/watch?v=ZMPpb-wG2G4\n   Let's turn to a 2-species competitive model in continuous time and see what kinds of equilibria we can find......\n\n[1]   Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"Lotka-Volterra competition equilibrium neural network activation sparse\" --max-results 8 2>&1\nSearch: critical point phase transition activation function neural network susceptibility\nFound: 8 results\n\n1. Susceptibility for extremely low external fluctuations and critical ...\n   https://link.aps.org/doi/10.1103/5l8g-w4cq\n   In this article, we study numerically and analytically the behavior of the susceptibility in a simple neuronal network model about a dynamical ......\n\n2. Competing nonlinearities, criticality, and order-to-chaos transition in ...\n   https://arxiv.org/html/2605.05294v1\n   The quenched activation disorder acts as a structural regularizer, suppressing memorization of corrupted labels while preserving generalization....\n\n3. DSLT 4. Phase Transitions in Neural Networks - LessWrong\n   https://www.lesswrong.com/posts/aKBAYN5LpaQMrPqMj/dslt-4-phase-transitions-in-neural-networks\n   At some critical value θ=θc, we recognise a phase transition as being a discontinuous change in the free energy or one of its derivatives, for ......\n\n4. [PDF] Susceptibility for extremely low external fluctuations and critical ...\n   http://www.famaf.unc.edu.ar/~cannas/papers/paper91.pdf\n   We consider the scaling behavior of the fluctuation susceptibility associated with the average activation in the Greenberg-Hastings neural ......\n\n5. Phase transitions and self-organized criticality in networks of ... - PMC\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC5098137/\n   We report analytic and computational results about phase transitions and self-organized criticality (SOC) in networks with general stochastic neurons. The ......\n\n6. [PDF] Thermodynamic Phase Transitions and Criticality in Dual-Mode ...\n   https://papers.ssrn.com/sol3/Delivery.cfm/7ae23049-ae01-47bb-8261-d99081279889-MECA.pdf?abstractid=6096180&mirid=1\n   While true thermodynamic phase transitions strictly occur in the limit N → ∞, observing systematic scal- ing of susceptibility peaks with system size confirms ......\n\n7. Data-driven detection of critical points of phase transitions ... - Nature\n   https://www.nature.com/articles/s42005-023-01429-0\n   We propose a giant-component-based DNB (GDNB) method inspired by the percolation theory, that directly selects the largest DNB as the transition core....\n\n8. [PDF] Phase Transitions in Neural Networks - Daniel Murfet\n   https://therisingsea.org/notes/MSc-Carroll.pdf\n   Given an analytic function K : W → R, x ∈ W is a critical point of K if ∇K(x) = 0, and if it further satisfies K(x) = 0 then it is a singularity ......\n\nSearch: implicit activation function deep learning 2024 forward equation\nFound: 8 results\n\n1. Implicit Neural Representations with Periodic Activation Functions\n   https://www.vincentsitzmann.com/siren/\n   We propose to leverage periodic activation functions for implicit neural representations and demonstrate that these networks, dubbed sinusoidal representation ......\n\n2. [PDF] Implicit Neural Representations with Periodic Activation Functions\n   https://proceedings.neurips.cc/paper_files/paper/2020/file/53c04118df112c13a8c34b38343b9c10-Paper.pdf\n   Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations....\n\n3. Implicit Neural Representations with Periodic Activation Functions\n   https://www.youtube.com/watch?v=Q2fLWGBeaiI\n   ... functions), the Poisson equation, and the Helmholtz and wave equations. ... Go to channel UofT CSC 2547 3D & Geometric Deep Learning · CSC2547 ......\n\n4. [PDF] reproducing activation function for deep learning\n   https://par.nsf.gov/servlets/purl/10515140\n   Abstract. We propose reproducing activation functions (RAFs) motivated by applied and com- putational harmonic analysis to improve deep learning accuracy ......\n\n5. Chapter 1: Introduction - Deep Implicit Layers\n   http://implicit-layers-tutorial.org/introduction/\n   We will provide you with the tools and background you need to apply implicit layers to a wide variety of problems and settings, with code examples throughout....\n\n6. Activation function - Wikipedia\n   https://en.wikipedia.org/wiki/Activation_function\n   In artificial neural networks, the activation function of a node is a function that calculates the output of the node based on its individual inputs and ......\n\n7. [R] [1802.00168] Deep Learning with Data Dependent Implicit ...\n   https://www.reddit.com/r/MachineLearning/comments/7uri4p/r_180200168_deep_learning_with_data_dependent/\n   Interpreting the propagation though a NN as solving process of a transport equation and the move from one layer to the next as a Euler step, ......\n\n8. STAF: Sinusoidal Trainable Activation Functions for Implicit Neural ...\n   https://arxiv.org/html/2502.00869v1\n   We introduce Sinusoidal Trainable Activation Functions (STAF), designed to directly tackle this limitation by enabling networks to adaptively learn and ......\n\n[2]   Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"critical point phase transition activation function neural network susceptibility\" --max-results 8 2>&1\nSearch: competitive exclusion lateral inhibition activation function deep learning sparse\nFound: 8 results\n\n1. Learning Winner-take-all Competition Between Groups of Neurons ...\n   https://papers.nips.cc/paper/1829-learning-winner-take-all-competition-between-groups-of-neurons-in-lateral-inhibitory-networks\n   Here we show how to organize lateral inhibition so that groups of neurons compete to be active. Given a collection of poten(cid:173) tially overlapping groups, ......\n\n2. Training Deep Normalization-Free Spiking Neural Networks with ...\n   https://arxiv.org/html/2509.23253v1\n   To resolve this conflict, we propose a normalization-free learning framework that incorporates lateral inhibition inspired by cortical circuits....\n\n3. How does Lateral Inhibition Provide Competition among Neurons?\n   https://ai.stackexchange.com/questions/22207/how-does-lateral-inhibition-provide-competition-among-neurons\n   The NxN layer is connected 1 on 1 to an NxN layer of inhibitory neurons. These neurons inhibit all other neurons except the one they are ......\n\n4. [PDF] Structured sparse coding via lateral inhibition - Yann LeCun\n   http://yann.lecun.com/exdb/publis/pdf/gregor-nips-11.pdf\n   This work describes a conceptually simple method for structured sparse coding and dictionary design. Supposing a dictionary with K atoms, we introduce a....\n\n5. [PDF] Pre-integration lateral inhibition enhances unsupervised learning\n   https://web-archive.southampton.ac.uk/cogprints.org/2380/1/neurocomp.pdf\n   Lateral inhibition provides competition by enabling nodes to inhibit each other from generating a response. This form of competition is used in numerous neural ......\n\n6. Competitive Perceptrons: The Relevance of Modeling New ... - PMC\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC10741702/\n   Competitive Learning by Lateral Inhibition. Competitive learning is a form of unsupervised learning in artificial neural networks in which nodes compete for ......\n\n7. [PDF] Lateral Inhibition Underlying Suppression of Neuronal Activity and ...\n   https://www.joig.net/uploadfile/2015/0911/20150911041629754.pdf\n   In previous studies, we showed that lateral inhibition serves to decrease firing rates in neurons to the level corresponding to the best....\n\n8. Suppression helps: Lateral Inhibition-inspired Convolutional Neural...\n   https://openreview.net/forum?id=N3kGYG3ZcTi\n   In this paper, we explicitly explore the filter dimension in the lateral direction and propose our lateral inhibition-inspired (LI) design....\n\n[3]-  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"competitive exclusion lateral inhibition activation function deep learning sparse\" --max-results 8 2>&1\n[4]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"implicit activation function deep learning 2024 forward equation\" --max-results 8 2>&1\n=== DONE ===", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [17] ASSISTANT · 2026-06-16 16:48:57 UTC

```
Let me now do deeper searches on the most promising directions.
```

### [18] TOOL CALL — Bash · 2026-06-16 16:48:57 UTC

```
Search QP activation, Curie-Weiss activation, ecological sparse, KAN comparison:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "quadratic programming activation function neural network linear complementarity" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "Curie-Weiss self-consistency equation activation function learnable criticality" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "ecological niche competitive exclusion sparse activation deep learning" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "KAN kolmogorov arnold network activation 2024 beyond spline" --max-results 8 2>&1 &
wait
echo "=== DONE ==="
```

### [19] TOOL RESULT — Bash · 2026-06-16 16:48:57 UTC

```
{"stdout": "Search: KAN kolmogorov arnold network activation 2024 beyond spline\nFound: 8 results\n\n1. [2404.19756] KAN: Kolmogorov-Arnold Networks - arXiv\n   https://arxiv.org/abs/2404.19756\n   KANs have learnable activation functions on edges (\"weights\"). KANs have no linear weights at all -- every weight parameter is replaced by a ......\n\n2. KAN: Kolmogorov–Arnold Networks - OpenReview\n   https://openreview.net/forum?id=Ozo7qJ5vZi\n   KANs replace the fixed activation functions on nodes in MLPs with learnable activation functions on edges, represented by B-splines....\n\n3. Trying Kolmogorov-Arnold Networks in Practice - Casey Primozic\n   https://cprimozic.net/blog/trying-out-kans/\n   KANs move the majority of the learnable parameters into the nodes/activation functions themselves. B-Splines. The usual choice of learnable ......\n\n4. KAN: Kolmogorov-Arnold Networks - YouTube\n   https://www.youtube.com/watch?v=sJe5wxJxLJ0\n   ... activation functions on ... Kan: Kolmogorov-arnold networks.\" arXiv preprint arXiv:2404.19756 (2024)....\n\n5. The Annotated Kolmogorov-Arnold Network (KAN) | Alex L. Zhang\n   https://alexzhang13.github.io/blog/2024/annotated-kan/\n   Kolmogorov-Arnold Networks (KANs) are an alternative representation to standard multi-layer perceptrons (MLPs)....\n\n6. KAN: Kolmogorov–Arnold Networks — A Short Summary - Medium\n   https://medium.com/pythons-gurus/kan-kolmogorov-arnold-networks-a-short-summary-a1aef1336990\n   KANs employ learnable activation functions on edges (“weights”), are less accurate than splines in low dimensions due to their inability to ......\n\n7. SineKAN: Kolmogorov-Arnold Networks using sinusoidal activation ...\n   https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1462952/full\n   In this work, we will use an efficient implementation of the KAN with learnable B-Spline activation functions (B-SplineKAN) (Cao, 2024 ) ......\n\n8. Kolmogorov-Arnold Networks (KANs): Towards Interpretable and ...\n   https://www.researchgate.net/publication/397495156_Kolmogorov-Arnold_Networks_KANs_Towards_Interpretable_and_Efficient_Function_Approximation_Beyond_MLPs\n   KANs utilize learnable activation functions parameterized as splines on network edges. This fundamental architectural change eliminates the ......\n\nSearch: ecological niche competitive exclusion sparse activation deep learning\nFound: 8 results\n\n1. Introduction to deep learning methods for multi‐species predictions\n   https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.14466\n   Species distribution models (SDMs), also known as ecological niche models or habitat suitability models (Guisan & Thuiller, 2005), are ......\n\n2. Algorithms going wild – A review of machine learning techniques for ...\n   https://www.sciencedirect.com/science/article/pii/S0304380025001498\n   This review critically analyzes and synthesizes the application of machine learning and deep learning in terrestrial ecology....\n\n3. Effects of niche overlap on coexistence, fixation and invasion in a ...\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC7062080/\n   One common theory, known as the Gause's rule or the competitive exclusion principle, postulates that due to abiotic constraints, resource usage, inter-species ......\n\n4. Convolutional neural networks outperform other presence ... - PNAS\n   https://www.pnas.org/doi/10.1073/pnas.2514886123\n   In contrast, CNNs maintained strong performance even for species with less than thirty presence points, highlighting their robustness when data are sparse....\n\n5. The challenge of modeling niches and distributions for data‐poor ...\n   https://www.ecography.org/blog/challenge-modeling-niches-and-distributions-data-poor-species\n   A species' niche is characterized by the biotic and abiotic factors that influence the conditions and places that the species can occupy....\n\n6. [PDF] Deep Learning in Ecology: Data-driven Methods for Ecosystem ...\n   https://osf.io/download/bnm5w\n   In this project I apply deep learning methods to the problem of missing link prediction in ecological networks, and I investigate methods to extract ecological....\n\n7. Sparling: End-to-End Spatial Concept Learning via Extremely Sparse...\n   https://openreview.net/forum?id=yfBs0GQxx9\n   Real-world processes often contain intermediate state that can be modeled as an extremely sparse activation tensor....\n\n8. Machine Learning | Publications - NEC Labs America\n   https://www.nec-labs.com/research/machine-learning/publications/\n   We introduce a framework to analyse interpretability in deep learning, by drawing on a formal notion of model semantics from the philosophy of science. We argue ......\n\nSearch: Curie-Weiss self-consistency equation activation function learnable criticality\nFound: 8 results\n\n1. [PDF] 2 The Curie–Weiss Model\n   https://www.unige.ch/~velenik/smbook/Curie-Weiss_Model.pdf\n   The value T = Tc corresponds to the critical regime. The Curie–Weiss model possesses a remarkable feature, for this approximation to be self-consistent, this ......\n\n2. Lee-Yang theory of the Curie-Weiss model and its rare fluctuations\n   https://link.aps.org/doi/10.1103/PhysRevResearch.2.033009\n   Curie-Weiss model, including its scaling behavior close to criticality and the large-deviation statistics of the rare fluctuations of the ......\n\n3. [1301.6911] A Curie-Weiss model of self-organized criticality - arXiv\n   https://arxiv.org/abs/1301.6911\n   Abstract:We try to design a simple model exhibiting self-organized criticality, which is amenable to a rigorous mathematical analysis....\n\n4. Self-consistency transcendental equation for Curie-Weiss model\n   https://math.stackexchange.com/questions/1599344/self-consistency-transcendental-equation-for-curie-weiss-model\n   In physics, the ferromagnetic Curie-Weiss spin model leads to a transcendental self-consistency equation for the magnetization m of the form m= ......\n\n5. [PDF] Nonlinear Self-Consistency Equation in Statistical Mechanics\n   https://ansne.du.ac.ir/article_2013_6481d6904c43ead310e98e86e0ec585f.pdf\n   This equation encodes how the average local magnetization responds to its own feedback meanfield selfconsistency equation captures qualitative ......\n\n6. Tutorial: a beginner's guide to interpreting magnetic susceptibility ...\n   https://www.nature.com/articles/s42005-022-00853-y\n   In this tutorial, we provide a guide to the interpretation of magnetic susceptibility data with a special emphasis on the Curie–Weiss law, a simple but ......\n\n7. [PDF] A Curie–Weiss model of self-organized criticality - HAL\n   https://hal.science/hal-03827291/document\n   Abstract. We try to design a simple model exhibiting self-organized criticality, which is amenable to a rigorous mathematical analysis....\n\n8. Dataset-Learning Duality and Emergent Criticality - PMC\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC12468801/\n   In artificial neural networks, the activation dynamics of non-trainable variables are strongly coupled to the learning dynamics of trainable variables....\n\nSearch: quadratic programming activation function neural network linear complementarity\nFound: 8 results\n\n1. A meta-interactive neural network for solving time-varying quadratic ...\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC12638829/\n   This study introduces MINN, a meta-interactive neural network that leverages coupled neuron topologies and flexible activation functions to ......\n\n2. Why is it that Neural Networks can represent complex formula?\n   https://www.reddit.com/r/MLQuestions/comments/buq4cb/why_is_it_that_neural_networks_can_represent/\n   A linear activate function would essentially be a matrix multiplication, in which case having multiple layers in your network would be the same ......\n\n3. Neural network models and its application for solving linear and ...\n   https://www.researchgate.net/publication/222657502_Neural_network_models_and_its_application_for_solving_linear_and_quadratic_programming_problems\n   In this paper we consider two recurrent neural network model for solving linear and quadratic programming problems. The first model is derived from an ......\n\n4. Activation Functions in Neural Networks - GeeksforGeeks\n   https://www.geeksforgeeks.org/machine-learning/activation-functions-neural-networks/\n   An activation function is applied to the weighted sum of inputs before producing the final output of a neuron. It introduces non-linearity, ......\n\n5. Neural network models for time-varying tensor complementarity ...\n   https://www.sciencedirect.com/science/article/abs/pii/S0925231222015120\n   Some neural networks for solving time-varying tensor inverse and TVTCP under the t-product are proposed and corresponding convergence are studied....\n\n6. Why Do We Need Activation Functions in Neural Networks? - YouTube\n   https://www.youtube.com/watch?v=DaixewJTF8k\n   In this video, we learn why we need activation functions in neural networks. ◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾◾ Programming Books & Merch The Python ......\n\n7. [PDF] Training of Perceptron Neural Network Using Peacewise Linear ...\n   http://jae.ece.ntua.gr/current/Volume13Number1June2011/paper%202%20Barbarosou.pdf\n   A new Perceptron training algorithm is presented, which employs the piecewise linear activation function and the sum of squared differences error function over ......\n\n8. Neural Networks with Quadratic Layers | by Anna Alexandra Grigoryan\n   https://thegrigorian.medium.com/capturing-non-linear-relationships-with-quadratic-layers-55e9f0f5d006\n   Activation functions like ReLU, sigmoid, or tanh introduce the element of transformation. They decide whether a neuron should fire or remain ......\n\n[1]   Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"quadratic programming activation function neural network linear complementarity\" --max-results 8 2>&1\n[2]   Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"Curie-Weiss self-consistency equation activation function learnable criticality\" --max-results 8 2>&1\n[3]-  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"ecological niche competitive exclusion sparse activation deep learning\" --max-results 8 2>&1\n[4]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"KAN kolmogorov arnold network activation 2024 beyond spline\" --max-results 8 2>&1\n=== DONE ===", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [20] ASSISTANT · 2026-06-16 16:50:28 UTC

```
Let me do one final targeted novelty check on the most promising direction before writing the hypothesis.
```

### [21] TOOL CALL — Bash · 2026-06-16 16:50:28 UTC

```
Final novelty verification for Curie-Weiss mean-field activation:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "mean-field activation coupled neurons shared magnetization order parameter deep learning" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "Ising activation function mean field neural network layer coupling" --max-results 8 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "self-consistent field neural network activation coupled fixed point single layer" --max-results 8 2>&1 &
wait
echo "=== DONE ==="
```

### [22] TOOL RESULT — Bash · 2026-06-16 16:50:28 UTC

```
{"stdout": "Search: Ising activation function mean field neural network layer coupling\nFound: 8 results\n\n1. Correspondence Between Ising Machines and Neural Networks\n   https://arxiv.org/html/2511.00746v1\n   Expressed in mean field equations, the network is mapped to an Ising ... neural network activation function because of its role in mean-field spin ......\n\n2. [PDF] Mean Field Theory and its application to deep learning - Mimee Xu\n   https://mimee.xyz/meanfield.pdf\n   We thus replace each pre-activation with Gaussian random variables pre- activation, whose coupling can be ignored. This leads to a formulation of mean field ......\n\n3. Beyond NTK: A Mean-Field Analysis of Neural Networks ... - YouTube\n   https://www.youtube.com/watch?v=vowUd1mR6a0\n   Tengyu Ma (Stanford University) https://simons.berkeley.edu/talks/tengyu-ma-stanford-university-2023-11-27 Optimization and Algorithm ......\n\n4. A simple mean field model of feature learning - OpenReview\n   https://openreview.net/forum?id=FVQzqSIJcC\n   The paper proposes a Mean-Field Automatic Relevance Determination (MF-ARD) framework for two-layer Bayesian neural networks trained with SGLD. The goal is to ......\n\n5. Activation Functions and Models of Magnets | Dalton A R Sakthivadivel\n   https://darsakthi.github.io/posts/2021/02/act-func/\n   One way of modelling the dynamics of the Ising model is by mean field theory (MFT), which looks at the 'average' dynamics of a system. The way ......\n\n6. Mean Field Langevin Dynamics, Mean Field Neural Networks, and ...\n   https://scholarsbank.uoregon.edu/items/5a766d8f-ba4b-41ac-a770-a73b13a7ba9f\n   We present three interconnected contributions that advance our understanding of Markov chain mixing, mean field optimization, and neural network ......\n\n7. [PDF] A Mean-Field Theory of Training Deep Neural Networks | CS231n\n   https://cs231n.stanford.edu/2024/papers/a-mean-field-theory-of-training-deep-neural-networks.pdf\n   In this paper, more activation functions than simply tanh are explored, but this paper still only focuses on the most basic deep neu- ral networks with only ......\n\n8. [PDF] Formalizing the Use of the Activation Function in Neural Inference\n   https://content.wolfram.com/sites/13/2022/12/31-4-4.pdf\n   We investigate how the activation function can be used to describe neu- ral firing in an abstract way, and in turn, why it works well in artificial neural ......\n\nSearch: mean-field activation coupled neurons shared magnetization order parameter deep learning\nFound: 8 results\n\n1. Mean Field Approaches to Learning Dynamics in Deep Networks\n   https://www.youtube.com/watch?v=XZyFwz5_vro\n   The result of this analysis is a dynamical mean field theory (DMFT) where all neurons obey independent stochastic single site dynamics....\n\n2. Effective theory of collective deep learning | Phys. Rev. Research\n   https://link.aps.org/doi/10.1103/PhysRevResearch.6.L042040\n   Collective learning in coupled neural networks: (a) Small mean-field network of N = 4 coupled neural units trained on private data classes ......\n\n3. [PDF] Mean Field Theory and its application to deep learning - Mimee Xu\n   https://mimee.xyz/meanfield.pdf\n   MFT highlights the dynamical system similarities between a deep network's parameters and interacting particles. applied to magnetization,...\n\n4. Mean field theory: from physics to deep neural nets | Ro's blog\n   https://rojefferson.blog/2020/06/13/mean-field-theory-from-physics-to-deep-neural-nets/\n   For this reason, the magnetization {s} is an example of an order parameter, since it parametrizes which “order” — that is, which phase — we ......\n\n5. Parameter and hidden-state inference in mean-field models ... - arXiv\n   https://arxiv.org/html/2602.09535v1\n   The neurons interact with each other via an excitatory mean-field coupling. combining deep learning with SINDy enables the identification of interpretable low- ......\n\n6. Model-agnostic neural mean field with a data-driven transfer function\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC11413991/\n   This paper derives a mean-field model by fitting a transfer function called Refractory SoftPlus, which is simple yet applicable to a broad variety of neuron ......\n\n7. Mean-Field Theory of Two-Layers Neural Networks - YouTube\n   https://www.youtube.com/watch?v=BMnxZaFeWNA\n   Share. Save. Report. Comments. Add a comment... ... Is Bigger Better for Bayesian Deep Learning? UCL Centre for ......\n\n8. [PDF] A Mean-Field Theory of Training Deep Neural Networks | CS231n\n   https://cs231n.stanford.edu/2024/papers/a-mean-field-theory-of-training-deep-neural-networks.pdf\n   First, we present a theoretical mean-field framework to study the depth scales of a fully- connected neural network as a function of the architecture....\n\n[1]   Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"mean-field activation coupled neurons shared magnetization order parameter deep learning\" --max-results 8 2>&1\n[2]-  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"Ising activation function mean field neural network layer coupling\" --max-results 8 2>&1\nSearch: self-consistent field neural network activation coupled fixed point single layer\nFound: 8 results\n\n1. Deep learning and inverse discovery of polymer self-consistent field ...\n   https://link.aps.org/doi/10.1103/PhysRevE.106.014503\n   We devise a deep learning solver inspired by physics-informed neural networks (PINNs) to tackle the polymer self-consistent field theory (SCFT) equations....\n\n2. Self-consistent determination of long-range electrostatics in neural ...\n   https://www.nature.com/articles/s41467-022-29243-2\n   A general approach for learning the long-range response of molecular systems in neural network potentials that relies on a physically meaningful separation of ......\n\n3. [PDF] Deep Learning and Self-Consistent Field Theory - UCSB Math\n   https://web.math.ucsb.edu/~hdc/public/Deep_Learning_and_Self_Consistent_Field_Theory__A_Path_Towards_Accelerating.pdf\n   A new framework that leverages data obtained from self-consistent field theory. (SCFT) simulations with deep learning to accelerate the exploration of parameter ......\n\n4. Neural network self-consistent fields for density functional theory\n   https://www.researchgate.net/publication/381668817_NeuralSCF_Neural_network_self-consistent_fields_for_density_functional_theory\n   We propose a neural network self-consistent fields (NeuralSCF) framework that establishes the Kohn-Sham density map as a deep learning objective ......\n\n5. Project: Single Layer Neural Network - rob-mcculloch.org\n   https://rob-mcculloch.org/2025_cs/webpage/projects/csproject_single-layer.html\n   Single Layer Model. Let's consider the single layer neural network model for predicting a single numeric Y. Let X=(X1,X2,…,Xp) be our vector ......\n\n6. NeuralSCF: Neural network self-consistent fields for density ... - arXiv\n   https://arxiv.org/html/2406.15873v1\n   We propose a neural network self-consistent fields (NeuralSCF) framework that establishes the Kohn-Sham density map as a deep learning objective....\n\n7. Single-Layer Neural Networks - Machine Learning 101 (Part 10)\n   https://www.youtube.com/watch?v=ZLhjo3Jz2_Q\n   In this video, we introduce single-layer neural networks. We provide the terminology of the architecture; nodes, input layer, hidden layers, ......\n\n8. Residual-based physics-informed neural network modelling for ...\n   https://www.sciencedirect.com/science/article/pii/S2666546826000613\n   In this study, a residual-based physics-informed neural network (RPM) was developed to predict multi-physical fields under steady state in the hydrogen-side GDL ......\n\n[3]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"self-consistent field neural network activation coupled fixed point single layer\" --max-results 8 2>&1\n=== DONE ===", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [23] ASSISTANT · 2026-06-16 16:50:38 UTC

```
Found critical potential overlap. Let me fetch and read these closely before proceeding.
```

### [24] TOOL CALL — Bash · 2026-06-16 16:50:38 UTC

```
Fetch activation-magnets blog and Ising-NN correspondence paper:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://darsakthi.github.io/posts/2021/02/act-func/" --max-chars 8000 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2511.00746" --max-chars 6000 2>&1 &
wait
echo "=== DONE ==="
```

### [25] TOOL RESULT — Bash · 2026-06-16 16:50:38 UTC

```
{"stdout": "URL: https://arxiv.org/abs/2511.00746\nType: HTML\nLength: 7616 chars (truncated)\n\n--- Content ---\n\nSkip to main content\n\n[](https://www.cornell.edu/)\n\n[Learn about arXiv becoming an independent nonprofit.](https://tech.cornell.edu/arxiv/)\n\nWe gratefully acknowledge support from the Simons Foundation, [member institutions](https://info.arxiv.org/about/ourmembers.html), and all contributors. [Donate](https://info.arxiv.org/about/donate.html)\n\n[](/IgnoreMe)\n\n[](/) > [cond-mat](/list/cond-mat/recent) > arXiv:2511.00746 \n\n[Help](https://info.arxiv.org/help) | [Advanced Search](https://arxiv.org/search/advanced)\n\nAll fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text\n\nSearch\n\n[](https://arxiv.org/)\n\n[ ](https://www.cornell.edu/)\n\nGO\n\n## quick links\n\n  * [Login](https://arxiv.org/login)\n  * [Help Pages](https://info.arxiv.org/help)\n  * [About](https://info.arxiv.org/about)\n\n\n\n# Condensed Matter > Disordered Systems and Neural Networks\n\n**arXiv:2511.00746** (cond-mat) \n\n[Submitted on 2 Nov 2025]\n\n# Title:Correspondence Between Ising Machines and Neural Networks\n\nAuthors:[Andrew G. Moore](https://arxiv.org/search/cond-mat?searchtype=author&query=Moore,+A+G)\n\nView a PDF of the paper titled Correspondence Between Ising Machines and Neural Networks, by Andrew G. Moore\n\n[View PDF](/pdf/2511.00746) [HTML (experimental)](https://arxiv.org/html/2511.00746v1)\n\n> Abstract:Computation with the Ising model is central to future computing technologies like quantum annealing, adiabatic quantum computing, and thermodynamic classical computing. Traditionally, computed values have been equated with ground states. This paper generalizes computation with ground states to computation with spin averages, allowing computations to take place at high temperatures. It then introduces a systematic correspondence between Ising devices and neural networks and a simple method to run trained feed-forward neural networks on Ising-type hardware. Finally, a mathematical proof is offered that these implementations are always successful. \n\nComments: | 22 pages, 4 figures  \n---|---  \nSubjects: |  Disordered Systems and Neural Networks (cond-mat.dis-nn); Emerging Technologies (cs.ET); Machine Learning (cs.LG); Quantum Physics (quant-ph)  \nCite as: | [arXiv:2511.00746](https://arxiv.org/abs/2511.00746) [cond-mat.dis-nn]  \n  | (or  [arXiv:2511.00746v1](https://arxiv.org/abs/2511.00746v1) [cond-mat.dis-nn] for this version)   \n  |  <https://doi.org/10.48550/arXiv.2511.00746> Focus to learn more arXiv-issued DOI via DataCite  \n  \n## Submission history\n\nFrom: Andrew Moore [[view email](/show-email/a5b618ed/2511.00746)]   \n**[v1]** Sun, 2 Nov 2025 00:13:57 UTC (547 KB)  \n\n\nFull-text links:\n\n## Access Paper:\n\nView a PDF of the paper titled Correspondence Between Ising Machines and Neural Networks, by Andrew G. Moore\n\n  * [View PDF](/pdf/2511.00746)\n  * [HTML (experimental)](https://arxiv.org/html/2511.00746v1)\n  * [TeX Source ](/src/2511.00746)\n\n\n\n[ view license ](http://creativecommons.org/licenses/by/4.0/ \"Rights to this article\")\n\n### Current browse context:\n\ncond-mat.dis-nn\n\n[< prev](/prevnext?id=2511.00746&function=prev&context=cond-mat.dis-nn \"previous in cond-mat.dis-nn \\(accesskey p\\)\")   |   [next >](/prevnext?id=2511.00746&function=next&context=cond-mat.dis-nn \"next in cond-mat.dis-nn \\(accesskey n\\)\")   \n\n\n[new](/list/cond-mat.dis-nn/new) |  [recent](/list/cond-mat.dis-nn/recent) | [2025-11](/list/cond-mat.dis-nn/2025-11)\n\nChange to browse by: \n\n[cond-mat](/abs/2511.00746?context=cond-mat)  \n[cs](/abs/2511.00746?context=cs)  \n[cs.ET](/abs/2511.00746?context=cs.ET)  \n[cs.LG](/abs/2511.00746?context=cs.LG)  \n[quant-ph](/abs/2511.00746?context=quant-ph)  \n\n\n### References & Citations\n\n  * [INSPIRE HEP](https://inspirehep.net/arxiv/2511.00746)  \n\n  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2511.00746)\n  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2511.00746)\n  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2511.00746)\n\n\n\nexport BibTeX citation Loading...\n\n## BibTeX formatted citation\n\n×\n\nloading...\n\nData provided by: \n\n### Bookmark\n\n[ ](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2511.00746&description=Correspondence Between Ising Machines and Neural Networks \"Bookmark on BibSonomy\") [ ](https://reddit.com/submit?url=https://arxiv.org/abs/2511.00746&title=Correspondence Between Ising Machines and Neural Networks \"Bookmark on Reddit\")\n\nBibliographic Tools\n\n# Bibliographic and Citation Tools\n\nBibliographic Explorer Toggle\n\nBibliographic Explorer _([What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))_\n\nConnected Papers Toggle\n\nConnected Papers _([What is Connected Papers?](https://www.connectedpapers.com/about))_\n\nLitmaps Toggle\n\nLitmaps _([What is Litmaps?](https://www.litmaps.co/))_\n\nscite.ai Toggle\n\nscite Smart Citations _([What are Smart Citations?](https://www.scite.ai/))_\n\nCode, Data, Media\n\n# Code, Data and Media Associated with this Article\n\nalphaXiv Toggle\n\nalphaXiv _([What is alphaXiv?](https://alphaxiv.org/))_\n\nLinks to Code Toggle\n\nCatalyzeX Code Finder for Papers _([What is CatalyzeX?](https://www.catalyzex.com))_\n\nDagsHub Toggle\n\nDagsHub _([What is DagsHub?](https://dagshub.com/))_\n\nGotitPub Toggle\n\nGotit.pub _([What is GotitPub?](http://gotit.pub/faq))_\n\nHuggingface Toggle\n\nHugging Face _([What is Huggingface?](https://huggingface.co/huggingface))_\n\nScienceCast Toggle\n\nScienceCast _([What is ScienceCast?](https://sciencecast.org/welcome))_\n\nDemos\n\n# Demos\n\nReplicate Toggle\n\nReplicate _([What is Replicate?](https://replicate.com/docs/arxiv/about))_\n\nSpaces Toggle\n\nHugging Face Spaces _([What is Spaces?](https://huggingface.co/docs/hub/spaces))_\n\nSpaces Toggle\n\nTXYZ.AI _([What is TXYZ.AI?](https://txyz.ai))_\n\nRelated Papers\n\n# Recommenders and Search Tools\n\nLink to Influence Flower\n\nInfluence Flower _([What are Influence Flowers?](https://influencemap.cmlab.dev/))_\n\nCore re\nURL: https://darsakthi.github.io/posts/2021/02/act-func/\nType: HTML\nLength: 9465 chars (truncated)\n\n--- Content ---\n\n[Home](/)\n\n[Research](/research/)[Talks](/talks.html)[Teaching](/teaching.html)[Texts and Lecture Notes](/texts.html)[Posts](/blog.html)\n\n# Activation Functions and Models of Magnets\n\n02 Feb 2021 \n\nAs stated on the home page of this website, I’m going to start writing the occasional blog post about my work. At the time of writing, I had resisted the temptation for a while, but I think it would be nice to post about specific things (e.g. papers) every once in a while; since publishing in pure mathematics really is once in a while, it seems like it won’t be too much to keep on top of. This inaugural post concerns a paper that I preprinted some time ago, which discusses the activation function in neural networks. The work in question can be found here: [Formalising the Use of the Activation Function in Neural Inference](https://arxiv.org/abs/2102.04896).\n\nAs someone who does occasional work on statistical mechanics I am quite familiar with the Ising model, and with _universality_. Universality refers to the fact that certain classes of phase transition, which are nothing but changes in the characteristics of an object (such as changing from a solid to a liquid to a gas), share key dynamical features. In this sense, a model that exhibits a phase transition can be used to model certain other systems faithfully, even if they are quite different. Universality is explained well in [David Tong’s notes on statistical field theory](https://www.damtp.cam.ac.uk/user/tong/sft.html), and in John Cardy’s _Scaling and Renormalisation in Statistical Physics_. There are some interesting references in [this tweet](https://twitter.com/stevenstrogatz/status/1392958445624696838) too, and [this response](https://twitter.com/nigelgoldenfeld/status/1394443499924230145) to that tweet discusses the same thing that is covered in chapter three of Tong’s notes.\n\nIn the course of working on something else, I came across an interesting case of the Ising universality class as a kind of toy model of a neural network. This paper discusses exactly this, and I read it as motivating the activation function ML people are familiar with beyond ‘it works.’ This is something like my broader research mission, formulating complex system theories like ML or neuroscience axiomatically, so I thought it was worth writing up. In that sense, hopefully it goes beyond the curiosity of ‘a neural net looks a bit like an Ising model; isn’t that clever.’\n\nThe way a simple neurone might be claimed to work is by the following essential anatomy of an action potential: the resting potential is slightly below ionic equilibrium, creating a concentration gradient of positive ions diffusing across the cell membrane. The way the neurone keeps the membrane potential low is by pumping these ions out as they diffuse in. When the voltage of the neural cell rises to a critical point, sensors in the neurone ‘un-gate’ the closed channels that prohibit mass diffusion and close the pumps getting rid of these ions, and positive ions flood the cell, going past even the equilibrium point. This is the characteristic spike in membrane potential that we read as an action potential, and foregoing some dynamical details about how exactly this model would work, it is sufficient to describe an action potential. We’ll hold on to this thought for now, and lay out the necessary physics; then we’ll revisit this model.\n\nThe Ising model, on the other hand, is a model of the electronic structure of a magnet. It is a lattice of atoms and their electrons, the latter of which possess a quantity called ‘spin’ from quantum mechanics. It isn’t important what spin is—and it probably doesn’t really have an intuitive explanation—other than to say that it points ‘up’ or ‘down.’ When all spins are aligned in one such direction, the metal has a magnetic moment from this alignment. The Ising model exhibits a phase transition wherein when the metal is heated, the energy added from the heat causes these electrons to start flipping their spins, just like molecules in a solid vibrating at high speeds when heated. This disorders the configuration of the lattice, and zeroes the magnetic moment \\\\(m\\\\). The contrapositive also holds: when the magnet is cooled once more, past a critical point \\\\(m\\\\) goes to one again. This is like a liquid solidifying below zero centigrade.\n\nOne way of modelling the dynamics of the Ising model is by mean field theory (MFT), which looks at the ‘average’ dynamics of a system. The way we do MFT is by approximating the system with a simpler system that is related in some way to the original (specifically, we use a trial Hamiltonian for which the free energy is bounded from below by the Bogoliubov inequality). The typical way in which this is done, and in some sense the most meaningful, is by replacing the system with a ‘mean field’ and ignoring fluctuations in the dynamics of smaller items constituting the system. MFT is thus a theory of mean fields, ignoring the fluctuations around a mean (consider the transport relation \\\\(\\delta A(t) = A(t) - \\langle A \\rangle\\\\) for the dynamics of an observable \\\\(A\\\\) in the presence of fluctuations. When we ignore fluctuations and the term \\\\(\\delta A(t)\\\\) vanishes, we have \\\\(A(t) = \\langle A \\rangle\\\\)). It is also a multiscale modelling method, if these fluctuations are due to the dynamics of smaller things in a large system, and the mean field is representative of the dynamics of the larger things. In this sense MFT is not just a clever approximation—not in my view, anyway—but has some extra ontological importance as a method of understanding a system’s dynamics at multiple scales.\n\nIn Section IIC, we do exactly this, derive a mean field model for the Ising model. It’s nothing new, I just go through it for the purpose of the paper. I actually use a short cut that neglects fluctuations, rather than performing the full formal derivation. This is, in fact, the same as the formal procedure—neglecting fluctuations produces a simpler trial Hamiltonian, for which the free energy is strictly greater than the real one, which we minimise with respect to a control parameter based on what we know of the Bogoliubov inequality. Again, it’s nothing but a short cut.\n\nRevisiting the model we discussed earlier, in Sections IIA and IIB we discuss the similarities between the Ising lattice and the network of channels in the cell membrane, with a spin equivalent to a channel containing a diffusing ion (\\\\(+1\\\\)) or not (\\\\(-1\\\\)). We consider the Ising model in a hot environment with an occasional quench applied, to model the effect of an external stimulus being applied that cools the lattice. In the neural case, this is a cell body in a disordered environment—some channels closed and some open—which occasionally is quenched and cooled below the critical temperature. When this cooling happens, all the channels open, the analogous Ising model is positively magnetised, and as the magnetic moment goes to one, we have an action potential. When the quench is removed, the neurone ‘heats up’ again, and the channels close just as spins get disordered.\n\nThe key feature of this phase transition is, if we claim a neurone is in the Ising universality class, and the indicated magnetisation function (Figure 1 in the paper) arises from a mean field model of the Ising model, then the typical sigmoidal activation function is a mean field model of a real neurone. Correspondingly, if we think of real neurones as the thing to aspire to in building artificial neural networks—indeed, human brains are the best learners that we know of—then this explains why the sigmoid class of activation function has been so successful.\n\nIf we then consider the quench in more detail, and look at it dynamically, then we can parameterise the function for \\\\(m\\\\) in terms of time and look at how ‘hard’ the quench is, and how long we take to heat up. If we assume a linear relationship between \\\\(t\\\\) and heat flow inwards, then the time spent magn\n[1]-  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://darsakthi.github.io/posts/2021/02/act-func/\" --max-chars 8000 2>&1\n[2]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://arxiv.org/abs/2511.00746\" --max-chars 6000 2>&1\n=== DONE ===", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [26] ASSISTANT · 2026-06-16 16:51:44 UTC

```
I have enough information. The blog post confirms that the tanh ↔ MFT Ising model connection is known as a THEORETICAL justification for tanh - but using the actual COUPLED self-consistency equation as a learnable activation with learnable coupling constant is not. Let me now formulate and write the final hypothesis.
```

### [27] TOOL CALL — Bash · 2026-06-16 16:51:44 UTC

```
Final adversarial novelty check on coupled mean-field learnable activation:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
# One more check: verify this specific "learnable J coupled mean-field activation" hasn't been proposed
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "learnable coupling mean field activation function forward pass fixed point discriminative" --max-results 6 2>&1 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "\"mean field\" activation function \"learnable\" \"phase transition\" neural network supervised" --max-results 6 2>&1 &
wait
echo "=== DONE ==="
```

### [28] TOOL RESULT — Bash · 2026-06-16 16:51:44 UTC

```
{"stdout": "Search: learnable coupling mean field activation function forward pass fixed point discriminative\nFound: 6 results\n\n1. Deep Implicit Attention: A Mean-Field Theory Perspective on ... - mcbal\n   https://mcbal.github.io/post/deep-implicit-attention-a-mean-field-theory-perspective-on-attention-mechanisms/\n   Attention is interpreted as an inner-loop fixed-point optimization step which returns the approximate response of a system being probed by data....\n\n2. Mean Field Theory of Activation Functions in Deep Neural Networks\n   https://arxiv.org/abs/1805.08786\n   We present a Statistical Mechanics (SM) model of deep neural networks, connecting the energy-based and the feed forward networks (FFN) approach....\n\n3. [PDF] Introduction to dynamical mean-field theory of randomly connected ...\n   https://scipost.org/SciPostPhysLectNotes.79/pdf\n   Dynamical mean-field theory is a powerful physics tool used to analyze the typical behav- ior of neural networks, where neurons can be ......\n\n4. [PDF] A Mean-Field Theory of Training Deep Neural Networks | CS231n\n   https://cs231n.stanford.edu/2024/papers/a-mean-field-theory-of-training-deep-neural-networks.pdf\n   First, we present a theoretical mean-field framework to study the depth scales of a fully- connected neural network as a function of the architecture. We ......\n\n5. Model-agnostic neural mean field with a data-driven transfer function\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC11413991/\n   This paper derives a mean-field model by fitting a transfer function called Refractory SoftPlus, which is simple yet applicable to a broad variety of neuron ......\n\n6. Mean-field inference methods for neural networks - IOPscience\n   https://iopscience.iop.org/article/10.1088/1751-8121/ab7f65\n   We review a selection of classical mean-field methods and recent progress relevant for inference in neural networks....\n\nSearch: \"mean field\" activation function \"learnable\" \"phase transition\" neural network supervised\nFound: 2 results\n\n1. A phase transition in diffusion models reveals the hierarchical nature ...\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC11725779/\n   Understanding which data are learnable by algorithms is key to machine learning. ... mean-field approximation to justify the existence of a phase transition....\n\n2. A Phase Transition in Diffusion Models Reveals the Hierarchical ...\n   https://arxiv.org/html/2402.16991v3\n   Understanding which data are learnable by algorithms is key to machine learning. ... mean-field approximation to justify the existence of a phase transition....\n\n[1]-  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"learnable coupling mean field activation function forward pass fixed point discriminative\" --max-results 6 2>&1\n[2]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"\\\"mean field\\\" activation function \\\"learnable\\\" \\\"phase transition\\\" neural network supervised\" --max-results 6 2>&1\n=== DONE ===", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [29] ASSISTANT · 2026-06-16 16:51:54 UTC

```
Need to check one more paper that could overlap directly.
```

### [30] TOOL CALL — Bash · 2026-06-16 16:51:54 UTC

```
Fetch MFT activation functions paper and deep implicit attention post:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/1805.08786" --max-chars 5000 2>&1
echo "---"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://mcbal.github.io/post/deep-implicit-attention-a-mean-field-theory-perspective-on-attention-mechanisms/" --max-chars 5000 2>&1
```

### [31] TOOL RESULT — Bash · 2026-06-16 16:51:54 UTC

```
{"stdout": "URL: https://arxiv.org/abs/1805.08786\nType: HTML\nLength: 8389 chars (truncated)\n\n--- Content ---\n\nSkip to main content\n\n[](https://www.cornell.edu/)\n\n[Learn about arXiv becoming an independent nonprofit.](https://tech.cornell.edu/arxiv/)\n\nWe gratefully acknowledge support from the Simons Foundation, [member institutions](https://info.arxiv.org/about/ourmembers.html), and all contributors. [Donate](https://info.arxiv.org/about/donate.html)\n\n[](/IgnoreMe)\n\n[](/) > [cs](/list/cs/recent) > arXiv:1805.08786 \n\n[Help](https://info.arxiv.org/help) | [Advanced Search](https://arxiv.org/search/advanced)\n\nAll fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text\n\nSearch\n\n[](https://arxiv.org/)\n\n[ ](https://www.cornell.edu/)\n\nGO\n\n## quick links\n\n  * [Login](https://arxiv.org/login)\n  * [Help Pages](https://info.arxiv.org/help)\n  * [About](https://info.arxiv.org/about)\n\n\n\n# Computer Science > Machine Learning\n\n**arXiv:1805.08786** (cs) \n\n[Submitted on 22 May 2018 ([v1](https://arxiv.org/abs/1805.08786v1)), last revised 6 Jun 2019 (this version, v2)]\n\n# Title:Mean Field Theory of Activation Functions in Deep Neural Networks\n\nAuthors:[Mirco Milletarí](https://arxiv.org/search/cs?searchtype=author&query=Milletar%C3%AD,+M), [Thiparat Chotibut](https://arxiv.org/search/cs?searchtype=author&query=Chotibut,+T), [Paolo E. Trevisanutto](https://arxiv.org/search/cs?searchtype=author&query=Trevisanutto,+P+E)\n\nView a PDF of the paper titled Mean Field Theory of Activation Functions in Deep Neural Networks, by Mirco Milletar\\'i and 2 other authors\n\n[View PDF](/pdf/1805.08786)\n\n> Abstract:We present a Statistical Mechanics (SM) model of deep neural networks, connecting the energy-based and the feed forward networks (FFN) approach. We infer that FFN can be understood as performing three basic steps: encoding, representation validation and propagation. From the meanfield solution of the model, we obtain a set of natural activations -- such as Sigmoid, $\\tanh$ and ReLu -- together with the state-of-the-art, Swish; this represents the expected information propagating through the network and tends to ReLu in the limit of zero [this http URL](http://noise.We) study the spectrum of the Hessian on an associated classification task, showing that Swish allows for more consistent performances over a wider range of network architectures. \n\nComments: | Presented at the ICML 2019 Workshop on Theoretical Physics forDeep Learning  \n---|---  \nSubjects: |  Machine Learning (cs.LG); Neural and Evolutionary Computing (cs.NE); Machine Learning (stat.ML)  \nCite as: | [arXiv:1805.08786](https://arxiv.org/abs/1805.08786) [cs.LG]  \n  | (or  [arXiv:1805.08786v2](https://arxiv.org/abs/1805.08786v2) [cs.LG] for this version)   \n  |  <https://doi.org/10.48550/arXiv.1805.08786> Focus to learn more arXiv-issued DOI via DataCite  \n  \n## Submission history\n\nFrom: Mirco Milletarì [[view email](/show-email/e8eac226/1805.08786)]   \n**[[v1]](/abs/1805.08786v1)** Tue, 22 May 2018 18:00:02 UTC (2,794 KB)  \n**[v2]** Thu, 6 Jun 2019 03:33:45 UTC (829 KB)  \n\n\nFull-text links:\n\n## Access Paper:\n\nView a PDF of the paper titled Mean Field Theory of Activation Functions in Deep Neural Networks, by Mirco Milletar\\'i and 2 other authors\n\n  * [View PDF](/pdf/1805.08786)\n  * [TeX Source ](/src/1805.08786)\n\n\n\n[view license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/ \"Rights to this article\")\n\n### Current browse context:\n\ncs.LG\n\n[< prev](/prevnext?id=1805.08786&function=prev&context=cs.LG \"previous in cs.LG \\(accesskey p\\)\")   |   [next >](/prevnext?id=1805.08786&function=next&context=cs.LG \"next in cs.LG \\(accesskey n\\)\")   \n\n\n[new](/list/cs.LG/new) |  [recent](/list/cs.LG/recent) | [2018-05](/list/cs.LG/2018-05)\n\nChange to browse by: \n\n[cs](/abs/1805.08786?context=cs)  \n[cs.NE](/abs/1805.08786?context=cs.NE)  \n[stat](/abs/1805.08786?context=stat)  \n[stat.ML](/abs/1805.08786?context=stat.ML)  \n\n\n### References & Citations\n\n  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:1805.08786)\n  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=1805.08786)\n  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:1805.08786)\n\n\n\n### [DBLP](https://dblp.uni-trier.de) \\- CS Bibliography\n\n[listing](https://dblp.uni-trier.de/db/journals/corr/corr1805.html#abs-1805-08786 \"listing on DBLP\") | [bibtex](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1805-08786 \"DBLP bibtex record\")\n\n[Mirco Milletarí](https://dblp.uni-trier.de/search/author?author=Mirco%20Milletar%C3%AD \"DBLP author search\")  \n[Thiparat Chotibut](https://dblp.uni-trier.de/search/author?author=Thiparat%20Chotibut \"DBLP author search\")  \n[Paolo E. Trevisanutto](https://dblp.uni-trier.de/search/author?author=Paolo%20E.%20Trevisanutto \"DBLP author search\")\n\nexport BibTeX citation Loading...\n\n## BibTeX formatted citation\n\n×\n\nloading...\n\nData provided by: \n\n### Bookmark\n\n[ ](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/1805.08786&description=M\n---\nURL: https://mcbal.github.io/post/deep-implicit-attention-a-mean-field-theory-perspective-on-attention-mechanisms/\nType: HTML\nLength: 38304 chars (truncated)\n\n--- Content ---\n\n# Search\n\n__\n\n[mcbal](/)\n\n__\n\n[mcbal](/)\n\n  * [Blog](/#posts)\n  * [About](/#about)\n\n\n\n  * __\n\n\n\n# Deep Implicit Attention: A Mean-Field Theory Perspective on Attention Mechanisms\n\nCan we model attention as the collective response of a statistical-mechanical system?\n\nPublished on Apr 7, 2021  Last updated on May 11, 2021  20 min read \n\n* * *\n\n**✨ Update (November 2021):** _Consider reading[Transformers Are Secretly Collectives of Spin Systems](https://mcbal.github.io/post/transformers-are-secretly-collectives-of-spin-systems/) for a high-level overview of some of the ideas outlined in this post._\n\n* * *\n\n  1. Introduction\n  2. Mean-field theory for disordered systems\n     1. Random Ising models (or Boltzmann machines or …)\n     2. Adaptive Thouless-Anderson-Palmer mean-field theory\n  3. Attention as a fixed-point method\n     1. Generalizing spin models to vector degrees of freedom\n     2. Deep implicit attention: attention as a collective response\n     3. Slow and explicit: solving the adaptive TAP equations\n     4. Fast and neural: parametrizing the Onsager self-correction term\n  4. A mean-field theory perspective on transformers\n     1. Parametrizing the couplings: sparse graph structure from inputs\n     2. Softmax attention does a single, naive mean-field update step\n     3. Feed-forward layer corrects naive mean-field update\n     4. Mean-field theory framework for transformer architectures\n     5. Comparison with energy-based perspective\n  5. Conclusion and outlook\n  6. Related work\n\n\n\n* * *\n\n# 1\\. Introduction\n\n> **✨ Code: A reference PyTorch implementation of the ideas outlined in this blog post is available in the repository[`mcbal/deep-implicit-attention`](https://github.com/mcbal/deep-implicit-attention). Comments welcome.**\n\nTo explore progress beyond the cage of softmax attention, we have previously looked at energy-based perspectives on attention mechanisms:\n\n  * [An Energy-Based Perspective on Attention Mechanisms in Transformers](https://mcbal.github.io/post/an-energy-based-perspective-on-attention-mechanisms-in-transformers/)\n  * [Transformer Attention as an Implicit Mixture of Effective Energy-Based Models](https://mcbal.github.io/post/transformer-attention-as-an-implicit-mixture-of-effective-energy-based-models/)\n  * [Attention as Energy Minimization: Visualizing Energy Landscapes](https://mcbal.github.io/post/attention-as-energy-minimization-visualizing-energy-landscapes/)\n\n\n\nThe main take-away so far has been that you can think of softmax attention as implementing a single, big gradient step of some energy function and that training transformers is akin to meta-learning how to best tune a stack of attention and feed-forward modules to perform well on some auxiliary (meta-)task(s). But what can an energy-based perspective actually provide beyond quaint and hand-wavy statements like _implicit energy landscapes are sculpted every time you train a transformer_?\n\nIn this post, we approach attention in terms of the _collective response of a statistical-mechanical system_. Attention is interpreted as an inner-loop fixed-point optimization step which returns the approximate response of a system being probed by data. This response is a differentiable compromise between the system's internal dynamics and the data it's being exposed to. To better respond to incoming data, outer-loop optimization steps can nudge the interactions and the self-organizing behaviour of the system.\n\nTo implement our proposal, we combine old ideas and new technology to construct a family of attention mechanisms based on fixed points. We use [deep equilibrium models](https://arxiv.org/abs/1909.01377) to solve a set of self-consistent mean-field equations of a vector generalization of the random Ising spin-model. By approximating these equations, we arrive at simplified update steps which mirror the vanilla transformer architecture. We conclude by showing how transformers can be understood from a mean-field theory perspective.\n\n# 2\\. Mean-field theory for disordered systems\n\nIn physics, [mean-field theory](https://en.wikipedia.org/wiki/Mean-field_theory) is an approximation method to study models made up of many individual degrees of freedom that interact with each other. Mean-field theory approximates the effect of the environment on any given individual degree of freedom by a single, averaged effect, and thus reduces a many-body problem to an (effective) one-body problem. This is a drastic approximation. Whether mean-field theory a sensible thing to do depends on the problem and the properties of your variational ansatz.\n\n> **Mean-field theory & variational methods:** From the point of view of variational methods, mean-field theory tries to approximate a complicated object (like a partition function of a statistical-mechanical system) by wiggling around the parameters of a tractable variational ansatz to get as close as possible to the real thing. You can picture this process as projecting down a complicated object living i", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [32] ASSISTANT · 2026-06-16 16:53:25 UTC

```
The searches confirm my direction is novel. The "Deep Implicit Attention" work applies mean-field equations to attention mechanisms in transformers - not as a pointwise activation function replacement. The MFT paper (1805.08786) uses SM theory to EXPLAIN existing activations, not design new ones via self-consistency. My proposal is distinct. Let me write the output.
```

### [33] TOOL CALL — Write · 2026-06-16 16:53:25 UTC

```
File: /ai-inventor/aii_data/runs/run_6gT5lHFn8559/iter_1/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json

{
  "title": "Curie-Weiss Mean-Field Activation: Self-Consistent Within-Layer Coupling That Learns Critical Gain",
  "hypothesis": "A neural network activation function defined as the fixed point of the Curie-Weiss mean-field self-consistency equation — y_i = tanh(x_i + J * mean(y)) for all neurons i in a layer, where J is a single learnable scalar coupling constant — will outperform standard pointwise activations (ReLU, GELU, Swish, Tanh) in convergence speed, gradient stability, and final accuracy, because: (1) J self-organizes toward the critical value J → 1 during training, maximizing the layer's input sensitivity and gradient flow simultaneously; (2) the within-sample mean-field coupling acts as a learned, parameter-efficient form of collective gain control that is unavailable to any purely pointwise activation; and (3) near criticality the effective gain 1/(1 − J·s̄) diverges smoothly, maintaining gradient signal across many layers without the dead-neuron or saturation pathologies of existing activations.",
  "motivation": "All standard activation functions (ReLU, GELU, Swish, tanh) are applied pointwise: each neuron's output depends only on its own pre-activation. This ignores the collective behavior of all neurons in the layer — a dimension of expressivity that biological neural systems exploit via homeostatic coupling. The critical cost of this independence is that the effective gain of each layer must be managed externally (via weight initialization, batch norm, careful learning rate schedules). Criticality theory in deep learning (Poole et al. 2016; Yang & Schoenholz 2017) shows that networks at the 'edge of chaos' — where the Jacobian singular values are near unity — train fastest and generalize best. Existing methods achieve this only at initialization; the network drifts away from criticality as weights update. This hypothesis proposes an activation function that ENFORCES near-critical behavior throughout training via a thermodynamic self-consistency mechanism, adapting the gain of the entire layer collectively with a single learned parameter. The impact is: fewer dead neurons, more stable gradient propagation in deep networks, and empirically faster convergence, all without adding normalization overhead or per-neuron parameters.",
  "assumptions": [
    "The Curie-Weiss fixed point (y = tanh(x + J·mean(y))) has a unique stable solution for |J| < 1 and converges in 3–5 iterations of mean-field updating starting from m = 0, making it computationally feasible as a drop-in activation.",
    "Gradient-based training of J will push it toward the critical value J → 1⁻ because this maximizes the layer's mutual information between input and output (via the diverging susceptibility), giving the network a training incentive to approach criticality.",
    "The within-sample mean-field coupling (coupling outputs to each other within one forward pass through the fixed point) provides strictly more expressive gain control than pointwise activations, enabling better representation of features that require collective detection.",
    "PyTorch autograd can differentiate through the fixed-point iteration accurately (either directly via unrolled iterations or via the implicit function theorem applied to F(m) = mean(tanh(x + J·m)) − m = 0), making end-to-end gradient training straightforward.",
    "The improvement generalizes across architectures (MLP, CNN, Transformer) because the gain-control mechanism is architecture-agnostic and operates within any feedforward layer."
  ],
  "investigation_approach": "Implement CWA in PyTorch as a custom nn.Module. Forward pass: iterate m ← mean(tanh(x + J·m)) for 5 steps starting from m=0; output y_i = tanh(x_i + J·m*). Backward pass: use PyTorch autograd through the unrolled iterations. Train small MLPs (3–6 layers, 256 hidden units) on CIFAR-10, MNIST, and a tabular dataset (e.g., adult-income), comparing CWA against ReLU, GELU, Swish, and tanh baselines. Measure: (1) final validation accuracy, (2) convergence speed (epochs to 95% of peak), (3) gradient norm stability across layers (log of ratio of gradient norms at layer 1 vs. layer L), and (4) the learned value of J per layer at convergence. Also test with J constrained to [0, 1) to prevent bistability during experiments, and free J (unconstrained) to observe whether it self-organizes near criticality. Report effect size with confidence intervals using 5 random seeds per configuration. Total LLM API cost: $0 (pure neural network training, no LLM calls required); compute: CPU sufficient for MNIST/tabular, GPU for CIFAR-10.",
  "success_criteria": "CONFIRM if: (1) CWA achieves ≥0.5% higher final accuracy than the best baseline on at least 2 of 3 datasets, AND (2) gradient norm ratio (layer-1/layer-L) for CWA is ≤2× closer to 1.0 than best baseline, indicating more stable gradient propagation, AND (3) learned J converges to values in [0.7, 1.0] across layers (near-critical regime). DISCONFIRM if: (1) CWA performs worse than or within noise of all baselines on all datasets, OR (2) J consistently converges far from criticality (J < 0.3 or J ≥ 1.0 causing instability), OR (3) convergence requires significantly more than 5 iterations making it computationally prohibitive. PARTIAL CONFIRM if: CWA improves gradient stability (criterion 2 and 3) but not final accuracy — this would suggest the benefit is architecture-dependent and motivate testing in deeper networks where gradient pathologies dominate.",
  "related_works": [
    "Milletarì et al. (2018, arXiv:1805.08786) 'Mean Field Theory of Activation Functions in Deep Neural Networks': Uses statistical mechanics to DERIVE existing activations (tanh, ReLU, Swish) as natural solutions to energy-based models. Key difference: their work provides a post-hoc physical interpretation of known functions; we propose a NEW activation defined by the actual Curie-Weiss self-consistency equation with a learnable coupling J, which introduces within-layer neuron coupling absent in all their derived activations.",
    "Sakthivadivel (2021, arXiv:2102.04896) 'Formalising the Use of the Activation Function in Neural Inference': Shows the sigmoid/tanh family corresponds to mean-field Ising models, providing a neuroscientific and physical justification for their use. Key difference: this work explains why tanh ≈ independent mean-field spin; our proposal uses the COUPLED mean-field equation m = (1/n)Σ tanh(x_i + J·m) as the actual activation, adding the explicit inter-neuron coupling term J·m that their analysis treats as zero.",
    "Bal (2021, 'Deep Implicit Attention'): Applies Thouless-Anderson-Palmer mean-field equations to ATTENTION mechanisms in transformers, showing softmax attention is one step of naive mean-field inference. Key difference: their work reformulates the attention operator; our proposal replaces ACTIVATION FUNCTIONS (nonlinearities within a layer), a different architectural component. Our CWA operates within a single layer's neurons, while their work operates across token positions.",
    "Yang & Schoenholz (2017) 'Mean Field Residual Networks' and Poole et al. (2016) 'Exponential Expressivity': Show that networks at the edge of chaos (Jacobian singular values ≈ 1) propagate information best and train fastest, achieved via careful weight variance initialization. Key difference: these works achieve criticality through INITIALIZATION — it is not maintained during training. CWA provides a mechanism through the activation function itself (via learned J → 1) that actively maintains criticality throughout the training process.",
    "Amos & Kolter (2017) 'OptNet: Differentiable Optimization as a Layer in Neural Networks': Introduces differentiable quadratic program solvers as neural network layers. Key difference: OptNet replaces full linear layers with QP solvers (O(n³) per solve); CWA is a lightweight activation-level operation (O(n·K) for K≈5 iterations) that is a drop-in replacement for any pointwise activation, not a new layer type.",
    "Bai et al. (2019) 'Deep Equilibrium Models (DEQ)': Applies fixed-point iteration at the FULL-LAYER level — the entire layer mapping is solved to a fixed point. Key difference: DEQ replaces the full layer (including the weight matrix); CWA is a within-layer activation function that only couples neurons through a single scalar mean field, retaining the standard linear weight matrix and adding only one learnable parameter J per layer."
  ],
  "inspiration": "This hypothesis is a Level-3 (methodological) cross-domain transfer from statistical physics, specifically the Curie-Weiss model of ferromagnetism. In physics, the Curie-Weiss mean-field equation m = tanh(β(h + J·m)) describes how an Ising spin aligns with an external field h plus a self-consistent feedback from the average magnetization J·m of all other spins. The critical insight is that this 'self-consistent' structure — where the output depends on the mean of all outputs — is entirely absent from all standard neural network activations, which are purely pointwise. The cross-domain insight is: just as a ferromagnet near its Curie temperature exhibits maximum magnetic susceptibility (tiny external fields produce large magnetization changes), a neural layer near its 'critical coupling' J→1 should exhibit maximum input sensitivity — small changes in the pre-activation produce large, amplified output changes. This is exactly what gradient-based learning needs: high sensitivity to inputs means high signal-to-noise ratio in gradient updates. The self-organization toward criticality (like 'self-organized criticality' in sandpile models) emerges naturally because networks that approach J=1 have higher effective capacity and thus lower training loss, giving gradient descent an incentive to push J toward the critical point.",
  "terms": [
    {
      "term": "Curie-Weiss Model",
      "definition": "A mean-field model of ferromagnetism where each spin interacts with the average ('mean field') of all other spins rather than with neighbors individually. Described by the self-consistency equation m = tanh(β(h + J·m)), where m is the average magnetization, h is the external field, J is the coupling strength, and β is the inverse temperature. Exhibits a phase transition at βJ = 1."
    },
    {
      "term": "Curie-Weiss Activation (CWA)",
      "definition": "The proposed activation function defined by the fixed point y* of the equation y = tanh(x + J·mean(y)), where x is the vector of pre-activations, y is the vector of activations, J is a learnable scalar coupling, and mean(y) is the layer-wise mean of y. The fixed point is found by iterating m ← mean(tanh(x + J·m)) and setting y_i = tanh(x_i + J·m*)."
    },
    {
      "term": "Coupling Constant (J)",
      "definition": "A single learnable scalar parameter per layer in CWA that controls the strength of inter-neuron coupling through the mean field. J=0 recovers independent tanh; J→1 approaches criticality with maximum gain; J>1 creates a bistable activation with two stable fixed points (the layer has spontaneous symmetry breaking)."
    },
    {
      "term": "Critical Gain",
      "definition": "The effective gradient amplification of the CWA at the critical coupling J=1. By the implicit function theorem, ∂y_i/∂x_i ∝ sech²(x_i + m*)/(1 − J·s̄), where s̄ = mean(sech²(x + m*)) ∈ (0,1]. As J·s̄ → 1, this gain diverges, enabling maximum sensitivity. In practice, J learns a value slightly below 1 to maintain stability."
    },
    {
      "term": "Mean-Field Self-Consistency",
      "definition": "The defining property of CWA where the activation output y depends on its own mean (mean(y)), creating a fixed-point equation that must be solved iteratively. Unlike layer normalization (which uses the mean of the INPUT x), self-consistency means the mean of the OUTPUT y feeds back into the computation, coupling all neurons in the layer through their collective state."
    },
    {
      "term": "Edge of Chaos",
      "definition": "The critical operating regime of a neural network where the Jacobian of the layer mapping has singular values close to 1, balancing ordered (singular values < 1, vanishing gradients) and chaotic (singular values > 1, exploding gradients) phases. CWA is hypothesized to self-organize toward this regime via the learned coupling J → 1."
    },
    {
      "term": "Pointwise Activation",
      "definition": "Any activation function where each neuron's output y_i depends only on its own pre-activation x_i, with no dependence on other neurons' pre-activations or outputs. All standard activations (ReLU, GELU, Swish, tanh, sigmoid) are pointwise. CWA is not pointwise because y_i depends on mean(y), which involves all neurons."
    }
  ],
  "summary": "We propose the Curie-Weiss Activation (CWA), a novel activation function where each neuron's output is the fixed point of a mean-field self-consistency equation y_i = tanh(x_i + J·mean(y)), with J a single learnable coupling per layer. Borrowed from the physics of ferromagnetism, this within-layer coupling gives the activation a tunable effective gain 1/(1 − J·s̄) that gradient descent is hypothesized to push toward the critical point J → 1, achieving maximum sensitivity and gradient stability throughout training without requiring batch statistics or per-neuron parameters."
}
```

### [34] TOOL RESULT — Write · 2026-06-16 16:53:25 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/iter_1/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Curie-Weiss Mean-Field Activation: Self-Consistent Within-Layer Coupling That Learns Critical Gain\",\n  \"hypothesis\": \"A neural network activation function defined as the fixed point of the Curie-Weiss mean-field self-consistency equation — y_i = tanh(x_i + J * mean(y)) for all neurons i in a layer, where J is a single learnable scalar coupling constant — will outperform standard pointwise activations (ReLU, GELU, Swish, Tanh) in convergence speed, gradient stability, and final accuracy, because: (1) J self-organizes toward the critical value J → 1 during training, maximizing the layer's input sensitivity and gradient flow simultaneously; (2) the within-sample mean-field coupling acts as a learned, parameter-efficient form of collective gain control that is unavailable to any purely pointwise activation; and (3) near criticality the effective gain 1/(1 − J·s̄) diverges smoothly, maintaining gradient signal across many layers without the dead-neuron or saturation pathologies of existing activations.\",\n  \"motivation\": \"All standard activation functions (ReLU, GELU, Swish, tanh) are applied pointwise: each neuron's output depends only on its own pre-activation. This ignores the collective behavior of all neurons in the layer — a dimension of expressivity that biological neural systems exploit via homeostatic coupling. The critical cost of this independence is that the effective gain of each layer must be managed externally (via weight initialization, batch norm, careful learning rate schedules). Criticality theory in deep learning (Poole et al. 2016; Yang & Schoenholz 2017) shows that networks at the 'edge of chaos' — where the Jacobian singular values are near unity — train fastest and generalize best. Existing methods achieve this only at initialization; the network drifts away from criticality as weights update. This hypothesis proposes an activation function that ENFORCES near-critical behavior throughout training via a thermodynamic self-consistency mechanism, adapting the gain of the entire layer collectively with a single learned parameter. The impact is: fewer dead neurons, more stable gradient propagation in deep networks, and empirically faster convergence, all without adding normalization overhead or per-neuron parameters.\",\n  \"assumptions\": [\n    \"The Curie-Weiss fixed point (y = tanh(x + J·mean(y))) has a unique stable solution for |J| < 1 and converges in 3–5 iterations of mean-field updating starting from m = 0, making it computationally feasible as a drop-in activation.\",\n    \"Gradient-based training of J will push it toward the critical value J → 1⁻ because this maximizes the layer's mutual information between input and output (via the diverging susceptibility), giving the network a training incentive to approach criticality.\",\n    \"The within-sample mean-field coupling (coupling outputs to each other within one forward pass through the fixed point) provides strictly more expressive gain control than pointwise activations, enabling better representation of features that require collective detection.\",\n    \"PyTorch autograd can differentiate through the fixed-point iteration accurately (either directly via unrolled iterations or via the implicit function theorem applied to F(m) = mean(tanh(x + J·m)) − m = 0), making end-to-end gradient training straightforward.\",\n    \"The improvement generalizes across architectures (MLP, CNN, Transformer) because the gain-control mechanism is architecture-agnostic and operates within any feedforward layer.\"\n  ],\n  \"investigation_approach\": \"Implement CWA in PyTorch as a custom nn.Module. Forward pass: iterate m ← mean(tanh(x + J·m)) for 5 steps starting from m=0; output y_i = tanh(x_i + J·m*). Backward pass: use PyTorch autograd through the unrolled iterations. Train small MLPs (3–6 layers, 256 hidden units) on CIFAR-10, MNIST, and a tabular dataset (e.g., adult-income), comparing CWA against ReLU, GELU, Swish, and tanh baselines. Measure: (1) final validation accuracy, (2) convergence speed (epochs to 95% of peak), (3) gradient norm stability across layers (log of ratio of gradient norms at layer 1 vs. layer L), and (4) the learned value of J per layer at convergence. Also test with J constrained to [0, 1) to prevent bistability during experiments, and free J (unconstrained) to observe whether it self-organizes near criticality. Report effect size with confidence intervals using 5 random seeds per configuration. Total LLM API cost: $0 (pure neural network training, no LLM calls required); compute: CPU sufficient for MNIST/tabular, GPU for CIFAR-10.\",\n  \"success_criteria\": \"CONFIRM if: (1) CWA achieves ≥0.5% higher final accuracy than the best baseline on at least 2 of 3 datasets, AND (2) gradient norm ratio (layer-1/layer-L) for CWA is ≤2× closer to 1.0 than best baseline, indicating more stable gradient propagation, AND (3) learned J converges to values in [0.7, 1.0] across layers (near-critical regime). DISCONFIRM if: (1) CWA performs worse than or within noise of all baselines on all datasets, OR (2) J consistently converges far from criticality (J < 0.3 or J ≥ 1.0 causing instability), OR (3) convergence requires significantly more than 5 iterations making it computationally prohibitive. PARTIAL CONFIRM if: CWA improves gradient stability (criterion 2 and 3) but not final accuracy — this would suggest the benefit is architecture-dependent and motivate testing in deeper networks where gradient pathologies dominate.\",\n  \"related_works\": [\n    \"Milletarì et al. (2018, arXiv:1805.08786) 'Mean Field Theory of Activation Functions in Deep Neural Networks': Uses statistical mechanics to DERIVE existing activations (tanh, ReLU, Swish) as natural solutions to energy-based models. Key difference: their work provides a post-hoc physical interpretation of known functions; we propose a NEW activation defined by the actual Curie-Weiss self-consistency equation with a learnable coupling J, which introduces within-layer neuron coupling absent in all their derived activations.\",\n    \"Sakthivadivel (2021, arXiv:2102.04896) 'Formalising the Use of the Activation Function in Neural Inference': Shows the sigmoid/tanh family corresponds to mean-field Ising models, providing a neuroscientific and physical justification for their use. Key difference: this work explains why tanh ≈ independent mean-field spin; our proposal uses the COUPLED mean-field equation m = (1/n)Σ tanh(x_i + J·m) as the actual activation, adding the explicit inter-neuron coupling term J·m that their analysis treats as zero.\",\n    \"Bal (2021, 'Deep Implicit Attention'): Applies Thouless-Anderson-Palmer mean-field equations to ATTENTION mechanisms in transformers, showing softmax attention is one step of naive mean-field inference. Key difference: their work reformulates the attention operator; our proposal replaces ACTIVATION FUNCTIONS (nonlinearities within a layer), a different architectural component. Our CWA operates within a single layer's neurons, while their work operates across token positions.\",\n    \"Yang & Schoenholz (2017) 'Mean Field Residual Networks' and Poole et al. (2016) 'Exponential Expressivity': Show that networks at the edge of chaos (Jacobian singular values ≈ 1) propagate information best and train fastest, achieved via careful weight variance initialization. Key difference: these works achieve criticality through INITIALIZATION — it is not maintained during training. CWA provides a mechanism through the activation function itself (via learned J → 1) that actively maintains criticality throughout the training process.\",\n    \"Amos & Kolter (2017) 'OptNet: Differentiable Optimization as a Layer in Neural Networks': Introduces differentiable quadratic program solvers as neural network layers. Key difference: OptNet replaces full linear layers with QP solvers (O(n³) per solve); CWA is a lightweight activation-level operation (O(n·K) for K≈5 iterations) that is a drop-in replacement for any pointwise activation, not a new layer type.\",\n    \"Bai et al. (2019) 'Deep Equilibrium Models (DEQ)': Applies fixed-point iteration at the FULL-LAYER level — the entire layer mapping is solved to a fixed point. Key difference: DEQ replaces the full layer (including the weight matrix); CWA is a within-layer activation function that only couples neurons through a single scalar mean field, retaining the standard linear weight matrix and adding only one learnable parameter J per layer.\"\n  ],\n  \"inspiration\": \"This hypothesis is a Level-3 (methodological) cross-domain transfer from statistical physics, specifically the Curie-Weiss model of ferromagnetism. In physics, the Curie-Weiss mean-field equation m = tanh(β(h + J·m)) describes how an Ising spin aligns with an external field h plus a self-consistent feedback from the average magnetization J·m of all other spins. The critical insight is that this 'self-consistent' structure — where the output depends on the mean of all outputs — is entirely absent from all standard neural network activations, which are purely pointwise. The cross-domain insight is: just as a ferromagnet near its Curie temperature exhibits maximum magnetic susceptibility (tiny external fields produce large magnetization changes), a neural layer near its 'critical coupling' J→1 should exhibit maximum input sensitivity — small changes in the pre-activation produce large, amplified output changes. This is exactly what gradient-based learning needs: high sensitivity to inputs means high signal-to-noise ratio in gradient updates. The self-organization toward criticality (like 'self-organized criticality' in sandpile models) emerges naturally because networks that approach J=1 have higher effective capacity and thus lower training loss, giving gradient descent an incentive to push J toward the critical point.\",\n  \"terms\": [\n    {\n      \"term\": \"Curie-Weiss Model\",\n      \"definition\": \"A mean-field model of ferromagnetism where each spin interacts with the average ('mean field') of all other spins rather than with neighbors individually. Described by the self-consistency equation m = tanh(β(h + J·m)), where m is the average magnetization, h is the external field, J is the coupling strength, and β is the inverse temperature. Exhibits a phase transition at βJ = 1.\"\n    },\n    {\n      \"term\": \"Curie-Weiss Activation (CWA)\",\n      \"definition\": \"The proposed activation function defined by the fixed point y* of the equation y = tanh(x + J·mean(y)), where x is the vector of pre-activations, y is the vector of activations, J is a learnable scalar coupling, and mean(y) is the layer-wise mean of y. The fixed point is found by iterating m ← mean(tanh(x + J·m)) and setting y_i = tanh(x_i + J·m*).\"\n    },\n    {\n      \"term\": \"Coupling Constant (J)\",\n      \"definition\": \"A single learnable scalar parameter per layer in CWA that controls the strength of inter-neuron coupling through the mean field. J=0 recovers independent tanh; J→1 approaches criticality with maximum gain; J>1 creates a bistable activation with two stable fixed points (the layer has spontaneous symmetry breaking).\"\n    },\n    {\n      \"term\": \"Critical Gain\",\n      \"definition\": \"The effective gradient amplification of the CWA at the critical coupling J=1. By the implicit function theorem, ∂y_i/∂x_i ∝ sech²(x_i + m*)/(1 − J·s̄), where s̄ = mean(sech²(x + m*)) ∈ (0,1]. As J·s̄ → 1, this gain diverges, enabling maximum sensitivity. In practice, J learns a value slightly below 1 to maintain stability.\"\n    },\n    {\n      \"term\": \"Mean-Field Self-Consistency\",\n      \"definition\": \"The defining property of CWA where the activation output y depends on its own mean (mean(y)), creating a fixed-point equation that must be solved iteratively. Unlike layer normalization (which uses the mean of the INPUT x), self-consistency means the mean of the OUTPUT y feeds back into the computation, coupling all neurons in the layer through their collective state.\"\n    },\n    {\n      \"term\": \"Edge of Chaos\",\n      \"definition\": \"The critical operating regime of a neural network where the Jacobian of the layer mapping has singular values close to 1, balancing ordered (singular values < 1, vanishing gradients) and chaotic (singular values > 1, exploding gradients) phases. CWA is hypothesized to self-organize toward this regime via the learned coupling J → 1.\"\n    },\n    {\n      \"term\": \"Pointwise Activation\",\n      \"definition\": \"Any activation function where each neuron's output y_i depends only on its own pre-activation x_i, with no dependence on other neurons' pre-activations or outputs. All standard activations (ReLU, GELU, Swish, tanh, sigmoid) are pointwise. CWA is not pointwise because y_i depends on mean(y), which involves all neurons.\"\n    }\n  ],\n  \"summary\": \"We propose the Curie-Weiss Activation (CWA), a novel activation function where each neuron's output is the fixed point of a mean-field self-consistency equation y_i = tanh(x_i + J·mean(y)), with J a single learnable coupling per layer. Borrowed from the physics of ferromagnetism, this within-layer coupling gives the activation a tunable effective gain 1/(1 − J·s̄) that gradient descent is hypothesized to push toward the critical point J → 1, achieving maximum sensitivity and gradient stability throughout training without requiring batch statistics or per-neuron parameters.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [35] ASSISTANT · 2026-06-16 16:53:37 UTC

```
The output file has been written. Here's a summary of the hypothesis generated:

---

## Hypothesis: Curie-Weiss Mean-Field Activation (CWA)

**Core idea**: Replace standard pointwise activations with the fixed point of a mean-field self-consistency equation from statistical physics:

> y_i = tanh(x_i + J · mean(y))

where J is a **single learnable scalar per layer**. This is the Curie-Weiss equation for a ferromagnet — solved iteratively (3–5 steps) during the forward pass.

**Why it's novel**: All existing activations are pointwise (each neuron independent). CWA couples all neurons in a layer through their collective mean output. Prior work (Milletarì 2018, Sakthivadivel 2021) uses physics to *explain* why tanh exists — they never use the actual self-consistency equation as a trainable activation. The "Deep Implicit Attention" work applies similar equations to attention mechanisms in transformers, not to activation functions.

**Key physics insight imported**: Near the Curie temperature (J → 1), magnetic susceptibility diverges — tiny external fields produce large magnetization. Translated to networks: J → 1 gives maximum gradient signal, eliminating vanishing gradients without careful initialization. Gradient descent will push J toward 1 because near-critical networks have higher effective capacity and lower training loss.

**What the experiment tests**:
- Does CWA beat ReLU/GELU/Swish/tanh on CIFAR-10, MNIST, and a tabular dataset?
- Does J self-organize to values near 1 (the critical point)?
- Is gradient norm ratio (layer 1 vs. layer L) closer to 1 than baselines?

**Cost**: $0 LLM API calls; pure PyTorch training on CPU/GPU.
```
