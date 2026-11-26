---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Diagram/Pad.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagram/Pad.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagram/Pad.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Removing scalar stations from a diagram 

### `prune`

 Every wire end already belongs to a station of positive arity. 

### `eval_prune`

 The product of the removed tables is independent of all bit assignments.
It may vanish, so we factor it out without dividing by it. 

 # Independent copies of a directed network 

 # Deterministic circuits with a specified set of additional tables 


# Padding ordered bundles of parallel wires

Collect the bits between each ordered pair of stations, then extend
their binary word by zeros. Empty bundles remain empty.

