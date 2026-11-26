---
{
  "module": "OAI/Computability/VPVNP/PairSimulationStackSteps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationStackSteps.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationStackSteps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native realization of each elementary bit-stack instruction 

### `Frame`

 Frame condition across a native stack step, preserving the persistent state, registers
outside the stack bank, and private cells outside all stack intervals. 
