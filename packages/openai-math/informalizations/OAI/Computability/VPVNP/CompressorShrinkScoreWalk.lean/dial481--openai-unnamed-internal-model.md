---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkScoreWalk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkScoreWalk.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkScoreWalk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The ten selected-score visits as a chronological native walk

The one-shot calendar programs return cursor one. Their memory operations
coincide with the clear and comparison operations in the score calculation.
The eight strided scans use exactly the original reports.


### `Stage`

 A stage of layout scoring clears both accumulators, scans one of the eight layout-and-role
coordinates, or compares the totals to choose a layout. 

### `stages`

 Score stages in execution order, clearing the accumulators once, scanning coordinates zero
through seven, then comparing the two layout scores. 

### `Stage.visit`

 The planner visit implementing a score stage on the selected plan’s term and accumulator
tables. 

### `visits`

 The ten score visits obtained by translating the ordered score stages into planner visits
for the supplied inputs. 

### `advance`

 Give a one-shot score report the calendar’s return cursor of one while retaining its event
trace. 

### `Native`

 Specifies a stage’s source reports. An axis executes its score worker once per motif with
empty choices, while clearing and comparison each produce one report returning cursor one. 

### `walk`

 Decompose the actual native score calculation into its ten recipe
occurrences, retaining every event and the complete post-memory. 
