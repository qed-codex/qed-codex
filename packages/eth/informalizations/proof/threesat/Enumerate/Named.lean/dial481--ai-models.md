---
{
  "module": "proof/threesat/Enumerate/Named.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Enumerate/Named.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Enumerate/Named.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 4 as worded, with the list named: proofs

Lemma 4 (cited): for every ε > 0 there is a constant M(ε) ≥ 1 such that for every 3-CNF φ on n
variables one can compute, in time 2^{εn} times a polynomial in n, at most 2^{εn} 3-CNFs on the same
variables, each with at most M(ε)·n clauses, such that φ is satisfiable if and only if at least one
of them is (the paper's Lemma 4 states more: every satisfying assignment of φ satisfies exactly one
of them). Line 2 of Algorithm 1: «for each Φ in the list that Lemma 4 computes from φ and ε do».
This file proves `StNamedOf`, `StNamed` and `StNamedGives` of proof/threesat/Enumerate/Defs.lean.
Below, the walk with parameter τ is the sparsification procedure of this development run on φ with
the parameter τ, and `produced τ n φ` is the list of the formulas that it produces, in its order.
`import all UniformInK.Top.Leaves`: the lemma `UniformInK.Leaves.tauOf_worksU` (τ = 2^(4s+17) is
large enough for ε = 1/2^s) is not public in that module.
`stNamedOf` follows proof/sparsification/SparsificationLemma/Mach/Full.lean and
Mach/LemSparsification.lean, but keeps the list named. The machine and its constant C₀ are those of
`SparsificationLemma.Mach.Prints`. Given ε > 0 take a rational q with 0 < q < min(ε, 1) and the
precision s = `precE (C₀ + 1) 3 q`, so that s ≥ `s0U 3` and (C₀ + 1)/ε ≤ (C₀ + 1)/q ≤ 2^s.
* The parameter τ = `tauOf s` = 2^(4s+17) is large enough for ε: τ ≥ 24, and (3/τ)·log₂(e·τ·τ⁶) ≤
  1/2^s ≤ ε (`enumerates_tauOf`). So the hypothesis `StEnumeratesTau` gives `Enumerates ε (τ⁶) τ`;
  M(ε) = τ⁶.
* The machine prints the code of `outTau 3 n τ φ`, which by the hypothesis `StProducedIsList` is the
  list that the walk produces.
* The time: C₀·(length of the input + 8)^C₀ ≤ c·(n+1)^c with c = C₀·(s+412)^C₀ + 4C₀, and C₀·⌊n/2^s⌋
  ≤ εn (`time_le_poly`).
`stNamedGives` unpacks: the list of the worded lemma `SparsificationLemma.Mach.LemSparsification` is
the list that the walk produces, and what the lemma says of it are the fields `few`, `sparse` and
`sat` of `Enumerates`. 

### `enumerates_tauOf`

 The parameter τ = 2^(4s+17) is large enough for ε as soon as s ≥ `s0U 3` and C/ε ≤ 2^s for some
C ≥ 1; so, by the enumeration for every parameter that is large enough, the walk with this parameter
is an enumeration for ε with M(ε) = τ⁶. (Lemma 4: «For every ε > 0 there is a constant M(ε) ≥ 1 such
that …».) 

### `time_le_poly`

 «in time 2^{εn} times a polynomial in n»: the bound C₀·(length of the input + 8)^C₀·2^(C₀·⌊n/2^s⌋)
of the machine is at most 2^{εn}·c(n+1)^c with c = C₀·(s+412)^C₀ + 4C₀, if C₀ ≤ C and C/ε ≤ 2^s. 

### `stNamedOf`

 **Lemma 4 as worded, with the list named, from its three parts**: the machine that prints the
list, «what the walk produces is that list», and the enumeration for every parameter that is large
enough: for every ε > 0 a constant M(ε) ≥ 1 and, for every 3-CNF φ on n variables, at most 2^{εn}
3-CNFs on the same variables, computed in time 2^{εn} times a polynomial in n, … 

### `stNamed`

 **Lemma 4 as worded, with the list named.** One machine of Mathlib for all ε; for every ε > 0 it
prints, «in time 2^{εn} times a polynomial in n», the code of the list of the formulas which the
walk with the parameter 2^(4s+17), s = s(ε), produces, in that order; and that walk is an
enumeration for ε and M(ε). 

### `stNamedGives`

 The form with the list named gives the lemma as worded, in its deciding form (at most 2^{εn}
3-CNFs on the same variables, computed in time 2^{εn} times a polynomial in n, each with at most
M(ε)·n clauses, such that φ is satisfiable if and only if at least one of them is), and the
enumeration. 
