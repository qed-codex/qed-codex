---
{
  "module": "proof/machines/StepMachines/Prog/GridLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/GridLoop.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/GridLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 A bound on the value of a network (Definition 2 of the paper): |Z| ≤ 2^{|J|(P+B) + |J|²B} for a
network on the nodes J with at most
2^P states a node and all weights and interactions at most 2^B in absolute value. 

 ### The value of a network is small 

### `abs_value_le`

 A network on the nodes J with at most 2^P states a node and all weights W and interactions Ψ at
most 2^B in absolute
value (part of `Sized P B`) has a value Z with |Z| ≤ 2^{|J|(P+B) + |J|²B}. 
