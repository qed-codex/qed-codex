---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Integral/Upper/SeparationInterpolation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/SeparationInterpolation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/SeparationInterpolation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Polynomial coefficient extraction by actual restrictions

Every coefficient of a bounded polynomial tensor is a linear combination of
evaluations at common interpolation nodes. If those evaluations are local
restrictions of one source tensor, the coefficient is a restriction of the
full direct sum of that many source copies. Applying this to tensor powers
gives the linear interpolation overhead required by restriction-monotone
characters. No continuity of a character on a Euclidean closure is assumed.


### `restrict_directSum_sum`

 Independent maps on each full source copy may have the same target. The
result is the sum of their restricted tensors, with no cross-copy terms. 

### `restrict_scale_first`

 Scaling one local map scales the whole restricted coefficient tensor. 

### `restrict_power`

 Tensor products of the local maps give a local restriction of every power.
Every input coordinate in every position is summed independently. 

### `polynomial_coeff_mem_restrictionOrbit`

 Interpolation at any common family of distinct nonzero nodes turns actual
restriction witnesses for the evaluations into one restriction witness for the
coefficient. The full number of source copies is charged explicitly. 

### `polynomial_power_mem_restrictionOrbit`

 The finite interpolation bound before applying any character. For every
power `j`, exactly `K*j+1` copies of the power of the original source suffice.
The infinite field supplies distinct nonzero nodes. 
