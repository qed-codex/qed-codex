---
{
  "module": "OAI/Computability/VPVNP/PairRefreshVertexPacket.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshVertexPacket.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshVertexPacket.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Resident refresh arguments after guessing the unique child

The one packet of the refresh placement is stored in its old-node frame.
The newer parent frame and the DFS geometry cells retain their values.


### `parent_fields`

 A child preceding its parent cannot overwrite any of the parent's bits. 

### `geometry`

 The retained stack-end pointer lies below the packet; both geometry slots
lie above it. The predicate therefore holds after the native child stores. 
