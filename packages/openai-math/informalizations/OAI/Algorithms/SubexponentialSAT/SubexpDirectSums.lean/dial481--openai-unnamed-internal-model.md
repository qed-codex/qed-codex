---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpDirectSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpDirectSums.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpDirectSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Arbitrary-color supported direct sums

The coordinate split is an actual linear equivalence: it restricts to each
pairwise-disjoint color support and to their complement. Its inverse is the
sum of the zero-extended pieces. A separate map realizes the direct sum of
any subspaces supported on those sets and proves exact additivity of dimension.


### `coordinateExtend`

 Zero extension from one finite coordinate support. 

### `coordinateExtend_restrict`

 Restricting a supported vector and extending it back loses no information. 

### `colorAssemble`

 Sum all zero-extended color pieces. 

### `coordinateAssemble`

 Reconstruct all coordinates from the complement piece and the color pieces. 

### `coordinateSplitEquiv`

 Restriction to disjoint coordinate supports and their complement is a
linear equivalence for every finite number of colors. 

### `coordinate_card_partition`

 Exact dimension accounting for the ambient coordinate split. 

### `subspaceSumLinear`

 The actual sum map from a family of ambient subspaces. 

### `colorSumSubspace`

 The ambient sum of the color subspaces. 

### `colorSumEquiv`

 Disjoint coordinate support turns the sum into a direct sum. 

### `card_packedSupportFinset`

 Exact size of a local support after placing it in every packed block. 
