# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 4 · `gen_art`
> Run: `run_6gT5lHFn8559` — Novel Activation Function
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 22:46:56 UTC

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

<research_methodology>
Design experiments like a researcher, not a programmer running a script.

- Every method needs a meaningful baseline — the current standard approach, not a strawman.
- Control your variables. When comparing methods, hold everything else constant.
- Results need variance, not just point estimates. A single run proves nothing.
- Implement the proposed method and baseline side-by-side in the same pipeline to eliminate implementation-level confounds.
</research_methodology>

<task>
Implement the research methodology as a production-ready experimental system.
Adapt your implementation approach based on the hypothesis and domain requirements.
</task>

<critical_requirements>
- Fully implement the methodology described in hypothesis
- Use appropriate frameworks based on research domain
- Load and process data from the specified data_filepath
- Complete working systems
- Handle all edge cases, errors, and exceptions properly
- Always implement baseline comparison method
</critical_requirements>

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

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_4/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx1
type: experiment
title: CWA Large-Scale IFT vs Unrolled Memory Benchmark
summary: >-
  Dedicated memory benchmark comparing IFT backward, unrolled K=50 autograd, and GELU baseline at layer widths n∈{256,1024,4096}
  with batch=64, testing both near-critical (x_scale=0.1, J*s_bar≈0.97) and saturated (x_scale=1.0, J*s_bar≈0.07) regimes.
  Primary output: ratio_ift_over_gelu[n] and ratio_ift_over_unrolled[n] to determine at what n IFT delivers meaningful memory
  savings over unrolled K=50 autograd.
runpod_compute_profile: gpu
implementation_pseudocode: |-
  # method.py — CWA Memory Benchmark
  # Measures peak GPU memory for IFT vs Unrolled vs GELU at n in {256,1024,4096}

  ## DEPENDENCIES:
  # torch, numpy, json (stdlib only — no pip installs needed)

  ## KEY PARAMETERS:
  # WIDTHS = [256, 1024, 4096]
  # X_SCALES = [0.1, 1.0]       # 0.1 → J*s_bar≈0.97 (near-critical); 1.0 → J*s_bar≈0.07 (saturated)
  # BATCH = 64
  # K_MAX = 50
  # J_RAW_FIXED = 4.0           # sigmoid(4.0) ≈ 0.982 → forces IFT path when x_scale=0.1
  # N_WARMUP = 3
  # N_MEASURE = 5

  ## STEP 1: Implement CWA_IFT_Function (torch.autograd.Function)

  class CWA_IFT_Function(torch.autograd.Function):
      @staticmethod
      def forward(ctx, x, J, K_max, tol):
          # x: (B, n), J: scalar tensor
          # Run fixed-point iteration UNDER no_grad() — stores NO intermediate tensors
          with torch.no_grad():
              B, n = x.shape
              m = torch.zeros(B, 1, device=x.device, dtype=x.dtype)
              for _ in range(K_max):
                  m_new = torch.mean(torch.tanh(x + J * m), dim=1, keepdim=True)  # (B,1)
                  if torch.max(torch.abs(m_new - m)).item() < tol:
                      m = m_new
                      break
                  m = m_new
          # y computed WITH grad engagement for output (needed for loss.backward())
          # But we'll handle this in backward manually
          y = torch.tanh(x + J * m)          # (B, n)  — this tensor IS kept for loss
          s_bar = torch.mean(1.0 - y**2, dim=1, keepdim=True)  # (B,1) = mean(sech²)
          K_actual = _  # approximate, track convergence iterations
          # Store only what backward needs: m (B,1), y (B,n), s_bar (B,1), J (scalar)
          ctx.save_for_backward(x, J, m, y, s_bar)
          ctx.B = B
          ctx.n = n
          return y

      @staticmethod
      def backward(ctx, grad_output):
          # grad_output: (B, n)
          x, J, m, y, s_bar = ctx.saved_tensors
          B, n = ctx.B, ctx.n
          # s_k = sech²(x_k + J*m*) = 1 - y_k²  (B, n)
          s = 1.0 - y**2
          # IFT gradient from research art_Lj-xi6yJR_yy:
          # dL/dx_k = s_k * [g_k + J * sum_i(g_i*s_i) / (n*(1-J*s_bar))]
          # where g_k = grad_output_k
          one_minus_Jsbar = 1.0 - J * s_bar          # (B, 1)
          sum_gs = torch.sum(grad_output * s, dim=1, keepdim=True)  # (B, 1)
          grad_x = s * (grad_output + J * sum_gs / (n * one_minus_Jsbar))  # (B, n)
          # dL/dJ via chain rule: ∂m*/∂J = m*·s̄/(1-J·s̄)
          # dL/dJ = sum_k(grad_output_k * sech²(x_k+J*m*) * m*/(1-J*s_bar))
          # = sum_k(grad_output_k * s_k) * m* / (1 - J*s_bar)   summed over batch too
          # But J is a scalar — sum over all batch and neuron dims
          grad_J = torch.sum(sum_gs * m / one_minus_Jsbar)  # scalar
          return grad_x, grad_J, None, None

  ## STEP 2: Implement CWA_Unrolled_Forward

  def cwa_unrolled_forward(x, J, K_max=50):
      # Runs ALL K iterations through autograd tape — stores K intermediate tensors
      B, n = x.shape
      m = torch.zeros(B, 1, device=x.device, dtype=x.dtype, requires_grad=False)
      for k in range(K_max):
          # Each tanh call adds (B,n) tensor to the autograd graph
          m = torch.mean(torch.tanh(x + J * m), dim=1, keepdim=True)  # (B,1)
      y = torch.tanh(x + J * m)
      return y

  ## STEP 3: Implement measurement harness

  def measure_peak_memory_MB(fn, *args, n_warmup=3, n_measure=5):
      # Warmup to avoid cold-start artifacts
      for _ in range(n_warmup):
          out = fn(*args)
          loss = out.sum()
          loss.backward()
          # Zero grads but keep tensors alive
          for a in args:
              if isinstance(a, torch.Tensor) and a.grad is not None:
                  a.grad = None
          del out, loss
          torch.cuda.empty_cache()
      # Measure
      peak_mbs = []
      for _ in range(n_measure):
          torch.cuda.reset_peak_memory_stats()
          gc.collect()
          torch.cuda.empty_cache()
          out = fn(*args)
          loss = out.sum()
          loss.backward()
          peak_mb = torch.cuda.max_memory_allocated() / 1e6
          peak_mbs.append(peak_mb)
          for a in args:
              if isinstance(a, torch.Tensor) and a.grad is not None:
                  a.grad = None
          del out, loss
      return float(np.mean(peak_mbs)), float(np.std(peak_mbs))

  ## STEP 4: Grid sweep

  results = []
  for n in [256, 1024, 4096]:
      for x_scale in [0.1, 1.0]:
          # Shared input: fresh for each (n, x_scale)
          x_data = (torch.randn(64, n, device='cuda') * x_scale)

          ## --- MODE: GELU ---
          linear = nn.Linear(n, n, bias=False).cuda()
          gelu = nn.GELU()
          def gelu_fn():
              x_in = x_data.clone().requires_grad_(True)
              return gelu(linear(x_in))
          mem_gelu, std_gelu = measure_peak_memory_MB(gelu_fn)

          ## --- MODE: IFT ---
          J_raw = torch.tensor(4.0, device='cuda', requires_grad=True)  # J≈0.982
          J = torch.sigmoid(J_raw)
          # Compute actual J*s_bar at this x_scale for reporting
          with torch.no_grad():
              m_test = torch.zeros(64, 1, device='cuda')
              for _ in range(50):
                  m_new = torch.mean(torch.tanh(x_data + J * m_test), dim=1, keepdim=True)
                  if torch.max(torch.abs(m_new - m_test)).item() < 1e-6:
                      m_test = m_new; break
                  m_test = m_new
              y_test = torch.tanh(x_data + J * m_test)
              s_bar_test = float(torch.mean(1.0 - y_test**2).item())
              Jsbar = float(J.item()) * s_bar_test

          def ift_fn():
              x_in = x_data.clone().requires_grad_(True)
              J_param = torch.tensor(4.0, device='cuda', requires_grad=True)
              J_val = torch.sigmoid(J_param)
              return CWA_IFT_Function.apply(x_in, J_val, 50, 1e-6)
          mem_ift, std_ift = measure_peak_memory_MB(ift_fn)

          ## --- MODE: UNROLLED K=50 ---
          def unrolled_fn():
              x_in = x_data.clone().requires_grad_(True)
              J_param = torch.tensor(4.0, device='cuda', requires_grad=True)
              J_val = torch.sigmoid(J_param)
              return cwa_unrolled_forward(x_in, J_val, K_max=50)
          mem_unrolled, std_unrolled = measure_peak_memory_MB(unrolled_fn)

          # Compute ratios
          ratio_ift_gelu = mem_ift / mem_gelu if mem_gelu > 0 else float('inf')
          ratio_ift_unrolled = mem_ift / mem_unrolled if mem_unrolled > 0 else float('inf')
          ratio_unrolled_gelu = mem_unrolled / mem_gelu if mem_gelu > 0 else float('inf')

          # Log results
          print(f'n={n}, x_scale={x_scale}, J*s_bar={Jsbar:.3f}')
          print(f'  GELU: {mem_gelu:.1f} MB  IFT: {mem_ift:.1f} MB  Unrolled: {mem_unrolled:.1f} MB')
          print(f'  IFT/GELU={ratio_ift_gelu:.2f}x  IFT/Unrolled={ratio_ift_unrolled:.2f}x  Unrolled/GELU={ratio_unrolled_gelu:.2f}x')

          results.append({
              'n': n,
              'x_scale': x_scale,
              'J': float(torch.sigmoid(torch.tensor(4.0)).item()),
              'Jsbar': Jsbar,
              'sbar': s_bar_test,
              'peak_MB_gelu': mem_gelu,
              'peak_MB_ift': mem_ift,
              'peak_MB_unrolled': mem_unrolled,
              'ratio_ift_over_gelu': ratio_ift_gelu,
              'ratio_ift_over_unrolled': ratio_ift_unrolled,
              'ratio_unrolled_over_gelu': ratio_unrolled_gelu,
              'std_gelu': std_gelu,
              'std_ift': std_ift,
              'std_unrolled': std_unrolled
          })

  ## STEP 5: Output method_out.json in exp_gen_sol_out schema
  # Each benchmark run = one 'example' with input config and output metrics
  examples = []
  for r in results:
      for mode, mem_key, ratio_key in [
          ('gelu', 'peak_MB_gelu', None),
          ('ift', 'peak_MB_ift', 'ratio_ift_over_gelu'),
          ('unrolled', 'peak_MB_unrolled', 'ratio_unrolled_over_gelu')
      ]:
          ex = {
              'id': f'n{r["n"]}_xscale{r["x_scale"]}_{mode}',
              'input': {
                  'n': r['n'],
                  'x_scale': r['x_scale'],
                  'mode': mode,
                  'batch': 64,
                  'K_max': 50,
                  'J_raw': 4.0,
                  'J': r['J'],
                  'Jsbar': r['Jsbar'],
                  'sbar': r['sbar']
              },
              'output': {
                  'peak_MB': r[mem_key],
                  'peak_MB_std': r[f'std_{mode}'],
                  'ratio_over_gelu': r[ratio_key] if ratio_key else 1.0,
                  'ratio_ift_over_unrolled': r['ratio_ift_over_unrolled'] if mode == 'ift' else None,
                  'ratio_unrolled_over_gelu': r['ratio_unrolled_over_gelu'] if mode == 'unrolled' else None
              },
              'prediction': {
                  'expected_ratio_theory': (
                      1.0 if mode == 'gelu' else
                      (1.0 if mode == 'ift' else 50.0)  # IFT≈GELU; Unrolled=50×GELU
                  ),
                  'hypothesis_claim': (
                      'IFT stores only m* (B,1) + output y (B,n) → O(n)' if mode == 'ift' else
                      ('Unrolled stores K=50 intermediate (B,1) tanh outputs → O(K)' if mode == 'unrolled' else
                       'GELU baseline: stores input activations (B,n) → O(n)')
                  )
              },
              'label': {
                  'confirms_ift_advantage': (
                      r['ratio_ift_over_unrolled'] < 0.5 if mode == 'ift' else None
                  ),
                  'ift_within_2x_gelu': (
                      r['ratio_ift_over_gelu'] <= 2.0 if mode == 'ift' else None
                  )
              }
          }
          examples.append(ex)

  method_out = {
      'schema': 'exp_gen_sol_out',
      'experiment': 'cwa_memory_benchmark',
      'description': 'Peak GPU memory comparison: IFT vs Unrolled K=50 vs GELU at n in {256,1024,4096}',
      'examples': examples,
      'summary': {
          'finding': <filled at runtime>,
          'ift_2x_criterion_met_at_n': <list of n where ratio_ift_gelu <= 2.0>,
          'ift_meaningful_savings_vs_unrolled_at_n': <list of n where ratio_ift_unrolled < 0.5>,
          'peak_jsbar_near_critical': <Jsbar at x_scale=0.1>,
          'peak_jsbar_saturated': <Jsbar at x_scale=1.0>
      }
  }
  with open('method_out.json', 'w') as f:
      json.dump(method_out, f, indent=2)
fallback_plan: |-
  ## Primary Failure Scenarios

  ### Failure 1: CUDA OOM at n=4096 with unrolled K=50
  K=50 iterations at n=4096, batch=64: 50 × 64 × 4096 × 4 bytes ≈ 52MB for intermediate tanh outputs, plus gradients → ~104MB; well within 20GB VRAM. OOM is unlikely. But if it occurs: reduce K to K=20 for unrolled, report at K=20 and note in summary.

  ### Failure 2: IFT backward produces NaN gradients
  Root cause: J*s_bar → 1 causes 1/(1-J*s_bar) to blow up. Fix: check that with J_raw=4.0 (J≈0.982) and x_scale=0.1, J*s_bar is verified to stay < 1. At x_scale=0.1, inputs to tanh are small, sech²≈1, so J*s_bar ≈ 0.982 × 1.0 = 0.982 — stable but high. If NaN appears, reduce J_raw to 3.0 (J≈0.952) or add clamping: one_minus_Jsbar = max(one_minus_Jsbar, 0.01).

  ### Failure 3: Fixed-point iteration diverges (no convergence in K=50)
  At J*s_bar < 1 convergence is guaranteed by Banach theorem. Geometric rate ρ=J*s_bar. At J*s_bar=0.97: residual after 50 steps = 0.97^50 × |m_0 - m*| ≈ 0.22 × initial error — may not fully converge. Fix: increase tol to 1e-4 (which is the adaptive tolerance from the hypothesis) or increase K_max to 200 for x_scale=0.1. Log actual K_actual for all runs.

  ### Failure 4: Memory measurement unreliable (GPU running other processes)
  Fix: add torch.cuda.synchronize() before and after the measured forward+backward pass. Use the minimum over N_MEASURE=5 runs (not mean) as the peak memory estimate, since other processes can inflate but not deflate readings.

  ### Fallback simplified version:
  If CUDA memory APIs are unavailable (CPU fallback): use tracemalloc Python memory tracking instead. Switch torch.cuda.max_memory_allocated() to tracemalloc snapshot comparison. This gives RAM not VRAM but still demonstrates the O(K*n) vs O(n) scaling difference.

  ### Fallback output if GPU unavailable:
  Run on CPU with n in {64, 256, 1024} only (skip n=4096 for time), measuring Python process RSS memory via psutil.Process().memory_info().rss before and after each call. Report memory_overhead_bytes instead of peak_MB_gpu.
testing_plan: |-
  ## Validation Strategy

  ### Step 0: Smoke test at n=64, K=10 (< 5 seconds)
  - Run IFT backward on tiny (batch=4, n=64) input, check:
    - Forward output matches unrolled output to tolerance 1e-4
    - IFT gradient matches unrolled gradient to tolerance 1e-3 (they should be close since K=50 unrolled is near-converged)
    - No NaN in gradients
    - Memory APIs return nonzero values
  - Print J, J*s_bar at x_scale=0.1 and x_scale=1.0 to confirm near-critical vs saturated regime

  ### Step 1: Gradient correctness check via torch.autograd.gradcheck
  - Run torch.autograd.gradcheck(CWA_IFT_Function.apply, inputs=(x_small, J_val, 50, 1e-7)) with x_small shape (4, 16)
  - Expect gradcheck to pass (default rtol=1e-3, atol=1e-5 is sufficient for the IFT approximation)
  - If gradcheck fails: add eps=1e-4 argument (larger finite difference step for numerical stability)

  ### Step 2: Quick memory scaling check at n=256 only
  - Run 3 warmup + 3 measure passes for all 3 modes at n=256
  - Confirm: unrolled memory > ift memory (this must hold; if not, there's an implementation bug where unrolled isn't actually tracking grads)
  - Check that ratios are in plausible range: unrolled/gelu should be >> 1 at n=256, K=50

  ### Step 3: Verify J*s_bar diagnostic
  - At x_scale=0.1, n=256: print J*s_bar, confirm it is > 0.8 (IFT path active)
  - At x_scale=1.0, n=256: print J*s_bar, confirm it is < 0.5 (deep saturation, matching the hypothesis's claim that J*s_bar ≈ 0.07 at |x|≈2.0)
  - This is a critical sanity check: if x_scale=0.1 gives J*s_bar < 0.8, the IFT regime is not being tested

  ### Step 4: Full benchmark n∈{256,1024,4096}
  - Run all 3×2×3=18 configurations
  - Expected pattern to confirm:
    - ratio_unrolled_gelu should scale roughly as K=50 (50×) regardless of n (O(K) overhead)
    - ratio_ift_gelu should stay near 1.0-2.0 regardless of n (O(1) overhead w.r.t. K)
    - The 'crossover' where IFT clearly beats unrolled should be visible at all n
  - If ratio_ift_gelu >> 5.57 (the prior micro-benchmark result), investigate: check that forward pass is actually running under no_grad()

  ### Step 5: Output validation
  - Confirm method_out.json is valid JSON with 'examples' array of 18 entries
  - Each entry has id, input, output, prediction, label fields
  - Report the IFT/GELU ratio at n=4096, x_scale=0.1 as the PRIMARY finding
  - Explicitly state whether the 2× memory criterion from the hypothesis is met at any n
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

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
out_dependency_files:
  file_list:
  - research_out.json

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

- **Multi-LLM Agents** — framework choices, implementation patterns, agent orchestration
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-06-16 22:46:56 UTC

```
Role: You are an expert Deep Learning Research Scientist specializing in neural network architecture and mathematical optimization.Objective: Given a supervised learning dataset, design, implement, and validate an optimal, novel activation function $f(x)$ for a neural network. Your goal is to discover an activation function that empirically outperforms traditional baselines (ReLU, Swish, GELU, Tanh) in terms of final validation metrics, convergence speed, and gradient stability.Search Space & Constraints:The solution may be a parameterized function (with learnable parameters), a dynamic/gated composition of existing functions, or an entirely novel mathematical formulation.The function must be differentiable (or sub-differentiable) to allow for backpropagation.Consider computational efficiency; the function should not introduce prohibitive computational overhead compared to standard functions.
```

### [3] SKILL-INPUT — aii-python · 2026-06-16 22:47:18 UTC

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

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-06-16 22:47:20 UTC

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

### [5] SKILL-INPUT — aii-json · 2026-06-16 22:47:22 UTC

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

### [6] SKILL-INPUT — aii-use-hardware · 2026-06-16 22:47:22 UTC

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

### [7] SKILL-INPUT — aii-file-size-limit · 2026-06-16 22:47:28 UTC

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

### [8] SKILL-INPUT — aii-parallel-computing · 2026-06-16 22:47:28 UTC

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

### [9] SYSTEM-USER prompt · 2026-06-16 22:57:32 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_4/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx1
type: experiment
title: CWA Large-Scale IFT vs Unrolled Memory Benchmark
summary: >-
  Dedicated memory benchmark comparing IFT backward, unrolled K=50 autograd, and GELU baseline at layer widths n∈{256,1024,4096}
  with batch=64, testing both near-critical (x_scale=0.1, J*s_bar≈0.97) and saturated (x_scale=1.0, J*s_bar≈0.07) regimes.
  Primary output: ratio_ift_over_gelu[n] and ratio_ift_over_unrolled[n] to determine at what n IFT delivers meaningful memory
  savings over unrolled K=50 autograd.
runpod_compute_profile: gpu
implementation_pseudocode: |-
  # method.py — CWA Memory Benchmark
  # Measures peak GPU memory for IFT vs Unrolled vs GELU at n in {256,1024,4096}

  ## DEPENDENCIES:
  # torch, numpy, json (stdlib only — no pip installs needed)

  ## KEY PARAMETERS:
  # WIDTHS = [256, 1024, 4096]
  # X_SCALES = [0.1, 1.0]       # 0.1 → J*s_bar≈0.97 (near-critical); 1.0 → J*s_bar≈0.07 (saturated)
  # BATCH = 64
  # K_MAX = 50
  # J_RAW_FIXED = 4.0           # sigmoid(4.0) ≈ 0.982 → forces IFT path when x_scale=0.1
  # N_WARMUP = 3
  # N_MEASURE = 5

  ## STEP 1: Implement CWA_IFT_Function (torch.autograd.Function)

  class CWA_IFT_Function(torch.autograd.Function):
      @staticmethod
      def forward(ctx, x, J, K_max, tol):
          # x: (B, n), J: scalar tensor
          # Run fixed-point iteration UNDER no_grad() — stores NO intermediate tensors
          with torch.no_grad():
              B, n = x.shape
              m = torch.zeros(B, 1, device=x.device, dtype=x.dtype)
              for _ in range(K_max):
                  m_new = torch.mean(torch.tanh(x + J * m), dim=1, keepdim=True)  # (B,1)
                  if torch.max(torch.abs(m_new - m)).item() < tol:
                      m = m_new
                      break
                  m = m_new
          # y computed WITH grad engagement for output (needed for loss.backward())
          # But we'll handle this in backward manually
          y = torch.tanh(x + J * m)          # (B, n)  — this tensor IS kept for loss
          s_bar = torch.mean(1.0 - y**2, dim=1, keepdim=True)  # (B,1) = mean(sech²)
          K_actual = _  # approximate, track convergence iterations
          # Store only what backward needs: m (B,1), y (B,n), s_bar (B,1), J (scalar)
          ctx.save_for_backward(x, J, m, y, s_bar)
          ctx.B = B
          ctx.n = n
          return y

      @staticmethod
      def backward(ctx, grad_output):
          # grad_output: (B, n)
          x, J, m, y, s_bar = ctx.saved_tensors
          B, n = ctx.B, ctx.n
          # s_k = sech²(x_k + J*m*) = 1 - y_k²  (B, n)
          s = 1.0 - y**2
          # IFT gradient from research art_Lj-xi6yJR_yy:
          # dL/dx_k = s_k * [g_k + J * sum_i(g_i*s_i) / (n*(1-J*s_bar))]
          # where g_k = grad_output_k
          one_minus_Jsbar = 1.0 - J * s_bar          # (B, 1)
          sum_gs = torch.sum(grad_output * s, dim=1, keepdim=True)  # (B, 1)
          grad_x = s * (grad_output + J * sum_gs / (n * one_minus_Jsbar))  # (B, n)
          # dL/dJ via chain rule: ∂m*/∂J = m*·s̄/(1-J·s̄)
          # dL/dJ = sum_k(grad_output_k * sech²(x_k+J*m*) * m*/(1-J*s_bar))
          # = sum_k(grad_output_k * s_k) * m* / (1 - J*s_bar)   summed over batch too
          # But J is a scalar — sum over all batch and neuron dims
          grad_J = torch.sum(sum_gs * m / one_minus_Jsbar)  # scalar
          return grad_x, grad_J, None, None

  ## STEP 2: Implement CWA_Unrolled_Forward

  def cwa_unrolled_forward(x, J, K_max=50):
      # Runs ALL K iterations through autograd tape — stores K intermediate tensors
      B, n = x.shape
      m = torch.zeros(B, 1, device=x.device, dtype=x.dtype, requires_grad=False)
      for k in range(K_max):
          # Each tanh call adds (B,n) tensor to the autograd graph
          m = torch.mean(torch.tanh(x + J * m), dim=1, keepdim=True)  # (B,1)
      y = torch.tanh(x + J * m)
      return y

  ## STEP 3: Implement measurement harness

  def measure_peak_memory_MB(fn, *args, n_warmup=3, n_measure=5):
      # Warmup to avoid cold-start artifacts
      for _ in range(n_warmup):
          out = fn(*args)
          loss = out.sum()
          loss.backward()
          # Zero grads but keep tensors alive
          for a in args:
              if isinstance(a, torch.Tensor) and a.grad is not None:
                  a.grad = None
          del out, loss
          torch.cuda.empty_cache()
      # Measure
      peak_mbs = []
      for _ in range(n_measure):
          torch.cuda.reset_peak_memory_stats()
          gc.collect()
          torch.cuda.empty_cache()
          out = fn(*args)
          loss = out.sum()
          loss.backward()
          peak_mb = torch.cuda.max_memory_allocated() / 1e6
          peak_mbs.append(peak_mb)
          for a in args:
              if isinstance(a, torch.Tensor) and a.grad is not None:
                  a.grad = None
          del out, loss
      return float(np.mean(peak_mbs)), float(np.std(peak_mbs))

  ## STEP 4: Grid sweep

  results = []
  for n in [256, 1024, 4096]:
      for x_scale in [0.1, 1.0]:
          # Shared input: fresh for each (n, x_scale)
          x_data = (torch.randn(64, n, device='cuda') * x_scale)

          ## --- MODE: GELU ---
          linear = nn.Linear(n, n, bias=False).cuda()
          gelu = nn.GELU()
          def gelu_fn():
              x_in = x_data.clone().requires_grad_(True)
              return gelu(linear(x_in))
          mem_gelu, std_gelu = measure_peak_memory_MB(gelu_fn)

          ## --- MODE: IFT ---
          J_raw = torch.tensor(4.0, device='cuda', requires_grad=True)  # J≈0.982
          J = torch.sigmoid(J_raw)
          # Compute actual J*s_bar at this x_scale for reporting
          with torch.no_grad():
              m_test = torch.zeros(64, 1, device='cuda')
              for _ in range(50):
                  m_new = torch.mean(torch.tanh(x_data + J * m_test), dim=1, keepdim=True)
                  if torch.max(torch.abs(m_new - m_test)).item() < 1e-6:
                      m_test = m_new; break
                  m_test = m_new
              y_test = torch.tanh(x_data + J * m_test)
              s_bar_test = float(torch.mean(1.0 - y_test**2).item())
              Jsbar = float(J.item()) * s_bar_test

          def ift_fn():
              x_in = x_data.clone().requires_grad_(True)
              J_param = torch.tensor(4.0, device='cuda', requires_grad=True)
              J_val = torch.sigmoid(J_param)
              return CWA_IFT_Function.apply(x_in, J_val, 50, 1e-6)
          mem_ift, std_ift = measure_peak_memory_MB(ift_fn)

          ## --- MODE: UNROLLED K=50 ---
          def unrolled_fn():
              x_in = x_data.clone().requires_grad_(True)
              J_param = torch.tensor(4.0, device='cuda', requires_grad=True)
              J_val = torch.sigmoid(J_param)
              return cwa_unrolled_forward(x_in, J_val, K_max=50)
          mem_unrolled, std_unrolled = measure_peak_memory_MB(unrolled_fn)

          # Compute ratios
          ratio_ift_gelu = mem_ift / mem_gelu if mem_gelu > 0 else float('inf')
          ratio_ift_unrolled = mem_ift / mem_unrolled if mem_unrolled > 0 else float('inf')
          ratio_unrolled_gelu = mem_unrolled / mem_gelu if mem_gelu > 0 else float('inf')

          # Log results
          print(f'n={n}, x_scale={x_scale}, J*s_bar={Jsbar:.3f}')
          print(f'  GELU: {mem_gelu:.1f} MB  IFT: {mem_ift:.1f} MB  Unrolled: {mem_unrolled:.1f} MB')
          print(f'  IFT/GELU={ratio_ift_gelu:.2f}x  IFT/Unrolled={ratio_ift_unrolled:.2f}x  Unrolled/GELU={ratio_unrolled_gelu:.2f}x')

          results.append({
              'n': n,
              'x_scale': x_scale,
              'J': float(torch.sigmoid(torch.tensor(4.0)).item()),
              'Jsbar': Jsbar,
              'sbar': s_bar_test,
              'peak_MB_gelu': mem_gelu,
              'peak_MB_ift': mem_ift,
              'peak_MB_unrolled': mem_unrolled,
              'ratio_ift_over_gelu': ratio_ift_gelu,
              'ratio_ift_over_unrolled': ratio_ift_unrolled,
              'ratio_unrolled_over_gelu': ratio_unrolled_gelu,
              'std_gelu': std_gelu,
              'std_ift': std_ift,
              'std_unrolled': std_unrolled
          })

  ## STEP 5: Output method_out.json in exp_gen_sol_out schema
  # Each benchmark run = one 'example' with input config and output metrics
  examples = []
  for r in results:
      for mode, mem_key, ratio_key in [
          ('gelu', 'peak_MB_gelu', None),
          ('ift', 'peak_MB_ift', 'ratio_ift_over_gelu'),
          ('unrolled', 'peak_MB_unrolled', 'ratio_unrolled_over_gelu')
      ]:
          ex = {
              'id': f'n{r["n"]}_xscale{r["x_scale"]}_{mode}',
              'input': {
                  'n': r['n'],
                  'x_scale': r['x_scale'],
                  'mode': mode,
                  'batch': 64,
                  'K_max': 50,
                  'J_raw': 4.0,
                  'J': r['J'],
                  'Jsbar': r['Jsbar'],
                  'sbar': r['sbar']
              },
              'output': {
                  'peak_MB': r[mem_key],
                  'peak_MB_std': r[f'std_{mode}'],
                  'ratio_over_gelu': r[ratio_key] if ratio_key else 1.0,
                  'ratio_ift_over_unrolled': r['ratio_ift_over_unrolled'] if mode == 'ift' else None,
                  'ratio_unrolled_over_gelu': r['ratio_unrolled_over_gelu'] if mode == 'unrolled' else None
              },
              'prediction': {
                  'expected_ratio_theory': (
                      1.0 if mode == 'gelu' else
                      (1.0 if mode == 'ift' else 50.0)  # IFT≈GELU; Unrolled=50×GELU
                  ),
                  'hypothesis_claim': (
                      'IFT stores only m* (B,1) + output y (B,n) → O(n)' if mode == 'ift' else
                      ('Unrolled stores K=50 intermediate (B,1) tanh outputs → O(K)' if mode == 'unrolled' else
                       'GELU baseline: stores input activations (B,n) → O(n)')
                  )
              },
              'label': {
                  'confirms_ift_advantage': (
                      r['ratio_ift_over_unrolled'] < 0.5 if mode == 'ift' else None
                  ),
                  'ift_within_2x_gelu': (
                      r['ratio_ift_over_gelu'] <= 2.0 if mode == 'ift' else None
                  )
              }
          }
          examples.append(ex)

  method_out = {
      'schema': 'exp_gen_sol_out',
      'experiment': 'cwa_memory_benchmark',
      'description': 'Peak GPU memory comparison: IFT vs Unrolled K=50 vs GELU at n in {256,1024,4096}',
      'examples': examples,
      'summary': {
          'finding': <filled at runtime>,
          'ift_2x_criterion_met_at_n': <list of n where ratio_ift_gelu <= 2.0>,
          'ift_meaningful_savings_vs_unrolled_at_n': <list of n where ratio_ift_unrolled < 0.5>,
          'peak_jsbar_near_critical': <Jsbar at x_scale=0.1>,
          'peak_jsbar_saturated': <Jsbar at x_scale=1.0>
      }
  }
  with open('method_out.json', 'w') as f:
      json.dump(method_out, f, indent=2)
fallback_plan: |-
  ## Primary Failure Scenarios

  ### Failure 1: CUDA OOM at n=4096 with unrolled K=50
  K=50 iterations at n=4096, batch=64: 50 × 64 × 4096 × 4 bytes ≈ 52MB for intermediate tanh outputs, plus gradients → ~104MB; well within 20GB VRAM. OOM is unlikely. But if it occurs: reduce K to K=20 for unrolled, report at K=20 and note in summary.

  ### Failure 2: IFT backward produces NaN gradients
  Root cause: J*s_bar → 1 causes 1/(1-J*s_bar) to blow up. Fix: check that with J_raw=4.0 (J≈0.982) and x_scale=0.1, J*s_bar is verified to stay < 1. At x_scale=0.1, inputs to tanh are small, sech²≈1, so J*s_bar ≈ 0.982 × 1.0 = 0.982 — stable but high. If NaN appears, reduce J_raw to 3.0 (J≈0.952) or add clamping: one_minus_Jsbar = max(one_minus_Jsbar, 0.01).

  ### Failure 3: Fixed-point iteration diverges (no convergence in K=50)
  At J*s_bar < 1 convergence is guaranteed by Banach theorem. Geometric rate ρ=J*s_bar. At J*s_bar=0.97: residual after 50 steps = 0.97^50 × |m_0 - m*| ≈ 0.22 × initial error — may not fully converge. Fix: increase tol to 1e-4 (which is the adaptive tolerance from the hypothesis) or increase K_max to 200 for x_scale=0.1. Log actual K_actual for all runs.

  ### Failure 4: Memory measurement unreliable (GPU running other processes)
  Fix: add torch.cuda.synchronize() before and after the measured forward+backward pass. Use the minimum over N_MEASURE=5 runs (not mean) as the peak memory estimate, since other processes can inflate but not deflate readings.

  ### Fallback simplified version:
  If CUDA memory APIs are unavailable (CPU fallback): use tracemalloc Python memory tracking instead. Switch torch.cuda.max_memory_allocated() to tracemalloc snapshot comparison. This gives RAM not VRAM but still demonstrates the O(K*n) vs O(n) scaling difference.

  ### Fallback output if GPU unavailable:
  Run on CPU with n in {64, 256, 1024} only (skip n=4096 for time), measuring Python process RSS memory via psutil.Process().memory_info().rss before and after each call. Report memory_overhead_bytes instead of peak_MB_gpu.
testing_plan: |-
  ## Validation Strategy

  ### Step 0: Smoke test at n=64, K=10 (< 5 seconds)
  - Run IFT backward on tiny (batch=4, n=64) input, check:
    - Forward output matches unrolled output to tolerance 1e-4
    - IFT gradient matches unrolled gradient to tolerance 1e-3 (they should be close since K=50 unrolled is near-converged)
    - No NaN in gradients
    - Memory APIs return nonzero values
  - Print J, J*s_bar at x_scale=0.1 and x_scale=1.0 to confirm near-critical vs saturated regime

  ### Step 1: Gradient correctness check via torch.autograd.gradcheck
  - Run torch.autograd.gradcheck(CWA_IFT_Function.apply, inputs=(x_small, J_val, 50, 1e-7)) with x_small shape (4, 16)
  - Expect gradcheck to pass (default rtol=1e-3, atol=1e-5 is sufficient for the IFT approximation)
  - If gradcheck fails: add eps=1e-4 argument (larger finite difference step for numerical stability)

  ### Step 2: Quick memory scaling check at n=256 only
  - Run 3 warmup + 3 measure passes for all 3 modes at n=256
  - Confirm: unrolled memory > ift memory (this must hold; if not, there's an implementation bug where unrolled isn't actually tracking grads)
  - Check that ratios are in plausible range: unrolled/gelu should be >> 1 at n=256, K=50

  ### Step 3: Verify J*s_bar diagnostic
  - At x_scale=0.1, n=256: print J*s_bar, confirm it is > 0.8 (IFT path active)
  - At x_scale=1.0, n=256: print J*s_bar, confirm it is < 0.5 (deep saturation, matching the hypothesis's claim that J*s_bar ≈ 0.07 at |x|≈2.0)
  - This is a critical sanity check: if x_scale=0.1 gives J*s_bar < 0.8, the IFT regime is not being tested

  ### Step 4: Full benchmark n∈{256,1024,4096}
  - Run all 3×2×3=18 configurations
  - Expected pattern to confirm:
    - ratio_unrolled_gelu should scale roughly as K=50 (50×) regardless of n (O(K) overhead)
    - ratio_ift_gelu should stay near 1.0-2.0 regardless of n (O(1) overhead w.r.t. K)
    - The 'crossover' where IFT clearly beats unrolled should be visible at all n
  - If ratio_ift_gelu >> 5.57 (the prior micro-benchmark result), investigate: check that forward pass is actually running under no_grad()

  ### Step 5: Output validation
  - Confirm method_out.json is valid JSON with 'examples' array of 18 entries
  - Each entry has id, input, output, prediction, label fields
  - Report the IFT/GELU ratio at n=4096, x_scale=0.1 as the PRIMARY finding
  - Explicitly state whether the 2× memory criterion from the hypothesis is met at any n
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

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
out_dependency_files:
  file_list:
  - research_out.json

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

- **Multi-LLM Agents** — framework choices, implementation patterns, agent orchestration
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
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
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
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
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [10] SYSTEM-USER prompt · 2026-06-16 22:58:48 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `layman_summary`: "This experiment measures how much GPU memory three approaches to running the Curie-Weiss Activation (CWA) use: a smart 'implicit' backward pass (IFT), a naive unrolled 50-step loop, and a standard GELU layer, showing that IFT uses up to 90% less memory at large layer sizes." is too long (at most 250 characters, got 274)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
