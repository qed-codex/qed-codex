---
{
  "module": "proof/machines/StepMachines/Math/SideCodes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SideCodes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SideCodes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The g × g grid of Section 2.5 of the paper, on words (lists of bits), for rows (tr = false) and
columns (tr = true) at once.
A «part» is a row, or a column if tr. The node number x of the part a is the node (a,x) of the grid,
or of the transposed
grid if tr; its position among the g² nodes of the instance is x + g·a, or a + g·x if tr. A
half-edge is one end's
copy of the label of an edge. The word of a state of a part: for each of its g nodes, the g²
half-edges that start there,
in the order of the positions of their other ends, n bits each. 

### `gridE`

 The g² nodes of the instance on the grid; transposed if tr. 

### `node`

 The position of the node number i of the part a. 

### `gridE_symm_val`

 The position of a node of the grid among the g² nodes of the instance. 

### `node_lt`

 Positions are below g². 

### `he`

 In the word z of a state of a part: the half-edge from the node number x of the part to the node
at position u. 

### `length_he`

 A half-edge in the word of a state has ℓ bits. 

### `vC`

 The code, on words of g·n bits, of the labels of the g edges between two parts that join nodes
of the same number. 

### `nodeC`

 The code, on words of g²·n bits, of the half-edges that start at one node. 

### `stC`

 The code, on words of g³·n bits, of a state of a part. 

### `stC_dec`

 The state named by a word, read half-edge by half-edge. 

### `instW`

 An instance on words of n bits, read as an instance with labels in Bits n; [] at the node
itself. 

### `sideR`

 The same, carried to the grid; to the transposed grid if tr. 

### `sideR_true`

 The instance on the transposed grid is the transpose of the instance on the grid. 

### `ZW_eq_Z`

 Z on words is Z with labels in Bits n. 

### `abs_sideR_le`

 The bound 2^B on the instance at the queries that are asked passes to the grid. 

### `sideR_nodeC`

 The tensor of a node of the grid, at the word of the half-edges that start at this node: 0
unless the block at the
node's own position is all zeros. 
