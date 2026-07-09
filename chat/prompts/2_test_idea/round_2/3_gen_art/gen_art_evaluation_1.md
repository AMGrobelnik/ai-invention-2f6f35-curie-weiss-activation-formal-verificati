# gen_art_evaluation_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_6gT5lHFn8559` — Novel Activation Function
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_evaluation_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 19:39:22 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<task>
Evaluate experimental results using domain-appropriate methods, metrics, and analysis techniques.
When in doubt, prefer more metrics over fewer — but only ones that make sense for the domain.
</task>

<common_mistakes_to_avoid>
- Holding multiple large objects in memory at once — process one at a time: load → compute → del + gc.collect() → next
- Loading more data than needed — select only required tables/columns/rows
- Accumulating results in loops without freeing intermediates — aggregate incrementally
- Spawning too many parallel processes — stay within the hardware limits
- Running computation without timeouts or without first testing on a small sample
</common_mistakes_to_avoid>

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

<CRITICAL_WARNING__PREVIOUS_ATTEMPT_CRASHED>
YOUR PREVIOUS EXECUTION ATTEMPT CATASTROPHICALLY FAILED.
The entire worker container crashed after 574s.
Error: Pod launch failed — no instance booted (tried 18, 0 still out of stock): Ability server transient error for 'aii_runpod__gen_pod': 502 <!DOCTYPE html>
<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en-US"> <![endif]-->
<!--[if IE 7]>    <html class="no-js ie7 oldie" lang="en-US"> <![endif]-->
<!--[if IE 8]>    <html class="no-

This was NOT a normal code error — the entire container died. Study the error
and last messages above carefully. Identify what caused the crash and be
EXTREMELY careful to avoid repeating it. Do NOT use the same approach.
</CRITICAL_WARNING__PREVIOUS_ATTEMPT_CRASHED>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/file.py`, `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_evaluation_1_idx4
type: evaluation
title: >-
  CWA Statistical Analysis: LM Paired Tests, K-Saturation Diagnostic, Gradient Bias Table & p_c Audit
summary: >-
  Load full_method_out.json from three dependency experiments (LM Exp3, MLP Exp1, ResNet Exp2), run all statistical tests,
  diagnose K-convergence behavior, compute warm-start-3 gradient bias, audit p_c consistency, and emit a single eval_out.json
  with all findings.
runpod_compute_profile: cpu_heavy
metrics_descriptions: |-
  1. PAIRED T-TESTS (LM experiment, art_DdhxnRglYGM6): For Shakespeare (3 seeds): extract per_seed BPC arrays for CWA=[3.3577,3.3501,3.3478] vs GELU=[3.2294,3.2346,3.2118], SELU=[3.3514,3.3528,3.3502], tanh_swish=[3.3389,3.3383,3.3342]. Run scipy.stats.ttest_rel (paired, same-seed indexing). For WikiText-2 (2 seeds): extract per_seed PPL arrays for CWA=[774.22,760.62] vs GELU=[745.77,731.73], SELU=[763.10,749.50], tanh_swish=[769.44,753.82]. Run scipy.stats.ttest_ind (Welch's, n=2 forces independent). For each comparison report: t_stat, p_value (two-sided and one-sided H0: CWA>=GELU), Cohen's d = (mean_diff / pooled_std), 95% CI on difference via bootstrapping (10000 resamples with replacement).

  2. K-SATURATION DIAGNOSTIC (LM experiment): The J_s_bar_trajectory_per_layer data shows K=5 at every logged step (steps 0,100,200,300,400 for layers 0-5, seed_42). Determine definitively whether K=5 is always K_max saturation or genuine tolerance convergence. Analytical check: with rho=J*s_bar~0.45 and K=5, |m_K - m*| <= rho^K * |m_0 - m*|. Assuming |m_0 - m*| <= 1.0 (bounded tanh outputs), rho^5 = 0.45^5 = 0.0185. The tolerance delta = 1e-4*(1-J*s_bar) ~ 1e-4*0.554 = 5.54e-5. Since 0.0185 >> 5.54e-5, K=5 is NOT genuine convergence if the initial residual is order 1. However if K_max=5 was coded in the implementation (capped at 5), K=5 indicates saturation (the code hit the cap, not the tolerance). Read the method.py from art_DdhxnRglYGM6 to check actual K_max value. Report: fraction_hits_K_max (1.0 if all K values equal K_max), analytical_residual_at_K5 = rho^5 * assumed_initial_gap, required_K_for_tolerance = ceil(log(delta/1.0)/log(rho)), note whether the experiment used K_max=5 (the iter-1 default) vs the iter-2 mandated K_max=50.

  3. GRADIENT BIAS TABLE: The warm-start-T approximation (T tracked steps from detached m*) introduces O(rho^T) relative gradient bias. From LM data: J*s_bar stabilized at 0.441-0.461 across layers (mean rho~0.45). For T=3: bias = rho^T = 0.45^3 = 0.091. For T=5: bias = 0.45^5 = 0.0185. Build a table for rho in {0.3, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60} and T in {3, 5, 10}: entry = rho^T. Highlight the empirically observed (rho=0.45, T=5) cell. Compare against IFT bias: if IFT is used (rho>=0.8), delta=1e-4*(1-rho) gives bias ~1e-4 uniformly. Since rho stayed at 0.45 throughout, IFT was never triggered (0 IFT calls confirmed). Document: 'Under iter-1 training conditions (rho~0.45, T=5 iterations), warm-start-5 gradient bias is approximately 1.85% relative; negligible for training purposes. IFT path was not exercised.'

  4. P_C CONSISTENCY AUDIT: From each experiment's metadata or method.py, extract what p_c value was used for the tanh+Swish (CompetingNonlinearities) baseline. The hypothesis mandates p_c=0.83 (analytically derived from Lesser & Chowdhury 2026 edge-of-chaos condition). Check: art_kKv207AAQYq2 summary states p_c=0.5 (quenched disorder mask). Check art_DdhxnRglYGM6 summary states tanh+Swish@0.5. Both differ from mandated 0.83. Document the deviation and its impact: at p_c=0.5, the Competing Nonlinearities baseline is NOT at the edge-of-chaos critical point and thus represents a suboptimal implementation that weakens the comparison.

  5. MLP GRADIENT RATIO ANALYSIS (art_kKv207AAQYq2): The MLP experiment status='experiment_in_progress' with only depth_6 relu and gelu completed. Extract available gradient ratios: relu depth=6 ratio=0.4579, gelu depth=6 ratio=1.685. CWA at depth=6,10,20 are missing (None). Report this as incomplete data. Compute what can be computed: for the 2 completed configs, verify ratio values are plausible. Report: 'MLP experiment only completed 2 of 27 planned configurations; CWA gradient ratios unavailable for hypothesis testing.'

  6. RESNET CIFAR-100 ANALYSIS (art_SVlh9mQatV8y): Extract per-epoch accuracy trajectories for CWA and GELU in the standard_no_bn config. CWA final=0.1401, GELU final=0.1893. Compute accuracy gap: -4.92 percentage points. Mean J*s_bar=0.306 (well below critical). Report: whether the experiment has multiple seeds (check metadata n_examples=56 which is 1seed*8epochs covers only partial data); compute learning curve AUC difference; note the interim status ('experiment still running' per metadata note).

  7. SOC ANALYSIS - J STABILITY: From the J_s_bar_trajectory across all logged steps (LM experiment), compute: max |J - J_init| across all layers and seeds. From the data: J varies between 0.499038 and 0.501251 (range ~0.002). Report: J_drift_max, J_drift_std across layers, whether any layer shows monotonic trend toward criticality. This quantifies the SOC failure claim ('J remains within 0.003 of initialization').

  8. OVERALL VERDICT SYNTHESIS: Combine all findings into a structured verdict following the hypothesis's success criteria: DISCONFIRM criteria 1 (CWA within noise of baselines on all tasks - BPC difference: CWA 3.352 vs GELU 3.225, delta=+0.127 BPC, CWA is WORSE); DISCONFIRM criteria 2 (SELU and tanh+Swish match/exceed CWA on LM tasks). Emit 'DISCONFIRM' with detailed evidence breakdown by experiment.
metrics_justification: |-
  These metrics directly address the four stated objectives of the artifact direction and the hypothesis's iter-2 claims:

  (1) PAIRED T-TESTS are the correct statistical tool because: (a) paired t-test (Shakespeare, n=3 seeds) controls for between-seed variability since each seed pair uses identical initialization and data ordering — any performance difference is activation-function-pure; (b) Welch's t-test (WikiText-2, n=2 seeds) handles unequal variance without assuming homoscedasticity, appropriate for very small n; (c) one-sided p-value for H0: CWA>=GELU directly answers 'how strong is the negative result?' — a large p-value (>0.5 for one-sided CWA<GELU) would indicate CWA is systematically worse; (d) Cohen's d provides effect size independent of n, crucial for interpreting small-sample significance. These tests turn the qualitative 'CWA is worse' observation into a quantitative disconfirmation strength.

  (2) K-SATURATION DIAGNOSTIC directly addresses a critical implementation flaw flagged in the hypothesis: the hypothesis mandates K_max=50 but iter-1 code appears to have K_max=5. If K=5 is saturation rather than convergence, all CWA forward passes were computing m* to only ~1.85% accuracy rather than the mandated ~0.005% (delta~5e-5). This would explain CWA's underperformance: the activation was not correctly computing the Curie-Weiss fixed point. The diagnostic either (a) exonerates the hypothesis (K=5 was genuine convergence) or (b) identifies the primary confound (K_max too small).

  (3) GRADIENT BIAS TABLE is required because the hypothesis explicitly mandates 'acknowledging the O(rho^3 ≈ 0.09) relative gradient bias' from warm-start-3. The iter-1 code used K=5 (warm-start-5), so the bias is actually rho^5~0.019 rather than 0.09 — a favorable correction for the hypothesis. This table provides the exact numbers needed for honest reporting in the paper and prevents overstatement of the bias magnitude.

  (4) P_C CONSISTENCY AUDIT matters because: if the Competing Nonlinearities baseline used p_c=0.5 instead of the analytically-correct p_c=0.83, it was handicapped relative to its optimal configuration. This affects the interpretation of all comparisons involving tanh+Swish — CWA beat a sub-optimal version of the competitor but the correct comparison remains unmeasured. Documenting this is essential for scientific integrity and for flagging what iter-2 experiments must fix.

  (5-8) The MLP analysis, ResNet analysis, SOC analysis, and verdict synthesis collectively provide the holistic picture needed to adjudicate the hypothesis's three gating experiments (fixed-J ablation as PRIORITY 1, depth ablation as CORE MISSING, high-LR sensitivity). The verdict synthesis explicitly maps each finding to the CONFIRM/DISCONFIRM/PARTIAL criteria defined in the hypothesis's success_criteria section.

  All metrics are computable purely from the loaded JSON files using scipy.stats, numpy, and standard Python — $0 LLM API cost. The cpu_heavy profile is appropriate because no GPU operations are needed, but the full_method_out.json files may be large (150+ examples with per-layer trajectories across seeds).
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
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
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Dependency 2 ---
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
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Dependency 3 ---
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
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

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

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — evaluation metrics, agent orchestration patterns, benchmark design
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand prediction format. Evaluate ALL experiments provided — do not skip or select a subset. Avoid re-training or re-executing the method unless absolutely necessary; prefer loading predictions from each dependency's method_out.json / predict_* fields. Read domain handbook if applicable (see <available_domain_handbooks>). Decide evaluation metrics based on artifact plan. Test basic functionality with 'uv run'.
TODO 3. Fully implement evaluation as described in artifact plan in './eval.py'. Use exp_eval_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant metrics or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-06-16 19:39:22 UTC

```
Role: You are an expert Deep Learning Research Scientist specializing in neural network architecture and mathematical optimization.Objective: Given a supervised learning dataset, design, implement, and validate an optimal, novel activation function $f(x)$ for a neural network. Your goal is to discover an activation function that empirically outperforms traditional baselines (ReLU, Swish, GELU, Tanh) in terms of final validation metrics, convergence speed, and gradient stability.Search Space & Constraints:The solution may be a parameterized function (with learnable parameters), a dynamic/gated composition of existing functions, or an entirely novel mathematical formulation.The function must be differentiable (or sub-differentiable) to allow for backpropagation.Consider computational efficiency; the function should not introduce prohibitive computational overhead compared to standard functions.
```

### [3] SKILL-INPUT — aii-python · 2026-06-16 19:39:44 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-json · 2026-06-16 19:39:44 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SKILL-INPUT — aii-long-running-tasks · 2026-06-16 19:39:44 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: Gradual scaling pattern for long-running autonomous tasks. Use when running experiments, evaluations, or any code that processes data at increasing scale with runtime checks.
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [6] SKILL-INPUT — aii-file-size-limit · 2026-06-16 19:39:48 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: File size check procedure for splitting oversized output files. Use after generating JSON output files to check and split files exceeding the provided size limit.
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [7] SKILL-INPUT — aii-use-hardware · 2026-06-16 19:39:48 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: Detect hardware and use it responsibly. Covers CPU/RAM/GPU detection, memory-safe data processing, and resource-aware computation.
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [8] SKILL-INPUT — aii-parallel-computing · 2026-06-16 19:39:48 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "CRITICAL PERFORMANCE SKILL. Maximize hardware utilization for compute-intensive tasks. Covers GPU acceleration, CPU parallelism, and async I/O. The difference between hours of failure and minutes of success. Use whenever writing ANY script that processes data, makes API calls, or does computation."
---

**ALWAYS parallelize. Sequential processing is unacceptable for any non-trivial workload.** A sequential script doing 1000 API calls takes hours and fails halfway. An async version finishes in minutes with proper error handling. ALWAYS ask: "Can this run in parallel?" — the answer is almost always yes.

Read aii-use-hardware skill first → get `NUM_CPUS`, `HAS_GPU`, `VRAM_GB`, `device`. Set `NUM_WORKERS` proportional to available CPU capacity — check `psutil.cpu_percent(interval=1)` and scale accordingly (e.g. 30% used → use ~70% of cores).

## Decision Tree (follow strictly)

- **I/O-bound** (API calls, downloads, web, file reads) → `asyncio` + `aiohttp` with `Semaphore(NUM_WORKERS * 4)`. NEVER do sequential HTTP requests in a loop.
- **CPU-bound, vectorizable** → GPU available: PyTorch on device / No GPU: NumPy vectorized ops. NEVER loop over array elements in Python.
- **CPU-bound, independent items** → `ProcessPoolExecutor(max_workers=NUM_WORKERS)`. NEVER process items one-by-one when they're independent.
- **Sequential** → only acceptable when items have data dependencies (each depends on the previous result).

## GPU Rules

- Use up to 90% of available VRAM — scale gradually (start small, increase after each successful run, keep 10% buffer)
- Move to device → compute → move back: `torch.tensor(data, device=device)` → `.cpu().numpy()`
- OOM fallback: catch `torch.cuda.OutOfMemoryError` → `empty_cache()` → halve batch size → retry on GPU. Keep reducing until it fits. Stay on GPU.
- Batch large data: chunk it, `del batch` between iterations to free VRAM

## Parallelism Rules

- **CPU-bound**: `ProcessPoolExecutor` + `as_completed`, pre-allocate result list indexed by submission order
- **I/O-bound**: `asyncio` + `aiohttp`, `Semaphore(NUM_WORKERS * 4)`, single shared `ClientSession`, `asyncio.gather(*tasks, return_exceptions=True)`
- Always add `tenacity` retries for transient failures, always set timeouts on HTTP requests
- **CRITICAL — `ProcessPoolExecutor` start method**: Default `fork` deadlocks with loguru (and any threading library). ALWAYS pass `mp_context=multiprocessing.get_context("spawn")` when constructing `ProcessPoolExecutor` in any script that uses loguru, threading, or async I/O. Example:
  ```python
  import multiprocessing as mp
  from concurrent.futures import ProcessPoolExecutor
  with ProcessPoolExecutor(max_workers=N, mp_context=mp.get_context("spawn")) as pool:
      ...
  ```
````

### [9] SYSTEM-USER prompt · 2026-06-16 19:45:32 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/file.py`, `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_evaluation_1_idx4
type: evaluation
title: >-
  CWA Statistical Analysis: LM Paired Tests, K-Saturation Diagnostic, Gradient Bias Table & p_c Audit
summary: >-
  Load full_method_out.json from three dependency experiments (LM Exp3, MLP Exp1, ResNet Exp2), run all statistical tests,
  diagnose K-convergence behavior, compute warm-start-3 gradient bias, audit p_c consistency, and emit a single eval_out.json
  with all findings.
runpod_compute_profile: cpu_heavy
metrics_descriptions: |-
  1. PAIRED T-TESTS (LM experiment, art_DdhxnRglYGM6): For Shakespeare (3 seeds): extract per_seed BPC arrays for CWA=[3.3577,3.3501,3.3478] vs GELU=[3.2294,3.2346,3.2118], SELU=[3.3514,3.3528,3.3502], tanh_swish=[3.3389,3.3383,3.3342]. Run scipy.stats.ttest_rel (paired, same-seed indexing). For WikiText-2 (2 seeds): extract per_seed PPL arrays for CWA=[774.22,760.62] vs GELU=[745.77,731.73], SELU=[763.10,749.50], tanh_swish=[769.44,753.82]. Run scipy.stats.ttest_ind (Welch's, n=2 forces independent). For each comparison report: t_stat, p_value (two-sided and one-sided H0: CWA>=GELU), Cohen's d = (mean_diff / pooled_std), 95% CI on difference via bootstrapping (10000 resamples with replacement).

  2. K-SATURATION DIAGNOSTIC (LM experiment): The J_s_bar_trajectory_per_layer data shows K=5 at every logged step (steps 0,100,200,300,400 for layers 0-5, seed_42). Determine definitively whether K=5 is always K_max saturation or genuine tolerance convergence. Analytical check: with rho=J*s_bar~0.45 and K=5, |m_K - m*| <= rho^K * |m_0 - m*|. Assuming |m_0 - m*| <= 1.0 (bounded tanh outputs), rho^5 = 0.45^5 = 0.0185. The tolerance delta = 1e-4*(1-J*s_bar) ~ 1e-4*0.554 = 5.54e-5. Since 0.0185 >> 5.54e-5, K=5 is NOT genuine convergence if the initial residual is order 1. However if K_max=5 was coded in the implementation (capped at 5), K=5 indicates saturation (the code hit the cap, not the tolerance). Read the method.py from art_DdhxnRglYGM6 to check actual K_max value. Report: fraction_hits_K_max (1.0 if all K values equal K_max), analytical_residual_at_K5 = rho^5 * assumed_initial_gap, required_K_for_tolerance = ceil(log(delta/1.0)/log(rho)), note whether the experiment used K_max=5 (the iter-1 default) vs the iter-2 mandated K_max=50.

  3. GRADIENT BIAS TABLE: The warm-start-T approximation (T tracked steps from detached m*) introduces O(rho^T) relative gradient bias. From LM data: J*s_bar stabilized at 0.441-0.461 across layers (mean rho~0.45). For T=3: bias = rho^T = 0.45^3 = 0.091. For T=5: bias = 0.45^5 = 0.0185. Build a table for rho in {0.3, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60} and T in {3, 5, 10}: entry = rho^T. Highlight the empirically observed (rho=0.45, T=5) cell. Compare against IFT bias: if IFT is used (rho>=0.8), delta=1e-4*(1-rho) gives bias ~1e-4 uniformly. Since rho stayed at 0.45 throughout, IFT was never triggered (0 IFT calls confirmed). Document: 'Under iter-1 training conditions (rho~0.45, T=5 iterations), warm-start-5 gradient bias is approximately 1.85% relative; negligible for training purposes. IFT path was not exercised.'

  4. P_C CONSISTENCY AUDIT: From each experiment's metadata or method.py, extract what p_c value was used for the tanh+Swish (CompetingNonlinearities) baseline. The hypothesis mandates p_c=0.83 (analytically derived from Lesser & Chowdhury 2026 edge-of-chaos condition). Check: art_kKv207AAQYq2 summary states p_c=0.5 (quenched disorder mask). Check art_DdhxnRglYGM6 summary states tanh+Swish@0.5. Both differ from mandated 0.83. Document the deviation and its impact: at p_c=0.5, the Competing Nonlinearities baseline is NOT at the edge-of-chaos critical point and thus represents a suboptimal implementation that weakens the comparison.

  5. MLP GRADIENT RATIO ANALYSIS (art_kKv207AAQYq2): The MLP experiment status='experiment_in_progress' with only depth_6 relu and gelu completed. Extract available gradient ratios: relu depth=6 ratio=0.4579, gelu depth=6 ratio=1.685. CWA at depth=6,10,20 are missing (None). Report this as incomplete data. Compute what can be computed: for the 2 completed configs, verify ratio values are plausible. Report: 'MLP experiment only completed 2 of 27 planned configurations; CWA gradient ratios unavailable for hypothesis testing.'

  6. RESNET CIFAR-100 ANALYSIS (art_SVlh9mQatV8y): Extract per-epoch accuracy trajectories for CWA and GELU in the standard_no_bn config. CWA final=0.1401, GELU final=0.1893. Compute accuracy gap: -4.92 percentage points. Mean J*s_bar=0.306 (well below critical). Report: whether the experiment has multiple seeds (check metadata n_examples=56 which is 1seed*8epochs covers only partial data); compute learning curve AUC difference; note the interim status ('experiment still running' per metadata note).

  7. SOC ANALYSIS - J STABILITY: From the J_s_bar_trajectory across all logged steps (LM experiment), compute: max |J - J_init| across all layers and seeds. From the data: J varies between 0.499038 and 0.501251 (range ~0.002). Report: J_drift_max, J_drift_std across layers, whether any layer shows monotonic trend toward criticality. This quantifies the SOC failure claim ('J remains within 0.003 of initialization').

  8. OVERALL VERDICT SYNTHESIS: Combine all findings into a structured verdict following the hypothesis's success criteria: DISCONFIRM criteria 1 (CWA within noise of baselines on all tasks - BPC difference: CWA 3.352 vs GELU 3.225, delta=+0.127 BPC, CWA is WORSE); DISCONFIRM criteria 2 (SELU and tanh+Swish match/exceed CWA on LM tasks). Emit 'DISCONFIRM' with detailed evidence breakdown by experiment.
metrics_justification: |-
  These metrics directly address the four stated objectives of the artifact direction and the hypothesis's iter-2 claims:

  (1) PAIRED T-TESTS are the correct statistical tool because: (a) paired t-test (Shakespeare, n=3 seeds) controls for between-seed variability since each seed pair uses identical initialization and data ordering — any performance difference is activation-function-pure; (b) Welch's t-test (WikiText-2, n=2 seeds) handles unequal variance without assuming homoscedasticity, appropriate for very small n; (c) one-sided p-value for H0: CWA>=GELU directly answers 'how strong is the negative result?' — a large p-value (>0.5 for one-sided CWA<GELU) would indicate CWA is systematically worse; (d) Cohen's d provides effect size independent of n, crucial for interpreting small-sample significance. These tests turn the qualitative 'CWA is worse' observation into a quantitative disconfirmation strength.

  (2) K-SATURATION DIAGNOSTIC directly addresses a critical implementation flaw flagged in the hypothesis: the hypothesis mandates K_max=50 but iter-1 code appears to have K_max=5. If K=5 is saturation rather than convergence, all CWA forward passes were computing m* to only ~1.85% accuracy rather than the mandated ~0.005% (delta~5e-5). This would explain CWA's underperformance: the activation was not correctly computing the Curie-Weiss fixed point. The diagnostic either (a) exonerates the hypothesis (K=5 was genuine convergence) or (b) identifies the primary confound (K_max too small).

  (3) GRADIENT BIAS TABLE is required because the hypothesis explicitly mandates 'acknowledging the O(rho^3 ≈ 0.09) relative gradient bias' from warm-start-3. The iter-1 code used K=5 (warm-start-5), so the bias is actually rho^5~0.019 rather than 0.09 — a favorable correction for the hypothesis. This table provides the exact numbers needed for honest reporting in the paper and prevents overstatement of the bias magnitude.

  (4) P_C CONSISTENCY AUDIT matters because: if the Competing Nonlinearities baseline used p_c=0.5 instead of the analytically-correct p_c=0.83, it was handicapped relative to its optimal configuration. This affects the interpretation of all comparisons involving tanh+Swish — CWA beat a sub-optimal version of the competitor but the correct comparison remains unmeasured. Documenting this is essential for scientific integrity and for flagging what iter-2 experiments must fix.

  (5-8) The MLP analysis, ResNet analysis, SOC analysis, and verdict synthesis collectively provide the holistic picture needed to adjudicate the hypothesis's three gating experiments (fixed-J ablation as PRIORITY 1, depth ablation as CORE MISSING, high-LR sensitivity). The verdict synthesis explicitly maps each finding to the CONFIRM/DISCONFIRM/PARTIAL criteria defined in the hypothesis's success_criteria section.

  All metrics are computable purely from the loaded JSON files using scipy.stats, numpy, and standard Python — $0 LLM API cost. The cpu_heavy profile is appropriate because no GPU operations are needed, but the full_method_out.json files may be large (150+ examples with per-layer trajectories across seeds).
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
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
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Dependency 2 ---
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
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Dependency 3 ---
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
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

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

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — evaluation metrics, agent orchestration patterns, benchmark design
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Use aii-json skill's format script with `--input eval_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to eval_out.json and full_eval_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "EvaluationExpectedFiles": {
      "description": "All expected output files from evaluation artifact.",
      "properties": {
        "script": {
          "description": "Path to eval.py script. Example: 'eval.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full evaluation JSON file. Example: 'full_eval_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini evaluation JSON file. Example: 'mini_eval_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview evaluation JSON file. Example: 'preview_eval_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "EvaluationExpectedFiles",
      "type": "object"
    }
  },
  "description": "Evaluation artifact \u2014 structured output + file metadata.\n\nEvaluates both proposed and baseline methods with appropriate metrics.\nProduces eval.py and eval_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Descriptive title (roughly 30-90 characters). Must describe content, NOT a status message.",
      "maxLength": 90,
      "minLength": 30,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/EvaluationExpectedFiles",
      "description": "All output files you created. Must include eval.py script plus full/mini/preview evaluation JSON files."
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "EvaluationArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [10] SYSTEM-USER prompt · 2026-06-16 19:46:46 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `layman_summary`: 'This evaluation statistically analyzes whether the Curie-Weiss Activation (CWA) neural network activation function outperforms standard baselines like GELU and SELU on language modeling and image tasks, finding it consistently underperforms and diagnosing a key implementation flaw (iteration cap too low) that explains the failure.' is too long (at most 250 characters, got 332)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
