---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary40/Column.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/Column.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/Column.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 40: what the programs for v-hinted Mv and Mv-hinted Mv share

Proof of Corollary 40: "we preprocess X := M and Y := V [...]  In Phase 3, the n entries of column i
of MV are n queries".  The procedure col asks the n queries for a column and writes the signs of the
counts (`col_meets`); the data structure is an arbitrary kit.


 ## The n queries for a column 

### `Size`

 The locals of col(N, D, aX, aY, fr, j, out).  The arguments: the size N, the inner dimension D,
the addresses of X, of Y and of the data structure, the column j, the address of the output.  Then
the row, which counts from 0 to N - 1, and the count that the query returns. 

### `colBody`

 col(N, D, aX, aY, fr, j, out): for every row r, out[r] := 1 if (XY)[r, j] > 0, else 0. 

### `tCol`

 The time of col, if a query takes tq steps. 

### `col_meets`

 **col** writes, for every row r, whether the entry (XY)[r, j] is positive. 

### `ite_pos_eq_bit`

 "a Boolean entry is 1 exactly when the corresponding integer entry is positive": what col writes
is the Boolean as a number. 
