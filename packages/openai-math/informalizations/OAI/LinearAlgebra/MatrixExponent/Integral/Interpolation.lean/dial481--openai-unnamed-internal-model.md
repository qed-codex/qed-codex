---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Integral/Interpolation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Interpolation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Interpolation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Polynomial interpolation over algebraic integers 

### `scoped instance : Pow O ℤ`

 These integer powers are used only on units, apart from
nonnegative exponents. 

### `phases`

 Shift signed exponents into a range of length six times the
branch count. Interpolation extracts the central coefficient. 
