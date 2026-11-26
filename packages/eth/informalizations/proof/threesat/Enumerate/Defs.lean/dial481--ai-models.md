---
{
  "module": "proof/threesat/Enumerate/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Enumerate/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Enumerate/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 4 as an enumeration (definitions and statements only)

Lemma 4 (cited from Impagliazzo, Paturi and Zane): «For every ε > 0 there is a constant M(ε) ≥ 1
such that for every 3-CNF φ on n variables one can compute deterministically, in time 2^{εn} times a
polynomial in n, at most 2^{εn} 3-CNFs on the same variables, each with at most M(ε)·n clauses, such
that an assignment satisfies φ if and only if it satisfies at least one of them, and no two of them
share a satisfying assignment.» Used here in the weaker form: φ is
satisfiable if and only if at least one of them is. The proof of Theorem 2 and line 2 of Algorithm 1
(«for each Φ in the list that Lemma 4 computes from φ and ε do») go through these formulas one after
the other.
This development has the lemma in two forms: `SparsificationLemma.Mach.LemSparsification` (as
worded: a Mathlib machine prints the list; no proof of Theorem 2 uses it) and
`SparsificationLemma.TreeWalk.lemSparsification_walk` (bounds for a walk that tests, at each leaf
(ψ, 𝒩), ψ and not the output ψ ∪ 𝒩); the statements `StSameTree` and `StNamedGives` below relate
them. The procedure is that of proof/sparsification/SparsificationLemma: nodes (ψ, 𝒩) with a side
list 𝒩 and outputs ψ ∪ 𝒩 as in Appendix C, but with the thresholds θ 0 = 1, θ i = 4·τ^(2i−1) instead
of Calabro's, and without Appendix C's first step (deleting the clauses that contain a variable and
its negation). The paper does not say which procedure computes the list of Lemma 4.
Here the lemma is read as an ENUMERATION: a depth-first walk through that tree, on a stack of
polynomial size, with polynomial-time moves, meets the leaves from left to right, and the formula
produced at a leaf is the output ψ ∪ 𝒩 (`SparsificationLemma.out`). `Enumerates ε M τ` says of the
parameter τ all that the lemma says of the list, clause by clause.
`StNamed` is the worded lemma with the list NAMED: one machine of Mathlib; for every ε there are
M(ε), s and c such that the machine prints, within 2^{εn}·c(n+1)^c steps, the code of the very list
that the walk with τ = `tauOf s` produces, and `Enumerates ε M(ε) (tauOf s)` holds. So the list of
the worded lemma and the formulas that
the deciding form of procedure #Sat of Algorithm 1 goes through are the same, in the same order.
Why an enumeration and not a stored list: in the model of step machines all states must have
polynomial size (`Groundwork.DecidesInSteps`), and a list of 2^{εn} formulas has not.
This file has no proofs. 

### `rule`

 The rule of the sparsification procedure at width 3 with parameter τ (thresholds θ 0 = 1, θ i =
4·τ^(2i−1)): the two children of a node (ψ, 𝒩), or nothing at a leaf. 

### `start`

 The root of the tree for a formula φ on n variables. (Its side list starts with the clauses xᵢ ∨
¬xᵢ, which `SparsificationLemma.out` drops again; the walk starts from this root, and the bounds on
its stack in the field `stack` of `Enumerates` are stated for it.) 

### `depth`

 Paths of the tree are cut after τ⁶·n steps. (For an enumeration no path is longer: field
`stops`.) 

### `produced`

 **The formulas Φ₁, Φ₂, … in the order in which the walk produces them**: the outputs ψ ∪ 𝒩 at
the leaves of the tree, from left to right. 

### `Enumerates`

 **Lemma 4 for the parameter τ, clause by clause**, for every 3-CNF φ on n variables (nonempty
clauses of at most 3 literals; a clause may be written twice here, and the bound on the stack is in
the number of clauses written; the statements that use this take inputs without repeated clauses). 

### `Enumerates.stops`

 the walk comes to an end: the procedure has stopped at every leaf 

### `Enumerates.few`

 «at most 2^{εn}» 

### `Enumerates.sparse`

 «3-CNFs on the same variables, each with at most M(ε)·n clauses»; no clause is written twice 

### `Enumerates.sat`

 φ is satisfiable if and only if at least one of them is (weaker than the paper's «an
  assignment satisfies φ if and only if it satisfies at least one of them») 

### `Enumerates.moves`

 «in time 2^{εn} times a polynomial in n», first half: the walk makes two moves for each
  formula that it produces (one less in all); this holds for every tree, and is a bound on the time
  only together with `few` 

### `Enumerates.rule_poly`

 second half: a move, and the passage from a leaf to its output, take polynomial time … 

### `Enumerates.stack`

 … in the size of the stack, which is polynomial: at most τ⁶·n + 1 nodes, each with at most
  8·|φ| + 2n clauses of at most 3 literals on the same variables 

### `StProducedIsList`

 The formulas that the walk produces are the list `SparsificationLemma.Geo.outTau 3 n τ φ`, which
the machine of `SparsificationLemma.Mach.Prints` prints. 

### `StSameTree`

 At each leaf the formula ψ that the walk of
`SparsificationLemma.TreeWalk.lemSparsification_walk` tests is the first component of the node whose
output ψ ∪ 𝒩 is produced here: the two walks go through the same tree. 

### `StEnumeratesTau`

 Lemma 4 as an enumeration, for every parameter that is large enough for ε: τ ≥ 24 and
(3/τ)·log₂(e·τ·τ⁶) ≤ ε. M = τ⁶. 

### `StEnumeration`

 **Lemma 4 as an enumeration.** «For every ε > 0 there is a constant M(ε) ≥ 1 such that …». 

### `StNamed`

 **Lemma 4 as worded, with the list named.** One machine of Mathlib for all ε. For every ε > 0
there are M(ε) ≥ 1, s and c such that the walk with the parameter τ = `tauOf s` is an enumeration
for ε and M(ε), and for every 3-CNF φ on n variables the machine, started on 1^s 0 1^3 0 code(φ),
prints the code of the list of the
formulas which that walk produces, in that order, within 2^{εn}·c(n+1)^c steps. 

### `StNamedOf`

 The worded lemma with the list named, from the machine that prints the list
(`SparsificationLemma.Mach.Prints`), from «what the walk produces is that list», and from the
enumeration for every parameter that is large enough. 

### `StNamedGives`

 The form with the list named gives the lemma as worded
(`SparsificationLemma.Mach.LemSparsification`) and the enumeration. 
