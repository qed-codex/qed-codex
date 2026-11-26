---
{
  "module": "proof/sparsification/SparsifyWidthK/Step.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/Step.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/Step.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification of a k-CNF on finite sets: one step keeps the invariant, and the final counts

The definitions are in `SparsifyWidthK/Defs.lean`. This file proves four of the interface statements
of `SparsifyWidthK/Interfaces.lean` (the names `St…`).

* `InvK.step`: a step that adds a family A of sets, all of one size r, keeps the invariant `InvK`.
  At size r the degree bound follows from
  `AddK.deg`; at every other size the set N only loses clauses. In the inequality `InvK.acc` the
  sizes below r do not change, size r gains A and loses
  nothing, and a size i above r loses at most |A| · d i clauses, which the right-hand side gains
  through the count at size r.
* `Rule.add_light`, `Rule.add_heavy`: both children of the rule of Impagliazzo, Paturi and Zane are
  such steps.
* `Node.light`, `Node.heavy`: the counters of steps and of heavy steps along a path.
* `Node.bound`, `Leaf.card_le`: the length of a path, the number of its heavy steps, the size of a
  leaf.

Where the argument is the same as for width 3 (the children computed, the clauses of a node, double
counting by `mul_card_le`) the proofs follow
`StepMachines/Math/Sparsify.lean`. That file has two weighted potentials and disjoint petals; the
counts per clause size are particular to this file. 

### `notMem`

 An added set is not a clause of F. 

### `red_union`

 After a step the minimal clauses are the added ones and the clauses of F that contain none of
them. 

### `lay_nextN_of_ne`

 At a size other than r, N keeps the clauses that contain no added set. 

### `lay_nextN_of_lt`

 Below size r, N does not change. 

### `lay_nextN_self`

 At size r, N gains A and loses nothing. 

### `sum_nextA_of_le`

 The counts below size i do not change if i ≤ r. 

### `sum_nextA_of_lt`

 The counts below size i grow by c in total if r < i. 

### `card_lay_le`

 A step removes at most |A| · d i clauses of size i from N. 

### `InvK.step`

 A step that adds A, all of size r, keeps the invariant: N becomes `nextN N A`, and the count at
size r grows by |A|. 

### `card_filter_mem_le_one`

 A literal lies in at most one set of size 1. 

### `card_over_le`

 Below the size j of the rule every literal lies in at most θ s clauses of size s + 1. 

### `exists_over`

 Some clause of size j contains the heart. 

### `card_of_mem_petals`

 Every petal has size j - |H|. 

### `card_petals`

 There are as many petals as clauses of size j over H. 

### `Rule.add_light`

 The light child of the rule is a step that adds one set of size |H|. 

### `Rule.add_heavy`

 The heavy child of the rule is a step that adds the petals, of size j - |H|. 

### `sub_add`

 After a step every clause is still a subset of a clause of φ, nonempty if that one is. 

### `nextA_zero`

 The count at size 0 does not change. 

### `node_root`

 The root of the tree of φ is a node with both counters 0. 

### `Node.light`

 The light child counts one more step. 

### `Node.heavy`

 The heavy child counts one more step and adds τ to t. 

### `Step.acc_le`

 At most β i · n clauses of size i are added along a path. U: the at most 2n literals. 

### `Node.subset_of`

 If the clauses of φ are subsets of U, so are the clauses of every node. 

### `Node.bound`

 A path has at most (β 0 + … + β (k-1)) · n steps, and its heavy steps use at most k · n units, τ
each. 

### `Leaf.card_le`

 A leaf has at most 2n · (θ 0 + … + θ (k-1)) clauses. 

 ### The interface statements of `SparsifyWidthK/Interfaces.lean` proved by this file 

### `stNodeRoot`

 `node_root`, in the form of the interface. 

### `stNodeStep`

 `Node.light` and `Node.heavy`, in the form of the interface. 

### `stNodeBound`

 `Node.bound`, in the form of the interface. 

### `stLeafCard`

 `Leaf.card_le`, in the form of the interface. 
