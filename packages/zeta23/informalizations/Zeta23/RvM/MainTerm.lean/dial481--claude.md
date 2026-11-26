---
{
  "module": "Zeta23/RvM/MainTerm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/MainTerm.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/MainTerm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/RvM/MainTerm.lean — the main term N(T,2T) = (T/2π)·ell1 T + O(log T).
The statements here are assembled into Zeta23.RvM.riemannVonMangoldt in Zeta23/RvM/Statement.lean.

Inputs (from other files):
 * Zeta23.RvM.zetaZeroConfig_local_count (LocalCount.lean, proved): local count.
 * Zeta23/Analytic/RectangleLogDeriv.lean: ∮_{∂Rect} g·f'/f = 2πi Σ m_ρ g(ρ) (PNT+ RectangleIntegral'
   conventions) — use with g ≡ 1, f = completedRiemannZeta (or riemannZeta·Gammaℝ) on [−1,2]×[T₁,T₂]
   (mind Λ's poles at s = 0, 1: for T₁ > 0 the rectangle avoids them).
 * Zeta23/WeilEF/XiLogDeriv.lean: logDeriv Λ = logDeriv ζ + logDeriv Gammaℝ (Re s > 0, away from
   zeros/pole); conj-symmetry Λ(conj s) = conj Λ(s); Λ(1−s) = Λ(s) (Mathlib completedRiemannZeta_one_sub).
 * Zeta23/RvM/Backlund.lean: backlund_horizontal (∃ C T₀, ∀ T ≥ T₀, GoodHeight T →
   |Im ∫_{1/2}^{2} ζ'/ζ(σ+iT) dσ| ≤ C log T) and vertical_two (|Im ∫_{T₁}^{T₂} ζ'/ζ(2+it)·i dt| ≤ 2 log 3).
 * Zeta23/RvM/GammaSide.lean: gamma_side : 0 < T₁ ≤ T₂ → (1/π)·(halfContour (logDeriv Gammaℝ) T₁ T₂).im
   = ∫ t in T₁..T₂, mu t.
 * GammaFacts.int_mu, GammaFacts.stirling (μ(τ) = (1/2π) log(|τ|/2π) + O(τ⁻²) ⇒ μ ≪ log on [T−1,2T+1]).
The assembly is proved once as the constant-parametric `rvM_main_param`; `rvM_main_aux` /
`rvM_main` are its ∃-corollaries; MainTermExplicit.lean keeps only the numeric inputs and `rvM_main_explicit`.
-/
```

### `N_eq_halfContour_completedZeta`

 (M2)+(M3): the folded argument principle. For zero-free ordinates 1 ≤ T₁ < T₂:
N(T₁,T₂) = (1/π)·Im ∫_L Λ'/Λ ds, L the right half-contour.  [Tit86 §9.3; fold by Λ(1−s̄) = conj Λ(s)] 

### `contour_point_facts`

 Points on the half-contour: ζ and Γℝ facts packaged. 

### `continuousAt_logDeriv_zeta`

 logDeriv ζ is continuous at good points. 

### `exists_goodHeight`

 Zero-free ordinates are dense enough: every interval [a, a+1] (a ≥ 0) contains one
(finitely many ordinates per window, Zeta23.zerosIn_finite). 

 (window arithmetic Ncount_add / Ncount_mono: Zeta23/Statement/SeamClosed.lean) 

### `rvM_main_param`

 **rvM_main, parametric in all constants**: the five constant sources —
Backlund CB TB, local count A₀, int_mu Cμ Tμ, μ ≪ log CM, continuity of μ — are explicit parameters, so numeric
inputs give a numeric C_N. 

### `rvM_main_aux`

 The assembly, stated against the two Backlund bounds as explicit hypotheses (∃-form; from
`rvM_main_param` instantiated with the ∃-witnesses of Backlund, the local count, H-Γ's int_mu, μ ≪ log, continuity). 

### `rvM_main`

 (M7)+assembly: H-RvM's main clause for ζ, conditional on the Γ-facts.
[Tit86, Thm 9.4]: N(T,2T) = (T/2π)(log(T/2π) + 2 log 2 − 1) + O(log T). 
