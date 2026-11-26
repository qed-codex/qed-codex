---
{
  "module": "proof/networks/Eight/ViaGrouping/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 1 along the printed proof: the program and the interfaces (definitions only)

The files of proof/networks/Eight/ViaGrouping/ hold the algorithm of the printed proof of Lemma 1,
for networks as Definition 2 prints them (passed to the form of the namespace `Paper` by
proof/networks/Eight/SecNetworks_LemGrouping.lean):
* «Go through all K^g groupings and fix the first good one», good as printed: (G1) every group has
  at most 2g/K nodes, (G2) Y_{γ,γ'} ≤ (U + gP/K)/K², with the P that the algorithm is given
  (`goodP`, `searchP`);
* L = max{1, ⌊(U + gP/K)/K²⌋} (`lamP`);
* the tables W̃_γ(Θ) = [all appended bits are 0]·Σ_{(z_a)} ∏ W_a(z_a) ∏ Ψ_{a,b}(z_a, z_b) ∏
  f_{a,b}(z_a, θ_{a,b}), each z_a ranging over S_a, computed with the four procedures of Definition
  2(iii) (`tableM`);
* «Run the algorithm for (K, e) with L, B' in the roles of λ, B … Answer each of its queries by
  computing the entry» (`netAlg`).
The plain functions that cut a setting of a group and a string Θ(γ') into their parts (`members`,
`zA`, `labOf`, `validB`, …) are those of proof/machines/StepMachines/Prog/NetProg.lean; they depend
only on the numbers P_a and c_{a,b}.

Different from the paper: the search goes on past the first good grouping (it runs through all K^g
and keeps the first), which the printed sentence allows but line 10 of Algorithm 1 does not do; a
string of P_a bits that is not a setting is met and gives the factor 0; the algorithm does not read
B:
the algorithm for cliques is not told B either, and its bound holds for every B that bounds the
entries. So `GiveP` leaves out «B is given», and the theorems of this folder ask less of the
procedures than Definition 2 does. On the other hand P, which the algorithm
does read, must be given in unary for the steps to take polynomial time (`KeepsP`).
This file has no proofs. 

 ## Definition 2(iii) without «B is given», and what Lemma 1 says of an algorithm 

### `GiveP`

 Definition 2(iii), all but one clause: in the context c the procedures give the numbers P, P_a,
c_{a,b} of N, decide membership in S_a for strings of P_a bits, and compute every value of W_a,
Ψ_{a,b}, f_{a,b}, each within τ steps on states of size at
most S. The clause left out: that they give B. 

### `IsNetworkP`

 Definition 2 with `GiveP` for (iii). Every network in the sense of `SecNetworks.IsNetwork` is
one in this sense. 

### `Correct`

 The bound of Lemma 1 for the algorithm NA, with the exponent ε·U + b·gP/K: one constant A (the
paper's C₁) such that NA outputs the value of every network on [g] with parameters P, B, τ and total
U within A·2^{εU + b·gP/K}·(P + B)^A·τ steps, on states
of size at most S + A·(size of the context + P + B)^A. Lemma 1 has ε = e and b = e + 2, since e·U +
(e + 2)·gP/K = e(U + gP/K) + 2gP/K. 

### `KeepsP`

 The procedures have polynomial-time steps (`SecNetworks.Procs.Keeps`), and the number P is given
in unary. The algorithm of the printed proof computes L = max{1, ⌊(KU + gP)/K³⌋} from P and gives it
to the algorithm for cliques, whose steps are known to take polynomial time only when λ is given in
unary. So P is asked to be given in unary too. 

### `AlgKeeps`

 The algorithm has polynomial-time steps whenever the procedures have and P is given in unary. 

 ## The program 

### `lamP`

 L = max{1, ⌊(U + gP/K)/K²⌋}, written max{1, ⌊(KU + gP)/K³⌋}, with the given P. 

### `goodP`

 Is the grouping number x good? (G1) K·|G_γ| ≤ 2g for every γ; (G2) K³·Y_{γ,γ'} ≤ K·U + g·P for
all γ ≠ γ'. 

### `qMb`

 The query (b, z_b), for the factor number i = a·g + b. 

### `qPsi`

 The query ((a, b), (z_a, z_b)) for Ψ_{a,b}, i = a·g + b. 

### `wM`

 [z_a ∈ S_a]·W_a(z_a). 

### `psiP`

 [z_a ∈ S_a][z_b ∈ S_b]·Ψ_{a,b}(z_a, z_b), by the procedure for Ψ. 

### `fM`

 [z_a ∈ S_a]·f_{a,b}(z_a, θ_{a,b}). 

### `termP`

 The factor number i = a·g + b of a term of W̃_γ(Θ): 1 if a is not in the group or b < a is in
it; the factor of W_a if b = a; of Ψ_{a,b} if b > a is in the group; of f_{a,b} if b is in another
group. 

### `tableM`

 One entry W̃_γ(Θ): 0 unless all appended bits are 0; else the sum, over all strings of Σ_{a ∈
G_γ} P_a bits, of the product of the g² factors. 

### `searchP`

 «Go through all K^g groupings and fix the first good one.» 

### `netAlg`

 **The algorithm of the proof of Lemma 1**: find the first good grouping, then run the algorithm
E for cliques on K nodes with L in the role of λ, answering each query by computing the entry of W̃.
The result is 0 if no grouping is good (which does not
happen for g = 3K⁸). 

 ## The steps of the proof, as statements 

### `StSearch`

 «A good grouping exists» and «fix the first good one»: for g = 3K⁸ the search finds a grouping x
< K^g, and it is good as printed (`SecNetworks.Good`). 

### `StTable`

 «So |W̃_γ| < 2^{B'} with B' = ⌈2gP/K⌉ + g²B, and one entry costs 2^{2gP/K}·poly(P + B)·τ
operations»: for a grouping with (G1) and Y_{γ,γ'} ≤ L ≤ 2gP, the procedure `tableM` answers every
query to the tables W̃ of the (K, L)-clique of the groups
(`Paper.groupedTables` of the network in the form of the namespace `Paper`;
`groupedTables_eq_display` in Display.lean writes them out as the display of the paper) within
c₁·2^{P·⌊2g/K⌋}·τ steps, on states of size at most S + c₁·(size c + P + B)^{c₁}; every entry is at
most
2^{P·⌊2g/K⌋ + g²B} in absolute value. The constant depends on K and g only. Here P·⌊2g/K⌋ ≤ 2gP/K;
the factor poly(P + B) of the paper is not needed, because steps are counted and a step may take
polynomial time (`StKeeps`); the sizes of the states are
bounded instead. 

### `StValue`

 «… so the value equals Z»: the (K, L)-clique with the tables W̃ has the value of the network. 

### `StKeeps`

 The algorithm has polynomial-time steps if E has. 

### `StLemGrouping`

 **Lemma 1 for the algorithm of its proof**: if E evaluates (K, λ)-cliques with the exponent e,
then `netAlg K (3K⁸) E` evaluates networks on [3K⁸] with the exponent e(U + gP/K) + 2gP/K. 

 ## From a network in the form of the namespace `Paper`, with a procedure for Ψ, to the data of Definition 2 

### `ofNetwork`

 A network in the form of the namespace `Paper`, read as the data of Definition 2: Ψ is the sum
that `Paper.Network` defines; `n` gives the lengths P_a. 

### `ofProcs`

 The procedures `Paper.NetworkProcedures`, with a function that gives P and a procedure Q for Ψ.
Every string of P_a bits is a setting, so the test for membership forgets the query and says yes. B
is not given (the entry is a dummy). 

### `StBridge`

 The bridge: a network in the form of the namespace `Paper` with parameters P, B, τ, together
with a procedure Q that computes its Ψ within τ steps, is a network in the sense of Definition 2
with parameters P, B + 1, τ («at most 2^B» gives «below 2^{B+1}»), with the same value and the same
total. 
