---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Grid.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Grid.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Grid.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The reduction from 3SUM to Convolution-3SUM: the loop over the splittings.  row and grid

A step added to the reduction of [CH20, Theorem 5.1], one of the reductions behind Theorem 21(a):
the reduction from 3SUM on one set to the version with three sets, by the first binary digit in
which two labels differ (the label of a value x is x + V).  Below, "round" is the routine of that
name, which handles one splitting; a round of a loop is called so only in the names rowRound and
gridRound and in their lemmas.

* row runs through the splittings `(β, β', v)` for a fixed `β` and adds up the answers of round
  (`row_spec`; a round of its loop is `rowRound_ends`, and what it does to the sum is
  `RowSum.succ`).
* grid runs through `β` and returns 1 if some row has a positive sum (`grid_spec`,
  `gridRound_ends`).


 ## The procedures 

### `Beta`

 The local variables of row: the arguments β, nd, val, bt, Λ, A, n, f, cx, fr; the sum; β'; and
the last answer.  Local 0 also takes the result. 

### `rowRound`

 A round of row: the answers for (β, β', false) and (β, β', true) are added to the sum. 

### `rowBody`

 row(β, nd, val, bt, Λ, A, n, f, cx, fr): sum := 0; a round for each β' < Λ; return the sum. 

### `NumValues`

 The local variables of grid: the arguments nd, val, bt, Λ, A, n, f, cx, fr; the answer so far;
β; and the sum of the last row.  Local 0 also takes the result. 

### `gridRound`

 A round of grid: if the sum of row β is positive, the answer is 1. 

### `gridBody`

 grid(nd, val, bt, Λ, A, n, f, cx, fr): answer := 0; a round for each β < Λ; return the
answer. 

 ## What the two routines share 

### `GridPre.down`

 What row and grid assume provides a word for 2Λ + 16, one more level of calls, and what the
routine one level below assumes. 

 ## row 

### `RowSum`

 What is known about the sum after the splittings (β, β', v) with β' < i: it lies between 0 and
2i, and it is positive exactly if one of the answers was yes. 

### `RowSum.succ`

 Adding the answers for (i, false) and (i, true) takes `RowSum S i` to `RowSum S (i + 1)`. 

### `RowInv`

 The state before round i of the loop of row: the locals are the arguments, the sum, i, and the
last answer; the sum is as `RowSum` says; and below the free pointer only the 3n cells from A have
changed. 

### `rowRound_ends`

 **A round of row** adds the answers for (β, β', false) and (β, β', true) to the sum. 

### `row_spec`

 **row** meets its specification. 

 ## grid 

### `FrontArgs.RowYes`

 Some splitting (β, β', v) of row β gives a yes-instance. 

### `GridInv`

 The state before round i of the loop of grid: the locals are the arguments, the answer so far,
i, and the sum of the last row; the answer tells whether one of the rows below i had a positive sum;
and below the free pointer only the 3n cells from A have changed. 

### `gridRound_ends`

 **A round of grid** asks for the sum of row i and sets the answer to 1 if it is positive. 

### `grid_spec`

 **grid** meets its specification. 
