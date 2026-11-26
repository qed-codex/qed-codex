---
{
  "module": "proof/machines/ToTuring/Poly/GridSide.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/GridSide.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/GridSide.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial time for the network of one side in Section 5 (One level of the recursion): one term
of the expansion over the rectangles of the g × g
grid, with all rows or all columns merged (the flag `tr` says which). Every plain function in a step
of the procedures of
this network is polynomial-time (`PolyT`), some of them when a length is given in unary (`Unary`),
and the procedures for the weights and the factors
are built from these functions and the procedure of one rectangle (`cutP`) by combinators that keep
`IsPolyT`. The procedures
are those of StepMachines/Prog/Side.lean; the functions on positions come from
StepMachines/Math/Side*.lean. 

 ### Positions in the words of the grid 

### `rectLen_polyT`

 The length of the chunk of a rectangle; the length n of the indices is given in unary. 

### `drop_sum_eq`

 Where a chunk starts: only as many earlier chunks as the word has bits need to be added up,
since no chunk is empty. 

### `sideChunk_polyT`

 The chunk of a rectangle in a label. 

### `viewAt_polyT`

 The input of the procedure of one rectangle; the length n is given in unary. 

### `sideCap_le'`

 A bound on the label bits of a pair of parts for every n (`Grid.sideCap_le` of
StepMachines/Math/SideNet.lean needs 1 ≤ n). 

 ### The weights 

 ### The factors 

 ### The procedures 

### `IsPolyT.sideWP`

 Every step of the procedure for the weight of a merged node is polynomial-time, if this holds of
the procedure `R` for
the entries of the tensors. 

### `IsPolyT.sideFP`

 Every step of the procedure for a factor of the interaction of two merged nodes, a product over
their rectangles, is
polynomial-time. 
