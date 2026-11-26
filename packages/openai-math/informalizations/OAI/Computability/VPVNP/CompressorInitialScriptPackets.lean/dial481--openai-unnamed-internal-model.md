---
{
  "module": "OAI/Computability/VPVNP/CompressorInitialScriptPackets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorInitialScriptPackets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorInitialScriptPackets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Catalog indices and checked packets for the actual initial script 

### `indices`

 The script's initial ordinals precede its repeated block. 

### `actual_order`

 The runtime allocation only changes the directory bounds and the catalog
arity. The four workers use the compiled scalar and array dimensions. 

### `budget`

 One finite bound covers all planner code and all four source workers. 

### `Attached`

 A checked initial packet whose catalog phase, public operands, entry memory, fuel, and
choices agree with its attached header visit. 

### `attach_initial`

 The four checked packets use the actual worker labels in the compiled
script and the computed public operands at each successive source memory. 
