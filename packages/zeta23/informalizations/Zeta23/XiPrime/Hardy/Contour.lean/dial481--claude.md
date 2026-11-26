---
{
  "module": "Zeta23/XiPrime/Hardy/Contour.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/Contour.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/Contour.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/Contour.lean — the argument principle for Ω = Γℝ·W on [−1,2]×[T₁,T₂] and the fold onto the
right half-contour. This is the function-specific part — zeros of Ω on the rectangle ↔ the W count; the fold itself is
the generic ZeroCount/GenericRvM.rectangleIntegral_eq_halfContour_of_fold instantiated at F := logDeriv Ω, valid for
heights T₁ ≥ t₀ > 0 where Ω is analytic and its zeros are W's with equal orders.
  N_W(T₁,T₂) = (1/π)·Im ∫_L Ω′/Ω,  L = [½+iT₁ → 2+iT₁ → 2+iT₂ → ½+iT₂]  (good heights t₀ ≤ T₁ ≤ T₂).
-/
```

### `GoodHeightW`

 T is a zero-free ordinate for W: no non-real zero of W has Im ρ = T. 

### `exists_goodHeightW`

 every unit interval [a, a+1] with a ≥ t₀ contains a good height. 

### `rectangleIntegral'_logDeriv_omegaW_eq_NcountW`

 **N_W(T₁,T₂) as a contour integral**: (1/2πi)∮_{∂([−1,2]×[T₁,T₂])} Ω′/Ω = NcountW T₁ T₂ for good heights
t₀ ≤ T₁ ≤ T₂ (all zeros there have 0 < Re < 1 by the strip hypothesis, so none sit on the vertical edges). 

 ### the fold 

### `rectangleIntegral_logDeriv_omegaW_eq_halfContour`

 **the fold**: for good heights 0 < T₁ ≤ T₂, ∮ Ω′/Ω = 2i·Im(halfContour (Ω′/Ω) T₁ T₂)
(instance of ZeroCount/GenericRvM's rectangleIntegral_eq_halfContour_of_fold with F := logDeriv Ω). 

### `NcountW_eq_im_halfContour`

 **N_W(T₁,T₂) = (1/π)·Im ∫_L Ω′/Ω** for good heights t₀ ≤ T₁ ≤ T₂. 
