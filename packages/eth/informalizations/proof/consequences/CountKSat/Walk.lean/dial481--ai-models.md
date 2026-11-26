---
{
  "module": "proof/consequences/CountKSat/Walk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/Walk.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/Walk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The walk that sums over the leaves

`proof/machines/StepMachines/Prog/Walk.lean` walks the tree of a step function depth first and says
whether some leaf passes a test. `walkSum` is the same loop with a number
in place of the truth value: it adds up the numbers that a computation T returns on the leaves. This
file has the lemma on trees (a quantity that splits at every
node is the sum over the leaves), the steps, the space and the result of `walkSum`, and its
polynomial-time certificate. The orbit of the loop, its length and its
leaves are taken from that file unchanged. 

### `foldl_add_sel`

 The loop's fold adds v over the points that sel picks. 

### `sum_prefix_le`

 The sum over a prefix of a list of numbers is at most the sum over the whole list. 

### `sum_leaves`

 A quantity that is the sum of its values at the two children, at every node with the invariant
G, is the sum of its values at the leaves. 

### `walkSum_runs`

 If T takes t steps on each leaf and the sum over the leaves is below 2^B, the summing walk takes
t + 2 steps per leaf and returns that sum. 

### `isPolyT_walkSum`

 Init, step and out of the summing walk are polynomial-time if `step`, `root` and the parts of T
are. 

 ### The interface statements of `proof/consequences/CountKSat/Interfaces.lean` that this file proves 

### `stSumLeaves`

 The lemma on trees, as the interface states it. 

### `stWalkSum`

 The steps, the space and the result of the summing walk, as the interface states them. 
