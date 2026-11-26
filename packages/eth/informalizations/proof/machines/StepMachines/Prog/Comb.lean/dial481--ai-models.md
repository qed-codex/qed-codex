---
{
  "module": "proof/machines/StepMachines/Prog/Comb.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Comb.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Comb.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Further combinators: a choice between two computations (branch, ite, optBind), two computations
on one input
(both, map2, mul2), constants. 

 ### Choice 

### `branch`

 M₁ on x if sel a = inl x, M₂ on y if sel a = inr y. No further step. 

### `iteSel`

 Left if p a, else right. 

### `ite`

 M if p a, else N, on the same input. No further step. 

### `const`

 The result b, whatever the input; one step. 

### `optSel`

 Left with (a, i) at (a, some i), right with a at (a, none). 

### `optBind`

 M; if its result is some i, then N on (a, i); if none, then dflt a. 

 ### Two computations on one input 

### `both`

 M, then N, on the same input; both results. 

### `map2`

 f of the results of M and N on the same input. 

### `mul2`

 The product of the results of M and N on the same input. 
