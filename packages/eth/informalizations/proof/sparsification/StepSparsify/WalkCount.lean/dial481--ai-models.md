---
{
  "module": "proof/sparsification/StepSparsify/WalkCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/WalkCount.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/WalkCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The walk through the counting tree, for any thresholds that serve

This file proves `StWalkCountG` of proof/sparsification/StepSparsify/Defs.lean. Two points deserve
note. What is known of the tree comes from the
hypothesis `Serves Θ Lc` (its field `tree`), not from `StTreeU`. And the root of the tree is the
formula without the clauses that contain a variable together with its negation. By
`SparsificationLemma.stNoTaut`,
deleting them keeps the width and the satisfying assignments, hence their number (`cntN_noTaut`),
and leaves no such clause, as `tree` asks; it does not make the formula longer (`length_noTaut_le`).
The facts on the walk are used as proved in their own files: `stWalkSG`, `stRoundS` and
`stRoundSEnd` on the walk and its rounds, `stStateLenU` on the length of its states, `stCntToN` on
the count of a formula read with natural numbers as variables. 

### `cntN_noTaut`

 Deleting the clauses that contain a variable together with its negation does not change the
number of satisfying assignments. 

### `length_noTaut_le`

 Deleting clauses does not make the formula longer. 

### `stWalkCountG`

 The walk returns the number of satisfying assignments, if the thresholds serve, `val` is right
on every node that has the properties of a leaf, and the pad suffices for the rounds and the stack. 
