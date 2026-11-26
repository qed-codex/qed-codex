---
{
  "module": "proof/machines/Tower/Kernel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Kernel.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Kernel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Rules for costs

`WithinFrom.mono` and the three rules of `stWithinRules` (proof/machines/QueryMachines/Runs.lean),
with implicit arguments: the form in which the proofs of this folder use them. Nothing is proved
anew here. 

### `wfMono`

 The cost and the bound on the sizes may be raised. 

### `wfHalt`

 A halted state costs nothing. 

### `wfStep`

 An own step costs 1. 

### `wfQuery`

 The query x costs w x. 
