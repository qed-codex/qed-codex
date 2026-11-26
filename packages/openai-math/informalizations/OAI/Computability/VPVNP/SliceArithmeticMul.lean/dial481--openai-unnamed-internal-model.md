---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticMul.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticMul.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticMul.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Multiplication in the advised polynomial basis

A companion operation multiplies by the adjoined root in the quotient by the
advised monic polynomial. Horner's rule multiplies two coefficient vectors
using exactly one round for each coefficient of the first input.


### `companion`

 The companion operation shifts the coordinates up one degree and uses the
advised monic relation to reduce the top coordinate. 

### `horner`

 Horner's rule traverses the coefficients from highest to lowest, using
one companion operation, one scalar multiplication and one addition per round. 

### `mul`

 Multiplication modulo the advised monic polynomial. 
