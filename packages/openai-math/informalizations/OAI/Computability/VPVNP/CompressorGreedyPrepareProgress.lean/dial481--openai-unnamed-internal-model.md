---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyPrepareProgress.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyPrepareProgress.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyPrepareProgress.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cursor progress of the native greedy preparation scans

Each call starts at the index of its vertex and returns the following index.
The memory before that call contains the prepared prefix of the directory.
This gives the exclusive stop guard for both the color and offset scans.


### `prep_progress`

 In a native preparation scan, every reported return advances to the next
vertex and the final cursor reaches the exclusive vertex count. 

### `color_prepare_progress`

 Progress for the color initializer on the memory left by tag projection. 

### `tag_prepare_progress`

 Progress for the offset initializer on the memory left by the color reader. 
