---
{
  "module": "Zeta23/Tail/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Tail/Count.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Tail/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Tail/Count.lean — the zero-count sum in the proof of [prop:tail] (the paper §4.2).


Paper, verbatim: "It remains to bound ∑_{γ∉I'} m_ρ D⁻³ (zeros counted with multiplicity).
Zeros with γ > 2T+D₀: grouping them into γ ∈ (2T+D₀+j, 2T+D₀+j+1], j ≥ 0, this part is at
most ∑_{j≥0} A₀ log(2T+D₀+j+4)(D₀+j)⁻³ ≤ (3/2)A₀ log(4T) D₀⁻² for T large (split at j = T
and use D₀ ≥ 2). Zeros with 0 < γ < T−D₀ contribute likewise at most (3/2)A₀ log(4T)D₀⁻²,
and zeros with γ ≤ 0 have D ≥ T and contribute at most ∑_{j≥0} A₀ log(j+4)(T+j)⁻³
≪ T⁻² log T. Altogether ∑_{γ∉I'} m_ρ D⁻³ ≤ 4A₀ log(4T) D₀⁻² for T ≥ T₀."

We prove the bound for every FINITE sub-family of tail zeros (which yields both the
summability and the bound for the full series downstream), with the explicit absolute
threshold T₀ of Zeta23/Tail/Basic.lean. Only the final constant 4 is load-bearing (it is
the 4 in θ₀); we do not follow the paper's intermediate 3/2 + 3/2 + o(1) split. Our
grouping: unit windows indexed by the integer distance j from the nearer endpoint of
I = [T,2T] (lower side: T−j−1 < γ ≤ T−j, which also covers ALL γ ≤ 0; upper side:
2T+j < γ ≤ 2T+j+1), each window weighted by max(D₀, j)⁻³ and counted by the two-sided
local count ≤ A₀ log(2T+4+j); integrals are replaced by telescoping sums.
-/
```

 #### Telescoping sums replacing ∫ x⁻³ and ∫ x⁻² 

### `sum_inv_pow_three_le`

 ∑_{i<n} (D + i)⁻³ ≤ D⁻³ + D⁻²/2 for D > 0 (any n). 

### `sum_inv_pow_two_le`

 ∑_{i<n} (D + i)⁻² ≤ D⁻² + D⁻¹ for D > 0 (any n). 

### `log_add_le_log_add_div`

 log(B + j) ≤ log B + j/B. 

 #### Summing the window weights 

### `sum_window_weights_le`

 The window weights: for a finite set F of window indices j with j + 1 ≥ D₀ (D₀ ≥ 2),
∑_{j∈F} max(D₀,j)⁻³ · log(B + j) ≤ (2D₀⁻³ + D₀⁻²/2)·log B + (2D₀⁻² + D₀⁻¹)/B. 

 #### One side of the tail, abstractly 

### `one_side_sum_le`

 One side of the tail: zeros at (signed) distance x_ρ ≥ D₀ beyond an endpoint of I,
grouped by an integer key with key ≤ x ≤ key + 1, each group counted by A₀ log(B + key). 

 #### Numerics at T ≥ T₀ 

### `two_sides_numeric`

 The window-weight total, doubled (two sides), is ≤ 4 log(4T)/T for T ≥ T₀. 

 #### The zero-count sum 

### `tail_count_sum_le`

 **Zero-count sum** (proof of [prop:tail]). For T ≥ T₀ and every finite set s of tail
zeros (γ_ρ ∉ I'), ∑_{ρ∈s} m_ρ · dist(γ_ρ, I)⁻³ ≤ 4 A₀ log(4T) / D₀², with D₀² = T. 

 #### The boundary count N(I' ∖ I) 

### `sum_mult_le_of_windows`

 Counting by unit windows: if every zero of s falls in one of K windows (key < K) and each
window holds total multiplicity ≤ C, then ∑_s m ≤ K·C. 

### `boundary_count_le`

 **Boundary count** N(I' ∖ I) = N(T−D₀, T] + N(2T, 2T+D₀] ≪ D₀·l (used in
[prop:zeroside], [prop:zeroside-rank]: "N(I'∖I) ≪ D₀ l by N(t+1)−N(t) ≤ A₀ log(t+3)").
Explicit form: for T ≥ T₀ and every finite set s of zeros with
γ_ρ ∈ (T−√T, T] ∪ (2T, 2T+√T], ∑_{ρ∈s} m_ρ ≤ 3 · A₀ · √T · log(4T)
(and log(4T) ≤ 2 log(T/2π) = 2l for T ≥ T₀, see log_four_mul_le_two_mul_l). 
