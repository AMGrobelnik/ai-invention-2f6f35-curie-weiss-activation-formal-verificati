import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Topology.MetricSpace.Contracting

-- CWA Proof: convergence, IFT formula, and bias bound
-- Three theorems for F(m) = tanh(x + J*m), J in (0,1)

-- ============================================================
-- Part 1: Derivatives of sinh, cosh, tanh
-- ============================================================

lemma hasDerivAt_sinh (x : ℝ) : HasDerivAt Real.sinh (Real.cosh x) x := by
  have h1 := Real.hasDerivAt_exp x
  have h2 : HasDerivAt (Real.exp ∘ Neg.neg) (Real.exp (-x) * (-1)) x :=
    (Real.hasDerivAt_exp (-x)).comp x (hasDerivAt_neg x)
  have h4 : HasDerivAt (fun x => (Real.exp x - Real.exp (-x)) / 2)
      ((Real.exp x - Real.exp (-x) * (-1)) / 2) x :=
    (h1.sub h2).div_const 2
  convert h4 using 1
  · funext y; exact Real.sinh_eq y
  · rw [Real.cosh_eq]; ring

lemma hasDerivAt_cosh (x : ℝ) : HasDerivAt Real.cosh (Real.sinh x) x := by
  have h1 := Real.hasDerivAt_exp x
  have h2 : HasDerivAt (Real.exp ∘ Neg.neg) (Real.exp (-x) * (-1)) x :=
    (Real.hasDerivAt_exp (-x)).comp x (hasDerivAt_neg x)
  have h4 : HasDerivAt (fun x => (Real.exp x + Real.exp (-x)) / 2)
      ((Real.exp x + Real.exp (-x) * (-1)) / 2) x :=
    (h1.add h2).div_const 2
  convert h4 using 1
  · funext y; exact Real.cosh_eq y
  · rw [Real.sinh_eq]; ring

lemma hasDerivAt_tanh (x : ℝ) : HasDerivAt Real.tanh (1 - Real.tanh x ^ 2) x := by
  have hcosh_ne : Real.cosh x ≠ 0 := (Real.cosh_pos x).ne'
  have hsinh := hasDerivAt_sinh x
  have hcosh := hasDerivAt_cosh x
  have hcosh_inv : HasDerivAt (fun y => (Real.cosh y)⁻¹) (-Real.sinh x / Real.cosh x ^ 2) x :=
    hcosh.inv hcosh_ne
  have hprod : HasDerivAt (fun y => Real.sinh y * (Real.cosh y)⁻¹)
      (Real.cosh x * (Real.cosh x)⁻¹ + Real.sinh x * (-Real.sinh x / Real.cosh x ^ 2)) x :=
    hsinh.mul hcosh_inv
  convert hprod using 1
  · funext y; rw [Real.tanh_eq_sinh_div_cosh]; field_simp
  · rw [Real.tanh_eq_sinh_div_cosh]
    have hid : Real.cosh x ^ 2 - Real.sinh x ^ 2 = 1 := Real.cosh_sq_sub_sinh_sq x
    field_simp
    nlinarith [Real.cosh_pos x]

lemma differentiable_tanh : Differentiable ℝ Real.tanh :=
  fun x => (hasDerivAt_tanh x).differentiableAt

-- ============================================================
-- Part 2: tanh is 1-Lipschitz
-- ============================================================

lemma sech_sq_nonneg (x : ℝ) : 0 ≤ 1 - Real.tanh x ^ 2 := by
  have hid : Real.cosh x ^ 2 - Real.sinh x ^ 2 = 1 := Real.cosh_sq_sub_sinh_sq x
  have hcp := Real.cosh_pos x
  rw [Real.tanh_eq_sinh_div_cosh, div_pow,
      one_sub_div (pow_ne_zero 2 hcp.ne')]
  apply div_nonneg _ (sq_nonneg _)
  nlinarith [sq_nonneg (Real.sinh x)]

lemma sech_sq_le_one (x : ℝ) : 1 - Real.tanh x ^ 2 ≤ 1 := by
  linarith [sq_nonneg (Real.tanh x)]

lemma nnnorm_deriv_tanh_le (x : ℝ) : ‖deriv Real.tanh x‖₊ ≤ 1 := by
  rw [(hasDerivAt_tanh x).deriv]
  have h0 := sech_sq_nonneg x
  have h1 := sech_sq_le_one x
  rw [show ‖(1 - Real.tanh x ^ 2)‖₊ = ⟨1 - Real.tanh x ^ 2, h0⟩ from by
    simp [nnnorm, NNNorm.nnnorm, Real.norm_of_nonneg h0]]
  exact_mod_cast h1

lemma tanh_lipschitzWith_one : LipschitzWith 1 Real.tanh :=
  lipschitzWith_of_nnnorm_deriv_le differentiable_tanh nnnorm_deriv_tanh_le

-- ============================================================
-- Part 3: F(m) = tanh(x + J*m) is J-Lipschitz and contracting
-- ============================================================

lemma lin_lipschitz (x : ℝ) {J : ℝ} (hJ0 : 0 ≤ J) :
    LipschitzWith ⟨J, hJ0⟩ (fun m => x + J * m) := by
  rw [lipschitzWith_iff_dist_le_mul]
  intro a b
  simp only [Real.dist_eq, NNReal.coe_mk]
  have h : x + J * a - (x + J * b) = J * (a - b) := by ring
  rw [h, abs_mul, abs_of_nonneg hJ0]

lemma F_lipschitz (x : ℝ) {J : ℝ} (hJ0 : 0 ≤ J) (hJ1 : J < 1) :
    LipschitzWith ⟨J, hJ0⟩ (fun m => Real.tanh (x + J * m)) := by
  have h := tanh_lipschitzWith_one.comp (lin_lipschitz x hJ0)
  simp only [NNReal.coe_one, one_mul] at h
  have heq : Real.tanh ∘ (fun m => x + J * m) = fun m => Real.tanh (x + J * m) := rfl
  rwa [heq] at h

lemma F_contracting (x : ℝ) {J : ℝ} (hJ0 : 0 < J) (hJ1 : J < 1) :
    ContractingWith ⟨J, le_of_lt hJ0⟩ (fun m => Real.tanh (x + J * m)) := by
  constructor
  · exact_mod_cast hJ1
  · exact F_lipschitz x (le_of_lt hJ0) hJ1

-- ============================================================
-- Theorem 1: CWA Banach Fixed-Point Theorem
-- ============================================================

theorem cwa_banach (x : ℝ) {J : ℝ} (hJ0 : 0 < J) (hJ1 : J < 1) :
    ∃! m_star : ℝ, Real.tanh (x + J * m_star) = m_star := by
  have hc := F_contracting x hJ0 hJ1
  let F := fun m => Real.tanh (x + J * m)
  use ContractingWith.fixedPoint F hc
  exact ⟨hc.fixedPoint_isFixedPt, fun y hy => hc.fixedPoint_unique hy⟩

-- ============================================================
-- Part 4: Algebraic helpers for IFT
-- ============================================================

lemma one_sub_J_sbar_pos {J : ℝ} (hJ0 : 0 < J) (hJ1 : J < 1)
    (s_bar : ℝ) (hs0 : 0 ≤ s_bar) (hs1 : s_bar ≤ 1) :
    0 < 1 - J * s_bar := by nlinarith

-- ============================================================
-- Theorem 2: IFT Gradient Formula
-- ============================================================

theorem ift_gradient_correct (x J m_star : ℝ) (hJ0 : 0 < J) (hJ1 : J < 1) :
    let s_bar := 1 - Real.tanh (x + J * m_star) ^ 2
    let grad := s_bar / (1 - J * s_bar)
    s_bar * (1 + J * grad) = grad := by
  simp only
  set s := 1 - Real.tanh (x + J * m_star) ^ 2
  have hs0 : 0 ≤ s := sech_sq_nonneg _
  have hs1 : s ≤ 1 := sech_sq_le_one _
  have hden : 1 - J * s ≠ 0 :=
    (one_sub_J_sbar_pos hJ0 hJ1 s hs0 hs1).ne'
  field_simp [hden]

-- IFT algebraic uniqueness: s*(1+J*d) = d implies d = s/(1-J*s)
lemma ift_equation_unique_solution (s_bar d J : ℝ)
    (hs0 : 0 ≤ s_bar) (hs1 : s_bar ≤ 1)
    (hJ0 : 0 < J) (hJ1 : J < 1)
    (heq : s_bar * (1 + J * d) = d) :
    d = s_bar / (1 - J * s_bar) := by
  have hden : 1 - J * s_bar ≠ 0 :=
    (one_sub_J_sbar_pos hJ0 hJ1 s_bar hs0 hs1).ne'
  field_simp [hden]
  linarith

-- ============================================================
-- Theorem 3: Bias Bound
-- ============================================================

lemma contraction_residual_bound {K : ℝ} (hK0 : 0 ≤ K) (hK1 : K < 1)
    {f : ℝ → ℝ} (hf_lip : LipschitzWith ⟨K, hK0⟩ f)
    {m_approx m_star : ℝ} (hstar : f m_star = m_star) :
    |m_approx - m_star| ≤ |f m_approx - m_approx| / (1 - K) := by
  have hden : 0 < 1 - K := by linarith
  rw [le_div_iff₀ hden]
  -- Lipschitz bound: |f(m_approx) - f(m_star)| ≤ K * |m_approx - m_star|
  have hlip : |f m_approx - f m_star| ≤ K * |m_approx - m_star| := by
    have h := hf_lip.dist_le_mul m_approx m_star
    simp only [Real.dist_eq, NNReal.coe_mk] at h
    linarith
  -- f(m_star) = m_star, so |f(m_approx) - m_star| ≤ K * |m_approx - m_star|
  rw [hstar] at hlip
  -- Triangle: |m_approx - m_star| ≤ |m_approx - f(m_approx)| + |f(m_approx) - m_star|
  have htri : |m_approx - m_star| ≤ |m_approx - f m_approx| + |f m_approx - m_star| := by
    calc |m_approx - m_star|
        = |(m_approx - f m_approx) + (f m_approx - m_star)| := by ring_nf
      _ ≤ |m_approx - f m_approx| + |f m_approx - m_star| := abs_add _ _
  -- Combine to get (1-K)*|m_approx - m_star| ≤ |f(m_approx) - m_approx|
  have hsym : |f m_approx - m_approx| = |m_approx - f m_approx| := abs_sub_comm _ _
  nlinarith [abs_nonneg (m_approx - m_star), abs_nonneg (f m_approx - m_approx),
             abs_nonneg (f m_approx - m_star)]

theorem cwa_ift_bias_uniform (x : ℝ) {J : ℝ} (hJ0 : 0 < J) (hJ1 : J < 1)
    {m_approx m_star : ℝ}
    (hstar : Real.tanh (x + J * m_star) = m_star)
    (hres : |Real.tanh (x + J * m_approx) - m_approx| ≤ 1e-4 * (1 - J)) :
    |m_approx - m_star| ≤ 1e-4 := by
  have hfl := F_lipschitz x (le_of_lt hJ0) hJ1
  have hbound : |m_approx - m_star| ≤
      |Real.tanh (x + J * m_approx) - m_approx| / (1 - J) :=
    contraction_residual_bound (le_of_lt hJ0) hJ1 hfl hstar
  have hpos : (0 : ℝ) < 1 - J := by linarith
  calc |m_approx - m_star|
      ≤ |Real.tanh (x + J * m_approx) - m_approx| / (1 - J) := hbound
    _ ≤ (1e-4 * (1 - J)) / (1 - J) := by
        apply div_le_div_of_nonneg_right hres
        linarith
    _ = 1e-4 := by field_simp

-- ============================================================
-- Main Combined Theorem
-- ============================================================

theorem cwa_main (x : ℝ) {J : ℝ} (hJ0 : 0 < J) (hJ1 : J < 1) :
    -- (1) Unique fixed point exists
    (∃! m_star : ℝ, Real.tanh (x + J * m_star) = m_star) ∧
    -- (2) IFT gradient formula is algebraically consistent
    (∀ m_star : ℝ,
      let s_bar := 1 - Real.tanh (x + J * m_star) ^ 2
      let grad := s_bar / (1 - J * s_bar)
      s_bar * (1 + J * grad) = grad) ∧
    -- (3) Adaptive tolerance 1e-4*(1-J) yields uniform bias bound 1e-4
    (∀ m_approx m_star : ℝ,
      Real.tanh (x + J * m_star) = m_star →
      |Real.tanh (x + J * m_approx) - m_approx| ≤ 1e-4 * (1 - J) →
      |m_approx - m_star| ≤ 1e-4) :=
  ⟨cwa_banach x hJ0 hJ1,
   fun m_star => ift_gradient_correct x J m_star hJ0 hJ1,
   fun m_approx m_star hstar hres => cwa_ift_bias_uniform x hJ0 hJ1 hstar hres⟩
