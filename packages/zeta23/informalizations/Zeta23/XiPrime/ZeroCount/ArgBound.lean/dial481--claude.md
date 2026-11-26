---
{
  "module": "Zeta23/XiPrime/ZeroCount/ArgBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/ArgBound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/ArgBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ZeroCount/ArgBound.lean — two generic "the argument moves by at most π" lemmas
(Mathlib only).

(A) If g : ℝ → ℂ has 0 < Re g on [a,b] then |Im ∫_a^b g′/g| ≤ π  (log g is a primitive; |arg| < π/2 at
    both ends).  Corollaries in the shapes used on the contour: the vertical segment t ↦ f(σ+it)
    (integrand logDeriv f (σ+it)·i) and the horizontal segment σ ↦ f(σ+iT).
    (Zeta23/RvM/Backlund.lean vertical_two is the instance f = ζ, σ = 2.)
(B) A single partial-fraction term along a horizontal segment: |Im ∫_a^b dσ/(σ+iT−ρ)| ≤ π.
-/
```

### `abs_im_integral_logDeriv_le_pi`

 **(A)** positive real part along a path ⇒ the argument varies by less than π. 

### `hasDerivAt_vertical`

 the vertical path t ↦ σ + it and its derivative i. 

### `hasDerivAt_horizontal`

 the horizontal path σ ↦ σ + iT and its derivative 1. 

### `abs_im_integral_logDeriv_vertical_le_pi`

 **(A), vertical segment**: f analytic with Re f > 0 along σ + i[T₁,T₂] ⇒ |Im ∫ f′/f(σ+it)·i dt| ≤ π. 

### `abs_im_integral_logDeriv_horizontal_le_pi`

 **(A), horizontal segment**: f analytic with Re f > 0 along [a,b] + iT ⇒ |Im ∫ f′/f(σ+iT) dσ| ≤ π. 

 ### (B) one partial-fraction term 

### `abs_im_integral_inv_sub_le_pi`

 **(B)** |Im ∫_a^b dσ/(σ + iT − ρ)| ≤ π whenever ρ is not on the segment. 
