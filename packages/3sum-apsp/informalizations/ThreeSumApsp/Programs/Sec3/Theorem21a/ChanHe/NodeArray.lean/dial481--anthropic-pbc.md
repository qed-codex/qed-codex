---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/NodeArray.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/NodeArray.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/NodeArray.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The reduction from 3SUM to Convolution-3SUM: the array of a node

Theorem 21(a), after [CH20, Theorem 5.1].
nodeArray(M, s₁, l₁, s₂, l₂, s₃, l₃, V, m, y, cnt, fr) writes the first `8 m²` cells of the
one-array instance of the node `(S₁, S₂, S₃, M)` (`ChanHe.Node.oneArray`) to `y`
(`nodeArray_spec`).  The array consists of c = 2m² groups of four cells; cell t of group i is the
cell y + 4i + t.

* With `W = 2V + 1` and `G = 3W + 1` the padding pattern `10G, W + G, W + 3G, -W + 4G` (`padVal`) is
  written to all groups (`pad_ends`).
* Then, for each of the three sets, a pass (`placeStmt`, `place_ends`) computes the remainders of
  the numbers sg · x, where x runs through the set and sg is 1 for the first two sets and -1 for the
  third; counts them in the count table; writes sg · x + g, for every x whose remainder r has the
  count 1, to cell off of group r (and of group r + M, for the third set; `placeRound_ends`,
  `PlaceInv`); and removes the counts again.  Here g is G, 3G, 4G and off is 1, 2, 3.
* In terms of the arrays of the reduction (`place_arr`): afterwards cell off of group i holds entry
  i of the array of the set, plus g (`place_col` for the first two sets, `place_colZ` for the
  third).
* The four kinds of cells make up the one-array instance (`oneArray_of_cells`); the parts are put
  together in `nodeArrayBody_ends`.

The three passes are the same piece of text, which reads its parameters from local variables.  It is
not a procedure of its own, so that the depth of calls is the one that the specification allows for.

From other files: `keys M L` is the list of the remainders of the numbers of L, as natural numbers;
`arr S M pd r` is the element of S with the remainder r if there is exactly one, and the padding
value pd otherwise; `arrZ` is the same for the negatives of S, repeated at r + M; `BucketPre` is
what coll and heavy assume about a set and the count table; `Counted` says that the remainders stand
at the free pointer and that the table holds how often each occurs.


 ## The local variables 

### `MOD`

 The local variables of nodeArray: the arguments M, s₁, l₁, s₂, l₂, s₃, l₃, V, m, y, cnt, fr; the
numbers W and G; a counter, an address, a remainder, a value and the result of a call, which the
padding loop and the passes use; the number 2m² of groups; the parameters of a pass, which are the
sign sg, the number g that is added, the address and the length of the set, the number of the cell
in its group, and the distance to the second cell; the free pointer behind the remainders; and the
padding pattern. 

### `ArrArgs`

 The arguments of nodeArray. 

### `padVal`

 The padding pattern: what cell t of a group holds before the passes. 

### `ArrScratch`

 The scratch variables of the padding loop and of a pass: counter, address, remainder, value,
result of a call, and the free pointer behind the remainders. 

### `arrLocals`

 The list of the local variables of nodeArray, once the constants have been computed. 

 ## The padding pattern 

### `padStmt`

 For i < 2m²: the four cells of group i become the padding pattern. 

### `PadInv`

 The memory before group j is written: the groups below j hold the pattern p, and no cell outside
the c groups has changed. 

### `PadInv.succ`

 One more group. 

### `pad_ends`

 **The padding pattern** is written to all groups. 

 ## One pass over a set 

### `placeRound`

 A round of the loop of a pass: key := mem[fr + j]; if mem[cnt + key] = 1 then
sg * mem[s + j] + g is written to the cells y + 4 key + off and y + 4 key + off + δ. 

### `placeLoop`

 The loop of a pass: a round for each j < len. 

### `placeStmt`

 One pass.  The remainders of the numbers sg · x go to the cells from the free pointer and are
counted; the loop writes sg · x + g for every x whose remainder has the count 1; the counts are
removed. 

### `tPlace`

 The time of a pass over len numbers: remainders, counting, the loop, and removing the counts. 

### `PlaceCell`

 The cells that a pass may write: the cells y + 4r + off and y + 4r + off + δ for r < M. 

### `PlaceInv`

 The memory μ' before element j of a pass is looked at.  μ is the memory before the loop, K the
list of the remainders, and val r what the cells of the remainder r are to hold.  The cells of the
remainders that have the count 1 and occur among the first j remainders hold their values, and no
other cell has changed. 

### `zero`

 Before the first element. 

### `mem_take_succ`

 The first j + 1 remainders are the first j and remainder number j. 

### `succ_one`

 An element whose remainder has the count 1 is written to its two cells. 

### `succ_many`

 An element whose remainder does not have the count 1 is passed over. 

### `done`

 After the last element. 

### `PassPre`

 What a pass assumes: what coll and heavy assume about the set and the count table; sg is 1
or -1; the array of ylen cells from y lies below the free pointer, apart from the set and the table,
and has room for the cells that the pass writes; off is the number of a cell in its group; the
second cell is the first one (δ = 0) or lies behind the first M groups; and sg · x + g fits in a
word. 

### `PassPre.placeCell_lt`

 A cell that a pass may write lies in the array. 

### `placeRound_ends`

 **A round of the loop of a pass** looks at element j.  μ₀ is the memory at the start of the pass
(of H only the layout and the limits are used), μ the memory at the start of the loop, when the
remainders K have been counted, and μ' the memory before the round. 

### `placeLoop_ends`

 **The loop of a pass.**  μ₀ is the memory at the start of the pass, μ the memory at the start of
the loop. 

### `place_ends`

 **One pass.**  val r is what the cells of the remainder r are to hold if r has the count 1. 

### `place_arr`

 One pass, in terms of the array `arr` of the set of the numbers sg · x: if the cells hold pd + g
before, for a padding value pd, they hold the entries of the array, plus g, afterwards. 

 ## A pass, in terms of the cells number off of the groups 

### `KeptCol`

 No cell below the free pointer has changed, except cell t of the c groups from y. 

### `KeptCol.cell`

 A cell of another kind has not changed. 

### `KeptCol.keptBut`

 The cells outside the array have not changed either. 

### `place_col`

 **A pass for the first or the second set**: if cell off of each of the c groups holds pd + g
before, then afterwards cell off of group i holds entry i of the array of the set with the padding
value pd, plus g, and no other cell below the free pointer has changed. 

### `place_colZ`

 **The pass for the third set**: if cell off of each of the c groups holds -(2V + 1) + g before,
then afterwards cell off of group i holds entry i of the third array of the node, plus g, and no
other cell below the free pointer has changed. 

 ## The routine 

### `arrConsts`

 The constants: W = 2V + 1, G = 3W + 1, the number 2m² of groups, and the padding pattern. 

### `arrPass₁`

 The pass for the first set: x + G goes to cell 1 of the group of its remainder. 

### `arrPass₂`

 The pass for the second set: x + 3G goes to cell 2 of the group of its remainder.  The sign 1
and the distance 0 are as the first pass left them. 

### `arrPass₃`

 The pass for the third set: -x + 4G goes to cell 3 of the groups r and r + M, where r is the
remainder of -x. 

### `nodeArrayBody`

 nodeArray(M, s₁, l₁, s₂, l₂, s₃, l₃, V, m, y, cnt, fr), over the procedures number pResid and
pTally. 

### `ArrPre`

 What nodeArray assumes, apart from the three sets: the modulus, the count table, the place of
the array, and the limits. 

### `ArrSet`

 What nodeArray assumes about one of the three sets, given as the list L at s. 

### `ArrPre.keptBut`

 The assumptions do not depend on the cells of the array. 

### `ArrSet.keptBut`

 The assumptions about a set do not depend on the cells of the array. 

### `ArrPre.word_le`

 The numbers up to 64 (V + 1) fit in a word. 

### `ArrPre.pass`

 What a pass assumes, from what nodeArray assumes. 

### `arrConsts_ends`

 **The constants** are computed. 

### `arrPass₁_ends`

 **The pass for the first set.** 

### `arrPass₂_ends`

 **The pass for the second set.** 

### `arrPass₃_ends`

 **The pass for the third set.** 

### `oneArray_of_cells`

 The four kinds of cells make up the one-array instance of the node. 

### `nodeArrayBody_ends`

 **The whole routine**, for the arguments a and the three sets as lists. 

### `nodeArray_spec`

 **nodeArray meets its specification**, in every program that holds its body and meets the
specifications of the two routines that it calls. 
