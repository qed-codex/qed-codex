---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkGreedyPhases.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkGreedyPhases.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkGreedyPhases.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # External state transfer between the shrinking assignment passes 

### `Assignment`

 A pair of actual reset-on-entry burst scans with the public parameters used
by the planner. The reader begins in exactly the memory left by preparation. 

### `Assignment.prep`

 Reports of preparing one operand row per old base vertex for a greedy assignment. 

### `Assignment.reads`

 Reports of the visits that read the prepared rows and write each vertex's assigned label. 

### `post`

 The memory containing the completed greedy assignment after row preparation and visits. 
