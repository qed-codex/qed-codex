---
{
  "module": "Nc/SlpCalc.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/SlpCalc.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/SlpCalc.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# A calculus for straight-line programs

Functions with values in `ℕ` (below `D`); `Cost D A c h` means that `h` is computed in at most `c` steps
from functions of the set `A`.


### `SlpN`

 Functions with values in `ℕ` that are computed in `p` steps. 

### `SlpN.snoc`

 One step more. 

### `SlpN.le`

 Idle steps. 

### `SlpN.inputs`

 All inputs. 

### `Cost`

 `h` is computed in at most `c` steps from functions of `A`. 

### `Cost.base`

 available 

### `Cost.const`

 constants 

### `Cost.op`

 binary operations 

### `Cost.mono`

 idle steps 

### `Cost.run`

 Running a computation. 

### `SlpN.stage`

 A family of functions. 

### `op1`

 A unary operation. 

### `sum`

 Sums. 

### `ind`

 The indicator of a property. 

### `CostP`

 A property is decided in at most `c` steps. 

### `rel`

 A relation between two values. 

### `rel1`

 A property of a value. 

### `const`

 A constant property. 

### `Cost.ite`

 A choice. 
