---
{
  "module": "proof/machines/StepMachines/Math/SparsifyTree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SparsifyTree.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SparsifyTree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Binary branching given by a step function: its leaves, a depth-first walk with an explicit
stack, and the count
of leaves when a path has at most D steps and at most T/q heavy steps. It is used for the branching
tree of the
sparsification lemma (Lemma 4). 

### `leaves`

 The leaves below s, left (light) to right (heavy), cut at depth k. 

### `round`

 One round of the depth-first walk on (stack, leaves found so far). 

### `round_iterate`

 The walk needs 2·(number of leaves) − 1 rounds for the tree below the top of the stack. 

### `round_iterate_of_le`

 After at least 2·(number of leaves) − 1 rounds from [s] the stack is empty and all leaves are
listed. 

### `roundB`

 One round of the walk that keeps only «some leaf so far passed the test». 

### `roundB_iterate_of_le`

 After at least 2·(number of leaves) − 1 rounds the flag says whether some leaf passes the test. 

 G s p t: the node s has used at least p of D units of depth and t of T units, of which a heavy
step uses q. 

### `length_leaves_le`

 The number of leaves is at most Σ_{j ≤ h} C(d, j): d steps and h heavy steps are left. 

### `step_eq_none_of_mem_leaves`

 If k ≥ D − p the cut at depth k removes nothing: the list holds true leaves only. 

### `exists_of_mem_leaves`

 Every listed node satisfies the invariant. 

### `iff_exists_mem_leaves`

 If a property holds at a node exactly when it holds at one of the node's two children, then it
holds at s exactly when it holds at one of the leaves below s. 

### `StackOK`

 The stack's invariant: the node at height j from the bottom has used at least j units of depth. 

### `stack_bound`

 At all times the stack holds at most D + 1 nodes, and each satisfies the invariant. 
