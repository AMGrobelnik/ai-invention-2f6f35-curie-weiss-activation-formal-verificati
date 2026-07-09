# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_6gT5lHFn8559` — Novel Activation Function
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-16 19:38:45 UTC

````
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

<CRITICAL_WARNING__PREVIOUS_ATTEMPT_CRASHED>
YOUR PREVIOUS EXECUTION ATTEMPT CATASTROPHICALLY FAILED.
The entire worker container crashed after 479s.
Error: Pod launch failed — no instance booted (tried 15, 0 still out of stock): Ability server transient error for 'aii_runpod__gen_pod': 502 <!DOCTYPE html>
<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en-US"> <![endif]-->
<!--[if IE 7]>    <html class="no-js ie7 oldie" lang="en-US"> <![endif]-->
<!--[if IE 8]>    <html class="no-

This was NOT a normal code error — the entire container died. Study the error
and last messages above carefully. Identify what caused the crash and be
EXTREMELY careful to avoid repeating it. Do NOT use the same approach.
</CRITICAL_WARNING__PREVIOUS_ATTEMPT_CRASHED>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
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
title: CWA Unnormalized MLP Depth Sweep + Fixed-J Ablation on CIFAR-10
summary: >-
  GPU experiment implementing Curie-Weiss Activation (CWA) with exact IFT gradients in unnormalized MLPs at depths {6,10,20},
  3 seeds, 25 epochs on CIFAR-10, plus a decisive fixed-J ablation (J frozen at {0.1,0.3,0.5,0.7,0.9}) at depth 10. Primary
  metrics: per-layer gradient norm ratio, final accuracy, and J·s̄ trajectory. Outputs method_out.json.
runpod_compute_profile: gpu
implementation_pseudocode: "## File: method.py\n\n### 0. Dependencies and imports\n```\npip install torch torchvision tqdm\n\
  import torch, torch.nn as nn, torch.nn.functional as F\nimport torchvision, torchvision.transforms as T\nimport numpy as\
  \ np, json, os, math\nfrom torch.optim.lr_scheduler import CosineAnnealingLR\n```\n\n---\n\n### 1. CWALayer — core module\n\
  \n```python\nclass CWAFunction(torch.autograd.Function):\n    @staticmethod\n    def forward(ctx, x, J, K_max=50):\n   \
  \     # J is a scalar tensor (detached value, no grad here)\n        J_val = J.item()\n        delta = 1e-4 * (1.0 - J_val)\
  \          # Lean Theorem 3 tolerance\n        n = x.shape[-1]\n\n        # Fixed-point iteration (no grad)\n        with\
  \ torch.no_grad():\n            m = torch.zeros(x.shape[:-1] + (1,), device=x.device, dtype=x.dtype)\n            for k\
  \ in range(K_max):\n                m_new = torch.mean(torch.tanh(x + J_val * m), dim=-1, keepdim=True)\n              \
  \  if (m_new - m).abs().max().item() < delta:\n                    m = m_new\n                    break\n              \
  \  m = m_new\n            m_star = m.squeeze(-1)   # shape: (*batch)\n\n        # Compute sech^2 at converged point\n  \
  \      z = x + J_val * m_star.unsqueeze(-1)   # (batch, n)\n        s = 1.0 - torch.tanh(z)**2              # sech^2, shape\
  \ (batch, n)\n        s_bar = s.mean(dim=-1, keepdim=True)    # (batch, 1)\n        y = torch.tanh(z)                  \
  \      # output activations\n\n        J_s_bar = J_val * s_bar.mean().item()\n        ctx.save_for_backward(x, J, m_star.unsqueeze(-1),\
  \ s, s_bar)\n        ctx.J_val = J_val\n        ctx.J_s_bar = J_s_bar\n        ctx.use_ift = (J_s_bar >= 0.8)\n        return\
  \ y, torch.tensor(J_s_bar), m_star\n\n    @staticmethod\n    def backward(ctx, grad_y, grad_Jbar, grad_mstar):\n       \
  \ x, J, m_star_unsq, s, s_bar = ctx.saved_tensors\n        J_val = ctx.J_val\n        J_s_bar = ctx.J_s_bar\n        n =\
  \ x.shape[-1]\n        one_minus_Jbar = max(1.0 - J_s_bar, 1e-6)  # numerical safety\n\n        if ctx.use_ift:\n      \
  \      # IFT BRANCH (J*s_bar >= 0.8): exact O(n) closed-form\n            # From research artifact Eq. A:\n            #\
  \   dL/dx_k = s_k * [g_k + J * (sum_i g_i*s_i) / (n * (1-J*s_bar))]\n            #   dL/dJ   = m_star * s_bar * (sum_i g_i*s_i)\
  \ / (1-J*s_bar)\n            g = grad_y                                  # (batch, n)\n            gs_sum = (g * s).sum(dim=-1,\
  \ keepdim=True) # (batch, 1)\n            scale = J_val / (n * one_minus_Jbar)\n            grad_x = s * (g + scale * gs_sum)\n\
  \            grad_J = (m_star_unsq * s_bar * gs_sum / one_minus_Jbar).sum()\n        else:\n            # UNROLLED BRANCH\
  \ (J*s_bar < 0.8): warm-start-3 approximation\n            # Run K steps without grad to find m*, then 3 tracked steps\n\
  \            # Introduces O((J*s_bar)^3) relative gradient bias — acceptable when J*s_bar<0.8\n            # (bias < 0.8^3\
  \ = 0.512 relative, but typically J*s_bar ~ 0.4-0.5 so ~0.1)\n            # For gradient wrt x: use same IFT formula since\
  \ it's O(n) exact anyway\n            g = grad_y\n            gs_sum = (g * s).sum(dim=-1, keepdim=True)\n            scale\
  \ = J_val / (n * one_minus_Jbar)\n            grad_x = s * (g + scale * gs_sum)\n            grad_J = (m_star_unsq * s_bar\
  \ * gs_sum / one_minus_Jbar).sum()\n\n        return grad_x, grad_J, None\n\n\nclass CWALayer(nn.Module):\n    def __init__(self,\
  \ fixed_J=None, K_max=50):\n        super().__init__()\n        self.K_max = K_max\n        self.fixed_J = fixed_J\n   \
  \     if fixed_J is None:\n            # Learnable J: J = sigmoid(J_raw), J_raw init=0 => J=0.5\n            self.J_raw\
  \ = nn.Parameter(torch.zeros(1))\n        else:\n            # Fixed J: store as buffer (not optimized)\n            self.register_buffer('J_buf',\
  \ torch.tensor([fixed_J], dtype=torch.float32))\n        self._last_J_s_bar = 0.0\n        self._last_K = 0\n        self._last_mode\
  \ = 'unrolled'\n\n    def get_J(self):\n        if self.fixed_J is None:\n            return torch.sigmoid(self.J_raw)\n\
  \        else:\n            return self.J_buf\n\n    def forward(self, x):\n        J = self.get_J()\n        # Use custom\
  \ Function for IFT-controlled backward\n        y, J_s_bar_t, m_star = CWAFunction.apply(x, J, self.K_max)\n        self._last_J_s_bar\
  \ = J_s_bar_t.item()\n        self._last_mode = 'ift' if self._last_J_s_bar >= 0.8 else 'unrolled'\n        return y\n```\n\
  \n**CRITICAL NOTES for executor:**\n- The `CWAFunction.forward` MUST wrap the fixed-point loop in `torch.no_grad()` — otherwise\
  \ memory explodes.\n- `s = 1 - tanh(z)^2` is numerically equivalent to `sech^2(z)` — do NOT compute `1/cosh^2` (overflow\
  \ risk).\n- The tolerance is `delta = 1e-4 * (1 - J_val)` where J_val is the raw sigmoid output, NOT J*s_bar — this matches\
  \ Lean Theorem 3 exactly.\n- The `CWAFunction.forward` should return only `y`; track J_s_bar and m_star in ctx for the backward\
  \ — don't return them as tensors from the autograd.Function since that complicates the graph. Instead, log them as attributes\
  \ on the module after the forward.\n- **REVISED forward pattern**: Actually, the cleanest approach is to NOT use a custom\
  \ autograd.Function and instead:\n  1. Run fixed-point loop in no_grad to get m_star\n  2. Re-engage grad by computing z\
  \ = x + J * m_star.detach() + J * (m_star - m_star.detach()) where the second term is zero but carries the IFT gradient.\
  \ This is equivalent to IFT for J*s_bar < 1.\n  3. Simpler still: for IFT branch, use `z = x + J * m_star.detach()` but\
  \ then add a correction term (phantom gradient). For the unrolled branch, re-run 3 steps with grad.\n  \n  **RECOMMENDED\
  \ SIMPLEST CORRECT APPROACH:**\n  ```python\n  def forward(self, x):\n      J = self.get_J()\n      J_val = J.item()\n \
  \     delta = 1e-4 * (1.0 - J_val)\n      \n      # Phase 1: converge m* without grad\n      with torch.no_grad():\n   \
  \       m = torch.zeros_like(x[..., :1])\n          K_conv = 0\n          for k in range(self.K_max):\n              m_new\
  \ = torch.mean(torch.tanh(x + J_val * m), dim=-1, keepdim=True)\n              if (m_new - m).abs().max().item() < delta:\n\
  \                  m = m_new; K_conv = k+1; break\n              m = m_new\n          else:\n              K_conv = self.K_max\n\
  \          m_star = m  # converged scalar mean, shape (batch, 1)\n      \n      # Phase 2: compute s_bar for mode selection\n\
  \      z_star = x + J_val * m_star\n      with torch.no_grad():\n          s_bar = (1 - torch.tanh(z_star)**2).mean().item()\n\
  \      J_s_bar = J_val * s_bar\n      self._last_J_s_bar = J_s_bar\n      self._last_K = K_conv\n      \n      if J_s_bar\
  \ >= 0.8:\n          # IFT BRANCH: use detached m_star, IFT phantom gradient\n          # y = tanh(x + J * m_star.detach())\
  \ -- but this cuts gradient to J\n          # Need to include gradient to J via IFT: dy/dJ = sech^2(z)*m*/(1-J*s_bar)\n\
  \          # Implement via: re-compute y at m_star with graph enabled for J only\n          m_star_detached = m_star.detach()\n\
  \          z = x.detach() + J * m_star_detached  # grad flows through J\n          s = 1 - torch.tanh(z.detach())**2\n \
  \         # IFT correction for x-gradient: y(x) = tanh(x + J_val * m*(x))\n          # where dm*/dx_i = s_i / (n * (1-J*s_bar))\n\
  \          # Implement via stop-gradient trick: add zero + IFT correction\n          y_from_J = torch.tanh(z)  # has grad\
  \ through J\n          # For x gradient: use a detached y + correction\n          y_full = torch.tanh(x + J_val * m_star_detached)\
  \  # has grad through x directly\n          # Combine: y = tanh(x + J*m*) where m* treated as constant for x-grad\n    \
  \      # This gives dy/dx_i = s_i (direct only, ignores IFT chain dx_i -> m*)\n          # IFT chain adds: s_i * J/(n*(1-J*s_bar))\
  \ * sum_k(s_k) [batch avg]\n          # For gradient stability test, the direct path dominates; IFT chain is a correction\n\
  \          # SIMPLIFICATION: use detach and add correction via a dummy zero tensor\n          one_minus_Jbar = max(1.0 -\
  \ J_s_bar, 1e-6)\n          # Full IFT y_i = tanh(z_i) with dL/dx_k = s_k*(g_k + J*gs_sum/(n*one_minus_Jbar))\n        \
  \  # Achieve this by: y = tanh(x + J_val * m_star_detached)\n          #   then register backward hook to modify grads\n\
  \          # CLEANEST: implement via custom Function (see above)\n          y = torch.tanh(x + J_val * m_star_detached)\
  \  # x grad = s_k (approx IFT)\n          self._last_mode = 'ift'\n      else:\n          # UNROLLED BRANCH: 3 tracked steps\
  \ from detached m_star\n          m = m_star.detach()\n          steps = min(K_conv, 3)\n          for _ in range(steps):\n\
  \              m = torch.mean(torch.tanh(x + J * m), dim=-1, keepdim=True)\n          y = torch.tanh(x + J * m)\n      \
  \    self._last_mode = 'unrolled'\n      \n      return y\n  ```\n  This is the RECOMMENDED implementation — unrolled path\
  \ gives exact gradients through x and J for small J*s_bar, IFT detach gives approximate x-gradients (s_k only, ignoring\
  \ IFT chain) for large J*s_bar. The IFT chain correction is O(J*s_bar/(n*(1-J*s_bar))) relative and small. Log mode, K,\
  \ J_s_bar after each forward.\n\n---\n\n### 2. Baselines\n\n```python\nclass CompetingNonlinearities(nn.Module):\n    #\
  \ Quenched random mixture: each neuron fixed at init as Swish (prob 0.83) or Tanh\n    def __init__(self, n_neurons, p_c=0.83):\n\
  \        super().__init__()\n        # Fixed mask: 1=Swish, 0=Tanh, shape (1, n_neurons), not a parameter\n        mask\
  \ = (torch.rand(1, n_neurons) < p_c).float()\n        self.register_buffer('mask', mask)  # survives .cuda()\n    \n   \
  \ def forward(self, x):\n        swish_out = x * torch.sigmoid(x)\n        tanh_out  = torch.tanh(x)\n        return self.mask\
  \ * swish_out + (1 - self.mask) * tanh_out\n\n# SELU: use nn.SELU() directly — PyTorch implements α=1.6733, λ=1.0507\n#\
  \ GELU: use nn.GELU()\n# ReLU: use nn.ReLU()\n# GELU+LN: insert nn.LayerNorm(hidden_dim) before nn.GELU() in each block\n\
  ```\n\n---\n\n### 3. MLP architecture\n\n```python\ndef build_mlp(depth, hidden=256, n_in=3072, n_out=10, activation='cwa',\n\
  \              fixed_J=None, use_ln=False, p_c=0.83):\n    layers = [nn.Linear(n_in, hidden)]\n    for i in range(depth):\
  \  # 'depth' hidden layers\n        if use_ln:\n            layers.append(nn.LayerNorm(hidden))\n        act = make_activation(activation,\
  \ hidden, fixed_J, p_c)\n        layers.append(act)\n        if i < depth - 1:\n            layers.append(nn.Linear(hidden,\
  \ hidden))\n    layers.append(nn.Linear(hidden, n_out))\n    return nn.Sequential(*layers)\n\n# NOTE: architecture is Linear\
  \ -> [LN] -> Act -> Linear -> ... -> Linear -> Act -> Linear -> out\n# For depth=10: 10 hidden layers means 10 activation+linear\
  \ pairs, so 11 linear layers total\n# Track gradient norms for W_1 (first Linear weight) and W_L (last Linear weight before\
  \ output)\n```\n\n**ARCHITECTURE NOTE**: For depths {6, 10, 20}, the MLP should have exactly that many activation functions,\
  \ with linear layers between them. The structure is:\n```\nLinear(3072, 256) -> Act -> Linear(256, 256) -> Act -> ... ->\
  \ Linear(256, 10)\n```\nSo for depth=D, there are D+1 linear layers and D activation layers.\n\n---\n\n### 4. Gradient ratio\
  \ measurement\n\n```python\ndef measure_gradient_ratios(model, loader, loss_fn, device):\n    # Compute gradient norms for\
  \ W_1 and W_L (first and last weight matrices)\n    model.zero_grad()\n    x, y = next(iter(loader))\n    x, y = x.to(device),\
  \ y.to(device)\n    loss = loss_fn(model(x), y)\n    loss.backward()\n    \n    # Find all Linear layers\n    linear_layers\
  \ = [m for m in model.modules() if isinstance(m, nn.Linear)]\n    W_first = linear_layers[0]\n    W_last = linear_layers[-1]\n\
  \    \n    grad_first = W_first.weight.grad.norm().item() if W_first.weight.grad is not None else float('nan')\n    grad_last\
  \  = W_last.weight.grad.norm().item()  if W_last.weight.grad is not None else float('nan')\n    \n    # Ratio = |log(grad_first)\
  \ / log(grad_last)|  (sign-insensitive ratio of log magnitudes)\n    # If grad_last is near zero, ratio is large (vanishing\
  \ gradient)\n    eps = 1e-10\n    ratio = abs(math.log(grad_first + eps) / math.log(grad_last + eps))\n    return ratio,\
  \ grad_first, grad_last\n```\n\n**IMPORTANT**: Measure gradient ratio at epoch 5 and epoch 25. Use a single batch (256 samples)\
  \ to avoid overhead.\n\n---\n\n### 5. Training loop\n\n```python\ndef train_one_config(depth, activation_name, seed, fixed_J=None,\
  \ epochs=25,\n                     hidden=256, batch=256, lr=1e-3, device='cuda'):\n    torch.manual_seed(seed)\n    np.random.seed(seed)\n\
  \    \n    # Data: CIFAR-10, flattened\n    transform = T.Compose([T.ToTensor(), T.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5)),\n\
  \                            T.Lambda(lambda x: x.view(-1))])\n    train_ds = torchvision.datasets.CIFAR10('.', train=True,\
  \ download=True, transform=transform)\n    test_ds  = torchvision.datasets.CIFAR10('.', train=False, transform=transform)\n\
  \    train_loader = torch.utils.data.DataLoader(train_ds, batch_size=batch, shuffle=True,\n                            \
  \                   num_workers=4, pin_memory=True)\n    test_loader  = torch.utils.data.DataLoader(test_ds, batch_size=512,\
  \ shuffle=False,\n                                               num_workers=4, pin_memory=True)\n    \n    use_ln = (activation_name\
  \ == 'gelu_ln')\n    model = build_mlp(depth, hidden=hidden, activation=activation_name,\n                      fixed_J=fixed_J,\
  \ use_ln=use_ln).to(device)\n    \n    optimizer = torch.optim.Adam(model.parameters(), lr=lr)\n    scheduler = CosineAnnealingLR(optimizer,\
  \ T_max=epochs, eta_min=1e-5)\n    loss_fn = nn.CrossEntropyLoss()\n    \n    metrics = {'train_loss': [], 'test_acc': [],\
  \ 'grad_ratio_epoch5': None,\n               'grad_ratio_epoch25': None, 'J_s_bar_traj': [], 'K_traj': [],\n           \
  \    'mode_traj': []}\n    \n    for epoch in range(1, epochs+1):\n        model.train()\n        epoch_loss = 0\n     \
  \   for xb, yb in train_loader:\n            xb, yb = xb.to(device), yb.to(device)\n            optimizer.zero_grad()\n\
  \            out = model(xb)\n            loss = loss_fn(out, yb)\n            loss.backward()\n            torch.nn.utils.clip_grad_norm_(model.parameters(),\
  \ 1.0)  # gradient clip\n            optimizer.step()\n            epoch_loss += loss.item()\n        scheduler.step()\n\
  \        \n        # Test accuracy\n        model.eval()\n        correct = total = 0\n        with torch.no_grad():\n \
  \           for xb, yb in test_loader:\n                xb, yb = xb.to(device), yb.to(device)\n                pred = model(xb).argmax(1)\n\
  \                correct += (pred == yb).sum().item()\n                total += yb.size(0)\n        test_acc = correct /\
  \ total\n        metrics['train_loss'].append(epoch_loss / len(train_loader))\n        metrics['test_acc'].append(test_acc)\n\
  \        \n        # Log J*s_bar and K for CWA variants\n        cwa_layers = [m for m in model.modules() if isinstance(m,\
  \ CWALayer)]\n        if cwa_layers:\n            J_s_bars = [m._last_J_s_bar for m in cwa_layers]\n            Ks = [m._last_K\
  \ for m in cwa_layers]\n            modes = [m._last_mode for m in cwa_layers]\n            metrics['J_s_bar_traj'].append(float(np.mean(J_s_bars)))\n\
  \            metrics['K_traj'].append(float(np.mean(Ks)))\n            metrics['mode_traj'].append(modes[0] if modes else\
  \ None)\n        \n        # Gradient ratio at epochs 5 and 25\n        if epoch == 5:\n            ratio, gf, gl = measure_gradient_ratios(model,\
  \ train_loader, loss_fn, device)\n            metrics['grad_ratio_epoch5'] = ratio\n            metrics['grad_first_epoch5']\
  \ = gf\n            metrics['grad_last_epoch5'] = gl\n        if epoch == 25:\n            ratio, gf, gl = measure_gradient_ratios(model,\
  \ train_loader, loss_fn, device)\n            metrics['grad_ratio_epoch25'] = ratio\n            metrics['grad_first_epoch25']\
  \ = gf\n            metrics['grad_last_epoch25'] = gl\n    \n    return metrics\n```\n\n---\n\n### 6. Experiment grid\n\n\
  **Experiment A — Depth sweep:**\n- Activations: ['cwa', 'relu', 'gelu', 'selu', 'competing_nl', 'gelu_ln']\n- Depths: [6,\
  \ 10, 20]\n- Seeds: [0, 1, 2]\n- Total: 6 × 3 × 3 = 54 runs\n\n**Experiment B — Fixed-J ablation (depth 10 only):**\n- Fixed\
  \ J values: [0.1, 0.3, 0.5, 0.7, 0.9]\n- Plus learned CWA: fixed_J=None\n- Seeds: [0, 1, 2]\n- Total: 6 × 3 = 18 runs\n\n\
  Total: 72 training runs × ~10 min per run = estimate ~4h on GPU (parallelize with torch.multiprocessing or run sequentially\
  \ with early progress saves).\n\n**IMPORTANT**: Save results after each run to a JSON cache file so partial results survive\
  \ interruption:\n```python\nRESULTS_CACHE = './results_cache.json'\n# Load existing cache at start, skip completed runs,\
  \ append after each run\n```\n\n---\n\n### 7. Output format (method_out.json)\n\nThe output must conform to exp_gen_sol_out\
  \ schema. Structure:\n\n```json\n{\n  \"experiment_name\": \"CWA Unnormalized MLP Depth Sweep + Fixed-J Ablation\",\n  \"\
  hypothesis_tested\": \"CWA provides gradient stability only when J near-critical; fixed-J ablation tests mechanism\",\n\
  \  \"verdict\": \"CONFIRM|DISCONFIRM|PARTIAL_CONFIRM\",\n  \"verdict_reason\": \"...\",\n  \"examples\": [\n    {\n    \
  \  \"id\": \"depth6_cwa_seed0\",\n      \"depth\": 6,\n      \"activation\": \"cwa\",\n      \"seed\": 0,\n      \"fixed_J\"\
  : null,\n      \"final_test_acc\": 0.412,\n      \"grad_ratio_epoch5\": 1.3,\n      \"grad_ratio_epoch25\": 1.1,\n     \
  \ \"J_s_bar_mean\": 0.44,\n      \"J_s_bar_traj\": [...],\n      \"K_mean\": 5.2,\n      \"fraction_converged_before_Kmax\"\
  : 0.99\n    },\n    ...\n  ],\n  \"summary_tables\": {\n    \"gradient_ratio_by_depth_activation\": {\n      \"depth6\"\
  : {\"cwa\": {\"mean\": 1.3, \"std\": 0.1}, \"gelu\": {\"mean\": 3.2, \"std\": 0.4}, ...},\n      \"depth10\": {...},\n \
  \     \"depth20\": {...}\n    },\n    \"accuracy_by_depth\": {\n      \"depth6\": {\"cwa\": {\"mean\": 0.412, \"std\": 0.008},\
  \ ...},\n      ...\n    },\n    \"fixed_j_gradient_ratios\": {\n      \"J0.1\": {\"mean\": ..., \"std\": ...},\n      \"\
  J0.3\": {\"mean\": ..., \"std\": ...},\n      \"J0.5\": {\"mean\": ..., \"std\": ...},\n      \"J0.7\": {\"mean\": ...,\
  \ \"std\": ...},\n      \"J0.9\": {\"mean\": ..., \"std\": ...},\n      \"learned_J\": {\"mean\": ..., \"std\": ...}\n \
  \   },\n    \"fixed_j_accuracy\": {...},\n    \"J_s_bar_trajectory\": {...},\n    \"fraction_steps_converged_before_K_max\"\
  : {...}\n  },\n  \"statistical_tests\": {\n    \"paired_ttest_cwa_vs_gelu_depth10_acc\": {\"t\": ..., \"p\": ..., \"significant\"\
  : true},\n    \"paired_ttest_cwa_vs_gelu_depth20_acc\": {...},\n    \"welch_fixedJ07_vs_gelu_grad_ratio\": {...}\n  },\n\
  \  \"key_findings\": [\n    \"CWA at depth 10 achieves gradient_ratio=X vs GELU gradient_ratio=Y\",\n    \"Fixed J=0.7 achieves\
  \ gradient_ratio=Z -- CONFIRMS/DISCONFIRMS mechanism\",\n    \"Learned J converges to J*s_bar ~ 0.44 (does not self-organize)\"\
  \n  ]\n}\n```\n\nThe `examples` list must have one entry per (depth, activation, seed) cell for Experiment A, and one per\
  \ (fixed_J_value, seed) for Experiment B. This is ~72 total entries.\n\n---\n\n### 8. Key implementation gotchas to avoid\n\
  \n1. **Tolerance uses (1-J) not (1-J*s_bar)**: `delta = 1e-4 * (1.0 - J_val)` where J_val = sigmoid(J_raw). Do NOT use (1\
  \ - J_s_bar). This matches the Lean proof.\n\n2. **mean() is within-sample neuron axis**: `torch.mean(..., dim=-1, keepdim=True)`\
  \ over the last dimension (neuron dim). NOT over the batch dimension.\n\n3. **CompetingNonlinearities mask must be fixed\
  \ at module init**: `register_buffer('mask', ...)` so it's not learned but moves with .cuda(). The mask shape is `(1, hidden_dim)`\
  \ so it broadcasts over the batch.\n\n4. **K_max=50** (not 5 as in iter 1). The fixed-point iteration is cheap (no grad),\
  \ so 50 iterations is affordable.\n\n5. **Gradient clip=1.0** applied via `torch.nn.utils.clip_grad_norm_(model.parameters(),\
  \ 1.0)` after loss.backward() and before optimizer.step().\n\n6. **CWA fixed_J variants**: When `fixed_J` is not None, J_raw\
  \ is NOT an nn.Parameter — use `register_buffer`. The optimizer only sees weight parameters, not J. Forward is identical;\
  \ backward w.r.t. J is not computed (but w.r.t. x is correct).\n\n7. **Per-layer gradient norms**: Use the first and last\
  \ `nn.Linear` layers' `.weight.grad` — NOT the activation modules. Make sure to call `model.zero_grad()` before the measurement\
  \ backward pass.\n\n8. **SELU initialization**: Use `nn.init.normal_(layer.weight, std=1.0/math.sqrt(layer.in_features))`\
  \ (LeCun init) for SELU layers. For all other activations, default PyTorch He/Kaiming init is fine.\n\n9. **Gradient ratio\
  \ formula**: The hypothesis uses `|log|∇W₁|/log|∇W_L||` which is the ratio of log magnitudes. At depth 20 with vanishing\
  \ gradients, `grad_last` → 0, so `log(grad_last)` → -inf. Implement as:\n   ```python\n   ratio = abs(math.log(grad_first\
  \ + 1e-12)) / abs(math.log(grad_last + 1e-12))\n   ```\n   Also report raw grad_first and grad_last values.\n\n10. **Run\
  \ time management**: At 72 runs × ~25 epochs, estimate ~3-4h on A4500. If running long, prioritize: (a) depth=10 all activations\
  \ (core results), (b) fixed-J ablation, (c) depth=6 and depth=20. Use the cache to resume.\n\n---\n\n### 9. Statistical\
  \ analysis\n\nAfter all runs complete:\n```python\nfrom scipy import stats\n\n# For each depth, paired t-test: CWA vs GELU\
  \ accuracy over seeds\nfor depth in [6, 10, 20]:\n    cwa_accs = [results[(depth,'cwa',s)]['final_test_acc'] for s in [0,1,2]]\n\
  \    gelu_accs = [results[(depth,'gelu',s)]['final_test_acc'] for s in [0,1,2]]\n    t, p = stats.ttest_rel(cwa_accs, gelu_accs)\n\
  \    ...\n\n# Fixed-J ablation: Welch's t-test for gradient ratios\nfor J_val in [0.1, 0.3, 0.5, 0.7, 0.9]:\n    j_ratios\
  \ = [results[('fixedJ', J_val, s)]['grad_ratio_epoch25'] for s in [0,1,2]]\n    gelu_ratios = [results[(10,'gelu',s)]['grad_ratio_epoch25']\
  \ for s in [0,1,2]]\n    t, p = stats.ttest_ind(j_ratios, gelu_ratios, equal_var=False)\n    ...\n```\n\nReport 95% CIs:\
  \ `mean ± 1.96 * std / sqrt(3)` (n=3 seeds).\n\n---\n\n### 10. Verdict logic\n\n```\nCONFIRM if:\n  grad_ratio_cwa_depth10\
  \ < 2.0 AND grad_ratio_gelu_depth10 > 5.0\n  AND cwa_acc > gelu_acc by >= 0.5% on >= 2 of 3 depths (p < 0.05)\n\nPARTIAL_CONFIRM\
  \ if:\n  EITHER gradient stability claim met\n  OR fixed-J=0.7/0.9 shows grad_ratio < 2.0 (mechanism sound, SOC is the issue)\n\
  \nDISCONFIRM if:\n  CWA grad_ratio >= GELU grad_ratio across all depths\n  AND fixed-J=0.9 still shows grad_ratio >= GELU\n\
  ```"
fallback_plan: |-
  ## If CWALayer training fails/diverges
  1. **Gradient explosion**: Reduce LR to 1e-4 and re-run. Also check that J_raw never becomes very negative (J→0 => delta→1e-4 very small, OK) or very positive (J→1 => delta→0, iteration never stops). Add a soft clip: `J_raw = J_raw.clamp(-4, 4)` or equivalently detect when J > 0.99 and cap iterations.

  2. **Fixed-point non-convergence**: If K=50 is insufficient (rare for J<1), increase K_max=100. Log the fraction of forward passes that hit K_max — if > 1%, increase K_max.

  3. **Competing Nonlinearities mask OOM**: At depth=20, CompetingNonlinearities stores an extra (1, 256) buffer per layer — negligible. If memory issues arise, reduce batch size to 128.

  4. **Depth=20 instability for all activations**: If all activations diverge at depth=20, add a skip-connection (residual) for depth=20 only and note this in the report. The hypothesis is about unnormalized networks, not necessarily non-residual.

  5. **Time budget overrun**: If 72 runs cannot complete in 6h, prioritize:
     - Priority 1: depth=10, all 6 activations, 3 seeds (18 runs, ~1.5h)
     - Priority 2: fixed-J ablation, depth=10, all 6 J values, 3 seeds (18 runs, ~1.5h)
     - Priority 3: depth=6 and depth=20, remaining activations
     - Minimum viable result: depth=10 depth sweep + fixed-J ablation = GATING experiment complete

  6. **SELU diverging**: SELU requires LeCun init. If SELU diverges, explicitly apply `nn.init.normal_(layer.weight, 0, 1/sqrt(in_features))` to all Linear layers in SELU MLPs.

  7. **If IFT branch never triggers (J*s_bar never reaches 0.8)**: This was the iter 1 finding. In that case, all runs use the unrolled branch — report this honestly and note that the IFT branch was not exercised in this domain. The gradient ratio and accuracy results are still valid.
testing_plan: |-
  ## Phase 1: Smoke test (5 min)
  Before full training, validate CWALayer correctness:
  ```python
  # 1. Verify fixed-point convergence
  x = torch.randn(4, 256)  # small batch
  cwa = CWALayer()
  y = cwa(x)
  assert y.shape == (4, 256), 'Shape mismatch'
  assert not torch.isnan(y).any(), 'NaN in output'

  # 2. Verify gradient flows to weights of the MLP
  model = build_mlp(10, activation='cwa')
  out = model(x)
  loss = out.sum()
  loss.backward()
  for name, p in model.named_parameters():
      assert p.grad is not None, f'No grad for {name}'
      assert not torch.isnan(p.grad).any(), f'NaN grad for {name}'
  print('PASS: gradients flow through CWA')

  # 3. Verify J_raw gets gradient
  cwa = CWALayer()
  y = cwa(torch.randn(4, 256))
  y.sum().backward()
  assert cwa.J_raw.grad is not None
  print(f'J_raw.grad = {cwa.J_raw.grad.item():.6f}')  # should be nonzero

  # 4. Verify fixed-J has no J parameter
  cwa_fixed = CWALayer(fixed_J=0.7)
  assert not any(p.requires_grad for p in cwa_fixed.parameters())
  print('PASS: fixed-J has no learnable coupling')

  # 5. Verify tolerance formula
  cwa = CWALayer()
  J_val = torch.sigmoid(cwa.J_raw).item()
  expected_delta = 1e-4 * (1.0 - J_val)
  print(f'J={J_val:.4f}, delta={expected_delta:.6f}')  # should be ~5e-5 at J=0.5
  ```

  ## Phase 2: 1-epoch mini run (10 min)
  Run 1 epoch for (depth=10, cwa, seed=0) and (depth=10, gelu, seed=0):
  ```bash
  uv run method.py --smoke --depth 10 --epochs 1 --activations cwa gelu
  ```
  Confirmation signals:
  - Train loss decreasing after 1 epoch for both
  - No NaN in loss
  - J·s̄ is logged and sensible (0.3 – 0.7 range)
  - Gradient ratio computable (both grad_first and grad_last nonzero)

  ## Phase 3: 3-epoch run for depth sweep (30 min)
  Run 3 epochs for all 6 activations × depth=10 × 1 seed:
  ```bash
  uv run method.py --quick-test --depth 10 --epochs 3 --seeds 0
  ```
  Confirmation signals:
  - SELU doesn't diverge with LeCun init
  - CompetingNonlinearities mask is fixed (same output on repeated forward passes with same input)
  - Gradient ratios vary by activation (not all identical)
  - CWA converges before K_max=50 for >99% of batches

  ## Phase 4: Full run
  Once Phase 3 passes, launch full experiment:
  ```bash
  nohup uv run method.py --full > logs/run.log 2>&1 &
  PID=$!
  echo $PID > .pid
  ```
  Monitor: `tail -f logs/run.log & TAIL_PID=$!`
  Check alive: `kill -0 $PID 2>/dev/null && echo Running || echo Done`

  Checkpoint: Save results after each completed (depth, activation, seed) triple to `results_cache.json`. If run is interrupted, restart will skip completed cells.

  ## Phase 5: JSON validation
  After all runs, validate method_out.json structure:
  - All 72 examples present
  - No NaN/null in numeric fields
  - Gradient ratios are positive finite numbers
  - Accuracy values in [0, 1]
  - Run through aii-json schema validator if available
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

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
````

### [2] HUMAN-USER prompt · 2026-06-16 19:38:45 UTC

```
Role: You are an expert Deep Learning Research Scientist specializing in neural network architecture and mathematical optimization.Objective: Given a supervised learning dataset, design, implement, and validate an optimal, novel activation function $f(x)$ for a neural network. Your goal is to discover an activation function that empirically outperforms traditional baselines (ReLU, Swish, GELU, Tanh) in terms of final validation metrics, convergence speed, and gradient stability.Search Space & Constraints:The solution may be a parameterized function (with learnable parameters), a dynamic/gated composition of existing functions, or an entirely novel mathematical formulation.The function must be differentiable (or sub-differentiable) to allow for backpropagation.Consider computational efficiency; the function should not introduce prohibitive computational overhead compared to standard functions.
```

### [3] SKILL-INPUT — aii-python · 2026-06-16 19:39:03 UTC

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

### [4] SKILL-INPUT — aii-use-hardware · 2026-06-16 19:39:03 UTC

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

### [5] SKILL-INPUT — aii-long-running-tasks · 2026-06-16 19:39:03 UTC

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

### [6] SKILL-INPUT — aii-json · 2026-06-16 19:39:07 UTC

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

### [7] SKILL-INPUT — aii-file-size-limit · 2026-06-16 19:39:07 UTC

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

### [8] SKILL-INPUT — aii-parallel-computing · 2026-06-16 19:39:07 UTC

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

### [9] SYSTEM-USER prompt · 2026-06-16 20:09:29 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_6gT5lHFn8559/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
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
title: CWA Unnormalized MLP Depth Sweep + Fixed-J Ablation on CIFAR-10
summary: >-
  GPU experiment implementing Curie-Weiss Activation (CWA) with exact IFT gradients in unnormalized MLPs at depths {6,10,20},
  3 seeds, 25 epochs on CIFAR-10, plus a decisive fixed-J ablation (J frozen at {0.1,0.3,0.5,0.7,0.9}) at depth 10. Primary
  metrics: per-layer gradient norm ratio, final accuracy, and J·s̄ trajectory. Outputs method_out.json.
runpod_compute_profile: gpu
implementation_pseudocode: "## File: method.py\n\n### 0. Dependencies and imports\n```\npip install torch torchvision tqdm\n\
  import torch, torch.nn as nn, torch.nn.functional as F\nimport torchvision, torchvision.transforms as T\nimport numpy as\
  \ np, json, os, math\nfrom torch.optim.lr_scheduler import CosineAnnealingLR\n```\n\n---\n\n### 1. CWALayer — core module\n\
  \n```python\nclass CWAFunction(torch.autograd.Function):\n    @staticmethod\n    def forward(ctx, x, J, K_max=50):\n   \
  \     # J is a scalar tensor (detached value, no grad here)\n        J_val = J.item()\n        delta = 1e-4 * (1.0 - J_val)\
  \          # Lean Theorem 3 tolerance\n        n = x.shape[-1]\n\n        # Fixed-point iteration (no grad)\n        with\
  \ torch.no_grad():\n            m = torch.zeros(x.shape[:-1] + (1,), device=x.device, dtype=x.dtype)\n            for k\
  \ in range(K_max):\n                m_new = torch.mean(torch.tanh(x + J_val * m), dim=-1, keepdim=True)\n              \
  \  if (m_new - m).abs().max().item() < delta:\n                    m = m_new\n                    break\n              \
  \  m = m_new\n            m_star = m.squeeze(-1)   # shape: (*batch)\n\n        # Compute sech^2 at converged point\n  \
  \      z = x + J_val * m_star.unsqueeze(-1)   # (batch, n)\n        s = 1.0 - torch.tanh(z)**2              # sech^2, shape\
  \ (batch, n)\n        s_bar = s.mean(dim=-1, keepdim=True)    # (batch, 1)\n        y = torch.tanh(z)                  \
  \      # output activations\n\n        J_s_bar = J_val * s_bar.mean().item()\n        ctx.save_for_backward(x, J, m_star.unsqueeze(-1),\
  \ s, s_bar)\n        ctx.J_val = J_val\n        ctx.J_s_bar = J_s_bar\n        ctx.use_ift = (J_s_bar >= 0.8)\n        return\
  \ y, torch.tensor(J_s_bar), m_star\n\n    @staticmethod\n    def backward(ctx, grad_y, grad_Jbar, grad_mstar):\n       \
  \ x, J, m_star_unsq, s, s_bar = ctx.saved_tensors\n        J_val = ctx.J_val\n        J_s_bar = ctx.J_s_bar\n        n =\
  \ x.shape[-1]\n        one_minus_Jbar = max(1.0 - J_s_bar, 1e-6)  # numerical safety\n\n        if ctx.use_ift:\n      \
  \      # IFT BRANCH (J*s_bar >= 0.8): exact O(n) closed-form\n            # From research artifact Eq. A:\n            #\
  \   dL/dx_k = s_k * [g_k + J * (sum_i g_i*s_i) / (n * (1-J*s_bar))]\n            #   dL/dJ   = m_star * s_bar * (sum_i g_i*s_i)\
  \ / (1-J*s_bar)\n            g = grad_y                                  # (batch, n)\n            gs_sum = (g * s).sum(dim=-1,\
  \ keepdim=True) # (batch, 1)\n            scale = J_val / (n * one_minus_Jbar)\n            grad_x = s * (g + scale * gs_sum)\n\
  \            grad_J = (m_star_unsq * s_bar * gs_sum / one_minus_Jbar).sum()\n        else:\n            # UNROLLED BRANCH\
  \ (J*s_bar < 0.8): warm-start-3 approximation\n            # Run K steps without grad to find m*, then 3 tracked steps\n\
  \            # Introduces O((J*s_bar)^3) relative gradient bias — acceptable when J*s_bar<0.8\n            # (bias < 0.8^3\
  \ = 0.512 relative, but typically J*s_bar ~ 0.4-0.5 so ~0.1)\n            # For gradient wrt x: use same IFT formula since\
  \ it's O(n) exact anyway\n            g = grad_y\n            gs_sum = (g * s).sum(dim=-1, keepdim=True)\n            scale\
  \ = J_val / (n * one_minus_Jbar)\n            grad_x = s * (g + scale * gs_sum)\n            grad_J = (m_star_unsq * s_bar\
  \ * gs_sum / one_minus_Jbar).sum()\n\n        return grad_x, grad_J, None\n\n\nclass CWALayer(nn.Module):\n    def __init__(self,\
  \ fixed_J=None, K_max=50):\n        super().__init__()\n        self.K_max = K_max\n        self.fixed_J = fixed_J\n   \
  \     if fixed_J is None:\n            # Learnable J: J = sigmoid(J_raw), J_raw init=0 => J=0.5\n            self.J_raw\
  \ = nn.Parameter(torch.zeros(1))\n        else:\n            # Fixed J: store as buffer (not optimized)\n            self.register_buffer('J_buf',\
  \ torch.tensor([fixed_J], dtype=torch.float32))\n        self._last_J_s_bar = 0.0\n        self._last_K = 0\n        self._last_mode\
  \ = 'unrolled'\n\n    def get_J(self):\n        if self.fixed_J is None:\n            return torch.sigmoid(self.J_raw)\n\
  \        else:\n            return self.J_buf\n\n    def forward(self, x):\n        J = self.get_J()\n        # Use custom\
  \ Function for IFT-controlled backward\n        y, J_s_bar_t, m_star = CWAFunction.apply(x, J, self.K_max)\n        self._last_J_s_bar\
  \ = J_s_bar_t.item()\n        self._last_mode = 'ift' if self._last_J_s_bar >= 0.8 else 'unrolled'\n        return y\n```\n\
  \n**CRITICAL NOTES for executor:**\n- The `CWAFunction.forward` MUST wrap the fixed-point loop in `torch.no_grad()` — otherwise\
  \ memory explodes.\n- `s = 1 - tanh(z)^2` is numerically equivalent to `sech^2(z)` — do NOT compute `1/cosh^2` (overflow\
  \ risk).\n- The tolerance is `delta = 1e-4 * (1 - J_val)` where J_val is the raw sigmoid output, NOT J*s_bar — this matches\
  \ Lean Theorem 3 exactly.\n- The `CWAFunction.forward` should return only `y`; track J_s_bar and m_star in ctx for the backward\
  \ — don't return them as tensors from the autograd.Function since that complicates the graph. Instead, log them as attributes\
  \ on the module after the forward.\n- **REVISED forward pattern**: Actually, the cleanest approach is to NOT use a custom\
  \ autograd.Function and instead:\n  1. Run fixed-point loop in no_grad to get m_star\n  2. Re-engage grad by computing z\
  \ = x + J * m_star.detach() + J * (m_star - m_star.detach()) where the second term is zero but carries the IFT gradient.\
  \ This is equivalent to IFT for J*s_bar < 1.\n  3. Simpler still: for IFT branch, use `z = x + J * m_star.detach()` but\
  \ then add a correction term (phantom gradient). For the unrolled branch, re-run 3 steps with grad.\n  \n  **RECOMMENDED\
  \ SIMPLEST CORRECT APPROACH:**\n  ```python\n  def forward(self, x):\n      J = self.get_J()\n      J_val = J.item()\n \
  \     delta = 1e-4 * (1.0 - J_val)\n      \n      # Phase 1: converge m* without grad\n      with torch.no_grad():\n   \
  \       m = torch.zeros_like(x[..., :1])\n          K_conv = 0\n          for k in range(self.K_max):\n              m_new\
  \ = torch.mean(torch.tanh(x + J_val * m), dim=-1, keepdim=True)\n              if (m_new - m).abs().max().item() < delta:\n\
  \                  m = m_new; K_conv = k+1; break\n              m = m_new\n          else:\n              K_conv = self.K_max\n\
  \          m_star = m  # converged scalar mean, shape (batch, 1)\n      \n      # Phase 2: compute s_bar for mode selection\n\
  \      z_star = x + J_val * m_star\n      with torch.no_grad():\n          s_bar = (1 - torch.tanh(z_star)**2).mean().item()\n\
  \      J_s_bar = J_val * s_bar\n      self._last_J_s_bar = J_s_bar\n      self._last_K = K_conv\n      \n      if J_s_bar\
  \ >= 0.8:\n          # IFT BRANCH: use detached m_star, IFT phantom gradient\n          # y = tanh(x + J * m_star.detach())\
  \ -- but this cuts gradient to J\n          # Need to include gradient to J via IFT: dy/dJ = sech^2(z)*m*/(1-J*s_bar)\n\
  \          # Implement via: re-compute y at m_star with graph enabled for J only\n          m_star_detached = m_star.detach()\n\
  \          z = x.detach() + J * m_star_detached  # grad flows through J\n          s = 1 - torch.tanh(z.detach())**2\n \
  \         # IFT correction for x-gradient: y(x) = tanh(x + J_val * m*(x))\n          # where dm*/dx_i = s_i / (n * (1-J*s_bar))\n\
  \          # Implement via stop-gradient trick: add zero + IFT correction\n          y_from_J = torch.tanh(z)  # has grad\
  \ through J\n          # For x gradient: use a detached y + correction\n          y_full = torch.tanh(x + J_val * m_star_detached)\
  \  # has grad through x directly\n          # Combine: y = tanh(x + J*m*) where m* treated as constant for x-grad\n    \
  \      # This gives dy/dx_i = s_i (direct only, ignores IFT chain dx_i -> m*)\n          # IFT chain adds: s_i * J/(n*(1-J*s_bar))\
  \ * sum_k(s_k) [batch avg]\n          # For gradient stability test, the direct path dominates; IFT chain is a correction\n\
  \          # SIMPLIFICATION: use detach and add correction via a dummy zero tensor\n          one_minus_Jbar = max(1.0 -\
  \ J_s_bar, 1e-6)\n          # Full IFT y_i = tanh(z_i) with dL/dx_k = s_k*(g_k + J*gs_sum/(n*one_minus_Jbar))\n        \
  \  # Achieve this by: y = tanh(x + J_val * m_star_detached)\n          #   then register backward hook to modify grads\n\
  \          # CLEANEST: implement via custom Function (see above)\n          y = torch.tanh(x + J_val * m_star_detached)\
  \  # x grad = s_k (approx IFT)\n          self._last_mode = 'ift'\n      else:\n          # UNROLLED BRANCH: 3 tracked steps\
  \ from detached m_star\n          m = m_star.detach()\n          steps = min(K_conv, 3)\n          for _ in range(steps):\n\
  \              m = torch.mean(torch.tanh(x + J * m), dim=-1, keepdim=True)\n          y = torch.tanh(x + J * m)\n      \
  \    self._last_mode = 'unrolled'\n      \n      return y\n  ```\n  This is the RECOMMENDED implementation — unrolled path\
  \ gives exact gradients through x and J for small J*s_bar, IFT detach gives approximate x-gradients (s_k only, ignoring\
  \ IFT chain) for large J*s_bar. The IFT chain correction is O(J*s_bar/(n*(1-J*s_bar))) relative and small. Log mode, K,\
  \ J_s_bar after each forward.\n\n---\n\n### 2. Baselines\n\n```python\nclass CompetingNonlinearities(nn.Module):\n    #\
  \ Quenched random mixture: each neuron fixed at init as Swish (prob 0.83) or Tanh\n    def __init__(self, n_neurons, p_c=0.83):\n\
  \        super().__init__()\n        # Fixed mask: 1=Swish, 0=Tanh, shape (1, n_neurons), not a parameter\n        mask\
  \ = (torch.rand(1, n_neurons) < p_c).float()\n        self.register_buffer('mask', mask)  # survives .cuda()\n    \n   \
  \ def forward(self, x):\n        swish_out = x * torch.sigmoid(x)\n        tanh_out  = torch.tanh(x)\n        return self.mask\
  \ * swish_out + (1 - self.mask) * tanh_out\n\n# SELU: use nn.SELU() directly — PyTorch implements α=1.6733, λ=1.0507\n#\
  \ GELU: use nn.GELU()\n# ReLU: use nn.ReLU()\n# GELU+LN: insert nn.LayerNorm(hidden_dim) before nn.GELU() in each block\n\
  ```\n\n---\n\n### 3. MLP architecture\n\n```python\ndef build_mlp(depth, hidden=256, n_in=3072, n_out=10, activation='cwa',\n\
  \              fixed_J=None, use_ln=False, p_c=0.83):\n    layers = [nn.Linear(n_in, hidden)]\n    for i in range(depth):\
  \  # 'depth' hidden layers\n        if use_ln:\n            layers.append(nn.LayerNorm(hidden))\n        act = make_activation(activation,\
  \ hidden, fixed_J, p_c)\n        layers.append(act)\n        if i < depth - 1:\n            layers.append(nn.Linear(hidden,\
  \ hidden))\n    layers.append(nn.Linear(hidden, n_out))\n    return nn.Sequential(*layers)\n\n# NOTE: architecture is Linear\
  \ -> [LN] -> Act -> Linear -> ... -> Linear -> Act -> Linear -> out\n# For depth=10: 10 hidden layers means 10 activation+linear\
  \ pairs, so 11 linear layers total\n# Track gradient norms for W_1 (first Linear weight) and W_L (last Linear weight before\
  \ output)\n```\n\n**ARCHITECTURE NOTE**: For depths {6, 10, 20}, the MLP should have exactly that many activation functions,\
  \ with linear layers between them. The structure is:\n```\nLinear(3072, 256) -> Act -> Linear(256, 256) -> Act -> ... ->\
  \ Linear(256, 10)\n```\nSo for depth=D, there are D+1 linear layers and D activation layers.\n\n---\n\n### 4. Gradient ratio\
  \ measurement\n\n```python\ndef measure_gradient_ratios(model, loader, loss_fn, device):\n    # Compute gradient norms for\
  \ W_1 and W_L (first and last weight matrices)\n    model.zero_grad()\n    x, y = next(iter(loader))\n    x, y = x.to(device),\
  \ y.to(device)\n    loss = loss_fn(model(x), y)\n    loss.backward()\n    \n    # Find all Linear layers\n    linear_layers\
  \ = [m for m in model.modules() if isinstance(m, nn.Linear)]\n    W_first = linear_layers[0]\n    W_last = linear_layers[-1]\n\
  \    \n    grad_first = W_first.weight.grad.norm().item() if W_first.weight.grad is not None else float('nan')\n    grad_last\
  \  = W_last.weight.grad.norm().item()  if W_last.weight.grad is not None else float('nan')\n    \n    # Ratio = |log(grad_first)\
  \ / log(grad_last)|  (sign-insensitive ratio of log magnitudes)\n    # If grad_last is near zero, ratio is large (vanishing\
  \ gradient)\n    eps = 1e-10\n    ratio = abs(math.log(grad_first + eps) / math.log(grad_last + eps))\n    return ratio,\
  \ grad_first, grad_last\n```\n\n**IMPORTANT**: Measure gradient ratio at epoch 5 and epoch 25. Use a single batch (256 samples)\
  \ to avoid overhead.\n\n---\n\n### 5. Training loop\n\n```python\ndef train_one_config(depth, activation_name, seed, fixed_J=None,\
  \ epochs=25,\n                     hidden=256, batch=256, lr=1e-3, device='cuda'):\n    torch.manual_seed(seed)\n    np.random.seed(seed)\n\
  \    \n    # Data: CIFAR-10, flattened\n    transform = T.Compose([T.ToTensor(), T.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5)),\n\
  \                            T.Lambda(lambda x: x.view(-1))])\n    train_ds = torchvision.datasets.CIFAR10('.', train=True,\
  \ download=True, transform=transform)\n    test_ds  = torchvision.datasets.CIFAR10('.', train=False, transform=transform)\n\
  \    train_loader = torch.utils.data.DataLoader(train_ds, batch_size=batch, shuffle=True,\n                            \
  \                   num_workers=4, pin_memory=True)\n    test_loader  = torch.utils.data.DataLoader(test_ds, batch_size=512,\
  \ shuffle=False,\n                                               num_workers=4, pin_memory=True)\n    \n    use_ln = (activation_name\
  \ == 'gelu_ln')\n    model = build_mlp(depth, hidden=hidden, activation=activation_name,\n                      fixed_J=fixed_J,\
  \ use_ln=use_ln).to(device)\n    \n    optimizer = torch.optim.Adam(model.parameters(), lr=lr)\n    scheduler = CosineAnnealingLR(optimizer,\
  \ T_max=epochs, eta_min=1e-5)\n    loss_fn = nn.CrossEntropyLoss()\n    \n    metrics = {'train_loss': [], 'test_acc': [],\
  \ 'grad_ratio_epoch5': None,\n               'grad_ratio_epoch25': None, 'J_s_bar_traj': [], 'K_traj': [],\n           \
  \    'mode_traj': []}\n    \n    for epoch in range(1, epochs+1):\n        model.train()\n        epoch_loss = 0\n     \
  \   for xb, yb in train_loader:\n            xb, yb = xb.to(device), yb.to(device)\n            optimizer.zero_grad()\n\
  \            out = model(xb)\n            loss = loss_fn(out, yb)\n            loss.backward()\n            torch.nn.utils.clip_grad_norm_(model.parameters(),\
  \ 1.0)  # gradient clip\n            optimizer.step()\n            epoch_loss += loss.item()\n        scheduler.step()\n\
  \        \n        # Test accuracy\n        model.eval()\n        correct = total = 0\n        with torch.no_grad():\n \
  \           for xb, yb in test_loader:\n                xb, yb = xb.to(device), yb.to(device)\n                pred = model(xb).argmax(1)\n\
  \                correct += (pred == yb).sum().item()\n                total += yb.size(0)\n        test_acc = correct /\
  \ total\n        metrics['train_loss'].append(epoch_loss / len(train_loader))\n        metrics['test_acc'].append(test_acc)\n\
  \        \n        # Log J*s_bar and K for CWA variants\n        cwa_layers = [m for m in model.modules() if isinstance(m,\
  \ CWALayer)]\n        if cwa_layers:\n            J_s_bars = [m._last_J_s_bar for m in cwa_layers]\n            Ks = [m._last_K\
  \ for m in cwa_layers]\n            modes = [m._last_mode for m in cwa_layers]\n            metrics['J_s_bar_traj'].append(float(np.mean(J_s_bars)))\n\
  \            metrics['K_traj'].append(float(np.mean(Ks)))\n            metrics['mode_traj'].append(modes[0] if modes else\
  \ None)\n        \n        # Gradient ratio at epochs 5 and 25\n        if epoch == 5:\n            ratio, gf, gl = measure_gradient_ratios(model,\
  \ train_loader, loss_fn, device)\n            metrics['grad_ratio_epoch5'] = ratio\n            metrics['grad_first_epoch5']\
  \ = gf\n            metrics['grad_last_epoch5'] = gl\n        if epoch == 25:\n            ratio, gf, gl = measure_gradient_ratios(model,\
  \ train_loader, loss_fn, device)\n            metrics['grad_ratio_epoch25'] = ratio\n            metrics['grad_first_epoch25']\
  \ = gf\n            metrics['grad_last_epoch25'] = gl\n    \n    return metrics\n```\n\n---\n\n### 6. Experiment grid\n\n\
  **Experiment A — Depth sweep:**\n- Activations: ['cwa', 'relu', 'gelu', 'selu', 'competing_nl', 'gelu_ln']\n- Depths: [6,\
  \ 10, 20]\n- Seeds: [0, 1, 2]\n- Total: 6 × 3 × 3 = 54 runs\n\n**Experiment B — Fixed-J ablation (depth 10 only):**\n- Fixed\
  \ J values: [0.1, 0.3, 0.5, 0.7, 0.9]\n- Plus learned CWA: fixed_J=None\n- Seeds: [0, 1, 2]\n- Total: 6 × 3 = 18 runs\n\n\
  Total: 72 training runs × ~10 min per run = estimate ~4h on GPU (parallelize with torch.multiprocessing or run sequentially\
  \ with early progress saves).\n\n**IMPORTANT**: Save results after each run to a JSON cache file so partial results survive\
  \ interruption:\n```python\nRESULTS_CACHE = './results_cache.json'\n# Load existing cache at start, skip completed runs,\
  \ append after each run\n```\n\n---\n\n### 7. Output format (method_out.json)\n\nThe output must conform to exp_gen_sol_out\
  \ schema. Structure:\n\n```json\n{\n  \"experiment_name\": \"CWA Unnormalized MLP Depth Sweep + Fixed-J Ablation\",\n  \"\
  hypothesis_tested\": \"CWA provides gradient stability only when J near-critical; fixed-J ablation tests mechanism\",\n\
  \  \"verdict\": \"CONFIRM|DISCONFIRM|PARTIAL_CONFIRM\",\n  \"verdict_reason\": \"...\",\n  \"examples\": [\n    {\n    \
  \  \"id\": \"depth6_cwa_seed0\",\n      \"depth\": 6,\n      \"activation\": \"cwa\",\n      \"seed\": 0,\n      \"fixed_J\"\
  : null,\n      \"final_test_acc\": 0.412,\n      \"grad_ratio_epoch5\": 1.3,\n      \"grad_ratio_epoch25\": 1.1,\n     \
  \ \"J_s_bar_mean\": 0.44,\n      \"J_s_bar_traj\": [...],\n      \"K_mean\": 5.2,\n      \"fraction_converged_before_Kmax\"\
  : 0.99\n    },\n    ...\n  ],\n  \"summary_tables\": {\n    \"gradient_ratio_by_depth_activation\": {\n      \"depth6\"\
  : {\"cwa\": {\"mean\": 1.3, \"std\": 0.1}, \"gelu\": {\"mean\": 3.2, \"std\": 0.4}, ...},\n      \"depth10\": {...},\n \
  \     \"depth20\": {...}\n    },\n    \"accuracy_by_depth\": {\n      \"depth6\": {\"cwa\": {\"mean\": 0.412, \"std\": 0.008},\
  \ ...},\n      ...\n    },\n    \"fixed_j_gradient_ratios\": {\n      \"J0.1\": {\"mean\": ..., \"std\": ...},\n      \"\
  J0.3\": {\"mean\": ..., \"std\": ...},\n      \"J0.5\": {\"mean\": ..., \"std\": ...},\n      \"J0.7\": {\"mean\": ...,\
  \ \"std\": ...},\n      \"J0.9\": {\"mean\": ..., \"std\": ...},\n      \"learned_J\": {\"mean\": ..., \"std\": ...}\n \
  \   },\n    \"fixed_j_accuracy\": {...},\n    \"J_s_bar_trajectory\": {...},\n    \"fraction_steps_converged_before_K_max\"\
  : {...}\n  },\n  \"statistical_tests\": {\n    \"paired_ttest_cwa_vs_gelu_depth10_acc\": {\"t\": ..., \"p\": ..., \"significant\"\
  : true},\n    \"paired_ttest_cwa_vs_gelu_depth20_acc\": {...},\n    \"welch_fixedJ07_vs_gelu_grad_ratio\": {...}\n  },\n\
  \  \"key_findings\": [\n    \"CWA at depth 10 achieves gradient_ratio=X vs GELU gradient_ratio=Y\",\n    \"Fixed J=0.7 achieves\
  \ gradient_ratio=Z -- CONFIRMS/DISCONFIRMS mechanism\",\n    \"Learned J converges to J*s_bar ~ 0.44 (does not self-organize)\"\
  \n  ]\n}\n```\n\nThe `examples` list must have one entry per (depth, activation, seed) cell for Experiment A, and one per\
  \ (fixed_J_value, seed) for Experiment B. This is ~72 total entries.\n\n---\n\n### 8. Key implementation gotchas to avoid\n\
  \n1. **Tolerance uses (1-J) not (1-J*s_bar)**: `delta = 1e-4 * (1.0 - J_val)` where J_val = sigmoid(J_raw). Do NOT use (1\
  \ - J_s_bar). This matches the Lean proof.\n\n2. **mean() is within-sample neuron axis**: `torch.mean(..., dim=-1, keepdim=True)`\
  \ over the last dimension (neuron dim). NOT over the batch dimension.\n\n3. **CompetingNonlinearities mask must be fixed\
  \ at module init**: `register_buffer('mask', ...)` so it's not learned but moves with .cuda(). The mask shape is `(1, hidden_dim)`\
  \ so it broadcasts over the batch.\n\n4. **K_max=50** (not 5 as in iter 1). The fixed-point iteration is cheap (no grad),\
  \ so 50 iterations is affordable.\n\n5. **Gradient clip=1.0** applied via `torch.nn.utils.clip_grad_norm_(model.parameters(),\
  \ 1.0)` after loss.backward() and before optimizer.step().\n\n6. **CWA fixed_J variants**: When `fixed_J` is not None, J_raw\
  \ is NOT an nn.Parameter — use `register_buffer`. The optimizer only sees weight parameters, not J. Forward is identical;\
  \ backward w.r.t. J is not computed (but w.r.t. x is correct).\n\n7. **Per-layer gradient norms**: Use the first and last\
  \ `nn.Linear` layers' `.weight.grad` — NOT the activation modules. Make sure to call `model.zero_grad()` before the measurement\
  \ backward pass.\n\n8. **SELU initialization**: Use `nn.init.normal_(layer.weight, std=1.0/math.sqrt(layer.in_features))`\
  \ (LeCun init) for SELU layers. For all other activations, default PyTorch He/Kaiming init is fine.\n\n9. **Gradient ratio\
  \ formula**: The hypothesis uses `|log|∇W₁|/log|∇W_L||` which is the ratio of log magnitudes. At depth 20 with vanishing\
  \ gradients, `grad_last` → 0, so `log(grad_last)` → -inf. Implement as:\n   ```python\n   ratio = abs(math.log(grad_first\
  \ + 1e-12)) / abs(math.log(grad_last + 1e-12))\n   ```\n   Also report raw grad_first and grad_last values.\n\n10. **Run\
  \ time management**: At 72 runs × ~25 epochs, estimate ~3-4h on A4500. If running long, prioritize: (a) depth=10 all activations\
  \ (core results), (b) fixed-J ablation, (c) depth=6 and depth=20. Use the cache to resume.\n\n---\n\n### 9. Statistical\
  \ analysis\n\nAfter all runs complete:\n```python\nfrom scipy import stats\n\n# For each depth, paired t-test: CWA vs GELU\
  \ accuracy over seeds\nfor depth in [6, 10, 20]:\n    cwa_accs = [results[(depth,'cwa',s)]['final_test_acc'] for s in [0,1,2]]\n\
  \    gelu_accs = [results[(depth,'gelu',s)]['final_test_acc'] for s in [0,1,2]]\n    t, p = stats.ttest_rel(cwa_accs, gelu_accs)\n\
  \    ...\n\n# Fixed-J ablation: Welch's t-test for gradient ratios\nfor J_val in [0.1, 0.3, 0.5, 0.7, 0.9]:\n    j_ratios\
  \ = [results[('fixedJ', J_val, s)]['grad_ratio_epoch25'] for s in [0,1,2]]\n    gelu_ratios = [results[(10,'gelu',s)]['grad_ratio_epoch25']\
  \ for s in [0,1,2]]\n    t, p = stats.ttest_ind(j_ratios, gelu_ratios, equal_var=False)\n    ...\n```\n\nReport 95% CIs:\
  \ `mean ± 1.96 * std / sqrt(3)` (n=3 seeds).\n\n---\n\n### 10. Verdict logic\n\n```\nCONFIRM if:\n  grad_ratio_cwa_depth10\
  \ < 2.0 AND grad_ratio_gelu_depth10 > 5.0\n  AND cwa_acc > gelu_acc by >= 0.5% on >= 2 of 3 depths (p < 0.05)\n\nPARTIAL_CONFIRM\
  \ if:\n  EITHER gradient stability claim met\n  OR fixed-J=0.7/0.9 shows grad_ratio < 2.0 (mechanism sound, SOC is the issue)\n\
  \nDISCONFIRM if:\n  CWA grad_ratio >= GELU grad_ratio across all depths\n  AND fixed-J=0.9 still shows grad_ratio >= GELU\n\
  ```"
fallback_plan: |-
  ## If CWALayer training fails/diverges
  1. **Gradient explosion**: Reduce LR to 1e-4 and re-run. Also check that J_raw never becomes very negative (J→0 => delta→1e-4 very small, OK) or very positive (J→1 => delta→0, iteration never stops). Add a soft clip: `J_raw = J_raw.clamp(-4, 4)` or equivalently detect when J > 0.99 and cap iterations.

  2. **Fixed-point non-convergence**: If K=50 is insufficient (rare for J<1), increase K_max=100. Log the fraction of forward passes that hit K_max — if > 1%, increase K_max.

  3. **Competing Nonlinearities mask OOM**: At depth=20, CompetingNonlinearities stores an extra (1, 256) buffer per layer — negligible. If memory issues arise, reduce batch size to 128.

  4. **Depth=20 instability for all activations**: If all activations diverge at depth=20, add a skip-connection (residual) for depth=20 only and note this in the report. The hypothesis is about unnormalized networks, not necessarily non-residual.

  5. **Time budget overrun**: If 72 runs cannot complete in 6h, prioritize:
     - Priority 1: depth=10, all 6 activations, 3 seeds (18 runs, ~1.5h)
     - Priority 2: fixed-J ablation, depth=10, all 6 J values, 3 seeds (18 runs, ~1.5h)
     - Priority 3: depth=6 and depth=20, remaining activations
     - Minimum viable result: depth=10 depth sweep + fixed-J ablation = GATING experiment complete

  6. **SELU diverging**: SELU requires LeCun init. If SELU diverges, explicitly apply `nn.init.normal_(layer.weight, 0, 1/sqrt(in_features))` to all Linear layers in SELU MLPs.

  7. **If IFT branch never triggers (J*s_bar never reaches 0.8)**: This was the iter 1 finding. In that case, all runs use the unrolled branch — report this honestly and note that the IFT branch was not exercised in this domain. The gradient ratio and accuracy results are still valid.
testing_plan: |-
  ## Phase 1: Smoke test (5 min)
  Before full training, validate CWALayer correctness:
  ```python
  # 1. Verify fixed-point convergence
  x = torch.randn(4, 256)  # small batch
  cwa = CWALayer()
  y = cwa(x)
  assert y.shape == (4, 256), 'Shape mismatch'
  assert not torch.isnan(y).any(), 'NaN in output'

  # 2. Verify gradient flows to weights of the MLP
  model = build_mlp(10, activation='cwa')
  out = model(x)
  loss = out.sum()
  loss.backward()
  for name, p in model.named_parameters():
      assert p.grad is not None, f'No grad for {name}'
      assert not torch.isnan(p.grad).any(), f'NaN grad for {name}'
  print('PASS: gradients flow through CWA')

  # 3. Verify J_raw gets gradient
  cwa = CWALayer()
  y = cwa(torch.randn(4, 256))
  y.sum().backward()
  assert cwa.J_raw.grad is not None
  print(f'J_raw.grad = {cwa.J_raw.grad.item():.6f}')  # should be nonzero

  # 4. Verify fixed-J has no J parameter
  cwa_fixed = CWALayer(fixed_J=0.7)
  assert not any(p.requires_grad for p in cwa_fixed.parameters())
  print('PASS: fixed-J has no learnable coupling')

  # 5. Verify tolerance formula
  cwa = CWALayer()
  J_val = torch.sigmoid(cwa.J_raw).item()
  expected_delta = 1e-4 * (1.0 - J_val)
  print(f'J={J_val:.4f}, delta={expected_delta:.6f}')  # should be ~5e-5 at J=0.5
  ```

  ## Phase 2: 1-epoch mini run (10 min)
  Run 1 epoch for (depth=10, cwa, seed=0) and (depth=10, gelu, seed=0):
  ```bash
  uv run method.py --smoke --depth 10 --epochs 1 --activations cwa gelu
  ```
  Confirmation signals:
  - Train loss decreasing after 1 epoch for both
  - No NaN in loss
  - J·s̄ is logged and sensible (0.3 – 0.7 range)
  - Gradient ratio computable (both grad_first and grad_last nonzero)

  ## Phase 3: 3-epoch run for depth sweep (30 min)
  Run 3 epochs for all 6 activations × depth=10 × 1 seed:
  ```bash
  uv run method.py --quick-test --depth 10 --epochs 3 --seeds 0
  ```
  Confirmation signals:
  - SELU doesn't diverge with LeCun init
  - CompetingNonlinearities mask is fixed (same output on repeated forward passes with same input)
  - Gradient ratios vary by activation (not all identical)
  - CWA converges before K_max=50 for >99% of batches

  ## Phase 4: Full run
  Once Phase 3 passes, launch full experiment:
  ```bash
  nohup uv run method.py --full > logs/run.log 2>&1 &
  PID=$!
  echo $PID > .pid
  ```
  Monitor: `tail -f logs/run.log & TAIL_PID=$!`
  Check alive: `kill -0 $PID 2>/dev/null && echo Running || echo Done`

  Checkpoint: Save results after each completed (depth, activation, seed) triple to `results_cache.json`. If run is interrupted, restart will skip completed cells.

  ## Phase 5: JSON validation
  After all runs, validate method_out.json structure:
  - All 72 examples present
  - No NaN/null in numeric fields
  - Gradient ratios are positive finite numbers
  - Accuracy values in [0, 1]
  - Run through aii-json schema validator if available
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

### [10] SYSTEM-USER prompt · 2026-06-16 20:37:34 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `layman_summary`: 'We tested a new physics-inspired activation function (Curie-Weiss Activation) against ReLU, GELU, SELU, and others in deep neural networks on CIFAR-10, finding that CWA achieves more balanced gradient flow at moderate depths but collapses at depth 20, partially confirming the gradient-stability hypothesis.' is too long (at most 250 characters, got 307)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [11] SYSTEM-USER prompt · 2026-06-16 20:38:16 UTC

```
<CRITICAL_ERROR>
Some files in your workspace exceed the 100MB size limit for GitHub deployment.

OVERSIZED FILES:
  - cifar_data/cifar-10-python.tar.gz (162.6 MB)

You MUST reduce these files to under 100MB each. Use ONE of these strategies:

=== STRATEGY 1: SPLIT FILES (PREFERRED) ===
Split large files into smaller parts and update code to read them sequentially.

For data files (JSON, JSONL, CSV, Parquet):
1. Split the file into parts under 100MB each:
   - data.jsonl -> data_part_001.jsonl, data_part_002.jsonl, ...
2. Update ALL code that reads this file to handle the split parts
3. Delete the original large file after splitting

=== STRATEGY 2: COMPRESSION (FALLBACK) ===
Only use if splitting is not feasible (e.g., binary files, model weights).

1. Compress the file with gzip
2. Update ALL code to decompress before use
3. Delete the original uncompressed file

=== REQUIRED: UPDATE AND TEST CODE ===
After applying your chosen strategy, you MUST:

1. Find ALL code files that reference the modified files (use grep/search)
2. Update each file to work with the new format (split parts or compressed)
3. Run the updated code to verify it still works correctly
4. Fix any errors that occur until the code runs successfully

Do NOT skip testing - the code must actually execute without errors.

Start by listing the oversized files with `ls -lh`, then apply the appropriate strategy.
</CRITICAL_ERROR>
```
