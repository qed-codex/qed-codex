---
{
  "module": "proof/threesat/Printed/End.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/End.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/End.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The end statements of proof/threesat/Printed/

The files of this folder prove each step from the steps before it, which are hypotheses (`…_of`,
`…_from`). Five statements come from other folders:
* «a good grouping exists … fix the first good one» (`Eight.ViaGrouping.StSearch`), proved through
  «Var Y_{γ,γ'} ≤ … = 4PU» in proof/networks/Variance (`Variance.stSearch`);
* the search stops at the first good grouping (`Exits.StSearchStops`), proof/threesat/Exits
  (`Exits.stSearchStops`);
* «so the value equals Z» (`Value.StValueEqualsZ`), proof/networks/Value (`Value.stValueEqualsZ`);
* «it suffices …», for deciding (`Suffices.StSuffices`), proof/threesat/Suffices
  (`Suffices.stSuffices`);
* Lemma 4 as an enumeration (`Enumerate.StEnumeration`), proof/threesat/Enumerate
  (`Enumerate.stEnumeration`).
`endStatements_of` has exactly these five as hypotheses. Below they are filled in, and every
statement `St…` of PrintedStatement.lean, Programs.lean and CodingDefs.lean is a closed theorem.
(Some are proved without these hypotheses in other files: `stAskServes`, `stCliqueValue`,
`stToLists` in Coding.lean; `stMono`, `stBrute`, `stHalf`, `stAnswerEachQuery` in Achievable.lean;
`stOnProcedures` in GroupingProcs.lean; `stEntryCost` in GroupingEntry.lean; `stGroupingTiedOf` in
GroupingRun.lean; `stGroupingPoly` in GroupingPoly.lean; `stBothNetworks`, `stLevelPoly` in
LevelFrom.lean.) 

### `endStatements_of`

 All end statements of proof/threesat/Printed/, from the five statements that other folders
prove. 

 ## Lemma 1 

### `stGroupingTied`

 **Lemma 1 for the algorithm of its proof, from ANY machine that does what Definition 4 asks.** 

### `groupingLemma`

 **Lemma 1.** 

 ## Proposition 3 

### `stLevelTied`

 **Proposition 3, first sentence, for the algorithm of its proof, from ANY machine that does what
Definition 4 asks.** 

### `levelProposition`

 **Proposition 3**, first sentence. 

### `eStarZero`

 **Proposition 3**, second sentence: e* = 0. 

### `stEveryEta`

 «That is, for every η > 0, (K, η) is achievable for infinitely many K.» 

 ## Section 8 and Section 6 

### `stClique`

 **Section 8: «By brute force and Proposition 3, (K_ℓ, e_ℓ) is achievable for every ℓ»**, by
Clique(ℓ). 

### `stCountCost`

 **Section 6, «Cost», for Count.** 

### `stAlgorithm`

 **Algorithm 1 decides 3-SAT, with the constants of its header.** 

### `stDecides`

 **Theorem 2 in its decision form for step machines, with the machine named.** 

### `stProofNamed`

 **The proof of Theorem 2 in Section 6, from the printed definition**, for ANY machine that does
what Definition 4 asks for (K, δ'/12). 

### `threeSat_through_eStar`

 **Theorem 2 in its decision form**, by the proof of Section 6: through e* = 0 for the printed
Definition 4. 

### `threeSat_by_algorithm`

 **Theorem 2 in its decision form**, by Algorithm 1. 

### `endStatements`

 The end statements of proof/threesat/Printed/. 
