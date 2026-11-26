---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Sparse/Entropy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Sparse/Entropy.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Sparse/Entropy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Measuring the support by a weighted count

In a fixed empirical type all three completion counts are constant.
The number of types is polynomial in the power. Consequently the
coloring loss and the cost of selecting a single type disappear.


 # The entropy refinement for sparse weighted products 

### `entropy_lower`

 Natural-log form with the actual arithmetic exponent. 

### `support_exponent`

 The bound in bits from Section 8. No rigidity premise is needed. 


# Preservation of the exponent at subpolynomial density

The lower bound allows both the support and the coefficients to vary
with the size. All-ones weightings attain the exponent even for exact
rank, by taking powers of a single slightly more efficient block.

