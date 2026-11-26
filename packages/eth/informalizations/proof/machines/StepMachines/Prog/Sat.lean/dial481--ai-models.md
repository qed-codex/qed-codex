---
{
  "module": "proof/machines/StepMachines/Prog/Sat.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Sat.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Sat.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The 3-SAT machine as a program: decode the input, walk the sparsification tree depth-first, test
every leaf;
and bounds on the sizes of lists and literals. 

### `decF`

 The formula written in the input. 

### `hasNil`

 Is there an empty clause? 

### `posZ`

 Is the count positive? 

### `satM`

 The 3-SAT machine: decode the input, answer false if there is an empty clause, otherwise walk
the sparsification
tree with parameter τ and answer true iff some leaf passes the test. M is the test of a leaf (a
count that is positive
iff the leaf is satisfiable). 

 ### Sizes 
