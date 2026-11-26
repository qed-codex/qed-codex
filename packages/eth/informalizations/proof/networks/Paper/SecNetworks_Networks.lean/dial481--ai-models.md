---
{
  "module": "proof/networks/Paper/SecNetworks_Networks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecNetworks_Networks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecNetworks_Networks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 3 of the paper: networks, cliques, achievable pairs, and the grouping in the proof of Lemma 1

Definition 1 (factoring through c bits) is in `Paper/SecNetworks_DefFactor.lean`. 

 ### Networks: the general problem, a sum of products over pairs of nodes 

### `Network`

 A network on the node set `J` (as in Definition 2): for each node `a` a finite set `S a` of
settings and a function `W a`; for each pair
of nodes the number `c a b` of shared bits and the two factors `f a b`, `f b a`.
Differences from the paper: Ψ is not given separately but *defined* from its factorization
(`Network.Ψ`), and θ ranges over a finite
set `N.lab a b` of labels, which Definition 2 below requires to be {0,1}^{c a b}. 

### `Psi_def`

 Ψ_ab(z, z') = Σ_θ f_ab(z, θ) · f_ba(z', θ) (Definition 2). 

 ### Definition 2: a network with parameters P, B, τ 

### `NetworkProcedures`

 A network given to an algorithm: procedures (step machines) that compute the values of W and f,
and the numbers P_a
(`n`) and c_ab (`cap`). All of them may depend on a context `c : C`, which stands for whatever the
calling algorithm holds in memory. 

### `IsNetwork`

 **Definition 2.** `N` is a network on [g] with parameters P, B, τ, given by the procedures `Np`
in the context `c`.
* `sized`: |S_a| ≤ 2^P; c_ab = c_ba; (i) Σ_{b ≠ a} c_ab ≤ P; at most 2^{c_ab} labels θ for the pair
  {a,b}; (ii) all values of W, Ψ, f
  are at most 2^B in absolute value (the paper: below 2^B).
* `presented`: (iii) S_a = {0,1}^{P_a}, θ ranges over {0,1}^{c_ab}, and every value of W and f is
  computed within τ steps on states
  of size at most `S`.
Differences from the paper: S_a is all of {0,1}^{P_a} (a string that is not a setting gets W = 0
instead of a membership test);
there is no procedure for Ψ (Ψ is computed from f); the algorithm is given the numbers P_a and c_ab
but not P
and B; and a bound `S` on the size of the states is carried along, which is needed to turn steps
into time. 

 ### Definition 3: the (K, λ)-clique 

### `Tables`

 The tables W_1, …, W_K of a clique on K nodes: `W w Θ` is the entry of the table of node `w` at
the setting `Θ`, which gives
for every other node `w'` the string on the edge {w, w'} (and the empty string at `w` itself). 

### `cliqueValue`

 **Definition 3**, the value of the (K, λ)-clique with tables `W`: the sum, over all choices of
one string of λ bits per edge, of
the product of the K table entries. Here the two copies of the string on an edge
have already been identified, as in the remark after Definition 3. The clique as a network (two
copies of each string, Ψ an equality test) is not used in this file. 

 ### Definition 4: achievable pairs 

### `CliqueAlgorithm`

 An algorithm for cliques: given λ and a procedure that answers table queries, a step machine
that returns an integer. 

### `CliqueAlgorithm.Within`

 The bound of Definition 4 for the algorithm `E`: there is a constant `A` (the paper's C) such
that for all λ ≥ 1, all B ≥ 0 and all
tables with entries at most 2^B in absolute value, `E` returns the value of the (K, λ)-clique within
A · 2^{e K² λ} · (B + λ)^A · t steps, where
`t` is the cost of one query; all states have size at most S + A · (size of the context + B + λ)^A. 

### `CliqueAlgorithm.PolyTimeSteps`

 The steps of the algorithm `E` are polynomial time, provided that λ is given in unary and the
steps of the procedure that
answers the queries are polynomial time. 

### `Achievable`

 **Definition 4.** The pair (K, e) is achievable: some algorithm with polynomial-time steps
computes the value of every
(K, λ)-clique within C · 2^{e K² λ} · (B + λ)^C steps, times the cost of a query.
Differences from the paper: steps with polynomial-time cost instead of operations; a query costs `t`
steps and the
bound has the factor `t`; entries are at most 2^B, not below 2^B; the algorithm is not given B, and
B = 0 is allowed; there is also
a bound on the size of the states (see `CliqueAlgorithm.Within`); K ≥ 2 and e ≥ 0 are not part of
the definition. 

### `Achievable.mono`

 "If (K, e) is achievable, so is (K, e₁) for every e₁ ≥ e" (after Definition 4). 

### `achievable_half`

 "Trying all 2^{λK(K-1)/2} choices of one string per edge shows that (K, 1/2) is achievable for
every K" (after
Definition 4). 

### `eStar`

 e*: "the infimum of all e such that (K, e) is achievable for infinitely many K" (after
Definition 4). The condition e ≥ 0, which
the paper puts into Definition 4, is put here. "For infinitely many K" is written as: for every K₀
there is such a K ≥ K₀. 

### `eStar_nonneg`

 0 ≤ e*. 

 ### Lemma 1 

 #### The length L of the groups 

### `groupedLength`

 L = max{1, ⌊(U + gP/K)/K²⌋}, written as max{1, ⌊(KU + gP)/K³⌋}. 

### `groupedLength_le`

 "K²L ≤ K² + U + gP/K" (multiplied by K). 

 #### "The algorithm" 

### `grouping`

 The grouping number x, for x < K^g: the digits of x in base K. 

### `groupedTables`

 The tables W̃_γ of the (K, L)-clique whose nodes are the groups of the grouping number x:
W̃_γ(Θ) = [all appended bits are 0] · Σ_{(z_a), a ∈ G_γ} ∏_{a ∈ G_γ} W_a(z_a) ∏_{{a,b} ⊆ G_γ}
Ψ_ab(z_a, z_b) ∏_{a ∈ G_γ, b ∉ G_γ} f_ab(z_a, θ_ab).
In two steps: `merge` makes each group one node, `toInst` sums over the settings of that node and
cuts Θ into its blocks. 

### `grouped_value`

 "… so the value equals Z": the (K, L)-clique with the tables W̃ has the value of the network. 
