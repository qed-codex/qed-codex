---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary40/Gather.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/Gather.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/Gather.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Writing selected entries of a matrix

Phase 2 of Mv-hinted Mv writes X := N_{[n],I}, and Phase 3 of uMv-hinted uMv writes Y := N_{I,J}.
Both programs write their matrix row by row, and a row by the same loop, `pick`: cell c of the row
receives the content of the cell of a row of N whose number is the c-th of the given indices.
`Ends.pick` is the rule for this loop.  `RowsWritten μ a B r μ'` is the invariant of the loop over
the rows; it holds at the start (`RowsWritten.zero`), writing one more row keeps it
(`RowsWritten.succ`), and at the end the matrix is written (`RowsWritten.matAt`).


 ## One row 

### `pick`

 for c < len: dst[c] := mem[row + mem[idx + c]].  The arguments are local variables: the counter
c, the length, and the three addresses. 

### `Ends.pick`

 **The rule for a row.**  The t indices J lie at aJ, and f b is the content of the cell
aRow + J_b.  The loop writes f 0, …, f (t - 1) to the cells from aDst on.  The cells that it reads
lie below aDst. 

 ## The rows 

### `RowsWritten`

 In the memory μ' the rows below r of the matrix B are written from the address a on, and only
cells of the matrix differ from μ. 

### `RowsWritten.zero`

 No row is written yet. 

### `rowFn`

 Row r of the matrix B, as a function on all natural numbers; it is 0 outside the matrix. 

### `rowFn_eq`

 Inside the matrix, `rowFn` gives the entries. 

### `RowsWritten.succ`

 One more row is written. 

### `RowsWritten.matAt`

 All rows are written. 
