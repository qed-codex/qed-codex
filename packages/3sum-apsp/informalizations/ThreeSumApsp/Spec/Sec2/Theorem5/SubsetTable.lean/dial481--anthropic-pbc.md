---
{
  "module": "ThreeSumApsp/Spec/Sec2/Theorem5/SubsetTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/SubsetTable.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec2/Theorem5/SubsetTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The table of subsets: how a row is made from the row before it

Section 2.3.4: "We fix K₀² ≤ K distinct subsets of {1, …, L} of size m, one for each block product
of the grid, the same in every tile."  The programs keep them in a table.  Row number `s` of the
table is the mask `Spec.unrank L m s`, as `L` cells 1 and 0 (`bit`).  No program occurs here.

* The first row is `m` ones followed by zeros (`bit_unrank_zero`).
* Two consecutive masks are `pre 1 0 0^a 1^b` and `pre 0 1 1^b 0^a` (`Spec.unrank_succ_shape`).  So
  one pass from the end of the old row finds `b` and the length of `pre`: `scanAt` is the state of
  this scan after a number of rounds, and `scanAt_shape` is what it has found after all rounds.
* A second pass writes the new row: `newCell` is the cell that it writes (`bit_unrank_succ`), and
  the numbers that it computes on the way are small (`scanAt_fits`).


### `bit`

 A truth value as a cell. 

### `bit_unrank_zero`

 Row 0 of the table is `m` ones followed by `L - m` zeros. 

### `getD_shape`

 The entries of a list of the form `pre ++ x :: y :: (u^a ++ v^b)`. 

 ## The backward scan 

### `Scan`

 The state of the scan: the phase (0 while the ones at the end of the row are counted, 1 while
the zeros before them are passed, 2 when the 1 before these zeros has been found), the number of
ones at the end of the row, and the position of the 1 that was found.  The three fields are the
contents of three local variables of the routine, so they are integers, and `scanStep` and `newCell`
compare them by `<`, the comparison of the language. 

### `Scan.phase`

 The phase: 0, 1 or 2. 

### `Scan.ones`

 The number of ones at the end of the row. 

### `Scan.pos`

 The position of the last 1 that is followed by a 0. 

### `Scan.Fits`

 The result of a scan fits into a row of `L` cells: the position `p` and the number `b` of ones
are natural numbers with `p + 2 + b ≤ L`. 

### `scanStep`

 One round of the scan: `x` is the cell that is read, and `q` its position. 

### `scanAt`

 The state of the scan of a row of length `L` after `j` rounds. 

### `scanStep_ones`

 One round counts at most one more 1. 

### `scanAt_ones_le`

 After `j` rounds at most `j` ones have been counted. 

### `row_sub`

 The cell that round `j` reads: 1 for the `b` ones at the end of the row, 0 for the `a + 1` zeros
before them, and 1 for the cell before these. 

### `scanAt_count`

 Phase 0: the `b` ones at the end of the row are counted. 

### `scanAt_pass`

 Phase 1: the `a + 1` zeros before the ones are passed. 

### `scanAt_found`

 Phase 2: the 1 before the `a + 1` zeros is found, at the position after `pre`, and from then on
the state stays as it is. 

### `scanAt_shape`

 The scan of a row of the shape `pre 1 0 0^a 1^b` finds `b` and the length of `pre`. 

 ## The writing pass 

### `newCell`

 The cell number `q` of the new row, from the cell of the old row and the result of the scan. 

### `bit_unrank_succ`

 **From one row to the next.**  If row number `s` has a successor, the cells of row `s + 1` are
given by `newCell`, from the cells of row `s` and the result of its scan. 

### `scanAt_fits`

 The result of the scan of a row that has a successor fits into a row. 
