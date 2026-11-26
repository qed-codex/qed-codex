---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SpectralRank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SpectralRank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SpectralRank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rank defects of diagonal operators

The rank here is the dimension of the actual range of a linear map.  The main
bound is obtained by identifying that range with the span of precisely those
basis vectors on which the diagonal coefficient is nonzero.


### `range_eq_span_basis_images`

 A linear map's image is spanned by its values on any basis. 

### `range_eq_span_nonzero`

 For a diagonal operator, only the nonzero diagonal entries contribute to
the range; every corresponding basis vector does belong to that range. 

### `finrank_range_eq_card_nonzero`

 Exact finite rank, counted by basis indices with nonzero eigenvalue. 

### `finrank_defect_eq_card`

 Exact rank of `id - M`: each eigenvalue different from one contributes
one basis index, with its full multiplicity. 

### `finrank_defect_le_card_bad`

 A designated set of good indices need only have eigenvalue one. Extra
unit eigenvalues outside that set can reduce the rank further. 

### `rank_defect_le_weight_bad`

 Weight-indexed form of the rank estimate used in equation (5.5). 

### `mul_rank_defect_le_of_weight_tail`

 A natural-number tail estimate gives the corresponding multiplied rank
bound, without introducing division in the coefficient field. 

### `badWeightEquiv`

 Partition the bad basis indices according to their actual finite weight.
This is an explicit equivalence, so the later multiplicity sum counts each
basis vector exactly once. 

### `card_bad_eq_sum_fibers`

 Exact cardinality decomposition, before assuming a binomial law. 

### `sum_bad_fin_eq_range`

 Rewrite a sum over bad finite weights in the ordinary range-sum form. 

### `rank_defect_le_sum_fibers`

 Rank bounded by the exact sum of the dimensions of all bad weight fibers. 

### `rank_defect_le_binomial_tail`

 Conditional bridge to the manuscript's binomial multiplicities. The
independently checkable `hmult` hypothesis records the tensor-basis count;
the rank inequality itself is proved rather than assumed. 

### `JointBasisIndex`

 Labels of the genuine joint-fiber eigenbasis: an unused-word assignment
and one local eigenvector label at each active position. 

### `jointEigenbasis`

 Transport the explicitly constructed product eigenbasis to the actual
joint fiber of universal types. 

### `jointEigenbasis_coordinate_eigen`

 The transported basis has the expected eigenvalue under the active
coordinate permutation. No diagonalization hypothesis is used here. 

### `jointEquivPairs_jointSwap`

 The concrete universal-type bit swap agrees with the independent-coordinate
swap after decomposing the joint fiber. 

### `jointEigenbasis_swap_eigen`

 The actual matrix-construction swap acts diagonally on the transported
joint basis. 

### `negativePositions`

 Active positions at which the local basis label is the negative eigenvector. 

### `jointWeight`

 Integer weight of a joint-basis index, unaffected by the spectator words. 

### `jointSign`

 Sign profile on all positions; its value at the pinned position is one. 

### `card_jointWeight`

 Exact multiplicity on the actual joint eigenbasis, including all unused bits. 

### `card_bad_jointWeight`

 Exact bad-weight cardinality for the concrete joint eigenbasis. 

### `joint_rank_defect_of_eigenaction`

 For this concrete basis, the integer binomial tail gives the desired
relative rank bound. Only the operator's eigenaction remains to be supplied. 

### `coefficientEigenvalue`

 The weight-dependent scalar appearing in the spectrum of the matrix (5.4). 

### `jointMatrix_eigenbasis`

 Spectral action of the shared concrete matrix on the actual joint basis. 

### `jointMatrix_rank_bound`

 Equation (5.5) for the actual matrix used by the support construction.
The coefficient interpolation and finite integer tail are the only numerical
hypotheses; the spectrum, multiplicities, and rank bound are all derived. 

### `jointMatrix_parity_rank_bound`

 The constructed parity-interpolation coefficients discharge the entire
spectral interpolation hypothesis of the concrete rank bound. 
