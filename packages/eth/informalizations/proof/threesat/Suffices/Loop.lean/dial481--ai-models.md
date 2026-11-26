---
{
  "module": "proof/threesat/Suffices/Loop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Suffices/Loop.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Suffices/Loop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The run of lines 1 to 4 of Algorithm 1

«for each Φ in the list that Lemma 4 computes from φ and ε do», with the test "Count(Φ) > 0" in
place of the paper's sum of counts, stopping at the first Φ that passes (the deciding form of
Algorithm 1, lines 2 to 4).
`stLoopRunsOf` takes the run of the walk that halts at the first leaf that passes
(`Exits.StWalkUntil`) as its hypothesis and applies it to the tree of an enumeration: the rule is
`Enumerate.rule τ`, the depth `Enumerate.depth τ n`, and the test of a leaf is Mc on the output ψ ∪
𝒩 of the leaf. The formulas tested are the outputs of the leaves tested (`tested_map`); the size of
the stack comes from the field `stack` of the enumeration.
`satLoop_polyTimeSteps_of` takes the polynomial-time steps of the loop that can be left
(`Exits.StFoldUntilPoly`) as its hypothesis; the moves of the walk and the passage from a leaf to
its output are polynomial-time by the fields `rule_poly` and `out_poly`. 

### `isKCNF_toN`

 What is read from the code of a 3-CNF without an empty clause is a 3-CNF in the sense of
`SparsificationLemma.IsKCNF` (nonempty clauses of at most 3 literals on variables below n). (The
case k = 3 of `SparsificationLemma.Mach.isKCNF_toN`, proved here so that this file need not import
the files on the Turing machine of Lemma 4.) 

### `le_length_enc`

 The number of variables and the number of clauses are at most N, the length of the code plus 1. 

### `stLoopRunsOf`

 **The run of lines 1 to 4 of Algorithm 1**, from the walk that halts at the first leaf that
passes: «for each Φ in the list that Lemma 4 computes from φ and ε do» (line 2), the test Count(Φ) >
0 in place of the paper's line 3, which counts. 

### `stLoopRuns`

 **The run of lines 1 to 4 of Algorithm 1**: «for each Φ in the list that Lemma 4 computes from φ
and ε do» (line 2), the test Count(Φ) > 0 in place of the paper's line 3, which counts; only the
formulas up to the first with a positive count are tested. 

### `satLoop_polyTimeSteps_of`

 If the machine Mc in the place of Count has polynomial-time steps, so does `satLoop τ Mc` (lines
1 to 4 of Algorithm 1). Uses the hypothesis `StFoldUntilPoly` for the loop that can be left early,
and the fields `rule_poly` and `out_poly` of the enumeration (Lemma 4: «in time 2^{εn} times a
polynomial in n»). 
