---
{
  "module": "proof/rates/CountedRecursion/SolverStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/SolverStages.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/SolverStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The stages of the solver

The solver at a level ℓ + 1 (`levelSolver`, SolverDefs.lean) runs its stages one after the other.
Here each stage is run against ANY oracle O and prices w, of which only what the stage asks is
assumed; nothing is said yet of the pieces or of the networks.
* `askInt_within`, `askList_within`: one query.
* `capsLoop_within`: «the numbers … c^row_i, c^col_i are computed once»: one query for each i in the
  list.
* `sumAndDivide_within`: «adding one Z_ι», for all ι; then «computing d^{|ℛ|} and dividing by it».
* `levelSolver_within`: all stages. The cost is 2ℓ + 5 + 2|𝓘| own steps, 2|𝓘| + 2 queries to the
  pieces, and the cost of `sumAndDivide`, which is the cost of the patterns, one step more for each
  pattern, and 2 steps more. 

### `askInt_within`

 One query, read as an integer. 

### `askList_within`

 One query, read as a list. 

 ### Numbers and lists 

### `size_le_of_le`

 The size of a number grows with the number. 

### `size_le_succ`

 A number n has size at most n + 1. 

### `size_mem_le`

 An element is not larger than the list. 

### `length_lt_size`

 A list has at most as many elements as its size. 

### `size_take_le`

 The first k elements are not larger than the list. 

### `map_range_getD`

 The first k elements, read off by their places. 

### `foldl_append_toNat`

 The loop that appends one number in each round makes the list of the numbers. 

 ### The stages 

### `capsLoop_within`

 «The numbers … c^row_i, c^col_i are computed once»: if the oracle answers the question for the
element number j of the list by the number at the place j of `caps`, at the price t, the loop
returns `caps` within |𝓘|·(t + 1) operations. 

### `sumAndDivide_within`

 «adding one Z_ι», for all ι; then «computing d^{|ℛ|} and dividing by it»: if the pattern number
y costs T₀ and has the value v y, |v y| ≤ V, the whole costs |𝓘|^{|ℛ|}·(T₀ + 1) + 2 operations. 

### `levelSolver_within`

 **All stages.** The oracle answers the question for 𝓘 by the list I, that for d by d, those for
c^row_i and c^col_i by the numbers of the lists c₀ and c₁, each at the price t; the numbers K and g
are written by the loop on states of size at most S₁; and the last stage, on what has been computed,
costs T₆ on states of size at most S₆. 
