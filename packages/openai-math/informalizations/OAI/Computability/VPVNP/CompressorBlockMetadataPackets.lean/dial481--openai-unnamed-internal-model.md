---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockMetadataPackets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockMetadataPackets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockMetadataPackets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native online packets for the three DFS metadata publications 

### `data_walk`

 Each source segment inherits the event footprint of its chronological
walk. The same footprint preserves the lower control words at every join. 

### `Published`

 All twelve descriptor fields, the next DFS row pointer and the role
are read from the actual post-memory. Writes outside these fourteen cells
are excluded on the complete chronological report stream. 

### `Published.levelsFrame`

 The controller may compose arbitrarily many substeps: metadata writes
touch only two consecutive headers. Earlier levels, later levels and the
live group's control words agree with the source. 
