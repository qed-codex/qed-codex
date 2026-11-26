---
{
  "module": "proof/threesat/ThreeSatOnTree/ThmEveryDelta.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/ThreeSatOnTree/ThmEveryDelta.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/ThreeSatOnTree/ThmEveryDelta.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification of Appendix C for the proof of Theorem 2

The proof of Theorem 2 in its decision form (Section 6) takes one thing from Lemma 4 in its form for
deciding: with ε = δ/3, it suffices to decide whether a 3-CNF Φ with m ≤ Mn clauses is satisfiable,
in time O(2^{δ'm}), δ' = δ/(3M). In this development it is
the property `Eight.SufficesSparse δ M S` of a constant M and of a construction S of machines,
defined in proof/networks/Eight/SecProof_Proof.lean.
This file proves the property from `SparsificationLemma.TreeWalk.lemSparsification_walk`
(`sufficesSparse_viaC`): the tree is that of the procedure of Appendix C at width 3 with the
thresholds θ 0 = 1, θ i = 4·τ^(2i−1), the tree whose leaves are the formulas ψ of the nodes (ψ, 𝒩)
of `SparsificationLemma.tree`.
M = 2·(θ 0 + θ 1 + θ 2) bounds the number of clauses of a leaf per variable. S = `satC τ`
(proof/threesat/ThreeSatOnTree/Defs.lean). Its correctness and its number of steps are `sat_correct`
of proof/consequences/WidthK/Top/Sat.lean, which asks of the tree only the property `Sparsifies`.
`one_le_leafCU` says that M ≥ 1.
Different from the paper: the walk tests ψ at a leaf and not the output ψ ∪ 𝒩; a formula is
satisfiable exactly if ψ is satisfiable at some leaf. The list of Lemma 4 is never written, and the
time clause of Lemma 4 is not used. 

### `one_le_leafCU`

 The constant M = 2·(θ 0 + θ 1 + θ 2) is at least 1. 

### `sufficesSparse_viaC`

 **«By Lemma 4 with ε = δ/3», in Theorem 2 in its decision form: it suffices to decide whether a
3-CNF Φ with m ≤ Mn clauses is satisfiable, in time O(2^{δ'm})**, with Lemma 4 in the form
`SparsificationLemma.TreeWalk.lemSparsification_walk`: M = 2·(θ 0 + θ 1 + θ 2) for its parameter τ,
and S = `satC τ`. 
