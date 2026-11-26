---
{
  "module": "proof/machines/ToTuring/Poly/Cut.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Cut.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Cut.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Every step of the procedure of one rectangle is polynomial-time (`IsPolyT`): every plain
function
in one of its steps is polynomial-time, and the procedure is built from these functions by
combinators that keep `IsPolyT`. 

 ### The tables of one bit: functions on finite types 

 ### Names of strings of values of type `Bell` 

### `toWordL_polyT`

 The word of a number, as long as a given word. 

 ### One rectangle 

### `IsPolyT.cutP`

 Every step of the procedure of one rectangle is polynomial-time. 
