---
{
  "module": "ThreeSumApsp/Util/Asymptotics/Logarithms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/Logarithms.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/Logarithms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Logarithms up to a constant factor

Bounds on logarithms in the calculus `Dominated`, for every argument of a domain and not only for
large ones.

* Absorbing logarithms, for `x ≥ 1`: `(log x + 1) ^ e` is `O(x ^ η)` for `η > 0`
  (`dominated_log_add_one_pow_rpow`), hence `x ^ a * (log x) ^ e = O(x ^ b)` for `a < b`
  (`dominated_rpow_mul_log_pow_rpow`).
* From 2 on: `log x + 1 = O(log x)` (`dominated_log_add_one_log`) and `⌈log_b n⌉ + 1 = O(log n)`
  (`dominated_clog_add_one_log`).

For a natural number or a field of a parameter record in place of `x`, use `Dominated.comp`.


 ### Absorbing logarithms, for all `x ≥ 1` 

### `dominated_log_add_one_rpow`

 `log x + 1 = O(x ^ η)` on `x ≥ 1`, for `η > 0`. 

### `dominated_log_add_one_pow_rpow`

 `(log x + 1) ^ e = O(x ^ η)` on `x ≥ 1`, for `η > 0`. 

### `dominated_rpow_mul_log_add_one_pow_rpow`

 Logarithms are absorbed: `x ^ a * (log x + 1) ^ e = O(x ^ b)` on `x ≥ 1`, for `a < b`. 

### `dominated_rpow_mul_log_pow_rpow`

 Logarithms are absorbed: `x ^ a * (log x) ^ e = O(x ^ b)` on `x ≥ 1`, for `a < b`. 

 ### `log x + 1` and `⌈log_b n⌉ + 1` are `O(log)`, from `2` on 

### `dominated_log_add_one_log`

 `log x + 1 = O(log x)` on `x ≥ 2`. 

### `dominated_clog_add_one_log`

 `⌈log_b n⌉ + 1 = O(log n)` on `n ≥ 2`, for every natural number `b`. 
