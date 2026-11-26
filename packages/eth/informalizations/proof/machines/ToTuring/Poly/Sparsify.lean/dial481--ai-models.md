---
{
  "module": "proof/machines/ToTuring/Poly/Sparsify.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Sparsify.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Sparsify.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The plain functions of the walk of the sparsification tree, defined in
`StepMachines.Math.SparsifyProg`, are polynomial-time (`PolyT`). Every certificate is stated for
arguments that depend on a
context x, the form in which the tactic `fun_prop` can use it. 

### `polyT_rootP`

 The root of the sparsification tree is computed in polynomial time. 

### `polyT_greedyP'`

 `greedyP k`, which picks at most k clauses of l that share no literal with `used` or with one
another, is
polynomial-time for every fixed k: the number of rounds is a constant of the machine. The induction
on k needs all
contexts α at once. 

### `pickP_eq`

 `pickP` with its case distinctions written by `Option.elim`. 

### `polyT_pickP`

 The choice of the branching rule at a node is polynomial-time. 

### `polyT_stepP`

 The two children of a node of the sparsification tree are computed in polynomial time. 
