---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/SearchRoutines.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/SearchRoutines.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/SearchRoutines.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Max-Weight Triangle from Exact Triangle: two routines

pw(x, dst) writes the powers of two up to x to dst and returns their number (`pw_meets`).
mask(n, src, r₀, c₀, Big, dst) copies a matrix and adds Big to the entries in the rows below r₀ and
in the columns below c₀ (`mask_meets`).


 ## The powers of two up to x 

### `lv`

 The number of powers of two up to x, for x ≥ 1. 

### `lt_two_pow_lv`

 The first power of two that is not written is larger than x. 

### `two_pow_lv_le`

 The first power of two that is not written is at most 2x. 

### `Bound`

 The locals of pw(x, dst): the bound x (this local also takes the result), the address of the
table, the power, and its exponent. 

### `pwBody`

 pw(x, dst): p := 1; j := 0; while p ≤ x: dst[j] := p; p := 2p; j := j + 1. 

### `pw_meets`

 **pw** writes the powers of two up to x, returns their number, and changes nothing else. 

 ## Switching off rows and columns 

### `Size`

 The locals of mask(n, src, r₀, c₀, Big, dst).  The arguments; then the place, its row and its
column, n², and what is added at this place. 

### `maskAdd`

 What is added: Big in the rows below r₀ and in the columns below c₀, and 0 elsewhere. 

### `maskWrite`

 The entry is written; then the row and the column of the next place. 

### `maskBody`

 mask(n, src, r₀, c₀, Big, dst): for all places q < n². 

### `maskAt`

 What is added at the place q. 

### `maskAdd_spec`

 **What is added** at the place q. 

### `maskWrite_spec`

 **The entry is written**, and the row and the column are those of the next place. 

### `mask_meets`

 **mask** writes the matrix with the rows below r₀ and the columns below c₀ switched off, and
changes nothing else. 
