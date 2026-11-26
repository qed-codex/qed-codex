---
{
  "module": "proof/threesat/Enumerate/Enumeration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Enumerate/Enumeration.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Enumerate/Enumeration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 4 as an enumeration: proofs

Lemma 4 (cited): for every ε > 0 there is a constant M(ε) ≥ 1 such that for every 3-CNF φ on n
variables one can compute, in time 2^{εn} times a polynomial in n, at most 2^{εn} 3-CNFs on the same
variables, each with at most M(ε)·n clauses, such that φ is satisfiable if and only if at least one
of them is (the paper's Lemma 4 states more: every satisfying assignment of φ satisfies exactly one
of them).
This file proves four statements of proof/threesat/Enumerate/Defs.lean.
* `stProducedIsList`: the formulas that the walk produces are the list
  `SparsificationLemma.Geo.outTau 3 n τ φ` (from `SparsificationLemma.stOutputsSame`: the clauses xᵢ
  ∨ ¬xᵢ with which the side list of the root starts do not reach an output).
* `stSameTree`: the first components of the nodes are the nodes of the procedure without side lists
  (from `SparsificationLemma.stUnchanged`: the rule never looks at the side list).
* `stEnumeratesTau`: the structure `Enumerates ε (τ⁶) τ`, clause by clause of the lemma, for τ ≥ 24
  with (3/τ)·log₂(e·τ·τ⁶) ≤ ε. The number of formulas, their form and «satisfiable if and only if»
  come from the theorem on sparsification `SparsificationLemma.Geo.stThmTau` at width 3, said of the
  list and carried over by `stProducedIsList`; that the walk ends, and the size of its stack, come
  from `SparsificationLemma.stTreeG`, the statement on the tree; the number of moves is
  `Groundwork.Stepped.length_visits`; the two functions are polynomial-time by
  `CountKSat.Poly.certStepC` and `CountKSatRate.Cert.leafM_polyT`.
* `stEnumeration`: for every ε > 0, with τ = ⌈(24/q)³⌉ for a rational q with 0 < q < min(ε, 1)
  (`SparsificationLemma.Geo.stTauE`), and M(ε) = τ⁶. 

### `stProducedIsList`

 Line 2 of Algorithm 1: «for each Φ in the list that Lemma 4 computes from φ and ε do». The
formulas that the walk produces, in its order, are the list `outTau 3 n τ φ`. 

### `stSameTree`

 The walk that produces the outputs ψ ∪ 𝒩 and the walk of
`SparsificationLemma.TreeWalk.lemSparsification_walk`, which tests ψ, go through the same tree: the
rule never looks at the side list 𝒩 (`SparsificationLemma.stUnchanged`). This ties the enumeration
to the form of Lemma 4 that `SparsificationLemma.TreeWalk.lemSparsification_walk` treats; no
sentence of the paper corresponds to it. 

### `out_polyT`

 The passage from a leaf (ψ, 𝒩) to its output ψ ∪ 𝒩 takes polynomial time. (Lemma 4: «in time
2^{εn} times a polynomial in n».) 

### `stops_and_stack`

 What `SparsificationLemma.stTreeG` says of the tree that the walk goes through, for τ ≥ 24: the
procedure has stopped at every leaf, and the stack is small. (Lemma 4: time 2^{εn} times a
polynomial in n.) 

### `sat_iff_of_exactlyOne`

 φ is satisfiable if and only if at least one of them is, from the property that every assignment
that satisfies φ satisfies exactly one formula of the list, and no other assignment any. 

### `stEnumeratesTau`

 **Lemma 4 as an enumeration, for every parameter that is large enough for ε**: in time 2^{εn}
times a polynomial in n, at most 2^{εn} 3-CNFs on the same variables, each with at most M(ε)·n
clauses, such that φ is satisfiable if and only if at least one of them is, with M(ε) = τ⁶. 

### `stEnumeration`

 **Lemma 4 as an enumeration.** For every ε > 0 there is a constant M(ε) ≥ 1 such that for every
3-CNF φ on n variables one can compute, in time 2^{εn} times a polynomial in n, at most 2^{εn}
3-CNFs on the same variables, each with at most M(ε)·n clauses, such that φ is satisfiable if and
only if at least one of them is (the paper's Lemma 4 states more: every satisfying assignment of φ
satisfies exactly one of them). 
