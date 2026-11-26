---
{
  "module": "proof/sparsification/SparsificationLemma/Nodes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Nodes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Nodes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The nodes of the tree of recursive calls

Lemmas for proof/sparsification/SparsificationLemma/StepSparsify.lean and
proof/sparsification/SparsificationLemma/Sketch.lean, which follow the sparsification of Lemma 4,
Appendix C and Step 5 of Appendix D sentence by sentence.
* For every step function: the leaves are among the nodes `nodesOf`
  (proof/sparsification/SparsificationLemma/StepSparsifyDefs.lean) of the tree
  (`mem_nodesOf_of_mem_leaves`), and what holds at the root and passes from a node to its two
  children holds at every node (`forall_nodesOf`).
* `node_facts`: at every node of the tree of a k-CNF ψ, for thresholds with `ThrC`, the formula is
  in normal form, none of its clauses contains another, it is a k-CNF on the variables below n, and
  it has at most as many clauses as ψ; every side clause has one literal, and the side list has at
  most k·(k−1)·n/τ clauses.
* `length_sideU_le`: the side list as it is written in the output has at most 2n clauses.
* `cntN_nil`: the formula without clauses has 2^n satisfying assignments. 

 ### All nodes of a tree, for every step function 

### `mem_nodesOf_of_mem_leaves`

 The leaves are among the nodes. 

### `forall_nodesOf`

 What holds at s and passes from a node to its two children holds at all nodes. 

 ### What holds at every node 

### `node_facts`

 At every node of the tree of a k-CNF ψ on n variables, for thresholds with `ThrC`: the formula
is in normal form, none of its clauses contains another, it is a k-CNF on n variables, and it has at
most as many clauses as ψ;
every side clause has one literal, on a variable below n; and the side list, as a list, has at most
k·(k−1)·n/τ clauses: only a step to a second child lengthens it, by at most k clauses, and a path
has at most (k−1)·n/τ such steps. 

 ### The length of the side list 

### `length_sideU_le`

 There are only 2n clauses with one literal: the side list as it is written in the output has at
most 2n clauses, if its variables are below n. 

 ### The number of satisfying assignments of the formula without clauses 

### `cntN_nil`

 The formula without clauses has 2^n satisfying assignments. 
