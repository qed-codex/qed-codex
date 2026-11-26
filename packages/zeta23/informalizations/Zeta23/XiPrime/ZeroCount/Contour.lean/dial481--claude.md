---
{
  "module": "Zeta23/XiPrime/ZeroCount/Contour.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/Contour.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/Contour.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ZeroCount/Contour.lean — the argument principle for ξ′ on [−1,2]×[T₁,T₂] and the fold onto the
right half-contour.  ξ′-analogue of Zeta23/RvM/CountByIntegral.lean + Zeta23/RvM/Fold.lean;
simpler than Λ there because ξ′ is ENTIRE and its symmetries ξ′(1−s) = −ξ′(s), ξ′(s̄) = conj ξ′(s) hold
everywhere, so logDeriv ξ′(1−s̄) = −conj logDeriv ξ′(s) at every s (Seam.lean).
  N_{ξ′}(T₁,T₂) = (1/π)·Im ∫_L ξ″/ξ′,  L = [½+iT₁ → 2+iT₁ → 2+iT₂ → ½+iT₂]  (good heights T₁ < T₂).
-/
```

### `GoodHeight`

 T is a zero-free ordinate for ξ′: no zero of ξ′ (any real part) has Im ρ = T. 

### `exists_goodHeight`

 every unit interval [a, a+1] contains a good height (finitely many ordinates per window). 

### `goodHeight_xiDeriv_ne_zero`

 a good height for two windows at once: T ∈ [a,a+1] avoiding the ordinates of all zeros. (same proof) 

### `rectangleIntegral'_logDeriv_xiDeriv_eq_Ncount`

 **N_{ξ′}(T₁,T₂) as a contour integral**: (1/2πi)∮_{∂([−1,2]×[T₁,T₂])} ξ″/ξ′ = Ncount T₁ T₂ for good
heights T₁ ≤ T₂ (all zeros have 0 < Re < 1 by (F2), so none sit on the vertical edges). 

 ### the fold 

### `continuous_logDeriv_xiDeriv_horizontal`

 logDeriv ξ′ is continuous along the whole horizontal line at a good height. 

### `horizontal_fold`

 horizontal fold at a good height T: ∫_{−1}^{2} F(σ+iT)dσ = 2i·Im ∫_{1/2}^{2} F(σ+iT)dσ, F = ξ″/ξ′. 

### `vertical_fold`

 vertical fold: ∫_{T₁}^{T₂} F(−1+it)dt = −conj ∫_{T₁}^{T₂} F(2+it)dt. 

### `rectangleIntegral_logDeriv_xiDeriv_eq_halfContour`

 **the fold**: for good heights T₁ ≤ T₂,
∮_{∂([−1,2]×[T₁,T₂])} ξ″/ξ′ = 2i · Im(halfContour (ξ″/ξ′) T₁ T₂). 

### `Ncount_eq_im_halfContour`

 **N_{ξ′}(T₁,T₂) = (1/π)·Im ∫_L ξ″/ξ′** for good heights T₁ ≤ T₂. 
