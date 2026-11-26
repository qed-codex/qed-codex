---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Tables/Subsets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Tables/Subsets.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Tables/Subsets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The table of subsets

Section 2.3.4: "We fix K₀² ≤ K distinct subsets of {1, …, L} of size m, one for each block product
of the grid, the same in every tile."  Section 2.4.4 counts the time to "list the K₀² subsets".
subsets(L, m, KK, mask), which is called with KK = K₀², writes the first KK masks of the enumeration
`Spec.unrank`, one after the other, as 0/1 cells from mask.  Row 0 is m ones followed by zeros
(`firstRow_spec`).  Each further row is made from the row before it: one pass from the end of the
old row finds the last 1 that is followed by a 0 (`scan_spec`), and one pass writes the new row
(`write_spec`).  There is no arithmetic on the entries, and a row takes O(L) steps.  What the two
passes compute is described without a program by `scanAt` and `newCell`, with the facts
`bit_unrank_succ` and `scanAt_fits`; here each pass is connected with this description,
`tableRow_spec` treats one row, and `subsetTable_spec` runs through the rows.  `subsets_entry` is
the specification that the callers of the procedure assume.


 ## The program 

### `Levels`

 The local variables of subsets: Levels = L, Size = m, Rows = KK, Table = mask (the arguments);
Row is the number of the current row and Addr its address; Phase, Ones and Pos are the state of the
scan (phase, number of ones at the end, position found); Cell is the counter of the inner loops. 

### `firstRowRound`

 One cell of the first row: 1 for the first m cells, then 0. 

### `firstRowLoop`

 The first row: m ones, then zeros. 

### `scanRound`

 One round of the scan: the cell number Cell from the end of the row before the current one. 

### `scanLoop`

 The scan of the row before the current one, from its end. 

### `writeRound`

 One cell of the new row, from the row before it and the result of the scan. 

### `writeLoop`

 The new row, from the row before it and the result of the scan. 

### `nextRow`

 A further row, from the row before it. 

### `tableRow`

 One round of the loop over the rows. 

### `subsetTableBody`

 subsets(L, m, KK, mask). 

 ## The three passes 

### `locals`

 The list of the local variables. 

### `prevRow`

 The row of L cells that ends just before the address a. 

### `newRow`

 The row that the writing pass forms from the row before the address a and the result S of its
scan. 

### `firstRow_spec`

 **The first row**: the pass writes m ones and then zeros to the L cells from a. 

### `scanRound_runs`

 One round of the scan does to the local variables what `scanStep` says of the cell number j from
the end of the row of L cells that ends just before the address a. 

### `scan_spec`

 **The scan** of the row of L cells that ends just before the address a changes no cell and
leaves its result in the local variables. 

### `write_spec`

 **The writing pass** writes the new row to the L cells from a, from the row of L cells before
it and the result S of the scan. 

### `nextRow_spec`

 **A further row**: the two passes write the new row to the L cells from a, from the row of L
cells before it, if the result of the scan leaves room. 

 ## The loop over the rows 

### `RowsDone`

 The state before row number s is written: the rows before it stand in the table, and no cell
outside the table has changed. 

### `tRow`

 The time of one round of the loop over the rows. 

### `rowDone_spec`

 The end of a round: row number s has been written, and the number and the address of the row
move on. 

### `tableRow_spec`

 **One round of the loop over the rows** writes row number `s`, the mask number `s`. 

### `subsetTable_spec`

 **subsets** writes the table and changes nothing else. 

### `subsets_entry`

 **The specification that the callers of subsets assume.** 
