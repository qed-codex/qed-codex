---
{
  "module": "ThreeSumApsp/Machine/PolylogIsLittleO.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Machine/PolylogIsLittleO.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Machine/PolylogIsLittleO.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# A bound with polylogarithmic factors is a bound n^{a+o(1)}

Used for Theorem 22, which prints its bounds for 3SUM as `n^{a+o(1)}`.  The exponent o(1) is
`logExponent e`, for which `n^a (log n)^e ≤ n^{a + logExponent e n}` (`rpow_mul_log_pow_le`).


### `SolvedInPolylogTime.solvedInLittleOTime`

 A bound `O(n^a (log n)^{O(1)})` is a bound `n^{a+o(1)}`. 
