---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderAuxiliaryStored.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderAuxiliaryStored.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderAuxiliaryStored.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Auxiliary source arrays after the nomination handoff

The nomination sweep writes its histogram above the live header allocation.
The outer stage tag lies below all seven source arrays, so their contents
are available at the start of the auxiliary stage.


### `Output.auxiliaryStoredInputArrays`

 The memory passed by the nomination stage contains the six decoded header
arrays and the nominated counters in their public source ranges. 
