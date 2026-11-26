---
{
  "module": "Paper/Grids.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Grids.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Grids.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "The flat case": sums over bits as permanents


### `GridEntry`

 The fixed entries of the grid matrix and the sums of weights of one row of clauses. 

### `prop_grid`

 **Paper: Proposition prop:grid.** "Let R be a commutative ring with an element ½, let v : N → V, w : N → K be
surjections of finite sets, and let W_n(x,r) ∈ R. Then ∑_x ∑_r ∏_n W_n(x_{v(n)}, r_{w(n)}) is the permanent of an S×S
matrix, for every S ≥ 3|N|, whose entries are 0, ±1, ±½ and sums of values W_n with the same w(n)." 

### `gridComplete_perm`

 The affine form of Proposition prop:grid: if the weights at an incidence are affine in the variable of its second
class, the matrix has entries that are affine in one variable each. So the permanent is complete for grid sums. 

### `clauseSum`

 A clause sum: the sum over the bits of the product over the clauses of the weight of the clause if all its
literals hold, and 1 otherwise. 

### `clauses_of_complete`

 A clause sum is a projection of every family that is complete for grid sums. 

### `cor_clauses`

 **Paper: Corollary cor:clauses.** "Let 2 ≠ 0 in k. A clause sum with N literals in all, whose weights are constants
or variables, is the permanent of an S×S matrix, S ≥ 3N, with entries that are affine in one variable each." 
