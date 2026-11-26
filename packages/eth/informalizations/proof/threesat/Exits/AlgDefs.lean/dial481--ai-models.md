---
{
  "module": "proof/threesat/Exits/AlgDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/AlgDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/AlgDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Algorithm 1, line by line (definitions and statements only)

The procedures COUNTp, NETWORKp, CLIQUEp of proof/networks/Eight/ViaGrouping/AlgDefs.lean differ
from Algorithm 1 as printed in the paper in these lines:
* line 6, «if m = 0 then return 1», is missing;
* line 10, «try all groupings into K_ℓ groups until one is good»: the loop runs through all K^g
  groupings and keeps the first good one.
Here are the four procedures, with lines 6 and 10 as printed and lines 1 to 4 in a deciding form
that returns at the first formula Φ with Count(Φ) > 0. Lines 11 and 12 and procedure Clique are as
in proof/networks/Eight/ViaGrouping (`lamP`, `tableM`, `levelAlgP`, `gridPsi`); as Clique and
Network call each other, all four are defined here.
What differs from the print: line 7, «choose the level ℓ», is carried out beforehand: ℓ depends on δ
only, δ is a real number that no machine receives, and the paper has one algorithm for each δ; so ℓ
is a parameter of the machines, and so is the parameter τ of Lemma 4, which stands for ε. A formula
with an empty clause is answered at once (in the paper clauses are nonempty).
The formulas of line 2 are produced one at a time and not stored. B' is not passed on in line 12
(the printed line does not pass it either).
The statements: each step of the chain Lemma 1 → Proposition 3 → (K_ℓ, e_ℓ) → Section 6, «Cost» →
Theorem 2, for THESE procedures, so that the proofs of Theorem 2 by Section 6 and by Algorithm 1 run
through the early exits, through Lemma 4 as an enumeration, and through the printed proofs of the
variance bound 4PU (proof/networks/Variance) and of «so the value equals Z» (proof/networks/Value).
«Achievable» is `Paper.Achievable`, in which a query costs t steps; in Definition 4 of the paper a
query costs one operation.
This file has no proofs. 

 ## The procedures 

### `search`

 **Line 10**: «try all groupings into K_ℓ groups until one is good» (here K for K_ℓ). The loop
halts at the first good grouping. 

### `netAlg`

 **The algorithm of the proof of Lemma 1, with the search of line 10**: lines 10 to 12 for an
algorithm E for cliques on K nodes. It differs from `Eight.ViaGrouping.netAlg K g E` in the search
alone. 

### `CLIQUE`

 **procedure Clique(ℓ, λ, the tables)**, lines 13 to 19. 

### `NETWORK`

 **procedure Network(ℓ, a network on g_ℓ nodes)**, lines 9 to 12. 

### `COUNT`

 **procedure Count(Φ)**, lines 5 to 8, for a fixed level ℓ: «if m = 0 then return 1»; «return
Network(ℓ, the network of Φ on g_ℓ clusters)». 

### `SAT`

 **Lines 1 to 4 for deciding** (the paper's procedure #Sat counts), for a fixed level ℓ and a
fixed parameter τ of Lemma 4. 

### `levelUp`

 The algorithm of the proof of Proposition 3, on the algorithm of Lemma 1 with the search of line 10. 

 ## The search 

### `StSearchStops`

 **Line 10 stops at the first good grouping**: if x is the first number below K^g to which the
test says yes, the search halts within 2·(x + 1) steps and returns x. (`Eight.ViaGrouping.searchP`
takes 2·K^g steps.) 

### `StSearchStopsOf`

 The run of the search from «try all … until one is good». 

 ## The chain 

### `StGroupingLemma`

 **Lemma 1 for the algorithm of its proof**, with the search of line 10: the statement
`Eight.ViaGrouping.StLemGrouping` for `Exits.netAlg`. 

### `StGroupingLemmaOf`

 Lemma 1 from the steps of its proof: «a good grouping exists … fix the first good one»
(`StSearch`), «one entry costs …» (`StTable`), «so the value equals Z» (`StValue`), and the run of
the search. 

### `StKeeps`

 The algorithm has polynomial-time steps if E has. 

### `StKeepsOf`

 Its polynomial-time steps from those of the loop. 

### `StLevelUp`

 **Proposition 3, first sentence, for the named algorithm.** 

### `StLevelUpOf`

 Proposition 3 for the named algorithm, from Lemma 1 for the algorithm of its proof («Apply Lemma
1 to the network with the smaller total»). 

### `StClique`

 **Section 8: «By brute force and Proposition 3, (K_ℓ, e_ℓ) is achievable for every ℓ, …»**, for
Clique(ℓ). 

### `StCliqueOf`

 «By brute force and Proposition 3». 

### `StCountNil`

 **Line 6**: on the formula without clauses Count returns 1 in one step, at every level. 

### `StCountCost`

 **Section 6, «Cost», for Count.** Let 0 < δ' ≤ 1. At every level ℓ with K_ℓ ≥ 72/δ' and e_ℓ ≤
δ'/12, Count(Φ) returns the number of assignments of the variables occurring in Φ that satisfy Φ
within A·2^{δ'm} steps, on states of polynomial size; and its steps take polynomial time. 

### `StCountCostOf`

 «Cost» for Count, from Lemma 1 for Network(ℓ), the polynomial-time steps of the algorithm of
Lemma 1, and the bound for Clique(ℓ). 

### `StAlgorithm`

 **The deciding form of Algorithm 1 decides 3-SAT, with the constants of its header.** Let 0 < δ
≤ 1 («We may assume δ ≤ 1»), ε = δ/3, let M ≥ 1 and τ be a constant and a parameter of Lemma 4 for ε
(`Enumerates (δ/3) M τ`), δ' = δ/(3M), and ℓ the first level with K_ℓ ≥ 72/δ' and e_ℓ ≤ δ'/12. Then
Sat(ℓ, τ) has polynomial-time steps and decides 3-SAT on n variables within c·2^{δn} steps. 

### `StAlgorithmOf`

 The deciding form of procedure #Sat of Algorithm 1 from its parts: «it suffices», and «Cost» for
Count. 

### `StDecides`

 **Theorem 2 in its decision form for step machines, with the machine named**: for every δ > 0
there are a level ℓ and a parameter τ such that Sat(ℓ, τ) has polynomial-time steps and decides
3-SAT on n variables within c·2^{δn} steps. 

### `StDecidesOf`

 From Algorithm 1 with the constants of its header and Lemma 4 («We may assume δ ≤ 1»). 

### `StProofNamed`

 **The proof of Theorem 2 in Section 6, for a named machine**: let 0 < δ ≤ 1, M, τ as above, δ' =
δ/(3M), and let E be an algorithm with polynomial-time steps that meets the bound of «achievable»
for (K, δ'/12), K ≥ 72/δ'. Then the loop of lines 1 to 4 over the machine the algorithm of Lemma 1
for E, on the network of Φ on g = 3K⁸ clusters, decides 3-SAT within c·2^{δn} steps. 

### `StProofNamedOf`

 The same with what it rests on in its hypotheses: «it suffices», Lemma 1 for the algorithm of
its proof, and its polynomial-time steps. 

### `StLevelAchievable`

 **Proposition 3, first sentence**: «If (K, e) is achievable and g = 3K⁸, then (g², e') is
achievable for e' = (ρ + 2/K)e + 2/K» (ρ = 11/12; g² is written 9K¹⁶), from the form for the named
algorithm. 

### `StLevelAchievableOf`

 From the form for the named algorithm. 

### `StEStarOf`

 «Hence e* = 0», from the first sentence of Proposition 3. 

### `StThroughEStarOf`

 **Theorem 2 in its decision form by the proof of Section 6**: «Since e* = 0 < δ'/12 … (K, δ'/12)
is achievable for infinitely many K. Fix such a K ≥ 72/δ'», Lemma 4, and the proof for a named
machine. 

### `StByAlgorithmOf`

 **Theorem 2 in its decision form by Algorithm 1**: a Turing machine of Mathlib simulates Sat(ℓ,
τ). 

 The end theorems of the folder are `eStar = 0` and `Sat3.ThmEveryDelta`, the latter twice (by
Section 6 and by Algorithm 1). The implications above state how they are proved here: through the
procedures of Algorithm 1, with the search of line 10 and lines 1 to 4 in their deciding form, both
left early. Statements that name these machines include `StAlgorithm`, `StDecides`, `StProofNamed`,
`StClique`, `StLevelUp`, `StGroupingLemma`. 
