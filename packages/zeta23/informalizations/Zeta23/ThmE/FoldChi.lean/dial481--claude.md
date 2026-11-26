---
{
  "module": "Zeta23/ThmE/FoldChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/FoldChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/FoldChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/FoldChi.lean — the symmetry fold for Λ_sym(s,χ) (χ-analogue of
Zeta23/RvM/Fold.lean), used in the assembly of the zero count for L(s,χ).

Global symmetries (primitive χ mod q > 1; everything is entire, so no side conditions):
  Λ(w,χ⁻¹) = conj Λ(w̄,χ)   (identity theorem from Λ = γ·L on Re > 0 + SeamL.LFunction_conj),
  Λ_sym(1−w,χ) = W(χ)·Λ_sym(w,χ⁻¹)  (CountByIntegralChi.completedLSym_one_sub), hence
  (Λ_sym'/Λ_sym)(1−s̄,χ) = −conj (Λ_sym'/Λ_sym)(s,χ)  for every s.
Folding the rectangle ∂([−1,2]×[T₁,T₂]) onto its right half exactly as for ζ:
  ∮ Λ_sym'/Λ_sym = 2i·Im(halfContour (Λ_sym'/Λ_sym) T₁ T₂),  so with CountByIntegralChi
  N_χ(T₁,T₂) = (1/π)·Im(halfContour (logDeriv (completedLSym χ)) T₁ T₂)
for good heights T₁ ≤ T₂ of any sign (Zeta23.RvM.halfContour reused verbatim).
-/
```

 ## χ⁻¹ is primitive when χ is 

 ## Conjugation: Λ(w,χ⁻¹) = conj Λ(w̄,χ), and the same for Λ_sym 

### `gammaFactor_inv`

 χ⁻¹ has the same parity, hence the same Γ-factor. 

### `completedLFunction_inv_eq_conj`

 **Λ(w,χ⁻¹) = conj Λ(w̄,χ)** for all w (χ mod q > 1 nontrivial). 

### `logDeriv_completedLSym_inv_conj`

 logDeriv Λ_sym(s̄,χ⁻¹)… in the form we need: logDeriv (Λ_sym χ⁻¹) (conj s) = conj (logDeriv (Λ_sym χ) s). 

### `logDeriv_completedLSym_one_sub_conj`

 **The fold symmetry for Λ_sym**, valid at every point:
(Λ_sym'/Λ_sym)(1 − s̄, χ) = −conj((Λ_sym'/Λ_sym)(s, χ)). 

 ## Continuity of Λ_sym'/Λ_sym at good heights 

 ## The fold 

### `horizontal_foldChi`

 Horizontal fold at a good height T:  ∫_{−1}^{2} F(σ+iT)dσ = 2i·Im ∫_{1/2}^{2} F(σ+iT)dσ. 

### `vertical_foldChi`

 Vertical fold: ∫_{T₁}^{T₂} F(−1+it)dt = −conj ∫_{T₁}^{T₂} F(2+it)dt. 

### `rectangleIntegral_logDeriv_completedLSym_eq_halfContour`

 **The fold** for Λ_sym(s,χ): for good heights T₁ ≤ T₂ (any sign),
∮_{∂([−1,2]×[T₁,T₂])} Λ_sym'/Λ_sym = 2i·Im(halfContour (Λ_sym'/Λ_sym) T₁ T₂). 

### `NcountL_eq_im_halfContour`

 **N_χ(T₁,T₂) = (1/π)·Im ∫_L Λ_sym'/Λ_sym** for good heights T₁ ≤ T₂ of any sign. 
