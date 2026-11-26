---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/ZOrderFacts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/ZOrderFacts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/ZOrderFacts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The table of `spread`: small facts

`spread i` is the number whose digits in base 4 are the binary digits of i; the place of the entry
(a, c) of a matrix in Z-order is 2 spread a + spread c.  The routines that write matrices in Z-order
and the routine that reads the count off their product look `spread` up in a table,
`spreadList n`, the list of spread 0, …, spread (n - 1).  Here are the facts on the table that both
use: a bound on its entries, how it grows, and what a cell of it holds.


### `spread_le_sq`

 The number whose digits in base 4 are the binary digits of i is at most i². 

### `seg_spreadList_get`

 A cell of the table. 
