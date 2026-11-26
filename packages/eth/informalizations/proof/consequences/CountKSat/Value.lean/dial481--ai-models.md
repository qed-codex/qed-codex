---
{
  "module": "proof/consequences/CountKSat/Value.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/Value.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/Value.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The value of the network of one sparse formula is the number of its satisfying assignments

`proof/machines/StepMachines/Math/SatNet.lean` proves that the value of the network of a formula is
the number of its good states, and that the good states are the
states of the models: the satisfying assignments that are false on every variable that does not
occur. Here the variables are natural numbers. If exactly
the variables below n occur, the models are the satisfying assignments to x₀ … xₙ₋₁, continued by
false (`value_net_eq_cntN`, `value_wordNet_eq_cntN`). 

### `ext_val`

 Below n the continued assignment is the assignment. 

### `ext_of_le`

 From n on the continued assignment is false. 

### `value_net_eq_cntN`

 The value of the network of a formula in which exactly the variables below n occur is the number
of its satisfying assignments on n variables. 

### `value_wordNet_eq_cntN`

 The same for the network that the program builds. 
