---
{
  "module": "ThreeSumApsp/Util/Asymptotics/Powers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/Powers.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/Powers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Powers of `n` and of `log n` for large `n`

The facts behind the paper's `O(n^a)`, `Õ(n^a)` and `n^{a+o(1)}`, for functions of a natural number
`n` and in the language of Mathlib's `f =O[atTop] g`. Powers of `n` are monotone in the exponent
(`isBigO_rpow_rpow_of_le`, `isBigO_rpow_mul_log_pow_of_le`) and multiply by adding exponents
(`rpow_mul_rpow_eventuallyEq`). A constant or a power of `log n` is below every positive power of
`n` (`eventually_le_rpow`, `isLittleO_log_pow_rpow`). Hence `n ^ a * (log n) ^ e` is `o(n ^ b)` and
`O(n ^ b)` for `a < b` (`isLittleO_rpow_mul_log_pow_rpow`, `isBigO_rpow_mul_log_pow_rpow`), which is
where logarithms are absorbed for large `n`; with the constant absorbed too, this is
`eventually_mul_rpow_mul_log_pow_le`. The rounded power `⌈n ^ μ⌉` tends to infinity for `μ > 0`
(`tendsto_ceil_rpow_atTop`).


### `isBigO_of_abs_le`

 A bound `|f n| ≤ C * g n` from some `n₀` on gives `f = O(g)`. 

### `eventually_le_rpow`

 Every constant is eventually at most `n ^ η`, for `η > 0`. 

### `tendsto_ceil_rpow_atTop`

 `⌈n ^ μ⌉` tends to infinity with `n`, for `μ > 0`. 

### `isBigO_rpow_rpow_of_le`

 `n ^ a = O(n ^ b)` for `a ≤ b`. 

### `rpow_mul_rpow_eventuallyEq`

 `n ^ a * n ^ b = n ^ (a + b)` for all large `n`. 

### `isLittleO_log_pow_rpow`

 `(log n) ^ e = o(n ^ η)` for `η > 0`. 

### `isBigO_log_pow_log_pow_of_le`

 `(log n) ^ e = O((log n) ^ e')` for `e ≤ e'`. 

### `isBigO_rpow_mul_log_pow_of_le`

 `n ^ a * (log n) ^ e = O(n ^ b * (log n) ^ e')` for `a ≤ b` and `e ≤ e'`. 

### `isLittleO_rpow_mul_log_pow_rpow`

 Logarithms are absorbed: `n ^ a * (log n) ^ e = o(n ^ b)` for `a < b`. 

### `isBigO_rpow_mul_log_pow_rpow`

 Logarithms are absorbed: `n ^ a * (log n) ^ e = O(n ^ b)` for `a < b`. 

### `eventually_mul_rpow_mul_log_pow_le`

 Constants are absorbed as well: `C * (n ^ a * (log n) ^ e) ≤ n ^ b` for all large `n`, if
`a < b`. 

### `eventually_mul_rpow_le`

 `C * n ^ a ≤ n ^ b` for all large `n`, if `a < b`. 
