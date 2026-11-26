---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/GridContracts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/GridContracts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/GridContracts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# 3SUM from Convolution-3SUM: the loop over the splittings.  Specifications

round handles one splitting `(β, β', v)`: three selections and one call of the recursive procedure.
row runs through `β'` and `v` for a fixed `β`, and grid runs through `β`.  This file fixes their
specifications.


### `FrontArgs`

 What the routines that run through the splittings are given, besides what the routines below
the recursion tree share: the number `Λ` of binary digits, the number `nd` of the distinct values
`D`, their address `val`, the addresses `bt` of the table of digits, `A` of the cells for the three
sets and `cx` of the block of parameters. 

### `FrontArgs.vals`

 The values of the arguments of grid; row and round get them after their own. 

### `FrontMem`

 What the memory holds while the splittings are run through: the `nd` distinct values `D` at
`val`, the table of their binary digits at `bt`, the block of parameters at `cx`, the primes, the
count table, and `3n` cells from `A` for the three sets of a splitting.  Everything lies below the
free pointer, and the cells from `A` and the count table meet nothing else. 

### `SplitYes`

 Some node of the tree of the splitting `(β, β', v)` of the set `S` gives a yes-instance. 

### `FrontArgs.Yes`

 Some node of the tree of the splitting `(β, β', v)` of the distinct values gives a
yes-instance. 

### `tTree`

 The time of the recursive procedure for one three-set input, with `f` levels. 

### `tRound`

 The time of round. 

### `tRow`

 The time of row. 

### `tGrid`

 The time of grid. 

### `gridNeed`

 The need of round, row (`extra = 1`) and grid (`extra = 2`): that of the recursive procedure,
and the levels of calls above it. 

### `GridPre`

 What round (`extra = 0`), row (`extra = 1`) and grid (`extra = 2`) assume besides the memory. 

### `RoundSpec`

 round(β, β', b, nd, val, bt, Λ, A, n, f, cx, fr), with `b` = 1 for `v = true` and 0 for
`v = false`, returns 1 if the splitting gives a yes-instance, and 0 if not.  The three sets are
written to `A`, `A + n`, `A + 2n`. 

### `RowSpec`

 row(β, nd, val, bt, Λ, A, n, f, cx, fr) returns a number between 0 and `2Λ` that is positive
exactly if some splitting `(β, β', v)` gives a yes-instance. 

### `GridSpec`

 grid(nd, val, bt, Λ, A, n, f, cx, fr) returns 1 if some splitting gives a yes-instance, and 0 if
not. 
