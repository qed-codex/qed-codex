---
{
  "module": "NS1/Interp.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Interp.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Interp.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# An interpreter that counts the names of constants

`IF` is a formula of the language that evaluates formulas; instead of multiplying by a named constant it subtracts 1
from a budget. `WF` also checks that in the end the budgets are used up. These formulas are plain: they use no
named constants.


### `DW`

 Subtract 1 from a number; the argument is (this program, the number). 

### `DC`

 Subtract 1 in a budget; the argument is (this program, (the name, the budget)). 

### `AW`

 Check that a number is 0. 

### `AZ`

 Check that all numbers of a budget are 0. 
