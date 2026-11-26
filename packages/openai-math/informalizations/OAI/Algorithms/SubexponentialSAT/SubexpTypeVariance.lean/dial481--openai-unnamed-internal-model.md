---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpTypeVariance.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTypeVariance.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTypeVariance.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Multicolor type assignment, explicit counts, and variance

This is Section 3.4 of the subexponential manuscript. Every parameter, including
the number r of colors, remains explicit. The probability space consists of
actual independent words at factor, head, and padding indices. Uniformity and
independence are proved from injective/disjoint coordinate reads.

The local completion bound is the square of the universal type cardinality.
No construction cost is hidden in a constant depending on r, Q, or Δ.


### `wordTypeEquiv`

 A head word and one word for each slot are exactly a multicolor type. 

### `assignmentType`

 The multicolor type read by a coordinate from the independent word assignment. 

### `mean_assignmentType`

 Exact uniform marginal law for every coordinate type, for every r > 0. 

### `mean_assignmentType_mul`

 Full pair-moment independence for coordinates that share no factor. 

### `mean_typeCount_explicit`

 The count has its claimed exact expected value D/N, with N displayed. 

### `assignment_deviation_eq_collisions`

 The collision identity makes every conditional expectation a sum of
functions of at most 2(Δ+1) word variables, plus a fixed constant. 

### `mean_squared_deviation_le`

 Expected discrepancy for the actual independent-word distribution. 

### `mean_squared_deviation_le_explicit`

 The same estimate with every growing parameter visible. 

### `exists_consistent_types_deviation_le`

 Consistent factor colors and a concrete type assignment with the discrepancy
bound needed for full-block packing. 

### `completion_count_le_type_choices_sq`

 Completing at most two local read sets requires at most N² assignments. 
