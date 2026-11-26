---
{
  "module": "proof/statements/GivenStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/GivenStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/GivenStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A «network on J with parameters P, B, τ», given by procedures: one definition (definitions and statements only)

Definition 2 of the paper, clause (iii): «an algorithm receives P, B and the numbers P_a, c_{a,b} as
input, and can decide membership in S_a and compute any value of W_a, Ψ_{a,b}, f_{a,b} with at most
τ operations.»
`Eight.SecNetworks.IsNetwork` (proof/networks/Eight/SecNetworks_Defs.lean) reads «at most τ
operations» as at most τ steps of four step machines. A step of a step machine is an arbitrary
function, so that definition alone bounds no cost; that the steps are computed in polynomial time,
and that the numbers are handed over in unary, are separate statements about the procedures.
Here the two are joined: `IsGivenNetwork` is Definition 2 with clause (iii) as one property. The two
sentences of the paper that say so of a network, «Both networks satisfy Definition 2 …» (proof of
Proposition 3) and «Definition 2 holds» (Section 6), are stated for it (`StGridGiven`,
`StFormulaGiven`), and Lemma 1 is applied to a network in this sense, with the number of operations
and the polynomial-time steps of the whole in one conclusion (`StOnGiven`).
proof/threesat/Given proves these three and from them proves Proposition 3, Section 8's sentence on
Clique(ℓ), «Cost» of Section 6 and Theorem 2, each in the form stated in the namespace `Printed`,
word for word.
This file has no proofs. 

### `PolyTimeProcs`

 What makes a step of the procedures an operation that costs something: the four numbers (P, B,
the P_a, the c_{a,b}) are computed from the context in unary in polynomial time, and each of the
four machines with query access has polynomial-time steps
(`QueryMachines.QueryMachine.PolyTimeSteps`: start, own step, result, the query asked and the taking
of its answer are computed in polynomial time in the length of the state, on Mathlib's Turing
machines).
The procedures do not know the oracle, so the polynomials do not depend on it. 

### `IsGivenNetwork`

 **Definition 2**, all clauses as one property: N is a network on [g] with parameters P, B, τ,
given by the procedures Np in the context c, where the procedures may query the oracle O.
First conjunct (`Eight.SecNetworks.IsNetwork` of the procedures with the oracle built in):
* «Let P, B, τ ≥ 1 be integers», the sets S_a ⊆ {0,1}^{P_a} with «one fixed length P_a ≤ P», the
  symmetry of Ψ and c, the factorization of Ψ_{a,b} through c_{a,b} bits, «(i) Σ_{b ∈ J∖{a}} c_{a,b}
  ≤ P for every a ∈ J», «(ii) all values of all W_a, Ψ_{a,b}, f_{a,b} are below 2^B in absolute
  value» (`Net.Is`, and 1 ≤ τ);
* (iii) «an algorithm receives P, B and the numbers P_a, c_{a,b} as input»: the procedures give
  these numbers in the context c; «and can decide membership in S_a and compute any value of W_a,
  Ψ_{a,b}, f_{a,b} with at most τ operations»: each of the four machines answers within τ steps when
  the oracle is built in, that is, within τ operations, an own step and a query to O each counted as
  one (`QueryMachines.StClose`), on states of size at most S.
Second conjunct (`PolyTimeProcs`): these operations are polynomial-time steps, uniformly in the
oracle, and the numbers are handed over in unary. With the bound S on the states this makes clause (iii)
a bound on cost: τ operations, each polynomial in S.
Not in the print: the bound S (the paper counts operations on words and bounds no memory), the
context c, and the oracle. A network may be given by procedures that themselves query something. For
Proposition 3 these are the tables of the larger clique; Section 8 says of the recursion: «a query
to W̃_γ is answered by evaluating the sum in Lemma 1, which in turn queries the tables one level
up». Procedures that are step machines are the case without queries (`ofProcs`, `noTable`). 

### `ofProcs`

 Procedures that are step machines, as procedures with query access that ask nothing. 

### `noTable`

 The oracle that answers nothing. 

### `StOnGiven`

 **Lemma 1, applied to a network given in this sense.** Let NM do what Lemma 1 says for (K, e) on
networks on [g] (`Printed.ComputesNetworks`: each query of Definition 2(iii) is charged τ
operations). On a network given by Np with the oracle O, the machine `networkOn g NM Np` (NM is
handed the numbers; each of its queries is answered by running the procedure, which may query O)
has polynomial-time steps if NM has, and outputs the value within 3·C₁·2^{e(U + gP/K) + 2gP/K}(P +
B)^{C₁}·τ operations, an own step and a query to O each counted as one. (The 3: a query of NM takes
the at most τ operations of the procedure and two more.) The count of operations holds for every NM,
so the hypothesis on the steps of NM stands where it is used. 

### `StGridGiven`

 **Proof of Proposition 3, «Two networks for each ι»: «Both networks satisfy Definition 2 with P =
g³λ (so gP = N), with B₁ = gB + g²λ + 1 in the role of B, and with τ = poly(B + λ)».** For g ≥ 1
there is a constant a such that, for every context c that holds λ ≥ 1 and B in unary, all tables
with |W_w| < 2^B of the clique on g² nodes and every y < (t + 1)^{|ℛ|}: the network
`levelNetP g tr λ y` (tr = false: rows; tr = true: columns) is a network with parameters g³λ, B₁,
a·(B + λ)^a,
given by `Printed.gridProcs g tr` in the context (c, y) with query access to the tables. 

### `StFormulaGiven`

 **Section 6, «Definition 2 holds»**, of the network of Φ on g clusters: with P = max{1, 2k·m̄},
B = 1 and τ = 1, given by `Printed.formulaProcs g k`, step machines that ask nothing. 
