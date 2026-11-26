---
{
  "module": "proof/machines/StepMachines/Prog/SidePresents.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/SidePresents.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/SidePresents.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 One level of the recursion (Section 5): in one term of the expansion all rows or all columns
(the flag `tr`) of the g × g grid are merged, which
gives a network `sideN` on g nodes: weights W at the nodes, factors f of the interaction of every
pair. This file shows
that what sideWP and sideFP compute on bit strings are these weights and factors, and that the sizes
for the weights stay within
S + a·(size c + B + λ)^a, where a = `sideA g` and B, S are bounds assumed of the procedure of the
instance on the grid. 

 ### Booleans and products of indicators 

### `prod_counter_pairs`

 The product over the counter j < g·g, with 1 off the pairs i < i', is the product over the pairs
i < i'. 

 ### The weights 

### `sideChk_iff`

 The test of sideWP, spelled out. 

### `sideN_W_eq`

 What sideWP computes is the weight of the network. 

 ### The factors 

### `prod_sideEdges`

 The test of sideFP, as a product of indicators. 

### `sideN_f_eq`

 What sideFP computes is the factor of the network. 

 ### The arithmetic of the bounds 

### `sideA`

 The constant a of the bounds. 

### `side_size_of`

 A size that is linear in size c + B + λ, beside S, is within the bound. 

### `size_pattern_le`

 The size of the number y that encodes the pattern ι ∈ {0,…,n}^R of one level of the recursion,
with R = `nRect g` rectangles. 

### `side_size_W`

 The sizes of the weights. 
