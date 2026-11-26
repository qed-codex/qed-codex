---
{
  "module": "proof/rates/GeneralPieces/Rec/Seq.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Rec/Seq.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Rec/Seq.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Parts (a) and (b) of the theorem on the general recursion as a clique solver with a sequence of indices, for every x₀ ≥ 18 with 2^x₀ ≥ c + 5

The index of level ℓ is the schedule of the steps from K_ℓ nodes down to K₀ nodes. Part (a) (K_ℓ <
K_{ℓ+1} ≤ K_ℓ^10, the bounds on e_ℓ) is `PartA.thmRunningTime_a`, used through `Num/PartAUse.lean`.
Part (b) has two halves: the
answer is right, by the statement on all levels under the hypotheses of case (ii) of the lemma on
groupings with explicit cost, because every step of the schedule is in order and a pad of
length 2^needG meets all budgets; and the exponent needG obeys the bound of part (b). As in Theorem
A of the paper, any such x₀ is allowed. 

### `pick_spec`

 What the program `ClauseBound.Gen.Pick.pick` does: from a bound in unary, in polynomial time,
the largest ℓ with K_ℓ ≤ bound (ℓ = 0 if the bound is below K₀) and the schedule of display (40) for
that ℓ. This is `ClauseBound.Gen.Pick.stPick` with the program named. 

### `seq_of_pick`

 The theorem on the general recursion, parts (a) and (b), in the form that the top levels use,
with a given program that picks the level. The constant is C₀ + 10 for the C₀ of part (b): the
fields `K_le` (K_{ℓ+1} ≤ K_ℓ^10) and `e_ge` want
it to be at least 10 and at least 1. 

### `stSeq2_of`

 The same from the five interface statements. 

### `stSeq2`

 The same from the two statements that are proved elsewhere: every step of the schedule is in
order, and all levels together give the value of the clique. 
