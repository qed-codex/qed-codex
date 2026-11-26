---
{
  "module": "proof/sparsification/UniformInK/Spars/Step.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Spars/Step.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Spars/Step.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification with geometric thresholds: one step keeps the invariant

The definitions are in proof/sparsification/UniformInK/Spars/Defs.lean. This file proves two of its
interface statements, StNodeRootU and StNodeStepU. It parallels the first part of
proof/sparsification/SparsifyWidthK/Step.lean, whose lemmas on the sets nextN N A and on the counts
nextA a r c are used as they are.

* inv_step: a step that adds a family A of sets, all of one size r, keeps the invariant InvU. At
  size r the bound on the clauses over a set Y follows from AddU.deg; at every other size N only
  loses clauses. In the inequality InvU.acc the sizes below r do not change, size r gains A and
  loses nothing, and a size i above r loses at most |A| · 2·θ(i−r) clauses, because each lost clause
  contains a set of A; the right-hand side gains exactly that much through the count at size r.
* add_light, add_heavy: both children of the rule of Impagliazzo, Paturi and Zane are such steps. A
  heart for size j is a nonempty set H with |H| < j that lies in at least θ(j−|H|) clauses of size
  j; no size below j has a heart, and no set larger than H is a heart for j.
* node_light, node_heavy: the counters of steps and of heavy steps along a path. 

### `toAddK`

 A step in the sense of this folder is a step in the sense of
proof/sparsification/SparsifyWidthK/Defs.lean: take one-element sets Y. 

### `wsum_nextA_of_le`

 The weighted counts below size i do not change if i ≤ r. 

### `wsum_nextA_of_lt`

 The weighted counts below size i grow by w r · c if r < i. 

### `card_lay_le`

 A step removes at most |A| · 2·θ(i−r) clauses of a size i ≥ r from N. 

### `inv_step`

 A step that adds A, all of size r, keeps the invariant: N becomes nextN N A, and the count at
size r grows by |A|. 

### `card_filter_subset_le_one`

 A set of r elements lies in at most one set of r elements. 

### `card_over_le`

 Below the size j of the rule every nonempty set Y of at most r literals lies in at most θ(r−|Y|)
clauses of size r. 

### `add_light`

 The light child of the rule is a step that adds one set of size |H|. 

### `add_heavy`

 The heavy child of the rule is a step that adds the petals, of size j − |H|. 

### `sub_add`

 After a step every clause is still a subset of a clause of φ, nonempty if that one is. 

### `node_root`

 The root of the tree of φ is a node with both counters 0. 

### `node_light`

 The light child counts one more step. 

### `node_heavy`

 The heavy child counts one more step and adds τ to t. 

### `stNodeRootU`

 The root of the tree is a node with both counters 0. 

### `stNodeStepU`

 Both children of a node are nodes: one more step, and τ more units at the heavy child. 
