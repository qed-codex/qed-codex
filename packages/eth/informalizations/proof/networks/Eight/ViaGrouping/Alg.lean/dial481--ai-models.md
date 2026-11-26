---
{
  "module": "proof/networks/Eight/ViaGrouping/Alg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Alg.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Alg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Algorithm 1 (Section 8) and Section 6 «Cost», on the algorithm of the printed proof of Lemma 1

Here the algorithm of Section 8 is put on top of `netAlg`
(proof/networks/Eight/ViaGrouping/Defs.lean), the algorithm of the printed proof of Lemma 1:

* CLIQUE(ℓ) meets the bound of «achievable» for (K_ℓ, e_ℓ), by brute force at level 0 and by Lemma 1
  and one level in each step (`CLIQUEp_within`, `CLIQUEp_polyTimeSteps`); the steps of NETWORK(ℓ)
  are polynomial time (`NETWORKp_keeps`);
* at a level with K_ℓ ≥ 72/δ' and e_ℓ ≤ δ'/12, COUNT counts the satisfying assignments within
  A·2^{δ'm} steps (`COUNTp_cost`, Section 6 «Cost»);
* from any sparsification with the property `Eight.SufficesSparse`, Algorithm 1 decides 3-SAT within
  c·2^{δn} steps (`algPseudocode_of`).

Used from the other files of this folder: Lemma 1 for the algorithm of its proof (`stLemGrouping`,
`stKeeps`; proof/networks/Eight/ViaGrouping/LemGrouping.lean, Keeps.lean), one level
(`levelAlgP_gridPsi_correct`, `levelAlgP_gridPsi_keeps`; LevelEnd.lean), the network of Φ
(`count_cost_of`,
`satProcs_keepsP`; Count.lean, SatPsi.lean), the program for Ψ in the two networks of a level
(`stGridPsi`, `stGridPsiPoly`; GridPsi.lean). No theorem of this file has a hypothesis of the form
`St…`.
Lemma 4 enters at one place only: through the property `Eight.SufficesSparse` of a constant M and a
construction S (proof/networks/Eight/SecProof_Proof.lean). `algPseudocode_of` holds for every M and
S with that property.
The numbers e_ℓ (`Eight.Level.levelE`) are those of proof/networks/Eight/Level/Defs.lean; they do
not depend on any algorithm. 

 ## Section 8: what CLIQUE and NETWORK do, and how long they take 

### `two_le_levelK`

 K_ℓ ≥ 2. 

### `zero_lt_levelG`

 g_ℓ ≥ 1. 

### `CLIQUEp_polyTimeSteps`

 The steps of CLIQUE(ℓ) are polynomial time. 

### `CLIQUEp_within`

 CLIQUE(ℓ) returns the value of every (K_ℓ, λ)-clique within C · 2^{e_ℓ K_ℓ² λ} (B + λ)^C steps,
times the cost of a query, with the e_ℓ of Section 8 for ρ = 11/12. The numbers are those of the
paper. Level 0 is brute force; the step from ℓ to ℓ + 1 is Lemma 1 for
the algorithm of its proof, then one level. 

### `NETWORKp_keeps`

 The steps of NETWORK(ℓ) are polynomial time, whenever those of the procedures of the network are
and P is given in unary. 

 ## Algorithm 1 decides 3-SAT, and Theorem 2 

### `COUNTp_polyTimeSteps`

 The steps of COUNT, at the level ℓ, are polynomial time. 

### `COUNTp_cost`

 **Section 6, «Cost», for COUNT of Algorithm 1.** Let 0 < δ' ≤ 1. At every level ℓ with K_ℓ ≥
72/δ' and e_ℓ ≤ δ'/12, COUNT(Φ) returns the number of assignments of the variables occurring in Φ
that satisfy Φ within A·2^{δ'm} steps, on states of polynomial size. 

### `algPseudocode_of`

 **The deciding form of procedure #Sat of Algorithm 1, from any sparsification.** Let δ > 0, and
let the constant M ≥ 1 and the construction S have the property that it suffices to decide whether a
3-CNF Φ with m clauses is satisfiable, in time O(2^{δ'm}) (`Eight.SufficesSparse δ M S`). Let
δ' = min(δ/(3M), 1). At every level ℓ with K_ℓ ≥ 72/δ' and e_ℓ ≤ δ'/12, the machine S(COUNT) decides
3-SAT within c·2^{δn} steps. Lemma 4 is used only through that property. Only steps are counted
here. That they take polynomial time: `COUNTp_polyTimeSteps` and the first part of
`Eight.SufficesSparse`. 
