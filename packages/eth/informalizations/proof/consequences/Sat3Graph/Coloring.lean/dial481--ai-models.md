---
{
  "module": "proof/consequences/Sat3Graph/Coloring.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Coloring.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Coloring.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 7, «In particular»: deciding k-Coloring

Proof of `StColoring` of proof/consequences/Sat3Graph/Defs.lean. The k-CNF on kn variables of the
proof of Corollary 7 (in the paper: «a k-CNF on kn variables, which says that each vertex has
exactly one color and that the ends of each edge have different colors») has n clauses of k
literals; all its other clauses have 2 literals. Splitting the n long clauses takes (k − 3)·n new
variables, so the 3-CNF has at most (2k − 3)·n variables. It is satisfiable exactly if the k-CNF is,
that is if the number of proper colorings is not 0 (`GraphProblems.stColor`, a statement on
numbers), that is if the graph can be colored (`GraphProblems.stDecideColor`). 

### `numFresh_append_le`

 Clauses of at most 3 literals written behind a formula need no new variable. 

### `numFresh_colorF`

 The formula of the colorings needs at most (k − 3)·n new variables. 

### `stColoring`

 **`StColoring`.** For k ≥ 3 and every procedure D for 3-SAT with an exponent δ₃ ≥ 0 such that
δ₃·(2k − 3) ≤ δ, the machine `COLOR k D` says on the code of a graph G on n vertices, within
c'·2^{δn} steps and on states of size at most c'·(n+2)^{c'}, whether G can be colored with k colors. 
