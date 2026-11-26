---
{
  "module": "proof/consequences/FromPrinted/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/Count.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Corollary 6 on the machines of proof/threesat/Printed/

The statements are those of proof/consequences/FromPrinted/CountDefs.lean. What
proof/consequences/SplitCount/ proves for every machine is used as it stands:
`SplitCount.stStepOneFor` («Φ has Z·2^{n'} satisfying assignments»), `SplitCount.stStepTwo`,
`SplitCount.stSuffices` («By the work of Dell et al. … this case suffices»; the reduction to 3-CNFs
lies inside it), `SplitCount.stCert`, `SplitCount.deltaPrime_facts`,
`SplitCount.counts_of_simulation`. What names a machine is proved here:
* `stComputesZ`: the proof of Theorem 2 computes Z: Lemma 1 for the algorithm of its printed proof,
  from any machine with `Printed.AchievedBy` (`Printed.stGroupingTied`), applied to the network of Φ
  (`Printed.onFormula`, `Printed.stOnProcedures`), and «Cost» of Section 6
  (`Printed.cost_of_bound`).
* `stFirstLine`, `stCountIsNetworkMachine`, `stStepOne`: COUNT of Algorithm 1 at level ℓ is line 6
  in front of that machine at K = K_ℓ with CLIQUE(ℓ) (`Printed.stClique`).
* `COUNT_polyTimeSteps`: the steps of COUNT are polynomial time at every level.
* `stCountsAt`, `stCountsWithAnyCliqueAlgorithm`, `stEngineCounts`, `stCOUNTsplitCounts`,
  `stTiedTM`, `endFrom`, `countingCorollary`: as in proof/consequences/SplitCount/Main.lean. 

### `stComputesZ`

 **The proof of Theorem 2, with K and g chosen from δ' as there, computes Z.** For 0 < δ' ≤ 1, K
≥ 2 with K ≥ 72/δ', g = 3K⁸ and any machine M for cliques on K nodes with
`Printed.AchievedBy M Cc K (δ'/12)`, the algorithm of the printed proof of Lemma 1 with M, run on
the network of Φ on g clusters, computes Z as Section 6 says. 

### `stFirstLine`

 **«if m = 0 then return 1».** If a machine computes Z as Section 6 says, with the exponent δ'
and the constant A, then so does that machine with line 6 of Algorithm 1 in front of it, with the
same exponent and some constant A' (the proof takes A' = A + 4). 

### `stCountIsNetworkMachine`

 COUNT of Algorithm 1 at level ℓ is line 6 in front of the machine of `StComputesZ` at K = K_ℓ
and M = CLIQUE(ℓ): g_ℓ = 3K_ℓ⁸ by definition. 

### `stStepOne`

 **The count of a 3-CNF by COUNT of Algorithm 1.** For 0 < δ' ≤ 1 and every level ℓ with K_ℓ ≥
72/δ' and e_ℓ ≤ δ'/12, `countThree ℓ` computes the number Z·2^{n'} of the proof of Corollary 6, in
the form that `SplitCount.stStepOneFor` states. 

### `COUNT_polyTimeSteps`

 The steps of COUNT of Algorithm 1 are polynomial time, at every level ℓ: those of CLIQUE(ℓ) are
(`Printed.stClique`), so those of the machine of Lemma 1 made from it (`Printed.stGroupingPoly`), so
those of that machine on the network of Φ (`Printed.onFormula_poly`), and line 6 keeps this
(`Printed.firstLine_poly`). 

### `stCountsAt`

 **The proof of Corollary 6 at a level of Algorithm 1, with the machine named.** Under the
hypotheses of `StCountsAt`, `engineSplit step ℓ` serves as the procedure for #k-SAT with the
exponent δ. 

### `stCountsWithAnyCliqueAlgorithm`

 **The same with Section 6's choice of K**: any K ≥ 2 with K ≥ 72/δ' and any machine M for
cliques on K nodes with `Printed.AchievedBy M Cc K (δ'/12)`, in the place of a level of Algorithm 1. 

### `stEngineCounts`

 **Corollary 6 for machines cut into steps, with the machine named**: for every k ≥ 1 and δ > 0
there are ℓ and τ such that `ENGINEsplit k ℓ τ` has polynomial-time steps and serves as the
procedure for #k-SAT with the exponent δ. 

### `stCOUNTsplitCounts`

 **#k-SAT with the machine named.** For every k ≥ 1 and δ > 0 there are ℓ and τ such that
`COUNTsplit k ℓ τ` has polynomial-time steps and writes the number of satisfying assignments of a
k-CNF on n variables, in n + 1 bits, within c·2^{δn} steps, on states of size at most c·(length of
the input + 1)^c. 

### `stTiedTM`

 **Tied to the machine, on Mathlib's Turing machines.** For every k ≥ 1 and δ > 0 there are ℓ, τ,
a Turing machine M with finite alphabets and numbers c, q such that `COUNTsplit k ℓ τ` has
polynomial-time steps and writes the number of satisfying assignments of a k-CNF on n variables
within c·2^{δn} steps on states of size at most c·(length + 1)^c;
M simulates it with the overhead q·(T+1)·(|x|+S+1)^q; and M counts the satisfying assignments of
k-CNFs within ⌊c·2^{δn}⌋ steps. 

### `endFrom`

 **Corollary 6**: «For every k ≥ 3 and δ > 0 there is a deterministic algorithm that computes the
number of satisfying assignments of a k-CNF on n variables in time O(2^{δn}). For k = 3 this says
that the counting version #ETH of ETH is false.»
The statement is `PaperSentences.CorCounting` of PaperSentencesStatement.lean, for Turing machines.
Here it is drawn from the tied statement `StTiedTM` as a hypothesis: both halves take the Turing
machine of that statement, which simulates `COUNTsplit k ℓ τ`; the second half at k = 3, by
`CountKSat.EndLemmas.not_CountETH_TM_of`. 

### `countingCorollary`

 **Corollary 6**, in the wording of PaperSentencesStatement.lean: `endFrom` on the proof
`stTiedTM` of the tied statement. 
