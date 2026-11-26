---
{
  "module": "proof/consequences/SplitSat/Sizes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Sizes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Sizes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 5: the tree with n carried along, and sizes

No sentence of the paper stands behind this file. A node of the tree of `SplitSat.reduceCore` is a
formula with n in unary beside it (`stepN step`).
* `leaves_stepN`, `stack_stepN`: the leaves and the stacks of the walk are those of `step`, with n
  beside every formula.
* `length_le_of_nodup`: a formula on n variables with at most k literals per clause and no clause
  written twice has at most 2^k·(n+2)^k clauses.
* `size_node_le`, `size_stack_le`, `final_bound`: the sizes that occur in the run of the reduction
  are at most c'·(n+2)^c'.
The first four lemmas on sizes repeat lemmas of proof/machines/StepMachines/Prog/Sat.lean and
proof/consequences/WidthK/Top/Sat.lean that are not visible from outside those files. 

 ### The tree with n carried along 

### `leaves_stepN`

 The leaves of the tree with n carried along are the leaves of the tree, with n beside each. 

### `round_stepN`

 One round of the walk commutes with putting n beside every formula. 

### `round_stepN_iterate`

 The same for any number of rounds. 

### `stack_stepN`

 The stack of the walk with n carried along, after i rounds, is the stack of the walk, with n
beside every formula. 

 ### The number of clauses 

### `length_le_of_nodup`

 A formula with variables below n, at most k literals per clause and no clause written twice has
at most 2^k·(n+2)^k clauses. 

 ### Sizes 

### `sum_size_le`

 The sum of (size + 1) over a list whose members have size at most s is at most (length)·(s+1). 

### `size_list_le`

 A list of at most k members of size at most s has size at most k·(s+1) + 1. 

### `size_lit_le`

 A literal on a variable below n has size at most n + 2. 

### `size_fml_le`

 A bound on the size of a formula of at most m clauses of at most k literals with variables below
n. 

### `size_unary_le`

 n in unary has size at most 2n + 1. 

### `size_node_le`

 A node (n in unary, x), where x has at most a·(n+2)^k clauses of at most k literals with
variables below n, has size at most (a·(2k+1) + 3)·(n+2)^(k+1). 

### `size_stack_le`

 A stack of at most Dd·n + 1 such nodes has size at most ((Dd+1)·(a·(2k+1) + 4) + 1)·(n+2)^(k+2). 

### `cOf`

 The constant c' of `reduceCore_decides`, from the constants of the size bounds in its proof. 

### `final_bound`

 The sizes that occur in the proof of `reduceCore_decides` are at most c'·W^c', where W = n + 2. 
