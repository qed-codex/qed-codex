---
{
  "module": "proof/consequences/PrintedOrder/Counting.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/PrintedOrder/Counting.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/PrintedOrder/Counting.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 6: the count is the sum of the counts of the outputs of the sparsification, because no two of them share a satisfying assignment, as in the paper's proof

* `boundsFrom`, `stBounds`: the bounds on the tree (number of leaves, clauses of a leaf, stack),
  without the sum. They come from `CountKSat.stProgC` as in proof/consequences/SplitCount/; that
  theorem has three hypotheses: the sum at one step, which gets `StStepAdds`, and
  proof/consequences/CountKSat/'s own `CountKSat.stRootCount` and `CountKSat.stSumLeaves`. Its sum
  over the leaves is dropped.
* `stepTwoFrom`: step 2 of the proof (`SplitCount.StStepTwo`) from `StTreeAddsUp` and `StBounds`,
  which are hypotheses. `StBounds` has no sum, so the sum over the leaves in the result can only be
  that of `StTreeAddsUp`.
* `engineCountsFrom`, `countsFrom`, `tiedFrom`: the last steps of
  proof/consequences/SplitCount/Main.lean, repeated with step 2 as a hypothesis.
* `countingCorollary`: `SplitCount.endFrom` on them. 

### `boundsFrom`

 **The bounds on the tree, without the sum**, from the sum at one step (`StStepAdds`), which is a
hypothesis: for every k and ε > 0 some threshold parameter τ gives a tree with at most 2^{εn}
leaves, O(n) clauses in each leaf and a short stack. The thresholds are those of
`WidthK.stExistsTau`; the bounds are those of `CountKSat.stProgC`, which gets the hypothesis for the
sum at one step and proof/consequences/CountKSat/'s own `stRootCount` and `stSumLeaves`;
`SplitCount.sparsifiesPlain_of` carries them to the tree whose side list starts empty; its sum over
the leaves is dropped. 

### `stBounds`

 **The bounds on the tree, without the sum**: `boundsFrom` on `stStepAdds`. 

### `stepTwoFrom`

 **Step 2 of the proof of Corollary 6**, from two statements taken as hypotheses: the numbers of
the leaves add up to that of the given formula (`StTreeAddsUp`), and the bounds on the tree
(`StBounds`, which has no sum). The proof only puts the pieces together: the sum is that of
`StTreeAddsUp` at the depth Dd·n. 

### `engineCountsFrom`

 `SplitCount.StEngineCounts` with step 2 as a hypothesis: for every k ≥ 1 and δ > 0 there are ℓ
and τ such that `ENGINEsplit k ℓ τ` has polynomial-time steps and serves as the procedure for #k-SAT
with the exponent δ. 

### `countsFrom`

 `SplitCount.StCOUNTsplitCounts` with step 2 as a hypothesis: for every k ≥ 1 and δ > 0 there are
ℓ and τ such that `COUNTsplit k ℓ τ` has polynomial-time steps and writes the number of satisfying
assignments of a k-CNF on n variables, in n + 1 bits, within c·2^{δn} steps. 

### `tiedFrom`

 **The tied statement of proof/consequences/SplitCount/ with step 2 as a hypothesis**: for every
k ≥ 1 and δ > 0 there are ℓ, τ, a Turing machine M with finite alphabets and numbers c, q such that
`COUNTsplit k ℓ τ` has polynomial-time steps and counts within c·2^{δn} steps, M simulates it with
polynomial overhead, and M counts the satisfying assignments of k-CNFs within ⌊c·2^{δn}⌋ steps. 

### `countingCorollary`

 **Corollary 6**, in the wording of PaperSentencesStatement.lean: `SplitCount.endFrom` on
`tiedFrom`, `stepTwoFrom`, `stTreeAddsUp` and `stBounds`. The sum over the outputs of the
sparsification comes from «no two of which share a satisfying assignment». 
