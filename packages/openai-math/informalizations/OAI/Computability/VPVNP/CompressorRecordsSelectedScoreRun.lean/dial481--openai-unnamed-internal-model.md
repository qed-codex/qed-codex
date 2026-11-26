---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsSelectedScoreRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsSelectedScoreRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsSelectedScoreRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native selection of the actual shrinking layout

The two accumulators and the level's chosen-layout cell lie in the allocated
workspace. Each of eight coordinate passes visits the selected term rows in
motif order and reads the payload and repetition words directly.


### `axes`

 The coordinate number, layout side, and integer weight used by one of the eight
score-accumulation passes. 

### `headAt`

 Address of the term record for a motif at the given position in the physical score scan. 

### `run_selected`

 Run all eight native scans on the true selected term records. Read the chosen
layout in the resulting memory, with exact call/probe charges and the frame. 
