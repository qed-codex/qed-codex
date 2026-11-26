---
{
  "module": "Zeta23/XiPrime/ZeroCount/Generic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/Generic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/Generic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ZeroCount/Generic.lean — the zero-counting templates with Y := ξ′/Γℝ abstracted to an
arbitrary f (the Hardy-W development instantiates f := hardyW).

INPUT DATA ("two-line data" for f about the line Re s = 2):
  hfa   : for |t| ≥ t₀, f is analytic on a neighbourhood of closedBall (2+it) (91/50);
  hgrow : ‖f s‖ ≤ Cf·|Im s|^k on 1/8 ≤ Re s ≤ 4, |Im s| ≥ 2;
  hlow' : ‖f(2+it)‖ ≥ 1 for |t| ≥ t₀.
OUTPUTS:
  logDeriv_partial_fraction_two_line — Landau: zero finset in the 22/25·91/50-ball, Σ ord ≤ C log(|t|+3), and
      f′/f = Σ ord/(s−ρ) + O(log(|t|+3)) on the 3/2-ball (|t| ≥ t₁ := max t₀ 4);
  horizontal_bound_two_line — |Im ∫_{1/2}^{2} f′/f(σ+iT)dσ| ≤ C log(|T|+3) whenever no right-half-plane zero of f
      has ordinate T;
  local_count_two_line — for a ZeroConfig Zc whose points with β ≥ 1/2 are zeros of f of the same order:
      N(t,t+1] ≤ A₀ log(|t|+3) for all t;
  good_heights_two_line — if moreover every right-half-plane zero of f with |Im| ≥ t₀ is in Zc: for j ≥ j₀ some
      R ∈ [j,j+1] has f ≠ 0, ‖f′/f‖ ≤ C log²(j+3) on Im s = ±R, 1/2 ≤ Re s ≤ 2.
(ZeroCount/{Landau,Sides,GoodHeights}.lean derive the f = Yfn := ξ′/Γℝ instances from these.)
-/
```

### `logDeriv_partial_fraction_two_line`

 **Landau partial fraction about 2+it, generic.** 

### `horizontal_bound_two_line`

 **Horizontal sides, generic**: with the data of `logDeriv_partial_fraction_two_line`, for every T with
|T| ≥ t₁ such that no zero of f in the right half-plane has ordinate T,
|Im ∫_{1/2}^{2} f′/f(σ+iT) dσ| ≤ C·log(|T|+3). 

 ### local count 

### `half_count_large_two_line`

 the β ≥ 1/2 half of the window (t, t+1] counted with multiplicity is ≪ log(|t|+3), for |t + 1/2| ≥ t₁. 

### `local_count_two_line`

 **Local count, generic**: N(t,t+1] ≤ A₀ log(|t|+3) for every real t, for a ZeroConfig linked to f. 

 ### good heights 

### `good_heights_two_line`

 **Good heights, generic**: with the two-line data for f and a ZeroConfig Zc whose β ≥ 1/2 points are zeros
of f with the same order (hlink) and which contains every right-half-plane zero of f with |Im ρ| ≥ t₀ (hlink'):
for j ≥ j₀ there is R ∈ [j, j+1] with f ≠ 0 and ‖f′/f‖ ≤ C log²(j+3) on Im s = ±R, 1/2 ≤ Re s ≤ 2. 
