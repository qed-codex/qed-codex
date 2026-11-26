---
{
  "module": "ThreeSumApsp/Util/Log.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Log.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Log.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Logarithms and real powers

Small facts on `Real.log`, `Real.logb`, `Nat.clog`, `Real.sqrt` and real powers that the estimates
of the paper use silently.

* Values, in the namespace `Real` and named by Mathlib's convention: `1 / 2 < log 2 < 1`,
  `log 4 = 2 log 2`, `log 9 = 2 log 3`, `1 ≤ log 4`, `1 / 2 ≤ log x` for `x ≥ 2`, `1 ≤ log x` for
  `x ≥ 3`, `log₂ 7 < 2.81`, `4 ≤ √D` for `D ≥ 16`.
* The rounded logarithm: `⌈log_b n⌉ < log_b n + 1` (`Real.natCast_clog_lt_logb_add_one`),
  `c ^ ⌈log_b n⌉ ≤ c * n ^ (log_b c)` (`Real.pow_clog_le_mul_rpow_logb`).
* The definition `logU u = log (max u 2)`, the paper's `log U`.


 ### Values 

### `one_half_lt_log_two`

 `1 / 2 < log 2`. 

### `log_two_lt_one`

 `log 2 < 1`. 

### `log_four`

 `log 4 = 2 log 2`. 

### `log_nine`

 `log 9 = 2 log 3`. 

### `one_le_log_four`

 `1 ≤ log 4`. 

### `one_le_log_of_three_le`

 `1 ≤ log x` for `x ≥ 3`. 

### `one_le_log_natCast_of_three_le`

 `1 ≤ log n` for a natural number `n ≥ 3`. 

### `one_half_le_log_of_two_le`

 `1 / 2 ≤ log x` for `x ≥ 2`. 

### `logb_two_seven_lt`

 The exponent of Strassen's algorithm: `log₂ 7 < 59 / 21 < 2.81`, because `7 ^ 21 < 2 ^ 59`. 

### `four_le_sqrt_natCast_of_sixteen_le`

 `4 ≤ √D` for a natural number `D ≥ 16`. 

 ### The rounded logarithm `Nat.clog` 

### `natCast_clog_lt_logb_add_one`

 `⌈log_b n⌉ < log_b n + 1`, for all natural numbers `b` and `n` (for `b ≤ 1` or `n = 0` both
logarithms are `0`). 

### `pow_clog_le_mul_rpow_logb`

 `c ^ ⌈log_b n⌉ ≤ c * n ^ (log_b c)`, for natural numbers `b` and `n ≥ 1` and a real number
`c ≥ 1`. 

### `logU`

 `log U`, read as `log 2` for `U < 2`, so that a bound with `log U` is positive at `U = 1` as
well. It occurs in the bounds of Theorem 21(b) and in the overhead for copying in
`ConditionalTimes.Claim.RectMinPlusFromSquare`. 
