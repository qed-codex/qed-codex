---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Speedup/Strict.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Speedup/Strict.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Speedup/Strict.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Supporting lines to the gain from a group 


# Grouped speedup for spectral points

Apply pole cancellation on the dense locus of spanning pivots, then
extend the price inequality to arbitrary decompositions. Subadditivity
lets us treat each full group independently.



# The square speedup constant

For groups of size `⌈v s²⌉`, the normalized gain tends to the profile at
`v`. The profile is zero at two and tends to zero at infinity, so its
positive maximum is attained in the open range.



# Detecting a full-support product at an ordinary maximizer

Mixed powers of the weighting and ordinary multiplication still have
full support. Their unconditional exact rank lower bound thus detects
a point maximizing the ordinary price without losing weighted price.


 # Mixed products of full-support and ordinary tensors 

### `Dominates.line`

 A uniform linear upper bound on two log-prices transfers from
the full-support weightings to their ordinary products. Integer
multiplicities approximate any nonnegative real slope. 

 # Right-hand slopes of the three-side exponent 

### `partialRight_spec`

 A maximum of affine price functions has an increasing secant slope.
The slope at zero is interpreted from the positive side, even on a face. 


# Grouped speedup for geometric border rank

Take a point maximizing the ordinary tensor while detecting the weighting.
An orientation with largest wire exponent achieves at least the average
exponent weighted by the three logarithmic side lengths. Spectral
sublevels are closed, so the group estimate survives geometric closure.


### `BorderRankLE.grouped`

 The grouped bound holds with the actual exponent, without assuming
a formula for its value. 


# Speedup with any one-sided slope

Linearize both terms of the grouped price bound at the proposed
ordinary value and directional slope. The resulting linear upper
bound on log-prices transfers to the ordinary product by mixed powers.


### `BorderRankLE.directional`

 Every one-sided partial derivative can replace the average
exponent. In particular one may take the largest of the three. 


# Strict speedup and the square surplus

If the asymptotic minimum exceeds every leg dimension, take a power
where it exceeds three times the largest dimension. At least one full
group then gives a strictly positive gain.

