---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafImageFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafImageFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafImageFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Preserving the other descriptor inputs, histogram and geometry at a leaf 

### `read_below`

 A successful physical leaf leaves every word below its allocated stacks
unchanged. This includes the cache of 38 actual auxiliary operands, the
geometry pointer and descriptors, the parent and sibling argument packets,
and the label histogram. 
