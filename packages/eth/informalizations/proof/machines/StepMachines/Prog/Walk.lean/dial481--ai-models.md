---
{
  "module": "proof/machines/StepMachines/Prog/Walk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Walk.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Walk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The depth-first walk of a binary tree given by a step function, as a computation cut into steps;
an expensive
test T is run on the leaves only, and the result says whether some leaf passes it. 

 ### Run T only where sel picks an input for it 

### `guard`

 T on sel x if that is some input; the result d at once if it is none. 

 ### Facts on orbits and folds, for any loop 

### `Orbit.forall`

 A property of the first point that each move keeps holds on the whole orbit. 

 ### The walk 

### `walkNext`

 The next stack: the top is dropped if it is a leaf, else replaced by its two children. 

### `walkSel`

 The top of the stack if it is a leaf. 

### `walk`

 Does some leaf below root a pass the test T? 

### `visits`

 The stacks met while the tree below s, cut at depth k, is walked above the rest r. 

### `length_visits`

 2·(number of leaves) − 1 stacks are met. 

### `filterMap_visits`

 The tops that are leaves are the leaves, in order. 

### `exists_round_of_orbit`

 Every stack on the orbit of [s] is the stack of the walk of SparsifyTree after some number of
rounds. 

### `walk_runs`

 The walk: (t + 2) steps a leaf, where the test takes t steps on each leaf. 
