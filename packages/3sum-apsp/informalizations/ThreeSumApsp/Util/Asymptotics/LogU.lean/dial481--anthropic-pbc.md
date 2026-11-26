---
{
  "module": "ThreeSumApsp/Util/Asymptotics/LogU.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/LogU.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/LogU.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# `logU`, the paper's `log U`

`logU u` is `log u`, read as `log 2` for `u < 2`.

* It is positive and nondecreasing, and `log (cu) ≤ log c + log u` for `c ≥ 1`.
* `log (cU) = O(log U)` (`dominated_logU_mul`) and `log (c n^κ) = O(log n)`
  (`dominated_logU_mul_rpow`).
* Along bounds `u(n) ≤ c n^κ` it is `Õ(1)` (`isPowPolylog_logU_of_le`).


### `log_two_le_logU`

 `logU u ≥ log 2`. 

### `logU_pos`

 `logU u > 0`. 

### `one_le_one_add_logU`

 `1 + logU u ≥ 1`. 

### `log_le_logU`

 `log u ≤ logU u` for `u > 0`. 

### `logU_mono`

 `logU` is nondecreasing. 

### `logU_mul_le`

 `logU (c u) ≤ log c + logU u` for `c ≥ 1`. 

### `logU_le_logU_mul`

 `logU u ≤ logU (c u)` for `c ≥ 1`, also for negative `u`. 

### `logU_rpow_le`

 `logU (n^κ) ≤ log 2 + κ log n` for `n ≥ 1` and `κ ≥ 0`. 

 ## `logU` of a multiple 

### `dominated_logU_mul`

 `log (cU) = O(log U)` for a constant `c ≥ 1`. 

### `dominated_logU_mul_rpow`

 `log (c n^κ) = O(log n)` on `n ≥ 2`. 

 ## `logU` along bounds that are polynomial in `n` 

### `isPowPolylog_logU_of_le`

 `log u(n) = Õ(1)` for bounds `1 ≤ u(n) ≤ c n^κ` on the numbers. 

### `isPowPolylog_logU_mul_rpow`

 `log (c n^κ) = Õ(1)`. 
