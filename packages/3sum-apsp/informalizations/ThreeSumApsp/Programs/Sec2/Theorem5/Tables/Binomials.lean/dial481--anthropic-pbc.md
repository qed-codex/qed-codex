---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Tables/Binomials.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Tables/Binomials.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Tables/Binomials.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# A binomial coefficient, by Pascal's triangle

Section 2.3.4 needs the number K = (L choose m) of subsets of size m.  binom(L, m, pas) returns this
binomial coefficient.  The cells pas, …, pas + L hold a row of Pascal's triangle.  Row 0 is 1
followed by zeros (`binomFirst_spec`), and the next row is formed in place, from right to left, so
that the two entries that are added are still those of the old row.  `binomPlace_spec` treats one
entry, by Pascal's rule, `binomInner_spec` one row, and `binom_spec` runs through the rows;
`binom_entry` is the specification that the callers of the procedure assume.


### `Levels`

 The local variables of binom: Levels = L, Size = m, Addr = pas (the arguments); Row is the
number of the row, and Place the place in it. 

### `binomPlace`

 One entry of the next row: the entry above it plus the entry to the left of that. 

### `binomInner`

 The loop that turns row i of the triangle into row i + 1, from right to left. 

### `binomRow`

 One round of the loop over the rows. 

### `binomFirst`

 Row 0 of the triangle: 1 followed by L zeros. 

### `binomBody`

 binom(L, m, pas).  The number of the row is not set at the beginning: local variables that are
not arguments start at 0.  The result of a procedure is what it leaves in local variable 0. 

 ## One row from the row before it 

### `Mixed`

 The memory while row i is turned into row i + 1: the entries to the right of place p are those
of row i + 1, the others still those of row i; no cell outside the L + 2 cells that the procedure
may use has changed. 

### `Mixed.step`

 One more entry has been replaced. 

### `Inv`

 The state after r entries have been replaced: the place is L - r. 

### `binomPlace_spec`

 **One entry**, by Pascal's rule. 

### `binomInner_spec`

 **One row**: the loop over the places turns row i of the triangle into row i + 1. 

 ## The loop over the rows 

### `RowAt`

 The state before round i: the cells hold row i of the triangle. 

### `tRow`

 The time of one round of the loop over the rows. 

### `binomRow_spec`

 **One round of the loop over the rows** turns row `i` of the triangle into row `i + 1`. 

### `binomFirst_spec`

 **Row 0** of the triangle is written: 1 followed by `L` zeros. 

### `binom_spec`

 **binom** returns (L choose m) and changes no cell outside the L + 2 cells from pas. 

### `binom_entry`

 **The specification that the callers of binom assume.** 
