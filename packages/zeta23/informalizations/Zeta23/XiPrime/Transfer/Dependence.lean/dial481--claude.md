---
{
  "module": "Zeta23/XiPrime/Transfer/Dependence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Transfer/Dependence.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Transfer/Dependence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization.

Zeta23/XiPrime/Transfer/Dependence.lean — ξ′ TRACE TRANSFER: [XF′ Lemma 6.1] AT FIXED T over the
abstract taper data (p : PrimeSide.Setting, F : PrimeSide.LocalFun, LocalHypsCore).

  A. integrability / linearity of the prime-side entry in the coefficients:
     GentryW 1 c₁ − GentryW 1 c₂ = GentryNu (P_{c₁−c₂})  (the μ and Π_X parts cancel);
     Q_{kl}(e) := GentryNu (P_e) k l is a FINITE ℝ-linear functional of (Re e_N, Im e_N)_{N≤X}, so an
     entrywise expansion e^{kl}_N = Σ_r e_r(N) δ_{kl}^r (HasSum) transfers to Q_{kl}(e^{kl}) = Σ_r δ^r Q_{kl}(e_r).
  B. the Dirichlet-kernel bound A_φ(y)‖Σ_{k<K} e^{−iτ_k y}‖ ≤ L²/(2 log 2) for EVERY K (ThmE's
     Aphi_mul_norm_tauKernel_le is the case K = d), and Abel summation in k with complex summands.
  C. the two fixed-T conclusions: Frobenius (Minkowski over r, Abstract §B) and trace (Abel over k).
-/
```

 ### A. Integrability, linearity, and Q as a finite linear functional 

### `integrable_phiHat_mul_mul_bdd`

 φ̂(·−τ_k) φ̂(·−τ_l) g is integrable for g continuous and bounded (2|ab| ≤ a² + b²). 

### `integrable_phiHat_sq_shift_mul_nucW`

 φ̂(·−t)² ν is integrable for ν = μ + ϖ·Π_X + P_c, t > 0 (translate the three diagonal part lemmas). 

### `integrable_gentryW_integrand`

 the full integrand of GentryW ϖ c is integrable (0 < τ_k, τ_l). 

### `gentryW_sub`

 **linearity**: the μ- and Π-parts cancel in a difference of two fixed-coefficient entries (any pole weight). 

### `gentryW_weight_sub`

 **the pole-weight difference**: GentryW ϖ₁ c − GentryW ϖ₂ c = (ϖ₁ − ϖ₂)·(Π-part entry). 

### `Jc`

 the cosine weight of frequency log N in Q_{kl}:  ∫ φ̂_k φ̂_l cos(τ log N)/(π√N). 

### `Js`

 the sine weight. 

### `gentryNu_Pc_eq_sum`

 **Q_{kl}(e) as a finite ℝ-linear functional of the coefficients**:
GentryNu (P_e) k l = Σ_{N≤X} (Re e_N · Jc N + Im e_N · Js N). 

### `hasSum_gentryNu_Pc`

 **series transfer**: an entrywise expansion of the coefficients transfers to Q_{kl}. 

 ### B. The Dirichlet kernel for every K, and Abel summation with complex summands 

### `Aphi_mul_norm_tauKernel_le'`

 A_φ(y)·‖Σ_{k<K} e^{−iτ_k y}‖ ≤ L²/(2 log 2) for every K (proof = ThmE.Aphi_mul_norm_tauKernel_le with
p.d ↦ K; that lemma's geometric-sum input abs_sin_mul_norm_geom_le is already K-general). 

### `norm_sum_smul_le_of_monotone`

 Abel summation with monotone bounded real weights and vector summands:
‖Σ_{k<d} w_k • q_k‖ ≤ 2WB when every ‖Σ_{k<K} q_k‖ ≤ B (K ≤ d). 

### `abs_weighted_diag_sum_le`

 the per-frequency oscillating sum of [XF′ Lemma 6.1]'s trace part, with monotone weights
0 ≤ w_k ≤ W:  |Σ_{k<d} w_k A_φ(y)(a cos(τ_k y) + b sin(τ_k y))| ≤ ‖a + bi‖ · 2W · L²/(2 log 2)
for y ≥ log 2  (a cos + b sin = Re((a+bi)e^{−iτy})). 

 ### C. The fixed-T conclusions 

### `geom_partial_le`

 geometric partial sums: Σ_{r<R} x^{r+1} ≤ 2x for 0 ≤ x ≤ 1/2. 

### `frobSq_ofReal_fin`

 cast helper: frobSq of a real d×d matrix indexed through Fin d → ℕ, as a double range sum. 

### `dependence_frob`

 **[XF′ Lemma 6.1], Frobenius part, at fixed T.**  If every entry's coefficient sequence expands as
g^{kl}_N = Σ_{r≥1} e_r(N) δ_{kl}^r with 0 ≤ δ_{kl} ≤ 1/2, and Σ_{kl} Q_{kl}(e_r)² ≤ K₁ρ^{2r} + K₀ (ρ ≤ 1),
then Σ_{kl} Q_{kl}(g^{kl})² ≤ 2(K₁ρ² + K₀). 

### `gentryNu_Pc_diag`

 translation: the diagonal entry as ∫ φ̂(s)² P_c(τ_k + s) ds. 

### `dependence_trace`

 **[XF′ Lemma 6.1], trace part, at fixed T.**  With the diagonal expansion g^{k}_N = Σ_{r≥1} e_r(N) δ_k^r
(0 ≤ δ_k ≤ 1/2, δ_k monotone in k), e_r(1) = 0 and S₁(e_r) ≤ σρ^r (ρ ≤ 1):
|Σ_{k<d} Q_{kk}(g^k)| ≤ (2/log 2)·L²·σ·ρ  (Abel in k against the Dirichlet kernel). 
