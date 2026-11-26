---
{
  "module": "proof/consequences/Consequences/Dom.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Consequences/Dom.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Consequences/Dom.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Bounds for counting dominating sets (Corollary 7)

Three bounds on counts and sizes that belong to the proof of Corollary 7, in which the clauses are
shortened by a tree, Corollary 6 is applied at each leaf, and the counts are added up.
`cntS_le` bounds the number of satisfying assignments with s true variables by 2^n. `size_dnode_le`
bounds the size of a node of the tree of proof/consequences/GraphProblems/ that shortens the clauses
(`GraphProblems.stShortens`). `dom_size` bounds the sizes of the states of the walk over that tree
that adds up the counts at its leaves (`CountKSat.stWalkSum`). 

### `cntS_le`

 There are at most 2^n satisfying assignments with s true variables. 

### `size_dnode_le`

 A node of the tree that shortens the clauses, for s ≤ n, at most n neighborhood clauses of at
most n variables below n, and at most 2n further clauses of width at most w on variables below n,
has size at most (4w + 12)·(n + 2)^3. 

### `dom_size`

 The bound on the sizes of the states of the walk that `CountKSat.stWalkSum` gives, with X = n +
2 and K = 8w + 40 + c·4^c, is at most (K + c + 4)·X^(K + c + 4). 
