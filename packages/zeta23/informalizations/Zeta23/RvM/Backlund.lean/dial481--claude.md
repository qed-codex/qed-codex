---
{
  "module": "Zeta23/RvM/Backlund.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/Backlund.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/Backlund.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/RvM/Backlund.lean — Backlund's bound for the horizontal variation of arg ζ, and the trivial
vertical side σ = 2. Consumed by Zeta23/RvM/Statement.lean, which proves
  N(T₁,T₂) = ∫_{T₁}^{T₂} μ + (1/π)·Im ∫_L ζ'/ζ ds,  L = ½+iT₁ → 2+iT₁ → 2+iT₂ → ½+iT₂
for non-ordinate heights and assembles RvM.main from GammaFacts.int_mu + the two bounds below.

* `backlund_horizontal` [Tit86 §9.4, Backlund 1918]: for T large and not the ordinate of a zero,
    |Im ∫_{1/2}^{2} ζ'/ζ(σ+iT) dσ| ≤ C log T.
  Route: g(z) := (ζ(z+iT) + conj ζ(z̄+iT))/2 is analytic near the disc |z−2| ≤ 1.9 and equals
  Re ζ(σ+iT) for real σ; g(2) = Re ζ(2+iT) ≥ 2 − π²/6 > 0; ZerosBound (PNT+ port, unit disc,
  r = 0.8, R = 0.9 after scaling by 1.9) + Zeta23.RvM.zeta_growth (δ = 0.2) give
  #{σ ∈ [½,2] : Re ζ(σ+iT) = 0} ≤ C log T; on each of the ≤ m+1 subintervals where Re ζ(σ+iT)
  has constant sign, Complex.log ∘ (±ζ(·+iT)) is a primitive of ζ'/ζ with |Im| ≤ π.
* `vertical_two`: |Im (I·∫_{T₁}^{T₂} ζ'/ζ(2+it) dt)| ≤ π — log ζ is a primitive on σ ≥ 2
  (‖ζ − 1‖ ≤ π²/6 − 1 < 1 there, Zeta23.RvM.norm_riemannZeta_sub_one_le), and
  |arg ζ(2+it)| ≤ π/2 since Re ζ(2+it) > 0.
-/
```

 ## The horizontal side, calculus half: variation of the argument

Fix a height `T ≠ 0` with `ζ ≠ 0` on the segment `[1/2, 2] + iT`.  If `Re ζ(σ+iT)` has no zero on an
open subinterval `(u,v)`, it has constant sign `ε` there (IVT), `log(ε ζ(σ+iT))` is a primitive of
`ζ'/ζ(σ+iT)` on `[u,v]` (at the endpoints `ε ζ` is `≥ 0` in real part and `≠ 0`, so still in the
slit plane), hence `|Im ∫_u^v ζ'/ζ| ≤ 2π`.  Splitting `[1/2,2]` at the finitely many zeros of
`Re ζ(σ+iT)` (the set `reZeroSet T`, counted by the Jensen bound `reZeroSet_card_le`) gives
`|Im ∫_{1/2}^{2} ζ'/ζ(σ+iT) dσ| ≤ 2π (#reZeroSet T + 1)` — by induction on the number of zeros inside
the interval (no sorting needed). 

### `hasDerivAt_riemannZeta_horizontal`

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
finitely many zeros, then `|Im ∫_{1/2}^{2} ζ'/ζ(σ+iT) dσ| ≤ 2π (#reZeroSet T + 1)`. 

 ## Assembly of Backlund's bound from (J) = `reZeroSet_card_le`  and (V) 

### `riemannZeta_ne_zero_on_segment`

 ζ has no zero on `[1/2,2] + iT` when `T` is not the ordinate of a nontrivial zero. 

### `backlund_horizontal_of_count_at`

 **Backlund's bound from the zero count (J)**, parametric form: a count ncard ≤ C·log T for
T ≥ T₀ gives |Im ∫_{1/2}^{2} ζ'/ζ(σ+iT)dσ| ≤ 2π(C+1)·log T for T ≥ max T₀ 3. 

### `backlund_horizontal_of_count`

 **Backlund's bound from the zero count (J).** 

### `backlund_horizontal`

 **Backlund's bound**. For all large T that are not ordinates of nontrivial zeros,
|Im ∫_{1/2}^{2} ζ'/ζ(σ + iT) dσ| ≤ C·log T. 

### `backlund_horizontal_at`

 **Backlund's bound, explicit**: for T ≥ 4 a zero-free height,
|Im ∫_{1/2}^{2} ζ'/ζ(σ+iT)dσ| ≤ 2π·(C_J + 1)·log T with C_J = (1/log(0.9/0.8))(|log 40| + 2) ≈ 48.3
(so the constant is ≈ 310). 

 ## The vertical side σ = 2 

### `re_riemannZeta_two_pos`

 `Re ζ(2+it) > 0` (indeed `≥ 2 − π²/6`), from `‖ζ(s) − 1‖ ≤ π²/6 − 1 < 1` on `Re s ≥ 2`. 

### `hasDerivAt_log_riemannZeta_two`

 `t ↦ log ζ(2+it)` is a primitive of `t ↦ ζ'/ζ(2+it)·i`. 

### `continuous_logDeriv_riemannZeta_two`

 Continuity of `t ↦ ζ'/ζ(2+it)·i`. 

### `vertical_two`

 **Vertical side σ = 2.** `|Im (∫_{T₁}^{T₂} ζ'/ζ(2+it)·i dt)| ≤ π` for all `T₁, T₂`:
`log ζ(2+it)` is a primitive, and `|arg ζ(2+it)| ≤ π/2` since `Re ζ(2+it) > 0`.
(The sharper constant `2 log 3` also holds — |arg| ≤ arcsin(π²/6−1) — but an absolute
constant suffices for the consumer.) 
