---
{
  "module": "Zeta23/Tail/Grid.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Tail/Grid.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Tail/Grid.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Tail/Grid.lean — the grid sum in the proof of [prop:tail] (the paper §4.2).


Paper, verbatim: "Let D := dist(γ, I) ≥ D₀. The points τ_k, 0 ≤ k < d, lie in I with
spacing h = 2π/L, so ‖u_ρ‖₂² ≤ C₁²X^{1/2} ∑_{0≤k<d} |γ−τ_k|⁻⁴
≤ C₁²X^{1/2}(D⁻⁴ + (L/2π)·D⁻³/3) ≤ C₁²X^{1/2} L D⁻³ (as D ≥ 1, L ≥ 2)."
Here τ_k := T + k h [eq:fk], h := 2π/L, d := ⌊T/h⌋ so that τ_0,…,τ_{d−1} ∈ [T, 2T).
We prove the pure inequality ∑_{k<d} |γ − τ_k|⁻⁴ ≤ L·D⁻³ (the constant C₁²X^{1/2} is
threaded in Zeta23/Tail.lean), replacing the integral comparison by a telescoping sum.
-/
```

### `inv_pow_four_step`

 Telescoping replacement for ∫ x⁻⁴: for a > 0, h > 0, h·(a+h)⁻⁴ ≤ (a⁻³ − (a+h)⁻³)/3. 

### `sum_inv_pow_four_le_telescope`

 Telescoped form: ∑_{k ≤ d} (D + k h)⁻⁴ ≤ D⁻⁴ + (D⁻³ − (D + d h)⁻³)/(3h). 

### `sum_inv_pow_four_le`

 ∑_{k<d} (D + k h)⁻⁴ ≤ D⁻⁴ + D⁻³/(3h) for D, h > 0 (any d). 

### `grid_const_bound`

 From D⁻⁴ + D⁻³/(3h), h = 2π/L, to L·D⁻³ "(as D ≥ 1, L ≥ 2)". 

### `grid_sum_le`

 **Grid estimate** (proof of [prop:tail]): with τ_k := T + k·h, h = 2π/L, d·h ≤ T,
L ≥ 2 and D := dist(γ, I) ≥ 1 (I = [T,2T]):  ∑_{k<d} |γ − τ_k|⁻⁴ ≤ L · D⁻³. 
