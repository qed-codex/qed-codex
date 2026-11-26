---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Upper/TagPolynomialBranches.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/TagPolynomialBranches.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/TagPolynomialBranches.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Polynomial branches in the heterogeneous tag construction

The determinant branches retain their actual output coordinates; finite
coordinate equivalences identify their classes with polynomial multiplication.
The middle tripling branch is a last-two-leg swap followed by the stated
invertible reversal of the shared first coordinate.


### `determinantQuotientTensor`

 The larger retained branch of the determinant filtration. 

### `determinantKernelTensor`

 The smaller retained branch of the determinant filtration. 

### `ofTensor_determinant_uniform`

 The uniform separation input is the whole graded determinant tensor. 

### `ofTensor_determinant_family`

 Both original polynomial branches survive zero padding exactly. 

### `triplingReverseEquiv`

 This reversal is an actual equivalence, including the empty finite type. 

### `ofTensor_triplingMiddle`

 The middle branch is evaluated using the permuted character. Its
first-coordinate reversal is removed only by an invertible local map. 

### `determinant_family_value_pos`

 Positivity for every padded determinant branch follows from the already
established positive polynomial character values. 

### `tripling_middle_value_pos`

 The positive middle value uses the actual permuted character. 

### `tripling_family_value_pos`

 These strict positive values are the hypotheses of the uniform tag
inequality, including the padded and reversed middle branch. 
