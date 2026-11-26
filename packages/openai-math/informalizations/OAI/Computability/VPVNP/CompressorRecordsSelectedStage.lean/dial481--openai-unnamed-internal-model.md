---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsSelectedStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsSelectedStage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsSelectedStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chronological layout, position and demand-record passes

After the selected motif records have been written, compare their two layout
scores. Use the resulting memory word as the placement scan's operand, then use
the newly written positions and the original incidence table to materialize the
absolute A/B/D/CD directory. The three groups of calls occupy consecutive,
disjoint workspace intervals.


### `Passes`

 Report groups in actual execution order. 

### `Passes.scores`

 The reports that accumulate the two layout scores and compare them to select a layout. 

### `Passes.positions`

 The reports of placing old sites using the layout selected by the preceding score
  comparison. 

### `Passes.roles`

 The reports that construct absolute A, B, D, and CD demand records from the selected
  placement and old incidence. 

### `Passes.afterScores`

 The memory containing the completed score accumulators and layout selection. 

### `Passes.afterPositions`

 The memory handed to the role scan after writing the selected old-site placements. 

### `Passes.final`

 The memory after scoring, site placement, and absolute role construction in chronological
order. 

### `Passes.all`

 Concatenate the score, position, and role reports in their execution order. 

### `Execution`

 The score writes, old-position scan, and final old-arc scan all run in this same memory. 

### `Stored`

 The workspace cells still available after constructing the old-arc record table. 
