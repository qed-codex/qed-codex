---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/TagEntropy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/TagEntropy.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/TagEntropy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The finite weighted entropy inequality

The positive-parameter inequality is the weighted arithmetic--geometric mean
inequality applied to `c i ^ (1 / p) / q i`. Zero weights contribute the factor
one, and are treated before taking logarithms. The logarithmic AM--GM argument
below uses only `Real.log_le_sub_one_of_pos`.

The zero-parameter endpoint has a separate pointwise hypothesis: if every
`c i ≤ x`, then the weighted product is at most `x`.


### `weighted_log_le_log_of_sum_le`

 The logarithmic weighted AM--GM inequality, with an upper bound on the
weighted arithmetic mean. The weights may vanish. 

### `weighted_geometric_mean_le_of_sum_le`

 A product form of weighted AM--GM, proved from its logarithmic form. 

### `tag_entropy_product_le`

 The finite entropy/tag inequality for a positive real parameter.
The convention `x ^ (0 : ℝ) = 1` includes every zero weight. 

### `tag_entropy_product_le_of_bound`

 Compose the entropy inequality with a bound on the optimized power sum. 

### `weighted_geometric_mean_le_of_pointwise`

 A weighted product of positive numbers is bounded by any pointwise upper
bound. This is the endpoint needed when the tag parameter is zero. 

### `tag_entropy_product_zero_le`

 The zero-parameter tag inequality, in the same product notation as the
positive-parameter result. No limiting convention for `1 / p` is used. 

### `tag_entropy_product_eq_exp`

 Rewrite the quotient product as the exponential of the Shannon entropy
times the unnormalized weighted product. This identity also holds at `p = 0`
and at zero weights; it requires no normalization of the weights. 

### `tag_entropy_exp_le`

 The positive-parameter entropy inequality in exponential notation. 

### `tag_entropy_exp_le_of_bound`

 Compose the exponential entropy inequality with an optimized power-sum
bound, without further assumptions on the auxiliary parameter `x`. 

### `tag_entropy_exp_zero_le`

 The zero-parameter endpoint in exponential entropy notation. 
