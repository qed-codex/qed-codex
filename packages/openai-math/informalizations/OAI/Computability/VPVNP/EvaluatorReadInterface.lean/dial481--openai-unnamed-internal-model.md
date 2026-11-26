---
{
  "module": "OAI/Computability/VPVNP/EvaluatorReadInterface.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorReadInterface.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorReadInterface.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coordinate-reader interface for the binary evaluator

The deterministic entry query takes the previous and chosen basis ordinals
in canonical binary registers. Its output is a packed element in the advised
field basis. This interface isolates the indexed Macaulay and Cramer computation
from the nondeterministic choices, finite-field multiplication and digit loops.


### `payload`

 Encoded current ordinal and scalar, between two successive linear steps. 

### `ReadsEntry`

 Deterministic finite-control entry query with a common time bound. It
restores the ordinal registers, the advised field and the caller's private
workspace. Its only output is the requested matrix entry. 

### `frobenius_realizes`

 Installing a Frobenius entry query gives the counted Frobenius callback
on every column, with the column and digit scheduler registers preserved. 

### `label_callback`

 Installing the formal-coordinate multiplication query gives the label
callback on all live label ordinals, including repeated visits in a digit. 
