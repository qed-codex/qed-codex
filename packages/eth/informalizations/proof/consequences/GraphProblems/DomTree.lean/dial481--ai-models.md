---
{
  "module": "proof/consequences/GraphProblems/DomTree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/DomTree.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/DomTree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 7: the tree that shortens the long clauses of Dominating Set

The formula of Dominating Set has one clause of positive literals for every vertex, and its width is
not bounded. The tree of `stepD w` branches on a clause C with more than w literals, with H its
first w variables: in the light child C is replaced by H, in the heavy child the variables of H are
false and are deleted from all open clauses. This file proves `StShortens`:

* an assignment that satisfies a node satisfies exactly one of its two children, the light one if it
  makes a variable of H true (`sat_light`, `sat_heavy`, `cntS_step`), so the numbers of the
  leaves add up to the number of the root (`sum_leaves`);
* a light step removes an open clause, of which there are n at the root, and a heavy step removes w
  variables from the open clauses, in which at most n variables occur; so a path has at most n light
  steps and at
  most n/w heavy steps (the invariant `Inv`, `inv_root`, `inv_step`);
* so the tree has at most Σ_{j ≤ n/w} C(Ln, j) leaves for every L ≥ 2, which is at most 2^{εn} for a
  suitable w (from `proof/sparsification/SparsifyWidthK/Thresholds.lean`). 

 ### Which assignments satisfy a node 

### `Hit`

 The assignment a makes a variable of the list D true. 

### `Sat`

 The assignment a makes a literal of every clause of ψ true. 

### `sat_light`

 The light child: the node, and a variable of H is true. 

### `sat_heavy`

 The heavy child: the node, and no variable of H is true. 

 ### The two children of a node 

### `stepD_some`

 What `stepD` returns. 

### `card_filter_split`

 A set that is cut in two by a property Q. 

### `cntS_step`

 The number of a node is the sum of the numbers of its two children. 

### `sum_leaves`

 A number that is the sum of the numbers of the two children is the sum of the numbers of the
leaves. 

 ### The invariant 

### `Inv`

 The node x lies at depth p of the tree and t variables have been set to false; a counts the
light steps, so that p ≤ a + t, and V holds the variables that may still occur in the open clauses. 

### `inv_size`

 What the invariant says on the size of a node. 

### `stShortens`

 For every ε > 0 some width w ≥ 1 works. 
