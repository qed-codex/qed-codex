---
{
  "module": "proof/statements/PrintedStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/PrintedStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/PrintedStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «Achievable» (Definition 4 with a bound on the sizes of the states added), and what the paper derives from it and for it (definitions and statements only)

Definition 4 of the paper: for an integer K ≥ 2 and a real e ≥ 0, the pair (K, e) is achievable if
there are an algorithm and a constant C, both depending only on K and e, such that for all integers
λ, B ≥ 1 and all tables with |W_w| < 2^B the algorithm, given λ, B and query access,
outputs the value of the (K, λ)-clique within C·2^{eK²λ}(B + λ)^C operations. Definition 3: the
tables are not written out; an algorithm queries them by naming w and z_w ∈ S_w, and receives
W_w(z_w) at the cost of one operation.
Here the algorithm is a machine with query access (`QueryMachines.QueryMachine`); its input is the
pair (λ, B); a query is a pair (w, z_w); operations are its own steps and its queries, each counted
once; the value is that of the network of Definition 3 (`Eight.SecNetworks.clique`).
Lemma 1 and Proposition 3 are stated FROM this definition and (Proposition 3) FOR it.

What remains of the model: (1) an own step is any function computed in polynomial time in the length
of the state (`PolyTimeSteps`), not an operation on words; (2) λ and B, and the numbers of a
network, are handed over in unary, as lists of that many units: the bounds are polynomial in B + λ,
and P + B, anyway;
(3) different from the printed Definition 4, which bounds no memory: all states have size at most
    C·(B + λ)^C. So `Achievable K e` says that (K, e) is achievable by an algorithm with polynomial
    memory. It implies the printed property (a state of that size is read and rewritten in poly(B +
    λ) operations on words; an argument outside Lean), but the converse is not claimed.
Lemma 1 and Proposition 3 are stated for this property; the algorithms of their printed proofs keep
their memory polynomial (Algorithm 1, line 11: the tables W̃ are «not stored; computed when
queried»), which is why they can be proved of it. Some bound is needed in this model (see
`AchievedBy`); (4) nodes are numbered from 0, and bit strings are lists. This file has no proofs. 

### `unary`

 The number n in unary: a list of n units. 

 ## Definition 3: query access to the tables of a clique 

### `TableQuery`

 A query to the tables of a clique names w and z_w; z_w is the concatenation of its K − 1 strings
of λ bits, as in Definition 3. 

### `tables`

 Query access to the tables W_0, …, W_{K−1} of a (K, λ)-clique: the query (w, z) is answered by
W_w(z) if w < K and z ∈ S_w, that is, z has (K − 1)λ bits; no other query is answered. 

 ## Definition 4 

### `AchievedBy`

 The machine M and the constant Cc do what Definition 4 asks for the pair (K, e): for all λ, B ≥
1 and all tables with |W_w| < 2^B, the machine, given λ, B and query access to the tables, outputs
the value of the (K, λ)-clique, and the number of its own steps plus the number of its queries is at
most
Cc·2^{eK²λ}(B + λ)^Cc. All its states have size at most Cc·(B + λ)^Cc.
The bound on the sizes of the states is NOT in the printed definition. It makes this definition
stronger than the printed one: achievable here implies achievable as printed; the converse is not
claimed (an algorithm that meets the printed bound only with more than polynomial memory is not
covered). Every algorithm of the paper meets it. In this model it cannot be left out: since an own
step may be any function computed in polynomial time in the length of the state, a machine without
it could ask for all K·2^{(K−1)λ} entries, keep them, and then do all the work in one step (the
state then has length at least K·2^{(K−1)λ}, and 2^{λK(K−1)/2} = (2^{(K−1)λ})^{K/2} is at most the
(K/2)-th power of that length, so the brute-force sum is polynomial in the length of the state, with
a degree that depends on K only). That machine would take about K·2^{(K−1)λ} operations, so (K, (K − 1)/K²)
would be achievable for every K and e* = 0 would hold with none of the paper's argument. 

### `Achievable`

 **Definition 4.** The pair (K, e) is achievable. 

### `StMono`

 «If (K, e) is achievable, so is (K, e₁) for every e₁ ≥ e.» 

### `eStar`

 «Define e* as the infimum of all e such that (K, e) is achievable for infinitely many K.» 

### `StHalf`

 «Trying all 2^{λK(K−1)/2} choices of one string per edge shows that (K, ½) is achievable for
every K, so e* ≤ ½.» 

### `StAnswerEachQuery`

 The step that the proof of Lemma 1 makes with Definition 4 («Answer each of its at most
C·2^{eK²L}(B' + L)^C queries by computing the entry»), for any way of computing the entries: the
machine asks at most Cc·2^{eK²λ}(B + λ)^Cc queries; and if a step machine R computes each entry
within t ≥ 1 steps
(c is whatever R needs to know), then M with its queries answered by R outputs the value within
3·Cc·2^{eK²λ}(B + λ)^Cc·t steps. 

 ## Definition 2(iii): what an algorithm is given of a network 

### `NetQuery`

 A query to a network: is z ∈ S_a? (first summand: (a, z)); W_a(z) (second: (a, z)); Ψ_{a,b}(z,
z') (third: ((a, b), (z, z'))); f_{a,b}(z, θ) (fourth: ((a, b), (z, θ))). 

### `netOracle`

 Definition 2(iii), «can decide membership in S_a and compute any value of W_a, Ψ_{a,b},
f_{a,b}»: membership is answered (1 for yes, 0 for no) for strings of P_a bits; W_a on S_a; Ψ_{a,b}
on S_a × S_b and f_{a,b} on S_a × {0,1}^{c_{a,b}}, for a ≠ b. No other query is answered. 

### `NetInput`

 Definition 2(iii), «an algorithm receives P, B and the numbers P_a, c_{a,b} as input»: ((P, B),
((P_a)_a, (c_{a,b})_{a,b})), all in unary. 

### `netInput`

 The input that belongs to the network N with the parameters P, B. (The place (a, a) of the last
table holds 0.) 

 ## Lemma 1 

### `ComputesNetworks`

 The machine NM and the constant C₁ do what Lemma 1 says for (K, e) on networks on [g]: for every
network with parameters P, B, τ (`Net.Is` is Definition 2 up to (ii); (iii) is the input, the query
access, and the price τ of a query) and total U, the machine outputs the value within
C₁·2^{e(U + gP/K) + 2gP/K}(P + B)^{C₁}·τ operations, where each decision of membership and each
value of W_a, Ψ_{a,b}, f_{a,b} costs τ operations. Added to the print, as in `AchievedBy`: all
states have size at most C₁·(P + B)^{C₁}. This makes the conclusion stronger than the printed one (a
machine that meets the printed bound only with more memory does not satisfy it). Since
`GroupingLemma` also assumes `Achievable`, which carries the same kind of bound,
the Lean Lemma 1 is Lemma 1 for algorithms with polynomial memory, in its hypothesis and in its
conclusion. The bound cannot be left out here either: without it a machine could ask for every value
of every W_a and Ψ_{a,b} and then do all the rest in one step. 

### `GroupingLemma`

 **Lemma 1.** «Let (K, e) be achievable and g = 3K⁸. There is a constant C₁ = C₁(K, e) such that
the value of every network on [g] with parameters P, B, τ and total U is computed within C₁·2^{e(U +
gP/K) + 2gP/K}(P + B)^{C₁}·τ operations.» One machine, fixed before the network. 

 ## Proposition 3 

### `LevelProposition`

 **Proposition 3**, first sentence. «If (K, e) is achievable and g = 3K⁸, then (g², e') is
achievable for e' = (ρ + 2/K)e + 2/K.» ρ = 11/12 (`Eight.rho`). 

### `EStarZero`

 **Proposition 3**, second sentence. «Hence e* = 0.» 

### `StEveryEta`

 The end of the proof of Proposition 3: «That is, for every η > 0, (K, η) is achievable for
infinitely many K.» (This is the form that Section 6 uses. `EStarZero` alone would also hold if no
pair were achievable, since the infimum of the empty set of reals is 0 in Mathlib; with `StHalf` it
says what it should.) 
