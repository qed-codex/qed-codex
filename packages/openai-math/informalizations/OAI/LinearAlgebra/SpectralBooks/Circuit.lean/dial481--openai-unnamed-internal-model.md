---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/Circuit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/Circuit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/Circuit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # From formal scalar circuits to tensor rank

At a product gate only two new products of linear forms enter the bidegree
`(1,1)` component. We maintain one shared list of these products across *all*
registers, so fan-out and multiple matrix entries incur no additional cost.


### `multiplicationCount`

 Number of scalar multiplication gates. Register loads, additions and
subtractions contribute zero. 

### `mixedPart`

 The coefficient of the squarefree monomial indexed by a left and a right input. 

### `InProductSpan`

 A common collection of products can be linearly recombined to give this register. 

### `matrixTensor_rank_le_twice_multiplicationCount`

 A formal division-free rectangular matrix multiplication circuit with `s`
products gives an exact rank decomposition with at most `2s` simple tensors. 

### `matrixTensor_rank_le_twice_cost`

 The total number of operations also bounds the rank, with the same factor two. 
