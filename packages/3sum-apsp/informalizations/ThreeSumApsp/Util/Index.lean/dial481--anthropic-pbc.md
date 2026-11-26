---
{
  "module": "ThreeSumApsp/Util/Index.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Index.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Index.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Index arithmetic: a pair of numbers as one number

General facts about natural numbers. A matrix with rows of length `n` is kept as one list, row
after row: the entry in row `a` and column `b < n` has the index `a * n + b`. This file has

* the bounds on such an index (`Nat.mul_add_lt_mul`, `Nat.mul_add_le_mul`);
* the way back from the index to the pair (`Nat.mul_add_div_of_lt`, `Nat.mul_add_inj_of_lt`,
  `Nat.div_lt_of_lt_mul'`, `Nat.mod_lt_of_lt_mul`, `Nat.exists_eq_mul_add_of_lt_mul`,
  `Nat.eq_mul_succ_iff`);
* the pair of the next index (`Nat.succ_div_mod_of_lt`, `Nat.succ_div_mod_of_ne`,
  `Nat.succ_div_mod_of_eq`);
* residues seen as natural numbers (`Int.toNat_emod_lt`, `Int.natCast_toNat_emod`).


 ## Bounds on an index 

### `mul_add_lt_mul`

 The index of an entry of a matrix with `m` rows and `n` columns is below `m * n`. 

### `mul_add_le_mul`

 Row `a < m` ends within the matrix: `a * n + b ≤ m * n` for `b ≤ n`, so also for `b = n`. 

 ## From the index back to the pair

The column is `Nat.mul_add_mod_of_lt : c < b → (a * b + c) % b = c`. 

### `mul_add_div_of_lt`

 The row of the index `a * n + b`. 

### `mul_add_inj_of_lt`

 The index determines the pair. 

### `div_lt_of_lt_mul'`

 The row of an index below `m * n` is below `m`. 

### `mod_lt_of_lt_mul`

 The column of an index below `m * n` is below `n`. 

### `exists_eq_mul_add_of_lt_mul`

 Every index below `m * n` is the index of a pair. 

### `eq_mul_succ_iff`

 The indices of the diagonal are the multiples of `n + 1`. 

 ## The next index 

### `succ_div_mod_of_lt`

 The next index, if it is in the same row. 

### `succ_div_mod_of_ne`

 The next index, if the test "is this the end of the row?" fails. 

### `succ_div_mod_of_eq`

 After the last index of a row comes the first index of the next row. 

 ## Residues as natural numbers 

### `toNat_emod_lt`

 The residue of an integer modulo `M ≥ 1`, as a natural number, is below `M`. 

### `natCast_toNat_emod`

 The residue of an integer modulo `M ≥ 1` is a natural number. 
