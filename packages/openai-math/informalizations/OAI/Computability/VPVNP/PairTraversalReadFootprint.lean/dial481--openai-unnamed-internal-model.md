---
{
  "module": "OAI/Computability/VPVNP/PairTraversalReadFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalReadFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalReadFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # External read addresses of the native placement-tree traversal 

### `EndpointBits.events_reads`

 A descriptor's child pointers occupy consecutive words. 

### `DFS.Visits.reads_of_row_bounds`

 Read addresses use the stored count and pointer of the current row.
Only rows visited by the selected preorder need to lie below the bound. 
