---
{
  "module": "proof/machines/StepMachines/Prog/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Count.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The network of a k-CNF as a program: the clauses are cut into g groups (the nodes), and the
weights and
the interactions are given by procedures; `presents` shows that these procedures compute
`wordNet g k φ` within the size `S₀`. 

### `Fml.Sat`

 Some assignment makes a literal of every clause true. 

### `satP`

 The network of φ, given by procedures: g groups of clauses (the nodes), one state bit for each
of the
k literal slots of a clause. The procedures take φ itself as their context. 

### `S₀`

 The size within which the procedures of satP answer. 

### `presents`

 The procedures of `satP` compute the network `wordNet g k φ`, each in one step and within size
`S₀`. 
