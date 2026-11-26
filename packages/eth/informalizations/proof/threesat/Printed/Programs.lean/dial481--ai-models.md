---
{
  "module": "proof/threesat/Printed/Programs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Programs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Programs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The algorithms of the proofs, as machines with query access, and what is proved of them (definitions and statements only)

PrintedStatement.lean states Definition 4, Lemma 1 and Proposition 3 in the paper's words: «there
are an algorithm and a constant». A statement of that form reads the same whichever way it was
proved. This file names the algorithms of the printed proofs and states each step for the named
algorithm:
* `bruteMachine K`: «Trying all 2^{λK(K−1)/2} choices of one string per edge» (after Definition 4);
* `groupingMachine K g M`: the algorithm of the proof of Lemma 1, made from ANY machine M for
  cliques on K nodes: find the first good grouping; L; B' = ⌈2gP/K⌉ + g²B; «Run the algorithm for
  (K, e) with L, B' in the roles of λ, B … Answer each of its … queries by computing the entry»
  (`QueryMachine.subst` with `tableQ`);
* `levelMachine K g M`: the algorithm of the proof of Proposition 3: for every ι, the machine of
  Lemma 1 on the row network or the column network, whose values are computed with queries to the
  tables of the clique on g² nodes; P = g³λ and B₁ = gB + g²λ + 1 are handed over;
* `CLIQUE`, `NETWORK`, `COUNT`, `SAT`: the four procedures of Algorithm 1.
The plain functions inside (which bits of a string belong to which node, when a grouping is good,
the functions of Lemma 2 on the grid, …) are those of proof/networks/Eight/ViaGrouping, and each
machine is built in the same way as the step machine of the same purpose there and in
proof/threesat/Exits (`tableM`, `Exits.netAlg`, `levelAlgP`, `brute`), with «ask» in the place of
the answering procedure.
Different from Algorithm 1 as printed: SAT decides, returning at the first formula with Count(Φ) >
0, where the printed #Sat adds up counts; Clique has B as an argument and is passed B' in line 12
(Definition 4 and the proof of Lemma 1 say so; the pseudocode does not pass it); the level ℓ and the
parameter τ of Lemma 4 are parameters of the machines (they depend on δ only).
This file has no proofs. 

### `CliqueMachine`

 A machine for cliques: queries to the tables, input (λ, B) in unary, an integer as result. 

### `NetMachine`

 A machine for networks: the queries of Definition 2(iii), the input of Definition 2(iii), an
integer as result. 

 ## Two ways to write a setting of a node of a clique 

### `toTable`

 The programs of this development name a setting of the node w as the list of K strings, the
empty string at w itself. As one string, the form of Definition 3: their concatenation. 

### `toLists`

 Back: z_w cut into its K − 1 strings z_w(w') of λ bits (`SecNetworks.copyAt`), the empty string
at w. 

### `askTable`

 Ask the tables for the entry named by the second component. 

 ## Brute force 

### `bruteMachine`

 «Trying all 2^{λK(K−1)/2} choices of one string per edge»: the sum over all choices of the
product over the nodes of the table entries; built as `Groundwork.brute`. B is not read. 

 ## Procedures that may ask 

### `ProcsQ`

 What an algorithm is given of a network (Definition 2(iii)), when the four procedures themselves
have query access to something else: `SecNetworks.Procs` with machines that may ask. 

### `ProcsQ.under`

 The same numbers, with the step machines underneath. It is used only to hand the NUMBERS to the
plain functions of proof/networks/Eight/ViaGrouping, which take a `SecNetworks.Procs` and read
nothing else of it. 

### `ProcsQ.close`

 The oracle built into all four procedures. 

### `dist`

 (c, x or y) is (c, x) or (c, y). 

### `ProcsQ.answer`

 The four procedures as ONE machine that answers the queries of Definition 2(iii); yes is 1 and
no is 0. 

### `answerOf`

 The same for procedures that are step machines. 

### `inputOf`

 The input of Definition 2(iii) for a network on [g], written down from the numbers. 

### `networkOn`

 A machine for networks, run on the network that the procedures Np give in the context c: it is
handed the numbers, and each of its queries is answered by running the procedure. 

### `networkOnSteps`

 The same for procedures that are step machines. 

 ## The algorithm of the proof of Lemma 1 

### `wQ`

 [z_a ∈ S_a]·W_a(z_a). 

### `psiQ`

 [z_a ∈ S_a][z_b ∈ S_b]·Ψ_{a,b}(z_a, z_b). 

### `fQ`

 [z_a ∈ S_a]·f_{a,b}(z_a, θ_{a,b}). 

### `termQ`

 The factor number i = a·g + b of a term of W̃_γ(Θ), as `Eight.ViaGrouping.termP`. 

### `tableQ`

 **One entry W̃_γ(Θ)**: 0 unless all appended bits are 0; else the sum, over all strings of Σ_{a
∈ G_γ} P_a bits, of the product of the g² factors. Built as `Eight.ViaGrouping.tableM`. 

### `asked`

 Definition 2(iii) read by a machine for networks: the numbers are read off the input, and each
of the four procedures is one query. 

### `bitsOut`

 «B' = ⌈2gP/K⌉ + g²B». 

### `groupingMachine`

 **The algorithm of the proof of Lemma 1**, made from a machine M for cliques on K nodes. «Go
through all K^g groupings (a constant) and fix the first good one» (`Exits.search`: it stops there,
as line 10 of Algorithm 1 says; it reads only the numbers c_{a,b} and P, and asks nothing). «Let L =
max{1, ⌊(U + gP/K)/K²⌋}» (`lamP`).
«Run the algorithm for (K, e) with L, B' in the roles of λ, B … Answer each of its … queries by
computing the entry»: M gets (L, B'), and its query (γ, Θ) is answered by `tableQ`, which asks the
queries of Definition 2(iii). The result is 0 if no grouping is good (which does not happen for g =
3K⁸). 

 ## The algorithm of the proof of Proposition 3 

### `sideWQ`

 The weight W_a of a row (or column): the product of the g table entries, each asked for, or 0 if
the check of the straight edges inside the row fails. Built as `Groundwork.Prog.sideWP`. 

### `gridProcs`

 **«Two networks for each ι»**: the row network (tr = false) or the column network (tr = true) of
ι, as Definition 2(iii) asks, in the context ((λ, B), y), y the number of ι. «P = g³λ», «B₁ = gB +
g²λ + 1 in the role of B». W_a is computed with g queries to the tables of the clique on g² nodes;
Ψ_{a,a'} (`gridPsi`) and
f_{a,a'} (`gridFf`) in one step, with no query; every string of g³λ bits is a setting (here each
grid point keeps a slot of λ bits for the edge to itself, where the paper encodes a row in g(g² − 1)λ
bits); W_a is 0 unless those slots are 0 and the straight edges inside the row agree. The numbers
and functions are those of `Eight.ViaGrouping.levelProcs`, but for B₁. 

### `levelMachine`

 **The algorithm of the proof of Proposition 3** for cliques on g² nodes, made from a machine M
for cliques on K nodes: for every ι : ℛ → {0, …, t}, t = ⌈λ/3⌉, «apply Lemma 1 to the network with
the smaller total»; «adding the Z_ι and dividing by 2^{t|ℛ|} gives Z». Built as
`Eight.ViaGrouping.levelAlgP`. 

 ## Algorithm 1 

### `CLIQUE`

 **procedure Clique(ℓ, λ, the tables)**: level 0 is brute force; level ℓ + 1 is the algorithm of
Proposition 3 on Clique(ℓ). 

### `NETWORK`

 **procedure Network(ℓ, a network on g_ℓ nodes)**: the algorithm of Lemma 1 with K = K_ℓ, which
calls Clique(ℓ). 

### `formulaProcs`

 The procedures of the network of Φ (`Eight.ViaGrouping.satProcs`), which also give «B = 1». 

### `COUNT`

 **procedure Count(Φ)**, for a fixed level ℓ: «if m = 0 then return 1»; «return Network(ℓ, the
network of Φ on g_ℓ clusters)». A step machine: the queries of Network are answered by the
procedures of the network of Φ. 

### `SAT`

 **Lines 1 to 4 for deciding** (the paper's procedure #Sat counts), for a fixed level ℓ and a
fixed parameter τ of Lemma 4 (`Suffices.satLoop`: lines 1 to 4, with the early return). 

 ## The statements, each for the named machine 

### `StBrute`

 «(K, ½) is achievable», by brute force. 

### `StEntryCost`

 **Proof of Lemma 1, «Cost», first half**: «So |W̃_γ| < 2^{B'} with B' = ⌈2gP/K⌉ + g²B, and one
entry costs 2^{2gP/K}·poly(P + B)·τ operations». For a network N on [g] with parameters P, B, a
grouping number x < K^g with (G1) and Y_{γ,γ'} ≤ L ≤ 2gP: the machine `tableQ`, asked for the entry
(γ, Θ) of the tables W̃ of the (K, L)-clique of the groups
(`Value.groupClique` has them as its tables: the display of the paper; of its first argument it
reads only the numbers P_a, c_{a,b}), returns it within c₁·2^{P·⌊2g/K⌋}·τ operations, if each query
of Definition 2(iii) costs τ, on states of size at most c₁·(P + B)^{c₁}; and the entry is below
2^{B'}. Here P·⌊2g/K⌋ ≤ 2gP/K, and the factor poly(P + B) of the print is not needed, because an own
step may take polynomial time; the sizes of the states are bounded instead.
K and g are positive (for g = 0 the entry is 1 and B' = 0). The constant depends on K and g only. 

### `StGroupingTied`

 **Lemma 1 for the algorithm of its proof, from ANY machine that does what Definition 4 asks.** 

### `StGroupingTiedOf`

 The same with the steps of the proof in its hypotheses: «a good grouping exists … fix the first
good one» (`Eight.ViaGrouping.StSearch`), the run of the search (`Exits.StSearchStops`), «one entry
costs …» (`StEntryCost`), «so the value equals Z» for the clique of the groups as the network of
Definition 3 (`Value.StValueEqualsZ`), and
«answer each of its at most … queries by computing the entry» (`StAnswerEachQuery` is the form for
step machines; here `QueryMachines.StSubst`). 

### `StGroupingPoly`

 The machine of Lemma 1 has polynomial-time steps if M has. 

### `StOnProcedures`

 **Lemma 1 for networks given by procedures** (`SecNetworks.IsNetwork`: Definition 2 with (iii)
as four step machines that take at most τ steps each): a machine that does what Lemma 1 says, with
its queries answered by the procedures, outputs the value within 3·C₁·2^{e(U + gP/K) + 2gP/K}(P +
B)^{C₁}·τ steps. 

### `StBothNetworks`

 **Proof of Proposition 3: «Both networks satisfy Definition 2 with P = g³λ (so gP = N), with B₁ =
gB + g²λ + 1 in the role of B, and with τ = poly(B + λ)».** For g ≥ 1 there is a constant a such
that for λ, B ≥ 1, tables with |W_w| < 2^B of the clique on g² nodes, and every y < (t + 1)^{|ℛ|}:
the network `levelNetP g tr λ y` is a network with parameters g³λ and B₁;
the input that `gridProcs` hands over is the input that belongs to it; and every query of Definition
2(iii) to it is answered by `gridProcs` within a·(B + λ)^a operations, a query to the tables counted
as one operation. 

### `StLevelTied`

 **Proposition 3, first sentence, for the algorithm of its proof, from ANY machine that does what
Definition 4 asks.** 

### `StLevelPoly`

 The machine of Proposition 3 has polynomial-time steps if M has. 

### `StClique`

 **Section 8: «By brute force and Proposition 3, (K_ℓ, e_ℓ) is achievable for every ℓ»**, by
Clique(ℓ). The numbers e_ℓ are `Eight.Level.levelE`, the recursion that the paper prints in Section 8. 

### `StCountCost`

 **Section 6, «Cost», for Count**: as `Exits.StCountCost`, for the machine of this file. 

### `StAlgorithm`

 **The deciding form of Algorithm 1 decides 3-SAT, with the constants of its header.** Let 0 < δ
≤ 1 («We may assume δ ≤ 1»), ε = δ/3, let Mc ≥ 1 and τ be a constant and a parameter of Lemma 4 for
ε (`Enumerate.Enumerates (δ/3) Mc τ`), δ' = δ/(3·Mc), and ℓ the first level with K_ℓ ≥ 72/δ' and e_ℓ
≤ δ'/12 (`Eight.Level.firstLevel`). Then Sat(ℓ, τ) has polynomial-time steps and decides 3-SAT on n
variables within c·2^{δn} steps. As `Exits.StAlgorithm`, for the machines of this file. 

### `StDecides`

 **Theorem 2 in its decision form for step machines, with the machine named**: for every δ > 0
there are a level ℓ and a parameter τ such that Sat(ℓ, τ) has polynomial-time steps and decides
3-SAT on n variables within c·2^{δn} steps. 

### `StProofNamed`

 **The proof of Theorem 2 in Section 6, from the printed definition**: «Since e* = 0 < δ'/12 and
achievability is monotone in e (Definition 4), (K, δ'/12) is achievable for infinitely many K»; for
ANY machine M that does what Definition 4 asks for (K, δ'/12), K ≥ 72/δ', the loop of lines 1 to 4
over the machine of Lemma 1 with M, on the network of Φ, decides 3-SAT within c·2^{δn} steps. 

### `EndStatements`

 The end statements of the chain. The last two fields are one and the same proposition:
`through_eStar` stands for the proof of Section 6 (through `everyEta` and `proofNamed`),
`by_algorithm` for Algorithm 1 (through `decides`); the statement itself does not say that these
proofs run through the definitions and machines of this file. `proofNamed` and `algorithm` speak of
a constant Mc and a parameter τ of Lemma 4 (`Enumerate.Enumerates`); that there are such for every ε
is the field `enumeration`, Lemma 4 as an enumeration (proof/threesat/Enumerate/). 
