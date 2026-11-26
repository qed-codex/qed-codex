---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Instances/WriteMatrices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Instances/WriteMatrices.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Instances/WriteMatrices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The two matrices of an instance (proof of Theorem 17)

"a ∼ (c, σ) ⟺ σ ≡ w(a,c) + ϱ, (c, σ) ∼ b ⟺ σ ≡ -w(b,c) (mod p)."

writeY(y, rbc, n, D, p, c0, len) writes the D × n matrix Y of the instances for the piece
{c0, …, c0 + len - 1} of C: the middle vertex (c, σ) is the row (c - c0) p + σ.  The n² cells from
rbc hold the residues of the weights w(b,c) mod p, that of (b, c) at place b n + c.
writeX(x, rac, n, D, p, c0, len, rho) writes the n × D matrix X for the residue rho; the cells from
rac hold the residues of the weights w(a,c), that of (a, c) at place a n + c.  In the statements and
docstrings below, c counts from 0 within the piece: the c-th member of the piece is the vertex
c0 + c.

Both clear the matrix and then run through the pairs of a vertex and a member of the piece; each
pair marks one cell with a 1.  So both are instances of one pair of loops:

* `markVal` says what a cell holds when the pairs before (u, w) have been handled, and `Marked` says
  it of the memory;
* `markPairs` runs the two loops, given what the body does for one pair (`MarkCtx`);
* `writeYCell_spec` and `writeXCell_spec` treat the bodies: read a residue, form the label, mark the
  cell;
* `getElem_yList` and `getElem_xList` identify the marks of all pairs with the matrices.


 ## Marking cells: the pure side 

### `CellMarked`

 The cell i has been marked when the pairs (u', w'), w' < W, before (u, w) in lexicographic order
have been handled; the pair (u', w') marks the cell pos u' w'. 

### `markVal`

 The content of the cell i when the pairs before (u, w) have been handled: 1 if it has been
marked, else 0. 

### `markVal_end`

 At the end, a cell is marked iff it is the cell of one of the pairs. 

 ## Marking cells: the memory 

### `Marked`

 The m cells from base hold the marks of the pairs before (u, w), and no other cell has
changed. 

### `start`

 After the clearing no pair has been handled. 

### `step`

 The pair (u, w) marks its cell. 

### `row`

 The end of a row of pairs is the beginning of the next row. 

### `seg`

 When all pairs have been handled, the cells hold the list of all marks. 

 ## Marking cells: the two loops 

### `MarkCtx`

 What the two loops `for u < U: for w < W: cell` need.  L u w t is the list of the locals: u and
w are the counters, in the locals cu and cw, and t is a temporary of the body.  The body takes at
most b steps and marks the cell of the pair (u, w). 

### `markRow`

 The inner loop: the pairs (u, 0), …, (u, W - 1) mark their cells. 

### `markPairs`

 **The two loops**: all pairs mark their cells. 

 ## Clearing the matrix 

### `clear_spec`

 The loop that clears a matrix: local 0 holds its address base, local t the number m of its
cells, and local c is the counter.  Afterwards the m cells hold 0, and no other cell has changed. 

 ## What both routines assume 

### `WritePre`

 The residues R of the n² weights, all below p, stand at res.  The matrix has m = D n cells at
base, apart from the residues.  The piece {c0, …, c0 + len - 1} lies within the n vertices, and its
len p labels within the D middle vertices. 

### `n_le_word`

 The number n of vertices fits in a word. 

### `len_le_word`

 The length of the piece fits in a word. 

### `index_lt`

 The place of the weight between the vertex u and the c-th member c0 + c of the piece. 

### `read`

 The residues can be read at any time. 

### `getD_lt`

 The residues are below p. 

### `middle_lt`

 The label s of the c-th member of the piece is one of the D middle vertices. 

 ## The matrix Y 

### `Y`

 The local variables of writeY: the arguments y, rbc, n, D, p, c0, len; the number c of the
member of the piece (before that, the counter of the clearing); the vertex b; the residue, then the
label, r; the number D n of cells. 

### `writeYCell`

 The pair (c, b) marks its cell: r := rbc[b n + c0 + c]; if r ≠ 0 then r := p - r;
y[(c p + r) n + b] := 1. 

### `writeYBody`

 writeY(y, rbc, n, D, p, c0, len). 

### `tWriteY`

 The time of writeY. 

### `labY`

 The label of the row that the pair (c, b) marks. 

### `posY`

 The cell that the pair (c, b) marks. 

### `getElem_yList`

 Entry i of yList, the matrix Y row by row, is 1 if one of the pairs (c, b) marks the cell i, and
0 if not. 

### `posY_lt`

 The cell of a pair lies in the matrix. 

### `labY_eq`

 The label, as the program computes it. 

### `writeYCell_spec`

 **One pair of writeY.** 

### `writeY_markCtx`

 The two loops of writeY are loops that mark cells. 

### `writeY_spec`

 **writeY** writes the matrix Y and changes nothing else. 

 ## The matrix X 

### `X`

 The local variables of writeX: the arguments x, rac, n, D, p, c0, len, rho; the vertex a (before
that, the counter of the clearing); the number c of the member of the piece; the label t; the number
n D of cells. 

### `writeXCell`

 The pair (a, c) marks its cell: t := rac[a n + c0 + c] + rho; if p ≤ t then t := t - p;
x[a D + c p + t] := 1. 

### `writeXBody`

 writeX(x, rac, n, D, p, c0, len, rho). 

### `tWriteX`

 The time of writeX. 

### `labX`

 The label of the column that the pair (a, c) marks. 

### `posX`

 The cell that the pair (a, c) marks. 

### `getElem_xList`

 Entry i of xList, the matrix X row by row, is 1 if one of the pairs (a, c) marks the cell i, and
0 if not. 

### `posX_lt`

 The cell of a pair lies in the matrix. 

### `labX_eq`

 The label, as the program computes it. 

### `writeXCell_spec`

 **One pair of writeX.** 

### `writeX_markCtx`

 The two loops of writeX are loops that mark cells. 

### `writeX_spec`

 **writeX** writes the matrix X and changes nothing else. 
