---
{
  "module": "proof/consequences/FromPrinted/CountDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/CountDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/CountDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 6 (#k-SAT in time O(2^{δn})) along its printed proof, on the machines of proof/threesat/Printed/: the machine and the statements (no proofs)

proof/consequences/SplitCount/Defs.lean states the four steps of the printed proof of Corollary 6.
Most of it has the machine that computes Z as a parameter: `timesFreeAfter Cnt`, `engineBy step D`,
`ComputesZ`, `CountsThree`, `StStepOneFor`, `StStepTwo`, `StStepThree`, `StSuffices`, `StCert`,
`deltaPrime`. Those are used here as they stand. A machine of the main text is named there in
`countThree` (`Eight.ViaGrouping.COUNTp ℓ`), so in `engineSplit`, `ENGINEsplit`, `COUNTsplit` and
the statements on them, and in `StComputesZ`, `StCountIsNetworkMachine`,
`StCountsWithAnyCliqueAlgorithm` (`Eight.ViaGrouping.netAlg`, `Eight.ViaGrouping.CLIQUEp`,
`Paper.CliqueAlgorithm`).
This file states those definitions and statements for another machine, under the same short names,
with `Printed.COUNT ℓ` in the place of `Eight.ViaGrouping.COUNTp ℓ`: COUNT of Algorithm 1 in the
form that the file proof/threesat/Printed/Programs.lean builds, from machines with query access to
the tables of a clique, for which «achievable» is `Printed.Achievable`: Definition 4 in the paper's
unit of cost (a table query costs one operation), with a bound on memory added. Nothing else is
changed, but for two things.
* In the place of «any algorithm E for cliques with `E.Within K (δ'/12)`» stands «any machine M with
  query access to the tables with `Printed.AchievedBy M Cc K (δ'/12)`» (what
  `Printed.Achievable K (δ'/12)` asks of a machine, but for polynomial-time steps), and in the place
  of `(netAlg K g E).app (satProcs g 3)` the machine of the proof of Lemma 1 made from M, with its
  queries answered by the procedures of the network of Φ
  (`Printed.networkOnSteps g (Printed.groupingMachine K g M) (Printed.formulaProcs g 3)`).
* `Printed.COUNT ℓ` begins with line 6 of Algorithm 1, «if m = 0 then return 1», which
  `Eight.ViaGrouping.COUNTp ℓ` does not have: `withFirstLine`, `StFirstLine`.
What differs from the paper is said at the heads of proof/consequences/SplitCount/Defs.lean (the
route of Corollary 6) and of proof/threesat/Printed/Programs.lean and PrintedStatement.lean (the
machines and Definition 4).
This file has no theorem. 

 ### The machine 

### `countThree`

 Step 1 with COUNT of Algorithm 1 at level ℓ. 

### `engineSplit`

 The procedure with COUNT of Algorithm 1 at level ℓ. 

### `ENGINEsplit`

 The procedure at width k, level ℓ, threshold parameter τ of the sparsification. 

### `COUNTsplit`

 The machine for #k-SAT: the reader of the input, then the procedure. 

 ### Step 1 

### `StComputesZ`

 **The proof of Theorem 2, with K and g chosen from δ' as there, computes Z, in the form of
Section 6.** Let 0 < δ' ≤ 1, let K ≥ 2 with K ≥ 72/δ', let M be ANY machine for cliques on K nodes,
with query access to the tables, with `Printed.AchievedBy M Cc K (δ' / 12)` (Definition 4 in the
paper's unit of cost (a table query costs one operation), with a bound on memory added, for (K,
δ'/12) with the constant Cc; «(K, δ'/12) is achievable», `Printed.Achievable`, asks besides that the
steps of M are polynomial time, which this statement does not need), and g = 3K⁸. The algorithm of
the printed proof of Lemma 1 with M, run on the network of Φ on g clusters, computes Z as Section 6
says.
It follows from `Printed.stGroupingTied`, `Printed.onFormula` and `Printed.cost_of_bound`. 

### `withFirstLine`

 Line 6 of Algorithm 1, «if m = 0 then return 1», in front of a machine Cnt. 

### `StFirstLine`

 **«if m = 0 then return 1».** If Cnt computes Z as Section 6 says, then so does Cnt with line 6
of Algorithm 1 in front of it, with the same exponent. It follows from
`Printed.cost_with_first_line`. 

### `StCountIsNetworkMachine`

 COUNT of Algorithm 1 at level ℓ is line 6 in front of the machine of `StComputesZ` at K = K_ℓ
and M = CLIQUE(ℓ). (By unfolding definitions.) 

### `StStepOne`

 **Step 1 for COUNT of Algorithm 1.** Let 0 < δ' ≤ 1. At every level ℓ with K_ℓ ≥ 72/δ' and e_ℓ ≤
δ'/12 (Section 6's constants; the level ℓ stands for Section 6's achievable K), `countThree ℓ` does
what step 1 says. It follows from `StComputesZ` at K = K_ℓ and M = CLIQUE(ℓ)
(`StCountIsNetworkMachine`, `StFirstLine`; `Printed.AchievedBy` holds of CLIQUE(ℓ) for (K_ℓ, e_ℓ),
e_ℓ ≤ δ'/12: `Printed.stClique`) and `StStepOneFor`, so that Section 6's form is on the path. 

 ### Step 4 and the end 

### `StCountsAt`

 **Step 4, with the machine named.** Let k ≥ 1 and δ > 0, let `step` sparsify width k for
counting with ε = δ/3 and leaves of at most Bl·n clauses, and δ' = `deltaPrime δ (max k 3) Bl` (for
the paper's k ≥ 3, max(k, 3) = k). At every level ℓ with K_ℓ ≥ 72/δ' and e_ℓ ≤ δ'/12,
`engineSplit step ℓ` serves as the procedure for #k-SAT with the exponent δ. It follows from
`StStepOne` and `StSuffices`. 

### `StCountsWithAnyCliqueAlgorithm`

 **Corollary 6 for machines cut into steps with Section 6's choice of K**, from end to end: in
the place of a level of Algorithm 1, any K ≥ 2 with K ≥ 72/δ' and any machine M for cliques on K
nodes with `Printed.AchievedBy M Cc K (δ'/12)`, δ' = `deltaPrime δ (max k 3) Bl`. 

### `StEngineCounts`

 **Corollary 6 for machines cut into steps, with the machine named**, in the form in which
Corollary 7 and the circuit lower bound for E^NP (Section 7) take it
(`Eight.ViaGrouping.EngineCounts`; there for every k ≥ 1: below 3 the width reduction changes
nothing). 

### `StCOUNTsplitCounts`

 **#k-SAT with the machine named.** For every k ≥ 1 and δ > 0 there are a level ℓ and a threshold
parameter τ such that `COUNTsplit k ℓ τ` has polynomial-time steps and writes the number of
satisfying assignments of a k-CNF on n variables, in n + 1 bits, within c·2^{δn} steps, on states of
size polynomial in the length of the input. 

### `StTiedTM`

 **Tied to the machine, on Mathlib's Turing machines.** For every k ≥ 1 and δ > 0 there are ℓ, τ
such that (1) `COUNTsplit k ℓ τ` ITSELF has polynomial-time steps and writes the number of
satisfying assignments of a k-CNF on n variables within c·2^{δn} steps, on states of size polynomial
in the length of the input; (2) a Turing machine M with finite alphabets simulates it with
polynomial overhead
(whenever that machine ends on a word x with a word w within T steps on states of size at most S, M
started on x halts with w within q·(T+1)·(|x|+S+1)^q steps); (3) M counts the satisfying assignments
of k-CNFs within ⌊c·2^{δn}⌋ steps. (Without (1), a machine that runs the named machine and another
one side by side would meet (2) and (3).) 

### `ThreeSatStatement`

 The end theorem has the statement `PaperSentences.CorCounting` of PaperSentencesStatement.lean.
Both of its halves follow from `StTiedTM`: the second, «#ETH is false», from `StTiedTM` at k = 3 by
the generic `not_CountETH_TM_of` of proof/consequences/CountKSat/EndLemmas.lean.
The end theorem is proved in two pieces:
`FromPrinted.SplitCount.endFrom : StTiedTM → ThreeSatStatement`, which has the tied statement as
HYPOTHESES, and the one-line instance
`FromPrinted.SplitCount.countingCorollary := endFrom stTiedTM`. Every theorem of this development
that the proof of `FromPrinted.SplitCount.endFrom : StTiedTM → ThreeSatStatement` uses says nothing
about a particular machine (such as `not_CountETH_TM_of`); so what the end theorem says about
machines can only come from the hypotheses.
The instance rests on the proofs of `StComputesZ`, `StFirstLine` and `StStepOne` (named
`FromPrinted.SplitCount.stComputesZ`, `stFirstLine`, `stStepOne`) and on the machines
`Printed.COUNT`, `Printed.NETWORK`, `Printed.CLIQUE`, not on the machines of the main text
(`Eight.ViaGrouping.COUNTp`, `Eight.ViaGrouping.CLIQUEp`, `Eight.ViaGrouping.netAlg`) or what is
proved of them. 
