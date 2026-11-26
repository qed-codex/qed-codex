---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Round.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Round.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Round.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The reduction from 3SUM to Convolution-3SUM: one splitting

round(β, β', b, nd, val, bt, Λ, A, n, f, cx, fr) handles the splitting `(β, β', v)` of the set of
the distinct values, where `b` is 1 for `v = true` and 0 for `v = false` (for Theorem 21(a), after
[CH20, Theorem 5.1]).  The first set of the splitting holds the values whose label x + V has the
binary digit β equal to v; the second and the third hold those whose digit β differs from v and
whose digit β' is 0 and 1 (`splitA`, `splitB`).  The routine selects the three sets by their binary
digits, writes them to `A`, `A + n` and `A + 2n` (`roundSets_ends`), and calls the recursive
procedure on them (`round_spec`).

What the memory holds while the splittings are run through (`FrontMem`) does not depend on the 3n
cells from `A` (`FrontMem.keptBut`).  So each of the three calls of pick finds what it needs
(`FrontMem.pick_meets`), and afterwards the three sets and the rest form the memory of a node
(`FrontMem.nodeMem`).  The time is `le_tRound`, with `ChRound.treeCalls_le_pow` for the number of
calls of the recursive procedure.


### `BETA`

 The local variables of round: the arguments β, β', b, nd, val, bt, Λ, A, n, f, cx, fr; then
1 - b, A + n, A + 2n, and the sizes of the three sets. 

### `roundSets`

 The three sets of the splitting are written to A, A + n and A + 2n. 

### `roundBody`

 round(β, β', b, nd, val, bt, Λ, A, n, f, cx, fr), over the procedures number pPick and pNodes:
the three sets are written, and the recursive procedure is called on them. 

### `ChRound.treeCalls_le_pow`

 The recursive procedure makes at most `2 · 3^f` calls. 

### `FrontMem.keptBut`

 What the memory holds while the splittings are run through is kept if, below the free pointer,
only the 3n cells from A change. 

### `FrontMem.of_sameOutside`

 The same if only the 3n cells from A change at all. 

### `FrontMem.pick_meets`

 pick, called for the distinct values, with the output in one of the three parts of the 3n
cells from A. 

### `FrontMem.nodeMem`

 Three subsets of the distinct values in the three parts of the 3n cells from A, with the rest of
the memory, are the memory of a node. 

### `roundSets_ends`

 **The three sets of the splitting** are written, and with the rest of the memory they are the
memory of a node. 

### `le_tRound`

 The time of round covers three calls of pick and the recursion tree: 48 steps and the three
calls for roundSets, 11 steps and the tree for the last call. 

### `round_spec`

 **round meets its specification**, in every program that holds its body and meets the
specifications of the two routines that it calls. 
