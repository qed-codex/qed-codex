---
{
  "module": "OAI/Algorithms/SubexponentialSAT/BranchTree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BranchTree.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BranchTree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Counting binary branch-tree paths

False labels an A edge and true labels a B edge. A word is encoded injectively
by its length and the finite set of positions occupied by B. This proves the
finite counting step in Appendix A.3 without any analytic hypotheses.


### `bPositions`

 The zero-based positions of B edges in an actual binary path. 

### `bPositions_subset`

 The B-position set is contained in the range of the path length. 

### `eq_of_length_bPositions_eq`

 Depth and B positions determine every edge of a binary path. 

### `pathCode`

 The concrete code used in the manuscript. 

### `positionSets`

 All possible B-position sets of size at most R in a D-position ambient set. 

### `card_paths_le`

 Every finite collection of actual binary paths obeys the node-count bound.
Prefix closure is unnecessary for this stronger statement. 

### `Tree`

 A finite rooted binary tree, with A as its left edge and B as its right edge. 

### `Tree.paths`

 All root-to-node paths, including the empty path to the root. 

### `Tree.nodeCount`

 The number of actual nodes of this finite tree. 

### `Tree.nodeCount_le`

 Appendix A.3's finite-tree bound, with every internal node included. 

### `Tree.nodeCount_le_sparsification`

 The paper's exact floor convention: natural division is floor division. 

### `card_paths_le_of_choose_le`

 Any pointwise binomial estimate produces precisely this polynomial factor. 

### `choose_le_rpow_real`

 A uniform binomial estimate valid at a real, not necessarily integral, cutoff. 

### `card_paths_le_rpow_real`

 The finite path bound with an arbitrary positive real cutoff. 

### `card_paths_le_two_rpow`

 The only budget used here is the explicit logarithmic exponent inequality. 

### `card_paths_le_sparsification_exponential`

 Appendix A.3, including floor division and the n=0 case, under its stated
fixed-parameter budget. This is an actual bound on finite path cardinality. 

### `Tree.nodeCount_le_sparsification_exponential`

 The exponential estimate applies to the actual number of tree nodes. 

### `Tree.nodeCount_le_of_admissible`

 No analytic hypothesis remains once the constants module supplies its
integer admissibility certificate. The remaining premises are the two
combinatorial path bounds to be established for the sunflower process. 

### `Tree.nodeCount_le_chosen_parameters`

 The deterministic selected constants meet the exponent budget for every
input size. Their dependence on k is explicit; there is no n-dependent choice. 

### `polynomial_prefactor_bound`

 The factor suppressed by `poly_k(n+1)` is at most a quadratic polynomial,
even without using M > 0. 

### `Tree.nodeCount_le_quadratic_exponential`

 A concrete quadratic polynomial dominates all of the node-count prefactors. 
