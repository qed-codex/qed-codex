---
{
  "module": "OAI/Computability/VPVNP/PairSimulationVertexControlFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationVertexControlFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationVertexControlFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The vertex memory frame along successful prefixes of the terminal program 

### `ordinalWorkerControl`

 Each successful vertex call preserves the protected address, including on a
prefix that never reaches the closing ordinal. A continuing call advances the
ordinal and preserves the linked frame after the controller stores its result. 
