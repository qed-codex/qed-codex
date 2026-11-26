---
{
  "module": "proof/sparsification/SparsificationLemma/One.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/One.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/One.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Every assignment that satisfies ψ satisfies exactly one output

This file proves three statements of proof/sparsification/SparsificationLemma/Defs.lean:
`StExactlyOne`, `StCountOfExactlyOne` and `StNoTaut`.

* One branching (`sat_first`, `sat_second`). An assignment satisfies the first child exactly if it
  satisfies the node and makes a literal of H true. It satisfies the second child exactly
  if it satisfies the node and makes no literal of H true: then every clause E ⊇ H has its true
  literal in E ∖ H.
* The tree (`countP_leaves`). By induction on the depth: below a node whose side clauses have one
  literal each, the number of positions in the list of outputs that b satisfies is 1 if b satisfies
  the node, and 0 otherwise. At the root the node has the satisfying assignments of ψ (`sat_rootP`).
* `exactlyOne_iff_countP` says that `ExactlyOne b ψ Φ` holds exactly if this number is 1 when b
  satisfies ψ and 0 otherwise. `stCountOfExactlyOne` adds these numbers up over all assignments to n
  variables.
* `stNoTaut`: every assignment satisfies a clause that contains a variable together with its
  negation, so deleting such clauses changes nothing.

The facts on one step come from proof/consequences/CountKSat/StepCount.lean. 

 ### Satisfying a formula 

### `instDecidableSat`

 Whether b satisfies ψ can be computed. 

### `sat_append`

 b satisfies a formula in two parts exactly if it satisfies both parts. 

### `sat_addP`

 b satisfies `addP A s` exactly if it satisfies A and s: a clause that `addP` deletes contains a
clause of A. 

### `sat_rootP`

 Deleting the clauses that contain another clause does not change the satisfying assignments. 

### `sat_leafM`

 If every side clause has one literal, `leafM x` has the satisfying assignments of `leafF x`: it
only lacks the repetitions in the side list. 

### `sat_out`

 Writing every clause once does not change the satisfying assignments. 

### `sat_out_iff`

 If every side clause has one literal, the output `out x` has the satisfying assignments of
`leafF x`. 

 ### One branching 

### `stepC_of_pickK`

 The two children of a node at which the rule picks H, with P the list of the E ∖ H. 

### `sat_first`

 b satisfies the first child exactly if it satisfies the node and makes a literal of H true. 

### `sat_second`

 b satisfies the second child exactly if it satisfies the node and makes no literal of H true. 

 ### The number of positions of a list that b satisfies 

### `countP_eq_card`

 The number of entries of a list with p is the number of positions whose entry has p. 

### `exactlyOne_iff_countP`

 `ExactlyOne b ψ Φ` says that the number of positions of Φ that b satisfies is 1 if b satisfies
ψ, and 0 otherwise. 

### `countP_leaves`

 Below a node whose side clauses have one literal each, b satisfies one position of the list of
outputs if it satisfies the node, and none otherwise. 

### `countP_outputs`

 The number of outputs (positions of the list) that b satisfies is 1 if b satisfies ψ, and 0
otherwise. 

### `stExactlyOne`

 Every assignment that satisfies ψ satisfies exactly one output, and every other assignment
satisfies none. 

 ### The counts 

### `cntN_eq_sum`

 The number of satisfying assignments on n variables, as a sum of ones and zeros over the
assignments. 

### `sum_cntN`

 The sum of the counts of the formulas of Φ is the sum, over the assignments, of the number of
positions of Φ that the assignment satisfies. 

### `stCountOfExactlyOne`

 If every assignment satisfies exactly one formula of Φ or none, according to whether it
satisfies ψ, the count of ψ is the sum of the counts of the formulas of Φ. 

 ### Clauses that contain a variable together with its negation 

### `stNoTaut`

 Deleting the clauses that contain a variable together with its negation: every assignment
satisfies such a clause. 
