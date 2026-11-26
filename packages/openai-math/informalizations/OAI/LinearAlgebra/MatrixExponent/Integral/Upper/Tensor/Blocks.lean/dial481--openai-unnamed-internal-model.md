---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Integral/Upper/Tensor/Blocks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/Tensor/Blocks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/Tensor/Blocks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Heterogeneous direct sums and restrictions

The two summands retain separate coordinates on every leg. Cross coefficients
are zero, and block diagonal local matrices give actual restriction witnesses.


### `blockSum`

 Direct sum of tensors whose three coordinate spaces may all differ. 

### `blockMatrix`

 Block diagonal local coefficient matrix, with no cross-summand maps. 

### `restrict_blockSum`

 Independent restrictions on the two summands combine into one restriction
on their full direct sum, including every vanishing cross coefficient. 

### `pullback_blockSum`

 Relabel the coordinates of each summand independently. 

### `Restricts.blockSum`

 Restriction is compatible with heterogeneous tensor direct sums. 

### `Restricts.product`

 Restriction is compatible with tensor products through the actual products
of the three local coefficient matrices. 
