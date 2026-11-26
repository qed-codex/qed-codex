---
{
  "module": "ThreeSumApsp/Sec4/Table2.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Table2.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Table2.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Table 2

Section 4.4 prescribes how an entry is computed. The left half has the `γ` of Corollary 31, "with
the c of the row and the θ that gives the q of the column (θ = 1/9 for q = 0.43)". The right half
has the `γ` of Corollary 32, "with the θ at which γ = κ - q". "The ε of a row of the table is the
smallest R_c(γ) over its entries." All values are rounded down (caption).

* The `θ` of a column of the left half does not depend on the row. It is enclosed between two
  decimal numbers (`exists_qOf_eq_010` to `exists_qOf_eq_090`): `q(θ)` is at most the `q` of the
  column at the lower number (`qOf_le`) and at least that `q` at the upper number (`le_qOf`), and it
  is continuous.
* A row (`table_2_c40` to `table_2_c10_5`) depends on `c` through two numbers: `ln(1/ρ_c)/ln 4`, by
  which `θ` is multiplied to give `γ` (`hg`), and the denominator of (11) at `γ = 0` (`hB`), which
  gives `ε < R_c(γ)` for every `γ` up to the largest one of the row (`hR`).
* An entry of the left half is `Table2Query.intro` at the enclosure of the `θ` of its column. An
  entry of the right half (`Table2Density.intro`) names two decimal numbers: at the lower one
  `γ + q ≤ κ` (`qOf_le`), at the upper one `γ + q ≥ κ` (`le_qOf`), so the root `θ` of `γ + q = κ`
  lies between them; and `γ = θ ln(1/ρ_c)/ln 4` has the printed four decimals at both.

How to read the numbers in the proofs. The two decimal numbers around a `θ` are `θ` cut after five
decimals and the next such number, or after six decimals where `γ` is too close to a multiple of
`0.0001`. The argument `k` of `qOf_le`, `le_qOf` and `log_mem` is the exponent of the power of two
nearest to the number whose logarithm is taken, and the second argument of `log_mem` is the number
of terms of the series.


 ## The `θ` of the columns of the left half 

### `exists_qOf_eq_010`

 The `θ` of the column `q = 0.10` is `0.01945042…`. 

### `exists_qOf_eq_025`

 The `θ` of the column `q = 0.25` is `0.05754017…`. 

### `exists_qOf_eq_050`

 The `θ` of the column `q = 0.50` is `0.13518246…`. 

### `exists_qOf_eq_075`

 The `θ` of the column `q = 0.75` is `0.22855783…`. 

### `exists_qOf_eq_090`

 The `θ` of the column `q = 0.90` is `0.29269537…`. 

### `qOf_ninth_mem`

 Caption of Table 2: at `θ = 1/9`, "more precisely, q = 0.4277…". 

 ## The six rows 

### `table_2_c40`

 Table 2, the row `c = 40`. 

### `gammaOf_21_one_mem`

 `ln(1/ρ_c)/ln 4` for `c = 21` (the proof of Corollary 26 uses it too). 

### `lnΛ_21_zero_mem`

 The denominator of (11) at `γ = 0` for `c = 21` (`Corollary26.Rc_digits` uses it too). 

### `table_2_c21`

 Table 2, the row `c = 21`. 

### `gammaOf_19`

 For `c = 19` one has `ρ_c = 1/2`, so `γ` is exactly `θ/2`. 

### `lnΛ_19_zero_mem`

 The denominator of (11) at `γ = 0` for `c = 19` (Table 1's column on Section 2 uses it too). 

### `table_2_c19`

 Table 2, the row `c = 19`. 

### `table_2_c15`

 Table 2, the row `c = 15`. 

### `table_2_c12`

 Table 2, the row `c = 12`. 

### `table_2_c10_5`

 Table 2, the row `c = 10.5`. 
