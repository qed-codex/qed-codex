---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordPreimageScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordPreimageScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordPreimageScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The preimage-list pass of the descriptor builder

Store the selected placement in increasing old-site order, followed by a count per new
site and a rectangular array of bounded preimage lists. The native visit from
`CompressorRecordPreimages` appends one old-site identifier to exactly its selected row.
The complete pass builds the placement fibers in scan order using five calls-plus-probes
per old site, starting with a zero count in each new-site row.


### `RowRegions`

 The owner inputs, the list counters and the row data occupy disjoint address ranges. 

### `preimagePrefix`

 All old identifiers below the scan cursor which have the specified owner. 

### `PreimagesAt`

 Complete contents of the scan tables after the first `k` old sites. 

### `rows_apart`

 A valid row of a different owner is disjoint from the current owner's row. 

### `collectPreimages_run`

 All calls of the actual preimage pass, starting at any valid intermediate cursor.
The final memory contains the complete ordered fibers through the resulting cursor. 

### `preimagePass_cost`

 In particular the pass uses exactly one call and four external probes per old site. 
