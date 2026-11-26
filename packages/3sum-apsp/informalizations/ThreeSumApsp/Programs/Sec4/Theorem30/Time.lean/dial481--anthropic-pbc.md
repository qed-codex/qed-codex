---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/Time.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Time.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Time.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 30 in the light language: the tiles and a query against the expressions (8) and L ∑ α_d

Pure arithmetic. The routines of Section 4 have explicit time functions. This file and the next one
show that, under the hypotheses of Theorem 30 (`Hyp30`), time and space of the preprocessing are at
most a constant times the expression (8), and the time of a query is at most a constant times
L ∑_{d ≤ t} α_d.

`Within8 f` says that f is at most a constant times (8). Such bounds can be added, multiplied by a
number and passed to smaller functions. Four quantities are within (8) by the counts in the proof of
Theorem 30: the number 1, the number 10^L of leaves, the work 10^L + L 7^L for each band, and L for
each box of each tile (`within8_one` to `within8_boxes`); the next file adds a fifth, N (L + 1)
(`within8_N_mul`). Every other function is bounded by a multiple of a sum of these: here the time
for all tiles (`within8_tAllTiles`) and the space of their tries (`within8_trieSpace`). For a query
see `exists_tQueryCore_le`.


 ## The hypotheses of Theorem 30, and what lies within (8) 

### `Hyp30`

 The hypotheses of Theorem 30 on the parameters. 

### `ten_pow_le_cost8`

 `10^L` is within (8): it is at most the last term. 

### `one_le_cost8`

 The expression (8) is at least 1. 

### `Within8`

 `f = O((8))`: at most a constant times the expression (8), for all parameters that satisfy the
hypotheses of Theorem 30. 

### `of_le`

 A smaller function. 

### `within8_bands`

 The work for the bands: `10^L + L 7^L` for each band. 

### `within8_boxes`

 The work for the boxes: `L` for each box of each tile. 

 ## The tiles 

### `one_le_length_starBoxes`

 For every e ≤ m - t with e ≤ L there is a box with e stars. 

### `succ_le_card_boxes`

 There are at least m - t + 1 boxes: one for each number of stars. 

### `tTile_eq`

 The time for a tile, in closed form. 

### `exists_tTile_le`

 The time for a tile, and what the loop over the tiles adds to it, is O(L) for each box (Lemma
29). The enumeration of the boxes with e stars is started once for each e ≤ m - t, in O(L) steps
each time; these m - t + 1 starts are paid for by the boxes, of which there are at least m - t + 1
(succ_le_card_boxes). 

### `within8_tAllTiles`

 **The tries of all tiles** are built within (8). 

### `within8_trieSpace`

 **The space of the tries and of their roots** is within (8). 

 ## A query 

### `cast_L_le_costQuery`

 The query cost of Theorem 30 is at least L. 

### `one_le_costQuery`

 The query cost of Theorem 30 is at least 1. 

### `exists_tQueryCore_le`

 **A query**, once the digits of its output string are known, takes O(L) steps for each number
that it reads. 
