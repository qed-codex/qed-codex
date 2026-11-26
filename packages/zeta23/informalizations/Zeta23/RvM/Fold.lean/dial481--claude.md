---
{
  "module": "Zeta23/RvM/Fold.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/Fold.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/Fold.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/RvM/Fold.lean — the symmetry fold of the argument-principle rectangle onto its right half
(used for MainTerm.lean's N_eq_halfContour_completedZeta).

With F := Λ'/Λ (Λ = completedRiemannZeta), A_T := ∫_{1/2}^{2} F(σ+iT)dσ, B := ∫_{T₁}^{T₂} F(2+it)dt:
the functional equation Λ(1−w) = Λ(w) and the reflection Λ(w̄) = conj Λ(w) give F(1−s̄) = −conj F(s)
on the right half-path, hence ∫_{−1}^{1/2}F(σ+iT)dσ = −conj A_T, ∫_{T₁}^{T₂}F(−1+it)dt = −conj B, and
    ∮_{∂([−1,2]×[T₁,T₂])} F = (A_{T₁} − conj A_{T₁}) − (A_{T₂} − conj A_{T₂}) + I(B + conj B)
                           = 2i·Im(A_{T₁} + B·i − A_{T₂}) = 2i·Im(halfContour F T₁ T₂).
Combined with Zeta23.RvM.rectangleIntegral'_logDeriv_completedZeta_eq_Ncount (CountByIntegral.lean):
    N(T₁,T₂) = (1/π)·Im(halfContour (logDeriv Λ) T₁ T₂)   for good heights 1 ≤ T₁ < T₂.
The conj-symmetry lemmas for Gammaℝ and Λ'/Λ (section ConjSymmetry) live here rather than in
MainTerm.lean so that both files can use them.
-/
```

### `cpow_ofReal_conj`

 (x : ℂ)^(conj w) = conj ((x : ℂ)^w) for real x > 0. 

### `Gammaℝ_conj`

 Γℝ(s̄) = conj Γℝ(s). 

### `logDeriv_completedZeta_conj`

 Conjugation symmetry of Λ'/Λ at points with Re > 0 where ζ ≠ 0. 

### `logDeriv_completedZeta_one_sub_conj`

 The fold symmetry: Λ'/Λ(1 − s̄) = −conj(Λ'/Λ(s)) (Re s > 0, s ≠ 1, ζ(s) ≠ 0). 

### `path_point_facts`

 Facts at a point of the closed right half-strip at a good height ≥ 1. 

### `continuousAt_logDeriv_completedZeta`

 Λ'/Λ is continuous at every point of height T whenever T ≥ 1 is a good height. 

### `horizontal_fold`

 Horizontal fold at a good height T ≥ 1:  ∫_{−1}^{2} F(σ+iT)dσ = 2i·Im ∫_{1/2}^{2} F(σ+iT)dσ. 

### `vertical_fold`

 Vertical fold:  ∫_{T₁}^{T₂} F(−1+it)dt = −conj ∫_{T₁}^{T₂} F(2+it)dt  (1 ≤ T₁ ≤ T₂). 

### `rectangleIntegral_logDeriv_completedZeta_eq_halfContour`

 **The fold.** For good heights 1 ≤ T₁ < T₂:
∮_{∂([−1,2]×[T₁,T₂])} Λ'/Λ = 2i · Im(halfContour (Λ'/Λ) T₁ T₂). 

### `Ncount_eq_im_halfContour`

 **N(T₁,T₂) = (1/π)·Im ∫_L Λ'/Λ** for good heights 1 ≤ T₁ < T₂ (this is MainTerm.lean's
N_eq_halfContour_completedZeta). 
