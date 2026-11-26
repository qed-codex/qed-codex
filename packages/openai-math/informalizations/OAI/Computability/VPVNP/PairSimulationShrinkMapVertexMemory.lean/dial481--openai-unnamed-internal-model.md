---
{
  "module": "OAI/Computability/VPVNP/PairSimulationShrinkMapVertexMemory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkMapVertexMemory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkMapVertexMemory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selected compressor levels at a physical vertex call

The terminal prefix publishes wire offsets in a table of the final level.
The traversal rows, shared wire bits and role tags all lie above the level
allocation. During the vertex scan the counter suffix lies below the levels
and the two terminal controller words lie above them. Consequently each
earlier level still has its calendar image when a vertex invokes a map.


### `VertexEntry.linkedLevelWindow`

 At each physical ordinal, all words up to the end of an earlier selected
level have their calendar values. This includes its map headers and term rows. 

### `VertexEntry.packedLevelWindow`

 The packed group workspace supplies the separation from both counter
stores and controller stores for the actual terminal public operands. The
calendar allocates one level for each selected pass and one for its output. 
