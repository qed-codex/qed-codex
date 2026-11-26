---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary39/GraphH/Fill.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/GraphH/Fill.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/GraphH/Fill.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 39 in the light language: filling a weight matrix of H

Corollary 39: a clique on k vertices of a k-partite graph G is a triangle of a graph H.
The vertices of the first t = k - 3⌊k/3⌋ parts are fixed, and the other parts form three groups.
With gw = ⌊k/3⌋, a vertex of H is a choice of one vertex in each of the gw parts of a group, so a
part of H has N = n^gw vertices; the chosen vertices are the digits of its number in base n, lowest
first.
The weight between a vertex of H in group i and one in group i + 1 is the sum of the weights of G
over a list L of pairs of parts: the pairs between the two groups, the pairs inside group i, the
pairs of a fixed part and a part of group i, and, for one of the three matrices, the pairs of fixed
parts.  This file writes one N × N weight matrix of H, for any list L.

The weights of G stand at g: the weight between vertex u of part p and vertex v of part q in cell
g + ((p k + q) n + u) n + v.  The current choice of one vertex in each part stands in the k cells at
vt.  The weights lie below these cells and below the matrix.  `sumPairs` adds up the weights over L.
`fillMat` runs through all pairs (row, column) of vertices of H by two odometers inside vt and
writes the sums, row by row.

The proof goes from the inside to the outside: the address of a weight (`wAddr_gives`), the sum
(`sumPairs_spec`), one step of an odometer (`inc_spec`, and `incCol_spec` for the column odometer),
and then one invariant, `FillInv`, "before column c of row r all earlier entries are written", which
an entry (`fillEntry_spec`), a row (`fillRow_spec`) and the step to the next row (`nextRow_spec`)
take to its next value; `fillMat_spec` puts them together.


 ## The local variables

The local variables 0 to 16 of the hosts for k-Clique, except local 3, which each host uses in its
own way.  `fillMat` and its parts read `Size`, `Weights`, `Side` and `Choice` and assign `Row`,
`Col`, `Place` and `Entry`. 

### `Size`

 n, the number of vertices of a part. 

### `Bound`

 U, the bound on the weights. 

### `Weights`

 g, the address of the weights. 

### `Side`

 N = n^⌊k/3⌋, the side of a matrix of H. 

### `Rounds`

 n^t, the number of choices of the fixed vertices. 

### `Choice`

 The address of the k cells of the chosen vertices. 

### `MatAB`

 The address of the matrix of H between the groups 0 and 1. 

### `MatBC`

 The address of the matrix of H between the groups 1 and 2. 

### `MatAC`

 The address of the matrix of H between the groups 0 and 2. 

### `Behind`

 The address of the first cell behind the three matrices. 

### `Round`

 The number of the current choice of the fixed vertices. 

### `Row`

 The row of the entry that `fillMat` writes next. 

### `Col`

 The column of the entry that `fillMat` writes next. 

### `Place`

 The address of the entry that `fillMat` writes next. 

### `Entry`

 The sum for the entry that `fillMat` writes next. 

### `Answer`

 The result of the call of the solver. 

### `FillLocals`

 Four local variables that fillMat and its parts only read.  (fillMat also reads the local that
holds the address of the matrix.) 

### `FillLocals.update`

 `FillLocals` survives an assignment to `Row`, `Col`, `Place` or `Entry`. 

 ## The sum of the weights over a list of pairs of parts 

### `widx`

 The place of the weight between vertex u of part p and vertex v of part q. 

### `wAddr`

 The address of the weight between the chosen vertices of the parts p and q. 

### `sumPairs`

 Add to Entry the weights between the chosen vertices, over a list of pairs of parts. 

### `ChoiceIs`

 The cells at vt hold the choice vf: vertex vf p of part p. 

### `memSum`

 The total weight between the chosen vertices vf, over the pairs of parts in L. 

### `FillCtx`

 Where things lie, and how large the weights are: the weights and the chosen vertices lie within
the memory, and the weights between parts p < q have absolute value at most U. 

### `FillCtx.of_kept`

 The context only looks at the cells up to the end of the weights. 

### `memSum_congr`

 The sum only looks at the cells up to the end of the weights. 

### `wAddr_gives`

 The address is safe, and its value is g plus the place of the weight. 

### `sumPairs_spec`

 **sumPairs** adds the weights over the list to Entry and changes nothing else; 21 steps for each
pair.  B bounds what Entry holds before. 

 ## The odometers 

### `withDigits`

 The choice vf, with the vertices of the gw parts from off on replaced by the digits of c in base
n, lowest first: what an odometer on these cells shows after c steps. 

### `choiceAt`

 The choice of vertices when the row odometer (gw cells from ro) shows r and the column odometer
(gw cells from co) shows c. 

### `choiceAt_eq_col`

 The column odometer on top of the row odometer: the two do not meet. 

### `withDigits_lt`

 The digits are vertices of their parts. 

### `choiceAt_lt`

 The chosen vertices are vertices of their parts. 

### `withDigits_pow`

 After n^gw steps an odometer shows 0 again. 

### `seg_digits_iff`

 The cells hold the digits of c as a list exactly if each holds its digit. 

### `OdometerOk`

 What a step of an odometer needs of the limits: an address fits in a word, n fits in a word, and
the kk cells of the chosen vertices lie within the memory. 

### `inc_spec`

 **One step of an odometer** on the gw cells from vt + off: it shows c + 1 instead of c, and
nothing else changes. 

### `incCol_spec`

 One step of the column odometer. 

 ## An entry, a row, and the whole matrix 

### `fillEntry`

 One entry: the sum over the list of pairs is written to the next place, and the column odometer
moves on. 

### `fillRow`

 One row: an entry for every column. 

### `fillMat`

 The N × N matrix, row by row, from the address in local dl on. 

### `incStmt_assigns`

 `incStmt` assigns no local variable. 

### `sumPairs_assigns`

 `sumPairs` assigns only `Entry`. 

### `fillMat_assigns`

 `fillMat` assigns only `Row`, `Col`, `Place` and `Entry`. 

### `entryTime`

 A bound on the number of steps of fillEntry, for a list of len pairs. 

### `rowTime`

 A bound on the number of steps of fillRow. 

### `matTime`

 A bound on the number of steps of fillMat. 

### `FillJob`

 What fillMat is asked to do: the graph has kk parts of n vertices, its weights stand at g and
have absolute value at most U; the chosen vertices stand at vt; the rows are counted by the gw
cells from vt + ro and the columns by the gw cells from vt + co; the other cells hold the choice
vf0; the matrix has side N = n^gw and goes to dst; an entry is the sum over the pairs of parts
in L. 

### `FillJob.choice`

 The chosen vertices for the entry in row r and column c. 

### `FillJob.entry`

 The entry in row r and column c, with the weights read from μ. 

### `MatCtx`

 What fillMat assumes of the memory μ at the start and of the limits: the two odometers lie among
the kk cells and do not meet; the sums fit in a word; the weights lie below the chosen vertices
and below the matrix, and these two do not meet. 

### `FillInv`

 **The invariant**, before column c of row r.  μ is the memory at the start.  The four locals
that are only read hold what they should; Place is the place of the next entry; the odometers show r
and c; the entries before this one, row by row, have been written; and outside the matrix and the
chosen vertices the memory is as at the start.  The column c runs up to N inclusive: (r, N) is the
same point as (r + 1, 0), but for the row odometer. 

### `Filled`

 **What fillMat achieves**: the matrix is written, both odometers show 0 again, and no other cell
has changed. 

### `MatCtx.side_le`

 The side of the matrix fits in a word. 

### `MatCtx.choice_last_col`

 After the last column the column odometer shows 0 again. 

### `MatCtx.choice_last_row`

 After the last row the row odometer shows 0 again. 

### `FillInv.kept`

 All cells up to the end of the weights are as at the start. 

### `FillInv.update`

 The invariant does not speak of the counters Row and Col and of Entry. 

### `FillInv.next_col`

 Storing the entry in row r and column c, and then changing only cells of the column odometer,
takes the invariant to the next column. 

### `fillEntry_spec`

 **fillEntry** writes the entry in row r and column c. 

### `fillRow_spec`

 **fillRow** writes row r. 

### `nextRow_spec`

 After the last column of row r comes the first column of row r + 1: the column odometer shows 0
again, and **the row odometer moves on**. 

### `fillMat_spec`

 **fillMat** writes the matrix.  Both odometers show 0 before and afterwards. 
