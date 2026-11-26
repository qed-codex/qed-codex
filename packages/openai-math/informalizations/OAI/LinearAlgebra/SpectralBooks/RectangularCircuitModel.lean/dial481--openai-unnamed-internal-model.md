---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/RectangularCircuitModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/RectangularCircuitModel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/RectangularCircuitModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Cost-preserving translation between two division-free circuit models

The integral model records a set of available polynomials, while the formal
model names registers. Both allow free loads of inputs and field constants. 

### `program_build`

 Reading the registers in order builds their polynomials at the same cost. 

### `CanRead`

 A finite selection suffices even when the initially available constants form an infinite set. 

### `computes_iff`

 Integral circuits order dimensions as rows, columns, inner dimension. 

### `formalOmega_eq_integral`

 The admissible exponents agree after translating wire order to matrix dimensions. 

### `formalOmega_max_zero`

 Negative weights and zero give the same rounded dimension at every admissible scale. 
