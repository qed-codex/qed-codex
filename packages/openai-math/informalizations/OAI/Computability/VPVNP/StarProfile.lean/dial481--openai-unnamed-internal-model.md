---
{
  "module": "OAI/Computability/VPVNP/StarProfile.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StarProfile.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StarProfile.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The width profile of a spectral point

Theorem 2.4 takes the supremum of the normalized spectral values of nonzero
tensors with local dimensions `2 ^ (h * w j)`. The coordinate rank bound
makes this supremum finite. It controls arbitrary covectors on a powered star,
including entangled covectors and the power zero.


### `StarWitness`

 A positive height and a nonzero tensor of the dimensions of the width profile. 

### `StarWitness.height`

 Positive integer scaling the logarithmic local dimensions in a witness for the width
  profile. 

### `StarWitness.coeff`

 Nonzero tensor coefficient array with local dimension `2 ^ (height * w j)` at party `j`. 

### `tensor`

 Package the coefficients and the prescribed bases into an old-party tensor. 

### `starRate`

 The supremum in equation (2.1), for a fixed integer width at every old party. 

### `starWitness_log_le`

 Coordinate rank bounds each normalized logarithm by the sum of local widths. 

### `starRate_isLUB`

 The defining supremum is the least upper bound of a nonempty, bounded set. 

### `value_le_starRate`

 Apply the profile to arbitrary finite local bases of the prescribed cardinalities. 

### `starPower_contraction_le`

 An arbitrary contraction of a star power has the advertised spectral upper bound. 

### `value_tensorPowerFin`

 Finite powers have the usual spectral value, also at exponent zero. 

### `starPower_exists_packed`

 The packed copies and their simple padding have exactly the value of the unpadded power. 

### `contractionValue_starPower_le`

 Real upper bound on the supremum over all center covectors. 

### `starPower_contractionRoot`

 The contraction values of the powered old factor and star in the proof
of Theorem 2.4 have the prescribed exponential rate. 

### `value_dyadicStar`

 The spectral value of the dyadic star is the exponential of its weighted wire sum. 

### `starRate_le_extension`

 Every extension of the given spectral point has weighted star length at
least the old width-profile rate. 
