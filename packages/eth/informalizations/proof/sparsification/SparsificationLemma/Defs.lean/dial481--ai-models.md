---
{
  "module": "proof/sparsification/SparsificationLemma/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Sparsification that preserves the number of satisfying assignments: objects and general statements

The procedure is the one of proof/consequences/CountKSat/Defs.lean (`stepC`): a node is a pair (ψ,
𝒩) of the formula that the branching rule looks at and a side list of clauses that the rule never
looks at.
The rule (`pickK` in proof/sparsification/SparsifyWidthK/DefsProg.lean; `Rule` in
proof/sparsification/SparsifyWidthK/Defs.lean on finite sets) looks for a set H of literals, 1 ≤ |H|
< c ≤ k, that lies in at least θ(c − |H|) clauses of size c; it takes the smallest such c,
then a largest such H. The first child gets the clause H; the second child gets the clauses E ∖ H
for the clauses E of size c that contain H, and on its side list the clause {¬ω} for every ω ∈ H. In
each child the clauses that contain a new clause are deleted (`addP`); since the parent had no
clause that contains another clause, neither has the child.
Here the side list is empty at the start, as in Appendix C, and the output at a leaf is the side
list followed by ψ, with every clause written once (`out`). As a set of clauses this is ψ ∪ 𝒩.
Everything in this file holds for arbitrary thresholds θ, or for all thresholds that satisfy the
four conditions `ThrC`. Two families used here satisfy them: θ 0 = 1, θ i = 4·τ^(2i−1), if 1 ≤ k and
8k ≤ τ
(proof/sparsification/UniformInK/Spars/Defs.lean; proof/sparsification/SparsificationLemma/Geo), and
the thresholds of Calabro's dissertation with any α ≥ 1
(proof/sparsification/SparsificationLemma/Cal).
This file has definitions only. The statements `St…` are propositions; they are proved in other
files. 

 ### Formulas and assignments 

### `IsKCNF`

 ψ is a k-CNF on the variables x₀, …, xₙ₋₁: every clause is nonempty and has at most k literals. 

### `Sat`

 The assignment b satisfies ψ: it makes a literal of every clause true. 

### `ExactlyOne`

 If b satisfies ψ, it satisfies exactly one formula of the list Φ (exactly one position of the
list); otherwise it satisfies none. 

### `occN`

 The number of clauses of ψ in which the variable v occurs. 

### `noTaut`

 ψ without the clauses that contain a variable together with its negation. 

 ### The tree and the outputs 

### `root`

 The root: ψ without the clauses that contain another clause (`rootP` also writes every clause
once, with its literals in a fixed order and without repetitions), and the empty side list. 

### `tree`

 The leaves of the tree of the procedure with thresholds θ and width k, from left to right. Every
path is cut after D steps, whether or not the procedure has stopped there; `StGen` says that for D
large enough it has stopped everywhere. 

### `out`

 The output at a node: the side clauses of one literal and the clauses of the formula, every
clause written once. (`leafM` writes every side clause once; a clause of one literal can also stand
in the formula.) 

### `outputs`

 The outputs: at every leaf, the formula together with the side list. 

 ### «Exactly one output», and further properties of the tree and the outputs 

### `StExactlyOne`

 Every assignment that satisfies ψ satisfies exactly one output, and every other assignment
satisfies none. This holds for all thresholds and wherever the paths are cut. 

### `StCountOfExactlyOne`

 If every assignment satisfies exactly one formula of Φ or none, according to whether it
satisfies ψ, then the number of satisfying assignments of ψ on n variables is the sum of those of
the formulas of Φ. 

### `StSide`

 No choice depends on the side list: the tree that starts with the side list X has the same first
components, and X behind every side list. 

### `StUnchanged`

 The first components of the nodes are the nodes of the unchanged procedure `stepK`. 

### `StOutputsSame`

 The outputs are those of the tree of proof/consequences/CountKSat/Defs.lean, whose side list
starts with the n clauses xᵢ ∨ ¬xᵢ. 

### `StNodup`

 No output has a clause twice. 

### `StLenOfOcc`

 Since every clause has a variable, a k-CNF on n variables in which every variable occurs in at
most Δ clauses has at most Δ·n clauses. 

### `StNoTaut`

 Deleting the clauses that contain a variable together with its negation changes neither the
satisfying assignments nor the property of being a k-CNF, and afterwards no clause contains a
variable together with its negation. 

 ### The conditions on the thresholds, and the counts along a path 

### `ThrC`

 What the counts need of thresholds θ and numbers β for width k. At most β i · n clauses of size
i < k are added along a path; a step that adds clauses E ∖ H of size r adds at least θ r ≥ τ · β r
of them.
It differs from `UniformInK.ThrU` at size 1 only, where it asks for 2 ≤ β 1: there are only 2n
clauses with one literal. 

### `StThrOfU`

 The conditions `ThrU` together with 2 ≤ β 1 imply the conditions `ThrC`. 

### `StBoundC`

 A path has at most (β 0 + … + β (k-1))·n steps, and its steps to a second child use at most
(k−1)·n units, τ each. U is a set of at most 2n literals that contains every clause of φ. 

### `StIfaceC`

 All that the walk of the tree needs to know about the rule on finite sets, for thresholds with
`ThrC`. 

 ### The general theorem 

### `StGen`

 The sparsification for thresholds with `ThrC`, τ ≥ 1, and D ≥ (β 0 + … + β (k-1))·n. No path has
more than D steps (the procedure has stopped at every node of `tree`);
there are at most Σ_{j ≤ (k−1)n/τ} C(D, j) outputs; every output is a k-CNF on the same variables,
in which a variable occurs in at most 2·(θ 0 + … + θ (k-1)) + 2 clauses;
the formula at a node that is listed has at most as many clauses as ψ. 

### `StTreeG`

 What `UniformInK.StTreeU` says of the thresholds `thetaU τ`, for all thresholds with `ThrC` and
k² ≤ τ, with (k−1)·n in place of k·n. The identity of the counts is derived from `StExactlyOne`. 
