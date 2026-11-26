---
{
  "module": "proof/sparsification/SparsificationLemma/TreeWalk/Walk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/TreeWalk/Walk.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/TreeWalk/Walk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 4 for a machine that walks the tree and tests every leaf

The machine of proof/consequences/WidthK/Top/Sat.lean decides k-SAT by a depth-first walk of a
sparsification tree. All it asks of the tree is the property `Sparsifies` defined there: few leaves,
few clauses in a leaf, ψ is
satisfied by an assignment exactly if some leaf is, and a small stack. This file proves `Sparsifies`
for the procedure `stepK (thetaU τ) k` with the thresholds θ 0 = 1, θ i = 4·τ^(2i−1), for every ε >
0 and a suitable τ
(`lemSparsification_walk_k`; for k = 3, `lemSparsification_walk`), and that no leaf has an empty
clause.
The walk tests at a leaf the formula ψ there, without the set 𝒩 of one-literal clauses that the
changed algorithm of Appendix C carries along. This is the
Sparsification Lemma in its original form: the formula is satisfiable exactly if one of the formulas
at the leaves is.
The proof applies `WidthK.ProgMain.sparsify_prog_of`
(proof/sparsification/SparsifyWidthK/ProgMain.lean), which holds for all thresholds and bounds that
satisfy `Iface`, to `stIfaceC`. The number of leaves is bounded as in
proof/sparsification/SparsificationLemma/Geo/Tau.lean; τ = ⌈(8k/ε')³⌉ for a rational ε' with 0 < ε'
< min(ε, 1) is large enough by `stTauE`. 

### `iface`

 What the walk needs to know about the rule on finite sets, for the thresholds `thetaU τ` with 1
≤ k and 8k ≤ τ, and depth τ^(2k)·n. 

### `sparsifies_tau`

 `Sparsifies` for any τ ≥ 8k with (k/τ)·log₂(e·τ·τ^(2k)) ≤ ε. 

### `leaf_ne_nil`

 No leaf of the tree of a k-CNF has an empty clause. 

### `lemSparsification_walk_k`

 Lemma 4 for the walk, at every width k ≥ 1: for every ε > 0 there is a τ ≥ 8k for which the
procedure sparsifies width k with at most 2^(εn) leaves, each with at most 2·(θ 0 + … + θ (k−1))·n
clauses, none of them empty. 

### `lemSparsification_walk`

 Lemma 4 for the walk, at width 3. 
