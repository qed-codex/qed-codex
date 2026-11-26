---
{
  "module": "proof/consequences/FromPrinted/Dom.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/Dom.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/Dom.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Corollary 7 on the machines of proof/threesat/Printed/: dominating sets, with the machine named

«Choose w so large that the number of leaves is at most 2^{δn/2}, apply Corollary 6 to each leaf,
and add up.»
The machine at a leaf is `FromPrinted.Consequences.SIZED w ℓ τ` (`SIZED_counts`, with δ/2). The tree
is that of proof/consequences/GraphProblems/ (`GraphProblems.stShortens`); the walk that adds up is
`CountKSat.walkSum` (`CountKSat.stWalkSum`); the bounds on sizes, which name no machine, are
`Consequences.cntS_le`, `Consequences.size_dnode_le`, `Consequences.dom_size`. 

### `stDominatingCounted`

 **Dominating sets of size s, with the machine named.** For every δ > 0 there are w, ℓ, τ, c such
that the tree that shortens the clauses to w literals has at most 2^{(δ/2)n} leaves
(`ShortensD w (δ/2)`), and `DOMcount w ℓ τ` has polynomial-time steps and returns, on the code of
(G, s), s ≤ n, the number of dominating sets of size s within c·2^{δn} steps, on states of size at
most c·(n+2)^c. 
