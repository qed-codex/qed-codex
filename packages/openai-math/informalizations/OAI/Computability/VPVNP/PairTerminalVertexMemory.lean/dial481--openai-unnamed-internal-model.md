---
{
  "module": "OAI/Computability/VPVNP/PairTerminalVertexMemory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalVertexMemory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalVertexMemory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Readback at the actual entry of the terminal vertex phase

The linked bit stage writes the shared interval and hands off through the two
controller cells. Its physical post-memory carries the selected DFS child rows,
role words and the same bit assignment. Earlier level descriptors and all
noncontrol header fields are still readable by the native vertex interpreter.


### `linked_vertexMemory`

 All data read by the DFS and endpoint gather after the linked shared
scan. The range of preserved header fields excludes the two stage controls. 
