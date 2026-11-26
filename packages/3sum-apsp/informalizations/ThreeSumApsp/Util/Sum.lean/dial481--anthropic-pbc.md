---
{
  "module": "ThreeSumApsp/Util/Sum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Sum.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Sum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Bounds on finite sums and products

General facts about sums and products over a finite set in an ordered ring or field.

* A sum of `s.card` numbers of absolute value at most `A` is at most `s.card * A` in absolute value
  (`Finset.abs_sum_le_card_mul`), also with coefficients of absolute value at most `1`
  (`Finset.abs_sum_mul_le`).
* A product of numbers of absolute value at most `1` has absolute value at most `1`
  (`Finset.abs_prod_le_one`). For integers, `Int.abs_le_one_iff` says that these are `0`, `1`, `-1`.
* A sum over the indices below `m * n` is a double sum (`Finset.sum_range_mul`).
* A part of a geometric series with ratio `0 < x < 1` is less than the whole series from its first
  term on (`geom_sum_Ico_lt_of_lt_one`).


### `abs_sum_le_card_mul`

 If `|f i| ≤ A` for all `i ∈ s`, then `|∑ i ∈ s, f i| ≤ s.card * A`. 

### `abs_sum_mul_le`

 If `|c i| ≤ 1` and `|a i| ≤ A` for all `i ∈ s`, then `|∑ i ∈ s, c i * a i| ≤ s.card * A`. 

### `abs_prod_le_one`

 If `|f i| ≤ 1` for all `i ∈ s`, then `|∏ i ∈ s, f i| ≤ 1`. 

### `sum_range_mul`

 A sum over the indices below `m * n`, row by row: the index `a * n + b` has row `a` and column
`b`. 

### `geom_sum_Ico_lt_of_lt_one`

 For `0 < x < 1`, `∑ i ∈ Ico m n, x ^ i < x ^ m / (1 - x)`. Mathlib's
`geom_sum_Ico_le_of_lt_one` has `≤`, for `0 ≤ x`. 
