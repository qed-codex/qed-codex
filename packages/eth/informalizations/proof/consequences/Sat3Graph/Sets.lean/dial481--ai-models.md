---
{
  "module": "proof/consequences/Sat3Graph/Sets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Sets.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Sets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 7 for deciding: Independent Set, Clique, Vertex Cover

Proof of `StSets` of proof/consequences/Sat3Graph/Defs.lean, from `stAskSized` at width 2 (no new
variable: B = 0). The formula is that for independent sets in all three cases: of the graph, of the
complement graph (`Complement.readClique`), or of the graph with n − s in the place of s
(`Complement.readCover`).
What the two readers hand over (`Complement.StReaders`) and the shape of the formula for independent
sets (`Complement.StIndepAlone`) are hypotheses here; Main.lean puts their proofs in. That subsets
of independent sets and of cliques, and supersets of vertex covers, are again such sets is
`GraphProblems.stDecide`. 

### `decidesGraph_of_reader`

 Let `askSized gates D` answer at width 2 as `StAskSized` says, with the constant c'. Let the
reader rd hand over, on the code of (G, s) with s ≤ n, some (n in unary, s', ψ) with s' ≤ n and ψ of
width 2 on x₀ … xₙ₋₁, such that ψ has a satisfying assignment with exactly s' true variables exactly
if p holds of (G, s). Then `askSized gates D` behind rd decides p with the same constant. 

### `stSets_of`

 **`StSets`**, from what the readers for cliques and vertex covers hand over and the shape of the
formula for independent sets: for every procedure D for 3-SAT with an exponent δ₃ ≥ 0 such that
δ₃·(a+1) ≤ δ, the machines `INDEP`, `CLIQUE`, `COVER` decide Independent Set, Clique and Vertex
Cover within c'·2^{δn} steps. 
