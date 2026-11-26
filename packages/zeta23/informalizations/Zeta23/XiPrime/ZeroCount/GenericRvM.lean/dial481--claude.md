---
{
  "module": "Zeta23/XiPrime/ZeroCount/GenericRvM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/GenericRvM.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/GenericRvM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ZeroCount/GenericRvM.lean — the GENERIC half-contour fold and Riemann–von Mangoldt main-term assembly.

Two facts abstracted over the function (instantiated both for ξ′ and for Ω = Γℝ·W):
 (A) `rectangleIntegral_eq_halfContour_of_fold`: if F(1 − s̄) = −conj F(s) along the right half of ∂([−1,2]×[T₁,T₂]) and F is
     continuous along the two horizontal lines, then ∮_{∂([−1,2]×[T₁,T₂])} F = 2i·Im(halfContour F T₁ T₂);
     `natCast_eq_im_halfContour`: so a count N with (1/2πi)∮F = N satisfies N = (1/π)·Im halfContour F.
 (B) `rvM_main_of`: for a ZeroConfig Zc, a good-height predicate with one good height per unit interval above a₀, the
     identity Zc.N T₁ T₂ = (1/π)Im halfContour(logDeriv Λ) at good heights, a residual bound
     |Im halfContour(logDeriv Λ) − Im halfContour(Γℝ′/Γℝ)| ≤ C log(|T₁|+3) + K + C log(|T₂|+3), and a local count, one gets
     |Zc.N(T,2T) − (T/2π)ℓ₁(T)| ≤ C′ log T — the μ-bookkeeping against Zeta23.RvM.gamma_side, done once.
Instances: Hardy/Contour.lean + Hardy/Count.lean (W); the ξ′ versions in ZeroCount.lean can be re-derived from these.
-/
```

 ### (A) the fold 

### `horizontal_fold_of`

 horizontal fold at height T: ∫_{−1}^{2} F(σ+iT)dσ = 2i·Im ∫_{1/2}^{2} F(σ+iT)dσ, given continuity along the line and
F(1 − s̄) = −conj F(s) at s = x + iT, x ∈ [1/2, 2]. 

### `vertical_fold_of`

 vertical fold: ∫_{T₁}^{T₂} F(−1+it)dt = −conj ∫_{T₁}^{T₂} F(2+it)dt. 

### `rectangleIntegral_eq_halfContour_of_fold`

 **(A) the fold**: ∮_{∂([−1,2]×[T₁,T₂])} F = 2i·Im(halfContour F T₁ T₂). 

### `natCast_eq_im_halfContour`

 from (1/2πi)∮F = N and the fold: N = (1/π)·Im halfContour F. 

 ### (B) the main-term assembly 

### `rvM_main_of`

 **(B) Riemann–von Mangoldt main term, generic**. 
