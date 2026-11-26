---
{
  "module": "Zeta23/ThmE/BacklundChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/BacklundChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/BacklundChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/BacklundChi.lean — Backlund's bound (horizontal variation of arg L(s,χ)) and the trivial
vertical side σ = 2, for a nontrivial Dirichlet character.
The analogue of Zeta23/RvM/Backlund.lean with ζ ↦ L(·,χ): no pole, so every height is admissible
and the statements are two-sided in T.  The zero count (J) `reZeroSetL_card_le` is in
Zeta23/ThmE/ReZeroCountChi.lean; here: (V) the variation half, the σ = 2 side, and the
assembly `backlund_horizontalChi_of_count`.  Constants may depend on q and χ.
-/
```

### `reZeroSetL`

 The zero set of `σ ↦ Re L(σ+iT, χ)` on `[1/2, 2]` (interface with the Jensen count). 

 ## The horizontal side, calculus half: variation of the argument

Fix a height `T ≠ 0` with `ζ ≠ 0` on the segment `[1/2, 2] + iT`.  If `Re ζ(σ+iT)` has no zero on an
open subinterval `(u,v)`, it has constant sign `ε` there (IVT), `log(ε ζ(σ+iT))` is a primitive of
`ζ'/ζ(σ+iT)` on `[u,v]` (at the endpoints `ε ζ` is `≥ 0` in real part and `≠ 0`, so still in the
slit plane), hence `|Im ∫_u^v ζ'/ζ| ≤ 2π`.  Splitting `[1/2,2]` at the finitely many zeros of
`Re ζ(σ+iT)` (the set `reZeroSetL χ T`, counted by the Jensen bound `reZeroSet_card_le`) gives
`|Im ∫_{1/2}^{2} ζ'/ζ(σ+iT) dσ| ≤ 2π (#reZeroSetL χ T + 1)` — by induction on the number of zeros inside
the interval (no sorting needed). 

### `hasDerivAt_LFunction_horizontal`

 `σ ↦ ζ(σ+iT)` has derivative `ζ'(σ+iT)` in the real variable `σ`. 

### `continuousOn_logDeriv_horizontal`

 `σ ↦ ζ'/ζ(σ+iT)` is continuous on `[1/2,2]` when ζ has no zero on that segment. 

### `im_integral_le_two_pi`

 **Base case.** If `Re ζ(σ+iT) ≠ 0` on `(u,v) ⊆ [1/2,2]` then `|Im ∫_u^v ζ'/ζ(σ+iT) dσ| ≤ 2π`. 

### `im_integral_logDeriv_le_aux`

 **Induction.** With `P ⊇` the zeros of `Re ζ(σ+iT)` in `[1/2,2]`:
`|Im ∫_u^v ζ'/ζ(σ+iT) dσ| ≤ 2π (#(P ∩ (u,v)) + 1)` for `1/2 ≤ u < v ≤ 2`. 

### `im_integral_logDeriv_le`

 **(V) Variation of the argument along `[1/2,2] + iT`:** if `ζ ≠ 0` there and `Re ζ(σ+iT)` has
finitely many zeros, then `|Im ∫_{1/2}^{2} ζ'/ζ(σ+iT) dσ| ≤ 2π (#reZeroSetL χ T + 1)`. 

 ## Assembly of Backlund's bound from (J) = `reZeroSet_card_le`  and (V) 

### `LFunction_ne_zero_on_segment`

 ζ has no zero on `[1/2,2] + iT` when `T` is not the ordinate of a nontrivial zero. 

### `backlund_horizontalChi_of_count`

 **Backlund's bound for L(s,χ) from the zero count (J)**, two-sided in the height. 

 ## The vertical side σ = 2 

### `re_LFunction_two_pos`

 `Re ζ(2+it) > 0` (indeed `≥ 2 − π²/6`), from `‖ζ(s) − 1‖ ≤ π²/6 − 1 < 1` on `Re s ≥ 2`. 

### `hasDerivAt_log_LFunction_two`

 `t ↦ log ζ(2+it)` is a primitive of `t ↦ ζ'/ζ(2+it)·i`. 

### `continuous_logDeriv_LFunction_two`

 Continuity of `t ↦ ζ'/ζ(2+it)·i`. 

### `vertical_twoChi`

 **Vertical side σ = 2**. `|Im (∫_{T₁}^{T₂} ζ'/ζ(2+it)·i dt)| ≤ π` for all `T₁, T₂`:
`log ζ(2+it)` is a primitive, and `|arg ζ(2+it)| ≤ π/2` since `Re ζ(2+it) > 0`.
(Only an absolute constant is needed downstream; the sharper bound `2 log 3` also holds
— |arg| ≤ arcsin(π²/6−1) — but is not worth the trigonometry.) 
