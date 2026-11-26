---
{
  "module": "proof/networks/Paper/SecLevel_Grid.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecLevel_Grid.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecLevel_Grid.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 5 of the paper: the g × g grid of the proof of Proposition 3 and its rectangles

The proof of Proposition 3 places the nodes of a (g², λ)-clique on a g × g grid. This file holds the
grid, the set ℛ of its rectangles
and their number (`card_rectangles`, `card_rectangles_le`), and the types of the settings of the
grid points and of the rows.

Here λ is written `lam`, a bit string of length λ has the type `Bits lam` (= `Fin lam → Bool`), and
rows and columns are numbered
by `Fin g` (0, …, g − 1).

The number of rectangles (`rectangles`, `card_rectangles`, `card_rectangles_le`) is used in the
proof of Theorem 2. 

 ## The grid and its rectangles 

### `Rectangle`

 A rectangle q of the g × g grid, written ((a, a'), (j, j')): two rows and two columns. The
conditions a < a' and j < j' are
part of `rectangles`. 

### `rectangles`

 The set ℛ of rectangles of the g × g grid (proof of Proposition 3): all choices of two rows a <
a' and two columns j < j',
adjacent or not. 

### `card_rectangles`

 The number of rectangles. The paper: «The set ℛ of rectangles has C(g,2)² ≤ g⁴/4 elements.» This
is the equality. Same as in the paper. 

### `card_rectangles_le`

 The inequality of the same sentence: |ℛ| ≤ g⁴/4. Same as in the paper. 

### `Settings`

 A choice of settings of all grid points: z w w' is the string z_w(w'), the copy that the grid
point w keeps of the string on
the edge {w, w'}. (The entry z w w is not used by the paper.) 

 ## The setting of a row 

### `RowSetting`

 A setting of a row (or column): the tuple of the settings of its g grid points. z j w' is the
string that the j-th grid point
of the row keeps for the edge to the grid point w'. 
