---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Prices/Motion/Tripod.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Prices/Motion/Tripod.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Prices/Motion/Tripod.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Parameters for private products

First fix the power count to amortize the two index strings per private
output. Then take the rank slack small compared with the sparse saving.
Rounding up to a binary length and the fixed multiplicative constant
each consume at most one further rank slack.



# Short output sums from a strict dual threshold

A sparse row is evaluated by a short list of products specific to that
output. Each rank-one summand in the error matrix contributes just one
common bilinear form. The two within-pair wires pay for the short lists,
so the four-site obstruction does not need one private product per output.



# Private products below the harmonic threshold

The rectangular upper bound at inner width one half suffices.
Approaching that width from below leaves room for the power and
sparsification overheads without a strict dual improvement.



# Contact on three fixed rays

Apply the one-sided short-sum bound at the two moving sites. Its two
labels have identical wire distances. The universal harmonic lower
bound on one of them therefore gives an upper bound on the other.
Crucially the latter only uses the three stationary disk centers.



# A common limit for all three rays

Approximate real radii by rational ones before taking the limit.
Integer radii are represented exactly, so the collision bounds survive
at each of the integer lengths used to approach the reciprocal face.


### `ray_atlas`

 The same atlas works for every integer length. 


# A moving family forces contact at infinity

For each large integer `i`, shrink collision placements with fixed
ratio of radii `i : 1 : 1`. The short-output estimate bounds the
three-terminal diagonal at all these ratios on one homogeneous
tripod. This gives a zero of the defect on the reciprocal face.

