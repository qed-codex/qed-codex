---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Derivatives.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Derivatives.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Derivatives.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Partial derivatives at the generic point

Perturb one input by a square-zero variable. Projection to the constant
term is the identity, so every nonzero polynomial maps to a unit. The
perturbation thus extends to rational functions in any characteristic.


### `partialD`

 Formal partial differentiation on the field of rational functions. 
