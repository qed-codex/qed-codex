---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/SpectralRank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SpectralRank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SpectralRank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual rank bounds for the multi-color swap construction

The linear-algebra input is the dimension of the actual range of `id - M`.
The local swap multiplicities and the finite tail are kept as ordinary natural
counts, and converted to real inequalities only at the final scaling step.


### `real_rank_defect_le_bad`

 The previously proved exact range computation gives a real rank bound
by the number of bad basis indices. 

### `scaled_rank_defect_le`

 Scale an actual rank bound by the number of slot constraints. 

### `scale_tail_bound`

 Spectator registers multiply the tail and the total mass by the same
ordinary integer. No field-characteristic condition enters this count. 

### `coefficientEigenvalue`

 The weight-dependent scalar in equation (3.5). 

### `scalar_signIndicator`

 Evaluate the actual elementary-symmetric expression at a sign profile.
The integer number of negative signs is retained before coefficients are
cast to the field, so this is valid when the truncation length exceeds the
characteristic. 

### `coefficientEigenvalue_parity`

 The constructed parity coefficients make that scalar exactly one at
every integer weight in the interpolation interval. 

### `normalizedTail`

 The probability of an integer weight outside the interpolation interval,
using the actual normalized tensor multiplicities. 

### `normalizedTail_eq_weightedTail`

 A common denominator converts the exact probability tail to the finite
integer multiplicity tail. 

### `normalizedTail_eq_binomial`

 The probability tail is exactly the source's binomial tail with negative
probability `(r - 1) / (2*r)`. 

### `normalizedTail_le_iff`

 The source probability bound and the denominator-cleared rank input are
equivalent when there is at least one color and one slot. 

### `matrixEigenvalue_signIndicator`

 Evaluate the scalar belonging to the same concrete matrix used by the
support theorem, rather than introducing a second matrix construction. 

### `jointMatrix_eigenbasis`

 The actual matrix acts diagonally on the explicitly constructed tensor
basis, with the integer number of negative local labels as its weight. 

### `jointMatrix_defect_rank_eq_card`

 Exact rank, retaining every tensor-basis multiplicity. This is useful
also when some eigenvalues outside the interpolation interval equal one. 

### `jointMatrix_rank_bound_real`

 Multi-color matrix rank bound in a form with no division. The tail uses
the actual positive and negative local multiplicities and is an ordinary
finite integer sum. 

### `jointMatrix_rank_bound`

 Rational form used by the authoritative multi-color layout interface. 

### `jointMatrix_parity_rank_bound`

 Constructed binomial interpolation coefficients discharge the coefficient
hypothesis without any restriction relating the color count to the field. 

### `jointMatrix_parity_rank_relative`

 The literal relative-rank conclusion of Lemma 3.1. 

### `jointMatrix_parity_rank_of_probability`

 Direct source-form wrapper: an actual binomial probability tail at most
`τ / Δ` bounds the rank defect of the concrete matrix by the same fraction. 

### `jointMatrix_parity_rank_relative_of_probability`

 The literal rank fraction, now with only the source probability-tail input. 
