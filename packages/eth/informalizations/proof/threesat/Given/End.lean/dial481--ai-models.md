---
{
  "module": "proof/threesat/Given/End.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Given/End.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Given/End.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The way from `IsGivenNetwork` to Theorem 2

Every statement here is a statement of the namespace `Printed` (PrintedStatement.lean,
proof/threesat/Printed/Programs.lean), unchanged. Only the proofs differ: wherever the proofs there
say that a network satisfies Definition 2, or apply Lemma 1 to it, the proofs here use
`stGridGiven`, `stFormulaGiven` and `stOnGiven`.
The steps that do not look at a network are used as they stand, from their hypotheses:
`Printed.levelProposition_of`, `eStarZero_of`, `stEveryEta_of`, `stClique_of`, `cost_of_bound`,
`cost_with_first_line`, `firstLine_poly`, `decidesSparse_of_cost`, `stAlgorithm_of`, `stDecides_of`,
`threeSat_through_eStar_of`, `threeSat_by_algorithm_of`; so are Lemma 1 for the algorithm of its
proof (`Printed.stGroupingTied`, `stGroupingPoly`), which speaks of every network and is given none,
and the statements of other folders.
That these proofs run through `IsGivenNetwork` cannot be read off the statements; it shows in what
they depend on. 

 ## Proposition 3 

### `levelProposition`

 **Proposition 3**, first sentence. 

### `eStarZero`

 **Proposition 3**, second sentence: e* = 0. 

### `stEveryEta`

 «That is, for every η > 0, (K, η) is achievable for infinitely many K.» 

### `stClique`

 **Section 8: «By brute force and Proposition 3, (K_ℓ, e_ℓ) is achievable for every ℓ»**, by
Clique(ℓ). 

 ## Section 6 

### `onFormula`

 **Lemma 1, applied to the network of Φ.** If NM does what Lemma 1 says for (K, e) on networks on
[g], then NM, with its queries answered by the procedures of the network of Φ, returns the value Z
of that network within C·2^{eU + (e+2)·gP/K}·(P + 1)^C steps: B = 1 and τ = 1. The bounds are
written as in `Eight.ViaGrouping.Correct.onFormula`; C = 3C₁ + 5 (the 3 is that of `StOnGiven`).
With it, in one conclusion: the machine has polynomial-time steps if NM has. The text is that of
`Printed.onFormula`, with `stFormulaGiven` and `stOnGiven` (read by `onSteps`) in the places of
`Printed.formula_isNetwork` and `Printed.stOnProcedures`. 

### `stCountCost`

 **Section 6, «Cost», for Count.** The text is that of `Printed.stCountCost_of`, with `onFormula`
of this file. 

### `stAlgorithm`

 **Algorithm 1 decides 3-SAT, with the constants of its header.** 

### `stDecides`

 **Theorem 2 in its decision form for step machines, with the machine named.** 

### `stProofNamed`

 **The proof of Theorem 2 in Section 6**, for any machine that does what `Printed.AchievedBy`
asks for (K, δ'/12). The text is that of `Printed.stProofNamed_of`, with `onFormula` of this file.
(The τ here is a threshold of the sparsification used for Lemma 4, not the price of a query in
Definition 2(iii).) 

 ## Theorem 2 

### `threeSat_through_eStar`

 **Theorem 2 in its decision form**, by the proof of Section 6: through e* = 0 (`Printed.eStar`). 

### `threeSat_by_algorithm`

 **Theorem 2 in its decision form**, by Algorithm 1. 

### `endStatements`

 The end statements of the namespace `Printed`, each field that rests on a network filled by the
corresponding theorem of this file. The fields `mono`, `half`, `answerEachQuery`, `groupingLemma`
and `enumeration` are given no network and are those of `Printed` and `Enumerate`. 
