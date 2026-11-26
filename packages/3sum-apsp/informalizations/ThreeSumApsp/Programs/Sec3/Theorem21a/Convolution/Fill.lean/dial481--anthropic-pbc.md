---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/Convolution/Fill.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/Convolution/Fill.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/Convolution/Fill.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Convolution-3SUM from Exact Triangle: writing one instance

Theorem 21(a), after [VW13, Theorem 4.3].  convFill(t, N, s, F, x, ab, bc,
ac) writes the three weight matrices of instance number s of the reduction, each of t² cells, row
by row, to ab, bc, ac: w(a,b) = x[a t + b], w(b,c) = x[c t + s - b], w(a,c) = -x[(a + c) t + s], and
the filler F where the index is out of range.  One loop runs through the t² cells; it keeps the
number of the cell, its row and its column in three counters.

The proof follows the text.  pickStmt reads a cell of x or the filler (`pick_runs`); putStmt
computes an index, picks, and stores (`put_runs`); fillCells does this for the three matrices
(`cells_runs`); then the counters move on.  After q rounds the memory is `A.filled μ q`: the first q
cells of each matrix have been written (`filled_succ` is one round).  The result is
`convFill_meets`.


 ## The program 

### `Side`

 The local variables of convFill: the arguments t (Side), N (Len), s (Inst), F (Filler), x
(Input), ab, bc, ac (MatAB, MatBC, MatAC); the row, the column and the number of the current cell
(Row, Col, Cell); an index into x and what is picked there (Index, Value); -F (NegFiller) and t²
(Area). 

### `pickStmt`

 Value := x[Index] if 0 ≤ Index < N, and the content of local f, a filler, if not. 

### `putStmt`

 Computes the index ze, picks the cell there (or the filler in local f), and stores it, or minus
it if neg is set, into the current cell of the matrix whose address is in local dst. 

### `fillCells`

 The current cell of each of the three matrices. 

### `fillRound`

 One round: the current cell of each matrix, and on to the next cell. 

### `convFillBody`

 convFill(t, N, s, F, x, ab, bc, ac). 

### `convFillTime`

 The time of convFill. 

 ## Picking and storing

The two lemmas of this section have the form of the rules for blocks: if R holds of the state in
which the part ends, then the part runs, within the limits, into R. 

### `InputAt`

 The list X of N numbers stands at x, within the memory, and addresses fit in a word. 

### `pick_runs`

 pickStmt puts `cellOr N F X z` into Value and changes nothing else. 

### `put_runs`

 putStmt stores `cellOr N F X z`, or minus it, into cell q of the matrix at D.  Of the locals it
changes only Index and Value. 

 ## The data and the memory 

### `Args`

 The arguments of convFill, with the list X that stands at x. 

### `Ctx`

 What convFill assumes: there is at least one row; the input lies below the three matrices, which
follow each other within the memory; V bounds the input and the filler; words hold addresses, V and
the indices. 

### `Post`

 What convFill achieves: the three matrices stand in the memory, and no cell before the first or
after the last of them has changed. 

### `Args.idxBC`

 The index into x for cell q of the second matrix: c t + s - b for row b and column c. 

### `Args.idxAC`

 The index into x for cell q of the third matrix: (a + c) t + s for row a and column c. 

### `Args.filled`

 The memory after q rounds: the first q cells of each matrix have been written. 

### `Args.locals`

 The local variables before round q; z and w are what the last round has left in Index and
Value. 

### `filled_succ`

 One round writes cell q of each matrix. 

### `sameOutside_filled`

 No cell before the first matrix or after the last one changes. 

### `post_filled`

 At the end the three matrices stand in the memory. 

### `inputAt_filled`

 The input is still there after q rounds. 

### `InputAt.write`

 A write to a cell of the matrices leaves the input alone. 

### `abs_cellOr_le_word`

 What is picked fits in a word. 

 ## The loop 

### `IndexBounds`

 The row and the column of a cell q < t² are below t, so the products that the two index
expressions form lie between 0 and 2t². 

### `cells_runs`

 fillCells writes cell q of each matrix. 

### `LoopInv`

 The invariant of the loop: before round q the counters stand at cell q, and the first q cells of
each matrix have been written. 

### `round_spec`

 Round q: cell q of each matrix is written, and the counters move on to cell q + 1. 

### `convFill_meets`

 **convFill** writes the three matrices of instance number s, changes no cell before the first or
after the last of them, and takes O(t²) steps. 
