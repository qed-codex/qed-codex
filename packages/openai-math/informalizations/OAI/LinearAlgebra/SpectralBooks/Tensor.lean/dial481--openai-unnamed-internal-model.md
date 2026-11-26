---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/Tensor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/Tensor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/Tensor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rectangular matrix multiplication over a field

We use the finite coefficient tensors and Kronecker powers from the matrix
multiplication library. The dimensions are the shared wire sizes, in the
paper's order `12, 23, 31`. The first site's coordinates are consequently
indexed by `Fin n31 × Fin n12`.


### `exists_rankAtMost`

 Expanding in the coordinate bases of the first two sites gives a finite
decomposition into simple tensors. 

### `tensorRank`

 The least number of simple tensors in a decomposition over the ground field. 

### `asymptoticRank`

 The infimum of the positive tensor-power rank roots. 

### `matrixTensor`

 The coefficient of the cyclic pattern `e_{ki} ⊗ e_{ij} ⊗ e_{jk}` is one. 
