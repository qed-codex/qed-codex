---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Sunflower.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Sunflower.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Sunflower.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The elementary sunflower bound and its literal-occurrence corollary. 

### `IsSunflowerWithCore`

 A finite family with a specified common core. Empty cores are allowed. 

### `SunflowerFree`

 No subfamily of exactly `z` members is a sunflower, even with empty core. 

### `link`

 The link at `x`, represented by removing `x` from sets which contain it. 

### `PairwiseDisjoint`

 Pairwise disjointness of a finite family. 

### `exists_disjoint_cover`

 A maximal disjoint subfamily hits every nonempty member of the original family. 

### `uniform_card_le`

 The elementary sunflower bound, proved by induction on the common set size. 

### `exists_sunflower_of_card_gt`

 If a uniform family exceeds the bound, it contains a sunflower of the requested size. 

### `NonemptyCoreSunflowerFree`

 Absence of sunflowers with nonempty core; disjoint families remain permitted. 

### `nonemptyCoreSunflowerFree_link`

 In a link even empty-core sunflowers are forbidden, because the deleted element
is restored to their core. 

### `occurrence_card_le`

 The number of members containing a fixed element in a uniform family with no
nonempty-core sunflower. The formula is valid even in width zero. 

### `literal_occurrence_le`

 Appendix A.2's per-literal bound, for width `j` inside an arbitrary family. 

### `unit_literal_occurrence_le`

 Distinct unit sets give the separately specified bound `L₁ = 1`. 

### `literal_total_occurrence_le`

 Summing the width-specific degrees bounds the total degree of one literal. 

### `variable_occurrence_le_of_literal_bound`

 A variable has two signs, so a common literal-degree cap gives twice that cap
for the number of clauses containing the variable. 

### `terminal_occurrenceAtMost`

 Terminal sparsification leaves satisfy the manuscript's total variable cap.
Width zero contributes no occurrences; width one uses distinctness of clauses. 
