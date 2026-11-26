---
{
  "module": "OAI/Computability/VPVNP/ComplexityLib/Circuit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ComplexityLib/Circuit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ComplexityLib/Circuit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Simulation of complexitylib arithmetic circuits

The program below keeps every upstream wire at its original index. Each upstream constant gate
becomes a binary gate adding the given scalar to zero. Thus every designated output has a
project circuit of exactly the upstream size, even when multiple operands use the same gate.


### `circuitSize_le_upstream`

 An upstream arithmetic circuit has a project circuit for each designated output with
the same number of gates, evaluated in the formal polynomial ring. 
