---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkGraph.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Placement columns on the typed shrinking graph

The four output columns of the native old-position scan encode the owner, the
thickness bit, the assigned outgoing bundle and the bundle's target. The
indexed old positions include the tag, mask, slot label and residual lane.


### `PositionCount`

 The number of old positions scanned for placement, counting every packing lane of each base
vertex. 

### `PlacementColumns`

 The fixed four columns as consumed by subsequent arc and preimage passes. 

### `placement_run`

 The shrinking scan on the entire old graph fills the typed placement arrays. 
