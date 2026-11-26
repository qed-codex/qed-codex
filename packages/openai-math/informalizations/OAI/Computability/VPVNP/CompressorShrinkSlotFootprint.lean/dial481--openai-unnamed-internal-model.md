---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkSlotFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSlotFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSlotFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External accesses in the shrinking slot preparation and column copies

Every preparation call has one external write and no reads. Each copy call
reads one live source cell and writes the corresponding destination cell.
The resulting bounds apply to every individual source segment of the
twenty-two-visit program when the directory and output scans have their
respective event bounds.


### `Reports.Native.footprint`

 All seven preparation phases access only their output cells. The stronger
upper bound is the start of the sorted rows, immediately after the counters. 

### `ColumnCell`

 Natural half-open intervals of the six live columns. 

### `Runs.footprint`

 Every copied report reads the selected source column at its own ordinal
and writes only the same ordinal in the corresponding destination column. 

### `SourceWalk.refine_footprints`

 An aggregate event bound on a chronological walk also holds at each
source stage in its own memory. 

### `sources_with_footprints`

 Combine the concrete preparation and copy accesses with the five directory
and four output scans. Each of the twenty-two stages retains its own source
execution and bounds on its own read and write events. 
