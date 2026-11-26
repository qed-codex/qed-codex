---
{
  "module": "proof/rates/ClauseBound/Grid/Expand.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Grid/Expand.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Grid/Expand.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The expansion over patterns, for any family of pieces

`Groundwork.Grid.Expand` expands the sum over the grid with one fixed family of pieces A_0, …, A_n,
which add up to the function X = [x = v][y = u] of a rectangle. Here the pieces are any functions
A_i, i ∈ I, that add up to d·X for an integer d. `ZG_cross_mul_eq_sum` is the identity d^|R| Z = Σ_ι
Z_ι of the proof of Theorem A on the grid (there R is the set of rectangles, here `Ω ρ γ`, and ι is
here `f`),
`Z_mul_eq_sum` the same for an instance carried to the grid, and `value_rowNet_tr` says that the row
network of the transposed grid, which is the column network,
has the value of the grid that was transposed. 

### `filter_mem_Ω`

 The rectangles, as the subset of all ω that lie in Ω. 

### `ZG_cross_mul_eq_sum`

 If the pieces A_i, i ∈ I, add up to d·X, then d^|Ω| times the sum over the grid with X at every
rectangle is the sum, over all ways f to choose a piece for every
rectangle, of the sum over the grid with the piece A_{f ω} at the rectangle ω. 

### `Z_mul_eq_sum`

 For an instance on any node set J that is laid out on the grid by a bijection e: d^|Ω| times its
value is the sum over all choices of pieces. 

### `value_rowNet_tr`

 The column network: if the cuts factor the functions of the transposed grid, the row network of
the transposed grid has the value of the grid itself. 
