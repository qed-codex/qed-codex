---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Upper/Character/Degeneration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/Character/Degeneration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/Character/Degeneration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Characters and polynomial degenerations

Restriction monotonicity suffices for a polynomial degeneration.  For each
fixed family, interpolation of its tensor powers costs only linearly many
copies.  The elementary estimate below removes that overhead without any
assumed continuity of the character.


### `le_of_pow_le_linear_mul_pow`

 A fixed linear overhead cannot mask a strictly larger exponential rate.
The proof uses Bernoulli's inequality twice, rather than a limit theorem. 

### `Character.polynomial_constant_le`

 Every normalized restriction-monotone character is monotone on the
constant coefficient of an actual bounded polynomial restriction family.
The degree is fixed before the tensor-power argument is applied. 
