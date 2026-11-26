---
{
  "module": "ThreeSumApsp/Lang/Lib/Emod.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/Emod.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/Emod.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The remainder of a division

emod(x, M, fr) returns the remainder of the integer x modulo M ≥ 1, a number in 0, …, M - 1.  The
language has no division: the routine writes M, 2M, 4M, … into a table at the free pointer fr as
long as they are at most |x|, subtracts them from |x| from the largest down where possible, and
corrects the sign (`emod_meets`).  With k = `emodRounds |x| M` doublings it takes `emodTime |x| M`
steps, a constant times k + 1, and k cells.


### `Arg`

 The local variables of emod: the arguments x, M and fr (the result replaces x), what is left
of |x|, the number of entries of the table, and the next multiple of M. 

### `emodTableRound`

 One entry of the table: the multiple is written to the table and doubled. 

### `emodTable`

 The table: M, 2M, 4M, … are written to the free pointer as long as they are at most |x|. 

### `emodReduceRound`

 The last entry of the table that has not been tried is subtracted if possible. 

### `emodReduce`

 The entries of the table are subtracted, from the largest down, where possible. 

### `emodSign`

 The sign: the remainder r of |x| gives the remainder of x. 

### `emodBody`

 emod(x, M, fr). 

### `emodRounds`

 The number of doublings: the least k with a < M 2^k. 

### `emodTime`

 The time of emod, for a = |x|. 

### `mul_two_pow_le_iff`

 The multiple M 2^i is at most a exactly for i below the number of doublings. 

### `emodRounds_le`

 There are at most log₂ (V + 1) + 1 doublings for a number up to V. 

### `neg_emod_nat`

 The remainder of a negative number. 

### `Pre`

 What emod asks of the limits, for a modulus M ≥ 1, numbers up to V and the free pointer fr. 

### `Table`

 The first i entries of the table are in place, and no cell below the free pointer has changed.


### `table_ends`

 **The table.**  With K doublings, the K multiples M 2^j ≤ a are written. 

### `reduce_ends`

 **The subtractions.**  What is left of a after the multiples M 2^j have been subtracted, from
the largest down, where possible, is the remainder of a. 

### `sign_ends`

 **The sign.** 

### `_root_.Light.emod_meets`

 **emod(x, M, fr)** returns the remainder of x modulo M and changes no cell below the free
pointer. 
