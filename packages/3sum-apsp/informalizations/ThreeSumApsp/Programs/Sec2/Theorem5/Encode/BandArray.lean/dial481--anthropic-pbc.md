---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Encode/BandArray.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Encode/BandArray.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Encode/BandArray.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The input array of a band (Section 2.3.4)

Section 2.3.3: "a[u] := X_Q[u], b[v] := Y_Q[v] for all the left strings u and the right strings v
whose inner set Q has exactly m elements, and a[u] := 0, b[v] := 0 at every other string"; in
Section 2.3.4, X_Q and Y_Q are the row block and the column block of the block product with subset
Q.  bandArray writes this input array for a row band of X or a column band of Y.  The array is
laid out by the codes of the left (right) strings and filled in the order of the tuples: the
procedure clears the array, and then, for every block product (g, h) of a tile, every row r of the
block and every column k, it computes the code of the string digit by digit and copies one entry of
the matrix.

The proof goes from the inside to the outside, one lemma for the body of each loop and one for the
loop: a level of the code (`bandLevel_spec`, `bandCodeLoop_spec`), an entry (`bandCell_spec`,
`bandColLoop_spec`), a row of a block (`bandRow_spec`, `bandRowLoop_spec`), a block product
(`bandRows_spec`, `bandBlock_spec`, `bandHLoop_spec`, `bandGLoop_spec`), and the whole procedure
(`bandArray_spec`, within the time `bandArray_time`).  The four outer loops keep the same fact about
the memory: cells of the array are overwritten only with entries of the target list
(`OverwrittenWith`), and the cells of the tuples handled so far are right (`Covered`).  So they are
four cases of one lemma, `coverLoop`.  `bandArrayL_entry` and `bandArrayR_entry`, the cases of X and
of Y, are the specifications that the callers of the procedure assume.


 ## The program 

### `Levels`

 The local variables of bandArray.  The arguments: `Levels` = L, `Size` = m, `Rows` = N, `Cols` =
D, `NumBlocks` = K0, `Width` = N0, `Cells` = S7, `BandNo` = β, `Side` = side; `Source` is the
address of the matrix, `StepRow` and `StepCol` the steps from row to row and from column to column;
`MaskTable`, `Digits3`, `Digits4` and `Dest` are the addresses of the table of subsets, of the two
tables of digits and of the array.  Then, by the depth of the loop that uses them: `PosG` = g (also
the counter of the clearing loop); `PosH` = h, `BlockIdx` the number of the block, `MaskRow` the
address of the mask of the subset; `Offset` = r, `Row` the number of the row of the matrix; `Col` =
k, `CodeAcc` the code, `Outer` and `Inner` the addresses of the next outer and of the next inner
digit, `CurLevel` the level. 

### `bandLevel`

 One level: Horner's rule in base 7, with the next outer digit, or 3 plus the next inner
digit. 

### `bandCodeLoop`

 The loop over the levels. 

### `bandCell`

 One entry: the code of the string, and the entry copied. 

### `bandColLoop`

 The loop over the columns k. 

### `bandRow`

 One row r of a block; rows beyond the matrix are skipped. 

### `bandRowLoop`

 The loop over the rows r of a block. 

### `bandRows`

 The address of the mask of the subset of the block product (g, h), and the rows of the block. 

### `bandBlock`

 One block product (g, h): the number of the block, which depends on the side, and the rest. 

### `bandHLoop`

 The loop over h. 

### `bandGLoop`

 The loop over g. 

### `bandZeroLoop`

 The clearing loop. 

### `bandArrayBody`

 bandArray(L, m, N, D, K0, N0, S7, β, side, aA, sI, sK, mask, dig3, dig4, arr). 

### `cBandArray`

 The constant of the running time. 

 ## The local variables as a list 

### `BlockTmp`

 The local variables of the loop over h. 

### `BlockTmp.h`

 h. 

### `BlockTmp.blk`

 The number of the block. 

### `BlockTmp.mrow`

 The address of the mask of the subset. 

### `RowTmp`

 The local variables of the loop over the rows of a block. 

### `RowTmp.r`

 r. 

### `RowTmp.row`

 The number of the row of the matrix. 

### `CellTmp`

 The local variables of the loop over the columns. 

### `CellTmp.k`

 k. 

### `CellTmp.code`

 The code. 

### `CellTmp.outer`

 The address of the next outer digit. 

### `CellTmp.inner`

 The address of the next inner digit. 

### `CellTmp.lev`

 The level. 

### `InnerTmp`

 The local variables of the three inner loops together. 

### `InnerTmp.block`

 Those of the loop over `h`. 

### `InnerTmp.row`

 Those of the loop over the rows of a block. 

### `InnerTmp.cell`

 Those of the loop over the columns. 

### `Band.locals`

 The list of the local variables. 

### `Band.blockTmp`

 The local variables of the loop over `h` for the block product `(g, h)`. 

### `Band.rowTmp`

 The local variables of the loop over the rows for the row `r` of the block product `(g, h)`. 

 ## The loop over the levels 

### `CodeCtx`

 What the loop over the levels reads: the mask bs at mrow, the outer digits o at d3 and the inner
digits i at d4. 

### `Band.codeTmp`

 The local variables of the loop over the columns after l levels. 

### `bandLevel_spec`

 **One level** leads from the state after `l` levels to the state after `l + 1` levels.  No cell
changes. 

### `bandCodeLoop_spec`

 **The loop over the levels** leaves the code of the string in the local `CodeAcc` and changes no
cell. 

 ## The surroundings 

### `BandCtx`

 Everything that the loops assume: the limits, the places of the tables and of the matrix in the
memory μ₀ at the start, and what is known about the list T that has to be produced. 

### `Covered`

 The cell of the tuple (g, h, r, k) is right. 

### `Covered.keep`

 A cell that is right stays right. 

### `places`

 Inequalities between the numbers: where the tables, the matrix and the array lie, and bounds on
the sizes. 

### `codeCtx`

 What the loop over the levels reads for the tuple (g, h, r, k), in a memory in which only cells
of the array have changed. 

 ## A loop that fills cells 

### `coverLoop`

 **The four loops at once.**  shape z x is the list of the local variables, with z in the counter
and the local variables x of the loops inside.  If round j overwrites cells only with entries of the
target and establishes fact j, which such writes keep, then the loop establishes fact j for all
j < rounds. 

 ## The loop over the columns 

### `tBandCell`

 The time of one entry. 

### `bandCell_spec`

 **One entry**: the code of the string is computed, and the entry of the matrix is copied to its
cell. 

### `tBandCol`

 The time of the loop over the columns. 

### `bandColLoop_spec`

 **The loop over the columns** fills the cells of the tuples (g, h, r, k), k < D. 

 ## The loop over the rows of a block 

### `CoveredRow`

 The cells of the row r of the block product (g, h) are right, if the row lies in the matrix. 

### `tBandRow`

 The time of one row of a block. 

### `tBandRows`

 The time of the loop over the rows of a block. 

### `bandRow_spec`

 **One row of a block**: if the row lies in the matrix, the cells of the tuples `(g, h, r, k)`,
`k < D`, are filled. 

### `bandRowLoop_spec`

 **The loop over the rows of a block** fills the cells of the tuples `(g, h, r, k)`, `r < N₀`,
whose row lies in the matrix. 

 ## The loops over h and g 

### `tBandBlock`

 The time of one block product. 

### `tBandH`

 The time of the loop over h. 

### `tBandG`

 The time of the loop over g. 

### `bandRows_spec`

 **The rows of the block product (g, h)**, once the number of the block is known. 

### `bandBlock_spec`

 **One block product**: the number of the block is formed, and the cells of the tuples
`(g, h, r, k)` whose row lies in the matrix are filled. 

### `bandHLoop_spec`

 **The loop over `h`** fills the cells of the tuples `(g, h, r, k)`, `h < K₀`, whose row lies in
the matrix. 

### `bandGLoop_spec`

 **The loop over `g`** fills the cells of all tuples `(g, h, r, k)` whose row lies in the
matrix. 

 ## The whole procedure 

### `bandArray_time`

 The time of the whole procedure is within the bound that its callers assume. 

### `Band.args`

 The arguments of bandArray as a list. 

### `bandArray_spec`

 **bandArray** writes the list T to the array and changes nothing else. 

 ## What the callers assume 

### `BandArgs.ofX`

 The arguments of `bandArray` for the row band `β` of `X`, which stands at `aX` row by row. 

### `BandArgs.ofY`

 The arguments of `bandArray` for the column band `β` of `Y`, which stands at `aY` row by row. 

### `bandArrayL_entry`

 **The specification that the callers of bandArray assume, for a row band of X.** 

### `bandArrayR_entry`

 **The specification that the callers of bandArray assume, for a column band of Y.** 
