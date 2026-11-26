---
{
  "module": "OAI/Computability/VPVNP/MacaulayFieldReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayFieldReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayFieldReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Coefficients of the actual matrix requested by the rank machine

The physical reader encodes elements of the advised finite field in a power
basis. Each row in the augmented matrix has exactly the coefficient described
by its shifted or powered branch, with the zero scalar on failed exponent
tests. The Cramer query uses this same encoded matrix.


### `shifted_matrix_entry`

 The original and affine rows differ only in their scalar coefficient
reader. Both use the multiplier and column monomial in this exact order. 

### `power_matrix_entry`

 Encoding a powered monomial row over the slice field yields the same
zero/one coefficient as testing its exponents in the native scalar type. 
