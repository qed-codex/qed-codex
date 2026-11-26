---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Descent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Descent.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Descent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `descendWeighted`

 A degree-`d` extension increases the cost of descending a rank witness
by at most a factor of `d²`. Only the two input legs are expanded in a basis.
A linear functional sending one to one recovers the output coefficients,
even in characteristics dividing `d`. 
