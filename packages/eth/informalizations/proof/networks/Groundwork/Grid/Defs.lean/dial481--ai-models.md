---
{
  "module": "proof/networks/Groundwork/Grid/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Grid/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Grid/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 One level of the recursion (the grid, its rectangles and the merged rows, as in the proof of
Proposition 3), definitions only: the clique on a grid with rows in a type ρ (not the
constant ρ), columns in γ and labels in α, written with half-edges; a function G of the four ends at
every rectangle; the
network obtained by merging every row into one node, for any factorisation («cut») of the functions
G top|bottom; the
transposed grid, which turns columns into rows; and the patterns ι that index the terms Z_ι. 

### `Rect`

 A rectangle ((a,b),(i,i')): rows a < b, columns i < i' (the inequalities are in Ω). 

### `Ω`

 The set of rectangles. 

### `Half`

 Half-edge labellings: ℓ w w' is the copy held by w of the label of the edge {w,w'}. 

### `app`

 G at the four ends x, y (top), u, v (bottom) of the two diagonals of the rectangle ω. 

### `onGrid`

 The instance carried to the grid along e; it vanishes unless the entry at the node itself is d. 

### `RowSt`

 A state of a row: z i w' is the half-edge from the node of the row in column i towards w'. 

### `RowLab`

 A label of two rows: the labels of the vertical edges between them, and a label in τ for each of
their rectangles. 

### `Cut`

 A factorisation top|bottom of a function of the four ends: G x y u v = Σ_{θ ∈ lab} top x y θ ·
bot u v θ (see Factors),
and the number of bits charged for it. 

### `Cut.Factors`

 The cut C is a factorisation of G. 

### `trInst`

 The grid transposed: the instance. 

### `trG`

 The grid transposed: the functions at the rectangles. Transposing exchanges the ends y (top
right) and u (bottom left). 

### `ZG`

 Σ_ℓ ∏_w R_w(ℓ(w,·)) · (equalities of the edges inside a row) · (equalities of the edges inside a
column)
· ∏_ω G_ω(x,y,u,v). The sum is over all ℓ, the entries ℓ w w included; for an instance made by
`onGrid`, R vanishes unless
ℓ w w is the default label, so that these entries add nothing. 

### `rowW`

 The weight of row a: its tensors and the equalities of the edges inside it. 

### `rowΨ`

 The interaction of rows a < b (z the state of a, z' that of b): the equalities of the vertical
edges and the functions G
of their rectangles. 

### `rowΘ`

 The label set of rows a < b. 

### `rowTop`

 The factor of rows a < b on the side of a. 

### `rowBot`

 The factor of rows a < b on the side of b. 

### `rowNet`

 All rows merged: the row network. L is the number of bits of α, used in the table of capacities
only:
c_ab = (number of columns)·L for the vertical edges, plus the bits charged for the rectangles on
rows a, b. 

 ### The patterns ι of the terms Z_ι 

### `Pat`

 The patterns ι: a number in {0,…,λ} for every rectangle (0 off the rectangles). 
