---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyProjectionAccess.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyProjectionAccess.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyProjectionAccess.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Memory used to prepare the shrinking tag operands

The first pass reads the old displacement column and writes the projected
tags. The second pass publishes their zero operand. Both label computations
can still read the old directed incidence tables afterward.

