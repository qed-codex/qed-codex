---
{
  "module": "proof/sparsification/StepSparsify/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 5 of Appendix D for any thresholds that serve: definitions and statements

Step 5 of Appendix D sparsifies with Calabro's thresholds, and the paper remarks that any
sparsification with few outputs, few occurrences of a variable and no satisfying assignment
shared by two outputs gives the same bound. This file is about one procedure (`stepC`, with its side
list), run with a family of thresholds Θ k s (width k, precision s, with 2^(−s) in the role of ε).
`Serves Θ Lc` says what Step 5 takes from such a family: at most 2^(⌊n/2^s⌋+1) leaves, at most Lc k
s occurrences of a variable at a leaf, the count as the sum over the leaves, and polynomial time.
Calabro's thresholds are such a family (`StServesCal`).
This is a special case of the remark, with fixed constants, not the remark itself.
The counting tree is walked depth first, one round for each unit of a pad (`walkSG`); the clauses
that contain a variable together with its negation are deleted first, as in the paper. Unlike in the
paper, the side list of the walk starts
with the n clauses xᵢ ∨ ¬xᵢ (`rootC`), which the count of a leaf leaves out again (`leafM`); the
outputs are the same (`SparsificationLemma.StOutputsSame`).
Calabro's thresholds are `SparsificationLemma.Cal.thetaC α` with α =
`SparsificationLemma.Cal.alphaC (max k 3) (1/2^s)`. The procedure runs with the width k; only α is
taken for K = max(k, 3), because the
bound on the number of leaves needs x = 32(K−1)²/ε ≥ 128. The paper runs the procedure with the
width max(k, 3), where k is the largest number of literals in a clause. On a k-CNF the two runs
should make the same steps, since no clause has more
than k literals, but this is not proved here.
This file has definitions only; each `St…` here is a proposition, and none is proved in this file. 

 ### What Step 5 takes from the sparsification 

### `Serves`

 The family of thresholds Θ k s, with the bound Lc k s on the occurrences of a variable, serves
for Step 5. 

### `Serves.tree`

 The tree for width k ≥ 1 and precision s ≥ `s0U k`, of a k-CNF in which no clause contains a
  variable together with its negation: what `UniformInK.StTreeU` says, with 2^(⌊n/2^s⌋+1) for the
  number of leaves and Lc k s for the occurrences. 

### `Serves.par`

 The bound on the occurrences, plus 2, is at most 2^(betaU k s) = 2^(2k(4s+17)). 

### `Serves.cert`

 The two children of a node are polynomial-time jointly in k, s and the node, if k, 2^k and s
  are given in unary. 

 ### The walk 

### `walkSG`

 The depth-first walk of the counting tree for width k with the thresholds θ, one round for each
unit of the pad. 

 ### The statements 

### `StWalkSG`

 If the procedure has stopped at every node that is listed when the paths are cut after d steps,
the pad has at least 2·(number of these nodes) − 1 units and the word of every state of the walk
fits under the pad, then `walkSG` returns the sum of the
values of these nodes. 

### `StWalkCountG`

 If `val` is right on every node that has the properties of a leaf, and the pad suffices for the
rounds and for the stack, the walk returns the number of satisfying assignments. 

### `StCertWalkSG`

 The summing walk is polynomial-time in the pad, jointly in the width k and the precision s, if
k, 2^k and s are given in unary. 

### `StCertNoTaut`

 Deleting the clauses that contain a variable together with its negation is polynomial-time. 

 ### Calabro's thresholds 

### `alphaS`

 Calabro's α for max(k, 3) in the place of k, and ε = 2^(−s). 

### `thCal`

 Calabro's thresholds with this α. 

### `lcCal`

 Their bound on the occurrences: 2·(θ₀ + … + θ_{k−1}). 

### `StAlphaS`

 α without fractions: with K = max(k, 3), α = 2(K−1)²·2^s·⌈log₂(32(K−1)²·2^s)⌉. 

### `StCalNumbers`

 Calabro's numbers fit the bounds of the plan, for k ≥ 1 and s ≥ `s0U k`: 1 ≤ α and k² ≤ α; β₁ +
… + β_{k−1} ≤ τ^(2k) for τ = 2^(4s+17); 2·(θ₀ + … + θ_{k−1}) + 2 ≤ 2^(2k(4s+17)). 

### `StCalLeaves`

 The tree with Calabro's thresholds has at most 2^(⌊n/2^s⌋+1) leaves, wherever the paths are cut,
as long as D ≥ (β₁ + … + β_{k−1})·n (no path is longer, so the tree is the same for all these D). 

### `StCertThCal`

 Calabro's thresholds are polynomial-time, jointly in k, s and the index, all given in unary. 

### `StServesCal`

 Calabro's thresholds serve. 
