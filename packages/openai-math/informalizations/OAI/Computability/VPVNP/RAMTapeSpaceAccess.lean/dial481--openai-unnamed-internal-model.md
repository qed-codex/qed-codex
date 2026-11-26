---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSpaceAccess.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSpaceAccess.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSpaceAccess.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Displacement for a packed stack instruction

The seek and rewind cancel on each tape. The scratch head therefore returns
to its original position. At the next instruction boundary the first head
has moved left by one cell on a push, right by one on a successful pop, and
zero cells on an empty pop or a jump.


### `step_travel`

 A deterministic stack instruction costs a positive number of transitions.
At the next instruction boundary, growth of the packed bank gives the exact
negative displacement of its head. 
