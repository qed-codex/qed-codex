---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/SeparationWeights.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/SeparationWeights.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/SeparationWeights.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integer phases and weights for auxiliary separation

The phase modulus `5M` has no nonzero multiple on the label interval. After
projection, the Laurent weight is a square and vanishes exactly when the
sector guess and the auxiliary labels agree. These are local identities;
they do not assert the tensor separation or its tag inequality.


### `projection_does_not_wrap`

 The paper's one-based label convention. 

### `projection_does_not_wrap_fin`

 The same no-wrap property for finite labels numbered from zero. 

### `projected_square_weight`

 The weight identity is independent of the choice of zero- or one-based
labels. 

### `squareExponent`

 The nonnegative exponent used after the Fourier projection. 
