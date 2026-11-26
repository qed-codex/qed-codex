---
{
  "module": "proof/machines/ToTuring/Poly/Walk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Walk.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Walk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 `IsPolyT` for `guard` and the depth-first walk of `StepMachines/Prog/Walk.lean`. 

### `guard`

 `guard sel T d` runs `T` on `sel x` when that is `some`, and otherwise answers `d` at once. Its
steps are
polynomial-time if `sel` is and the steps of `T` are. 

### `walk`

 The depth-first walk from `root x` of the binary tree given by `step` (`none` at a leaf, else
the two children), which
runs `T` at every leaf it visits. Its steps are polynomial-time if `step`, `root` and the steps of
`T` are. 
