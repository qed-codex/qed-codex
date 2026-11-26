---
{
  "module": "proof/rates/GeneralPieces/Group/CaseII.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Group/CaseII.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Group/CaseII.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 8 (Appendix A), case (ii): some grouping has exactly g/K nodes in every group and Y < (U + 2ζgP)/K²

The proof of Appendix A, sentence by sentence, by counting instead of probability. The sample space
is the set of all permutations e of the g = K·n nodes; the grouping that belongs to e is χ₀∘e,
where χ₀ is one fixed grouping with n nodes in every group. "With probability at most ε" reads "for
at most ε·(K·n)! permutations". The order of the file is that of the text: the random grouping
(`group_uniform`), Hoeffding's inequality (`hoeffding_sample`, `exp_le_inv`), the numbers c_a and U
(`cz`, `cs`, `tot`), the two kinds of events (`event_first_kind`, `event_second_kind`), the union
bound
(`card_events_lt`, `exists_no_event`), the display (`display_left`, `display_right`), and the claim
(`GeneralPieces.stCaseII`). 

 ### The random grouping 

### `cls_eq`

 The group number γ of the grouping χ₀∘e, written out. 

### `card_group`

 "Let χ be uniformly random among the groupings in which every group has exactly g/K nodes":
every grouping χ₀∘e has exactly n = g/K nodes in every group. 

### `group_uniform`

 "Then each G_γ is a uniformly random set of g/K nodes": if at most the fraction ε of all sets of
n nodes have a property, then for at most the fraction ε of all permutations e the group γ of χ₀∘e
has it. 

 ### Hoeffding's inequality for sampling without replacement 

### `hoeffding_sample`

 "The sum S of a uniformly random set of j entries of a list of numbers in [0, R] satisfies Pr(S
≥ E S + ζjR) ≤ exp(−2jζ²)." Here E S is j times the mean of the list. The text cites this; the
proof is `ClauseBound.Group.card_sample_tail_le`. 

### `exp_le_inv`

 "Which for j = g/K is at most 1/(2gK)", because 2ζ²g ≥ K·ln(2gK). 

### `group_tail`

 Hoeffding's inequality for the sum of a list x of numbers in [0, R] over the group number γ: its
expectation is (Σ x)/K, and j = n. 

 ### The numbers c_a and U 

### `cz`

 "Let c_{a,a} = 0": the numbers c_{a,b} as reals, with 0 on the diagonal. 

### `cs`

 "c_a = Σ_{b ∈ [g]} c_{a,b}". 

### `tot`

 "So that U = Σ_{a ∈ [g]} c_a". 

### `cs_eq`

 c_a is the sum of c_{a,b} over the nodes b ≠ a. 

### `tot_eq`

 U is the sum of c_{a,b} over the ordered pairs of different nodes. 

 ### The two kinds of events 

### `event_first_kind`

 The event of the first kind, one for each group γ: "apply the inequality to Σ_{a ∈ G_γ} c_a,
with R = P and expectation U/K". The event Σ_{a ∈ G_γ} c_a ≥ (U + ζgP)/K has at most the
fraction exp(−2(g/K)ζ²) of all e. 

### `event_second_kind`

 The event of the second kind, one for each node a and each group γ': "apply the inequality to
Σ_{b ∈ G_γ'} c_{a,b}, with R = P/g and expectation c_a/K". The event
Σ_{b ∈ G_γ'} c_{a,b} ≥ (c_a + ζP)/K has at most the fraction exp(−2(g/K)ζ²) of all e. 

 ### The union bound 

### `card_events_lt`

 "These are (g+1)K < 2gK events." 

### `exists_no_event`

 "So for some χ none of them occurs. For this χ we have Σ_{a ∈ G_γ} c_a < (U + ζgP)/K and Σ_{b ∈
G_γ'} c_{a,b} < (c_a + ζP)/K for all γ, γ' and a." 

 ### The display 

### `Yg`

 Y_{γ,γ'} for the groups of χ₀∘e: the sum of c_{a,b} over a ∈ G_γ and b ∈ G_γ'. 

### `display_left`

 The first inequality of the display, "summing the second bound over the g/K nodes a ∈ G_γ, where
γ ≠ γ'": Y_{γ,γ'} < (1/K)·Σ_{a ∈ G_γ} c_a + (g/K)·(ζP/K). 

### `display_right`

 The second inequality of the display, "inserting the first": (1/K)·Σ_{a ∈ G_γ} c_a +
(g/K)·(ζP/K) < (U + 2ζgP)/K². 

### `stCaseII`

 The existence claim in the proof of Lemma 8 (Appendix A), case (ii). 
