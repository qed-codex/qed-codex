---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Prices/Tensor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Prices/Tensor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Prices/Tensor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Imposing one price bound

For a target r strictly above the tested price of X, replace the
additive functional M(U) by the sum of M(X^n U) / r^n over n.
Shifting the index gives the desired inequality. All earlier linear
inequalities stable under multiplication are preserved.



# The additive closure envelope

Take the supremum of the old spectral value over tensors obtained from
a restriction with trivial output legs at the added sites.



# Simultaneous price extension

We work with spectral values, i.e. exponentiated unit-scale prices.
The test runs through finite lists with repetitions. It therefore
includes closures that couple arbitrarily many copies.


### `character_of_products`

 Turn the linear closure bounds into a single multiplicative evaluation. 

 # Assisted costs and simultaneous interpolation 

### `ExtensionData`

 Uniform hypotheses for ordinary and valued price extensions. 

### `assisted`

 The exponentiated assisted cost. All positive powers and all restrictions
to a tensor with trivial legs at the added sites are tested. 

### `assisted_extension_iff`

 The product test in terms of assisted costs. 

### `interpolate`

 Interpolate all tensor evaluations at once, preserving the old price. 


# Extending an ordinary tensor price

We use spectral values so that zero needs no infinite logarithm.
By `pad_le_ofRaw_iff`, testing `pad U B ≤ A` is equivalent (for
monotone prices) to testing every simultaneous closure of A at U.
Each functional has access to the entire local space of its site.


### `assisted`

 The exponentiated assisted cost. All positive powers and all restrictions
to a tensor with trivial legs at the added sites are tested. 

### `assisted_extension_iff`

 The product test in terms of assisted costs. 

### `interpolate`

 Interpolate all tensor evaluations at once, preserving the old price. 
