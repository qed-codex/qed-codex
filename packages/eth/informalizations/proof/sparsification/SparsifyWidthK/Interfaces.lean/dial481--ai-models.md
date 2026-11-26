---
{
  "module": "proof/sparsification/SparsifyWidthK/Interfaces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/Interfaces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/Interfaces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The interface statements, as propositions

Every statement that one file needs from another is written here as a definition `St… : Prop`.
Nothing is proved and nothing is assumed: this file has no
theorem. One file proves `theorem … : St…`; a file that needs the statement takes `(h : St…)` as a
hypothesis. 

 ### Finite sets: the tree of the rule 

### `StNodeRoot`

 The root of the tree is a node with both counters 0. 

### `StNodeStep`

 Both children of a node are nodes: one more step, and τ more units at the heavy child. 

### `StNodeBound`

 A path has at most (β 0 + … + β (k-1))·n steps, and its heavy steps use at most k·n units, τ
each. U: the at most 2n literals. 

### `StLeafCard`

 A leaf has at most 2·(θ 0 + … + θ (k-1))·n clauses. 

### `StLightEq`

 For a heart H of a reduced F, the light child is H together with the clauses of F that do not
contain H. 

### `StHeavyEq`

 For a heart H of a reduced F, the heavy child is the petals together with the clauses of F that
contain no petal. 

### `StSatIff`

 F is satisfied exactly if one of the children is. 

 ### The thresholds and the number of leaves 

### `StThr`

 The thresholds `theta τ` and the bounds `beta τ` have the three properties that the final count
needs. 

### `StBetaSum`

 β 0 + … + β (k-1) is at most `bsum τ k`. 

### `StLeafCount`

 The bound on the number of leaves, Σ_{j ≤ kn/τ} C(bsum τ k · n, j), is at most 2^{εn} if
(k/τ)·log₂(e·τ·bsum τ k) ≤ ε. 

### `StExistsTau`

 For every ε > 0 some τ, as large as we like, has (k/τ)·log₂(e·τ·bsum τ k) ≤ ε. 

 ### The program 

### `Iface`

 What the walk of the tree needs to know about the rule on finite sets. `Node F₀ F p t`: F is a
node of the tree of F₀ after p steps and t units, of which a
heavy step uses q. `Ok F₀` is a condition on the formula at the start. D and T bound p and t, and
`leafB` bounds the number of clauses of a leaf. 

### `Refines`

 The functions on lists carry out the rule on finite sets. On a formula in normal form, `pickK`
returns a heart and its petals as the rule demands, or `none`
at a leaf; `rootP` returns a formula in normal form whose set of clauses is the set of the
inclusion-minimal clauses. 

### `StRefines`

 `Refines` holds whenever all thresholds are at least 1. 

### `StProg`

 The sparsification lemma for width k, for the functions `stepK` and `rootP` with the thresholds
`theta τ`. ψ has variables below n and nonempty clauses of
at most k literals. There are at most Σ_{j ≤ kn/τ} C(bsum τ k · n, j) leaves, each with at most
leafC τ k · n clauses; ψ is satisfied exactly if some leaf is;
the stack of the walk never holds more than bsum τ k · n + 1 formulas, each with at most 2^k times
as many clauses as ψ. 

### `StCertStep`

 One step of the tree is computed in polynomial time. 
