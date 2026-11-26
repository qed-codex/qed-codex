---
{
  "module": "proof/machines/ToTuring/Poly/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 `IsPolyT` (every part of a stepped computation is polynomial-time) is closed under the
combinators `mapIn`, `mapOut`
and `bind` of `StepMachines/Prog/Stepped.lean`. 

### `mapIn`

 Applying a polynomial-time `f` to the input before running `M` keeps `IsPolyT`. 

### `mapOut`

 Applying a polynomial-time `f` to the output of `M` keeps `IsPolyT`. 

### `bind`

 Running `M`, then `N` on the input paired with the output of `M`, keeps `IsPolyT`. The state
carries the input while
`M` runs. 
