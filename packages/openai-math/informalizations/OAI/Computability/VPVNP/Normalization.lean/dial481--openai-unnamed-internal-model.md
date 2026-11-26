---
{
  "module": "OAI/Computability/VPVNP/Normalization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Normalization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Normalization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Additivity under subparty normalization

The direct-sum expansion on a subset of parties in Lemma 2.3 of *VP and VNP
differ over every field* has `m + 1` binomial groups. Bounding each group by
the whole expansion and the whole expansion by the sum of group values
suffices to recover exact additivity after normalizing by the diagonal
exponent.


### `tendsto_binomialGroupCount_root`

 The number of binomial groups has exponential growth rate one. 

### `le_of_binomialGroupCount_pow_le`

 A factor `m + 1` in a comparison of all powers disappears in the growth rate. 

### `normalizedAdditivity_of_binomialBounds`

 Lemma 2.3's binomial-group bounds imply additivity of the normalized
value. `h` is the positive exponent of the embedded local diagonal, `a` and
`b` are the normalized values of two tensors, and `z` is the normalized
value of their direct sum. 

### `normalized_multiplicative_value_add`

 The numerical bounds of Lemma 2.3 follow from the semiring binomial
expansion. The embedded tensor value is multiplicative, subadditive on
direct sums, and monotone under projection onto either direct summand. 
