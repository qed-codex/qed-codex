---
{
  "module": "proof/consequences/Sat3Graph/Dominating.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Dominating.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Dominating.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 7, «In particular, they decide … Dominating Set»

Proof of `StDominating` of proof/consequences/Sat3Graph/Defs.lean.

The machine `DOM w gates D` walks the tree of the proof of Corollary 7 that shortens the clauses to
w literals, and asks at each leaf (`askSized`). A leaf has at most 3n clauses of at most w literals
(`GraphProblems.ShortensD`), so `stAskSized` applies with B = 3·(w − 3), and a leaf costs at most
c₁·2^{(δ/2)n} steps. There are at most 2^{(δ/2)n} leaves. The machine `Stepped.walk` answers «yes»
exactly if some leaf does (`Stepped.walk_runs`); the numbers `cntS` of the leaves add up to that of
the formula for dominating sets (`GraphProblems.ShortensD`), which is the number of dominating sets
of size s (`GraphProblems.stDom`), and a sum of natural numbers is not 0 exactly if one of them is
not 0. 

### `sum_ne_zero_iff`

 A sum of natural numbers is not 0 exactly if one of them is not 0. 

### `size_dnode_le`

 The size of a node of the tree for Dominating Set: at most (4w + 12)·(n+2)³. 

### `stDominating`

 **`StDominating`.** Let the tree for w have at most 2^{δn/2} leaves
(`GraphProblems.ShortensD w (δ/2)`) and let D decide 3-SAT with an exponent δ₃ ≥ 0 such that δ₃·(a +
1 + 3·(w − 3)) ≤ δ/2. Then `DOM w gates D` decides Dominating Set within c'·2^{δn} steps, on states
of size at most c'·(n+2)^{c'}. 
