---
{
  "module": "OAI/Computability/VPVNP/CompressorPublishedScoreRoom.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPublishedScoreRoom.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPublishedScoreRoom.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The shrinking layout bit lies beyond the published heads

The term planner starts in the old level's first scratch table. The selected
layout bit follows the motif term rows in that table. Its numerical address
therefore lies above the scalar cells at offsets 36 through 53.


### `of_header`

 Reading the typed old header identifies the actual term base and row count. 

### `allocated`

 The compiled table allocation supplies all address bounds, including the
room needed for the ten-word motif rows and the selected-layout score. 
