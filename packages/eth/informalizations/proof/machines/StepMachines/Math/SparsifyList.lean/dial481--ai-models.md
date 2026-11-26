---
{
  "module": "proof/machines/StepMachines/Math/SparsifyList.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SparsifyList.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SparsifyList.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Two tools for the branching tree of the sparsification lemma of Impagliazzo, Paturi and Zane,
with the formulas written as plain lists of lists of literals.
`leaves_sim`: a map that carries one step function to another on the states with an invariant
carries the leaves of the one tree to the leaves of the other.
`redLL` keeps the inclusion-minimal clauses of a list, and `map_redLL` says that it agrees with
`redL` on finsets. 

### `leaves_sim`

 If f carries step' to step on the states with I, it carries leaves to leaves. 

### `redLL`

 The inclusion-minimal clauses of a list. 
