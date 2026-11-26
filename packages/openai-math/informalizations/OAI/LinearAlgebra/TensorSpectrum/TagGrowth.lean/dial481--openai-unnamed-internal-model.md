---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/TagGrowth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/TagGrowth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/TagGrowth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Removing polynomial overhead from tensor-power inequalities

A fixed polynomial factor cannot compensate for a strictly smaller exponential
base. The exponent of the overhead may be any fixed nonnegative real number.
This is the scalar limit step used after the finite-word tag decomposition.


### `le_of_pow_le_polynomial_mul_pow`

 Remove a fixed real polynomial overhead from an inequality valid for every
positive tensor power. This statement includes zero exponential bases. 
