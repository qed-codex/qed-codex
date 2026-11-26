---
{
  "module": "OAI/Computability/VPVNP/PairRefreshHookReader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshHookReader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshHookReader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A typed parser for the refresh hook

The parent is reconstructed from its private packet, and the old half is the
single prefix consumed from the branch tape. The local map receives the scratch
after the packet write. A success records both halves, the exact chronological
trace and the complete resulting scratch.


### `packet`

 Form the old child's argument packet from its DFS row address and its packed half-wire
bits. 

### `reader`

 Decode the resident parent and the guessed old child, store the child packet, and invoke
the refresh action on the two assignments. 

### `realizes`

 A packet parser with a genuine successful native prefix and both native
rejection cases realizes the DFS hook on all complete and truncated tapes. 
