---
{
  "module": "ThreeSumApsp/Lang/Lib/Odometer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/Odometer.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/Odometer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# An odometer in the memory

`incStmt vb vn j len` adds 1 to the number whose len digits in base n, least significant first, are
in the cells base + j, base + j + 1, …; a carry out of the last digit is dropped (`incStmt_ends`).
Local vb holds base and local vn holds n.  The number of digits is known when the program is
written, so the statement has no loop: it is a chain of len tests, and the proof is an induction on
the list of the digits.  The pure model is `ThreeSumApsp.incDigits`.


### `incStmt`

 Add 1 to the number with the digits at base + j, …, base + j + len - 1. 

### `incStmt_ends`

 **incStmt** replaces the digits l by `ThreeSumApsp.incDigits n l`, changes nothing else, and
takes at
most 14 len + 5 steps. 
