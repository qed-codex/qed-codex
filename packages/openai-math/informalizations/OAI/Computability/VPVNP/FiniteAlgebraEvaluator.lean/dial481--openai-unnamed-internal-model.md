---
{
  "module": "OAI/Computability/VPVNP/FiniteAlgebraEvaluator.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FiniteAlgebraEvaluator.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FiniteAlgebraEvaluator.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theorem 8.1 of “VP and VNP differ over every field”

The fixed two-tape table reads the initialized Macaulay and Cramer workspaces
from its polynomial-length advice. At each satisfiable length the same
advised algebra and functional apply to every exponent width. All literal
branches halt by the uniform clock, including the rejecting index guesses.


### `fields`

 Fixed order of the work and advice fields in the evaluator's binary prefix. 

### `program`

 The same literal machine table serves every input length and exponent
width, in positive characteristic and in characteristic zero. 

### `finiteEvaluatorGround`

 Finite enumeration of the slice ground field for the finite-algebra evaluator. 

### `finiteEvaluatorAmbient`

 Algebra structure on the ambient algebraic closure induced by embedding the slice ground
field. 

### `HasFiniteAlgebraEvaluation`

 The advised finite reduced algebra and its computation at one length.
The radius bounds all visited head positions and the full encoded tape state. 

### `finite_algebra_evaluator`

 The finite reduced algebra, its solution, the advised prime and the fixed
binary evaluator at every sufficiently large satisfiable length. 

### `finite_algebra_evaluator_of_small_circuits`

 The same fixed evaluator and length exponents at every exceptional small
circuit in the fixed characteristic. The polynomial is computed exactly and
its circuit may contain arbitrary field constants. 
