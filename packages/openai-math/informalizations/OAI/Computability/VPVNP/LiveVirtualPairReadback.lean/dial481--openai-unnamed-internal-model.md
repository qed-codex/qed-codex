---
{
  "module": "OAI/Computability/VPVNP/LiveVirtualPairReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveVirtualPairReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveVirtualPairReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The canonical virtual pair's reset memory in the live shadow array 

### `physicalPairIndex`

 Transport a fixed-program pair index to the actual execution group's auxiliary index type
using equality of the two chain heights. 

### `VirtualPairs.shadow_initial`

 The sparse-copy entry of the actual live machine agrees at every
address with the reset memory of the canonical auxiliary pair. This
includes the seven input arrays, unoccupied sparse slots and unused RAM. 
