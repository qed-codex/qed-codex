---
{
  "module": "proof/rates/ClauseBound/Alg/GridPresents.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/GridPresents.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/GridPresents.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The programs of a grid with p rows and d columns present its network

The file treats a grid with p rows and d columns in the way the square grid is treated in
Prog/SidePresents.lean. `gridW` and `gridFf` are written with tests on lists and with loops. First
they are rewritten as products over the nodes of a part and over the pairs of nodes of a part; then
the weights and the factors of the network `gridN` are brought to the same form;
`presents` puts the two together. 

### `all_range_fin`

 A test on all i < n holds if and only if it holds for all i in Fin n. 

### `prod_ind_range`

 A product of indicators is the indicator of the test on all i < n. 

### `bitsOf_bitsOf`

 A word of n bits, read as a function and written again, is the word. 

### `chkG_iff`

 The test of `gridW`, spelled out. 

### `gridW_eq`

 The weight of the part a at the word z: the product of the entries of its nodes (0 unless the
half-edge of a node to itself is all zeros), times the tests that the two ends
of every edge inside the part agree. 

### `item`

 The factor of the rectangle on the nodes number i < i' of the parts a, b, on the side of a: z is
the word of the state of a and θ the label. 

### `gridFf_eq`

 The factor of the parts a, b on the side of a: the tests on the edges between nodes of equal
number, times the factors of the rectangles. 

 ### The weights of the network 

### `gridR_nodeC`

 The tensor of a node of the grid, at the word of the half-edges that start at this node: 0
unless the block at the node's own position is all zeros. 

### `gridN_W`

 The weight of the part a at the word z of a state. 

### `gridW_eq_W`

 What `gridW` computes from a table is the weight of the network of the instance of the table. 

 ### The factors of the network 

### `mem_gridCl_D`

 Every word of the right length names a label of the parts a < b. 

### `grid_core`

 Both factors of two parts a < b at once: o is the other part, and top says whether the function
`top` or the function `bot` of the factorizations in `cutsG` is taken. 

### `gridN_f`

 The factor of the parts a ≠ b on the side of a: the tests on the edges between nodes of equal
number, times the factors of the rectangles. 

 ### The programs present the network 

### `presents`

 The functions of `gridF` are the weights and the factors of `gridN` for the instance of the
table, on all words of the right lengths. 
