---
{
  "module": "OAI/Computability/VPVNP/StarGrowth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StarGrowth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StarGrowth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Growth of contractions of a powered star

Section 2.3 of *VP and VNP differ over every field* computes the exponential
rate of the supremum of the values of contractions at a new party. A tensor
with local widths indexed by `h` fits into `u*m` copies of the width profile
exactly `u*m/h` times, using natural-number division.


### `packedCopyRatio_tendsto`

 The fraction of the power occupied by copies of a fixed witness has the
limit used in the star construction. 

### `packedStarRoot_tendsto`

 Taking roots in the value of a single packed witness. 

### `starContractionRoot_tendsto`

 In the star case of Theorem 2.4, `I` indexes the pairs of a positive
width parameter and a nonzero old tensor of that width. `g` is the supremum
of their normalized log values, `a` is the old factor's value, and `C m` is
the supremum of the contracted values of the monomial's `m`-th power.
The packing and contraction inequalities imply the claimed root limit, even
for zero star multiplicity. 

### `exists_gt_half_of_isLUB`

 A positive contraction supremum admits a contraction strictly above half its value. 

### `limit_le_of_half_power_bound`

 Any fixed multiplicative loss disappears after taking the `m`-th root. It is
sufficient for the power estimate to hold on an unbounded set of integers. 
