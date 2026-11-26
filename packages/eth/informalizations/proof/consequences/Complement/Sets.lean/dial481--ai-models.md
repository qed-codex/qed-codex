---
{
  "module": "proof/consequences/Complement/Sets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Complement/Sets.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Complement/Sets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 7: «The cliques of size s are the independent sets of size s of the complement graph, and the vertex covers of size s are the complements of the independent sets of size n − s.»

* `stCliques`: the first half, for sets and for their numbers; it is Mathlib's
  `SimpleGraph.isNIndepSet_compl`.
* `stCovers`: the second half, for s ≤ n; from Mathlib's
  `SimpleGraph.isIndepSet_compl_iff_isVertexCover` and `Finset.card_compl`. The numbers agree
  because S ↦ Sᶜ is one-to-one.
* `stComplMatrix`: `complMatrix` turns the adjacency matrix of G into that of the complement graph. 

### `stCliques`

 «The cliques of size s are the independent sets of size s of the complement graph»: the same
sets, hence the same number. 

### `stCovers`

 «the vertex covers of size s are the complements of the independent sets of size n − s», for s ≤
n: S is a vertex cover of size s exactly if Sᶜ is an independent set of size n − s; hence the same
number. 

### `pairs_eq`

 `pairs n` is the list of the pairs (u, v) of vertices u, v : Fin n, as numbers, with u in the
outer and v in the inner loop, both in increasing order. 

### `entry_compl`

 One entry: u ≠ v and the entry (u, v) of the matrix of G is 0, exactly if u and v are adjacent
in the complement graph. 

### `stComplMatrix`

 `complMatrix` turns the adjacency matrix of G into the adjacency matrix of the complement graph. 
