---
{
  "module": "OAI/Computability/VPVNP/CompressorSourceGroups.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceGroups.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceGroups.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Joining contiguous groups of online descriptor packets

Each group retains the actual execution on the raw memory, the event footprint and
clock bounds, and the recipe evaluation at the packet's live ordinal. Groups are
joined at the exact post-memory of their predecessors, shifting the ordinal by the
number of preceding visits.


### `Packet`

 One online script visit together with its source memory and native worker reports. 

### `post`

 Memory after replaying the reports from a list of online visit packets in order. 

### `Group`

 Chronological packets whose runs satisfy the clock and memory bounds and whose recipes
match successive live ordinals. 
