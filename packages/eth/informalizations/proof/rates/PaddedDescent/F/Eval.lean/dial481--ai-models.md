---
{
  "module": "proof/rates/PaddedDescent/F/Eval.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Eval.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Eval.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One evaluation, and the count for one sparse formula

`stValF`: the top rebalancing, the descent through the levels and exhaustive search at the bottom
compute the value of every network with entries 0, 1, −1 that is
given by plain functions, if the pad is long enough. `stEval`: hence one evaluation, the sum over
the admissible profiles of the values of the networks of marks, is
the cut-off sum `Mark.trunc`. `stCountM`: hence the choice of the layers by the program is the
choice of the layers with exact evaluations, no cut-off by the pad
is active, and `countM` is the number of satisfying assignments. The hypotheses are interface
statements of `proof/rates/PaddedDescent/F/Interfaces.lean`. 

 ### The value of a network 

### `le_lamG`

 x ≤ lamG K g Ub₀ P if K³·x ≤ K³ + K·U + g·P' with U ≤ Ub₀ and P' ≤ P. 

### `val_core`

 `StValF` with the numbers K and g of nodes as free variables. 

### `length_gU`

 The number of nodes at the top. 

### `stValF`

 `valF` computes the value of every network that F presents, if its entries are 0, 1, −1 and the
pad is long enough. 

 ### One evaluation 

### `map_range_getD`

 A function of the members of a list, listed by position. 

### `length_cls`

 The list of all clauses with the index of their layer has as many members as the layers have
clauses. 

### `nProf_le`

 The number of profile numbers grows with the number of clauses and of layers. 

### `stEval`

 One evaluation is exact if the pad is long enough. 

 ### The layers: their form does not depend on the evaluation function 

### `take_getD_drop`

 A list is its first i members, its member number i, and the rest. 

### `Form`

 R + 1 layers that hold c clauses, all of 1 to k literals on variables below n. 

### `Form.placeAt`

 Adding a clause to a layer keeps the form. 

### `Form.placeE`

 Placing a clause keeps the form, whatever the evaluation function. 

### `form_replicate`

 The empty layers. 

### `len_lit_le`

 A bound on the length of the word of a literal with variable below n. 

### `len_layers_le`

 A bound on the length of the word of layers, by the number of their clauses. 

### `Form.len_le`

 The word of layers of the given form fits under a pad of length layLen k n m R, if they hold at
most m clauses. 

### `foldl_cap_eq`

 No cut-off by the pad is active in the loop that places the clauses. 

### `layersF_eq`

 The layers that the program chooses are those of the generic choice with the program's
evaluation function. 

 ### The count 

### `stCountM`

 `countM k` counts the satisfying assignments of a formula with clauses of 1 to k literals, if
the pad is long enough. 
