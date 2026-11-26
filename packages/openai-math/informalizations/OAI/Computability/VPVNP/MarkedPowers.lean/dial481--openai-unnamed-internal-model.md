---
{
  "module": "OAI/Computability/VPVNP/MarkedPowers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedPowers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedPowers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tensor powers of a marked index

In the proof of Lemma A.1, the same tensor power is placed at three different
parties. Regrouping the marked indices of its copies gives a single index of
dimension `q ^ n`, with the same coefficient table at each placement. The
rounded exterior levels then bound both terms of the split by the same geometric
mean to the power `n`.


### `markedPowerTable`

 The product of `n` copies of the coefficient table, with their marked indices
grouped separately from the background coordinates. 

### `marked_coeff_eq_zero_iff`

 Moving a marked index preserves whether the coefficient array is zero. 

### `marked_power_mutual`

 The regrouped marked array and the product of the original tensors have
mutually invertible local changes of basis, including for the zeroth power. 

### `SpectralPoint.value_markedPower`

 Spectral values of the regrouped marked table are the powers of the values
at the original placement. 

### `marked_reindex_mutual`

 Relabeling the marked index preserves the tensor up to invertible local
changes of basis. The background coordinates are arbitrary. 

### `markedPowerIndex`

 The index set used for the exterior operators on the powered tensor. 

### `SpectralPoint.value_markedPower_fin`

 The coefficient table with the marked tuples numbered from zero to `q ^ n - 1`
has the original spectral value to the `n`th power at every placement. 

### `relocation_log_bounds`

 Moving the index in both directions puts the balancing exponent in the
interval of exponents attainable by exterior powers. 

### `exterior_term_le`

 Compare a contribution from one endpoint to the target using its
logarithmic dimension bound. 

### `relocation_of_power_bounds`

 The positive powers and the two adjacent binomial ratios imply the
geometric interpolation inequality for the marked tensor. 
