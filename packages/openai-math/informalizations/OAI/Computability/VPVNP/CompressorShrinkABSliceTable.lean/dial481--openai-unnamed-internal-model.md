---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkABSliceTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# All AB copy slices in the shrinking graph

Each assigned bundle receives a contiguous bank. The three native scans
clear the endpoint counts, read both existing prefix columns to write
interval frames, and link positive frames into the two endpoint directories.


### `columns`

 Four source columns are packed by a common bundle ordinal, with
independent row strides for the old thick and the AB fields. 

### `bank`

 The starting word address of bundle `i` in the consecutive AB banks, using the capacity for
`m` old and `n` new fields. 

### `Layout`

 The AB banks fit in machine addresses, the two row strides accommodate their field counts,
and all four input columns end before the banks. 

### `Runs`

 Actual banks for all absolute bundle ordinals. 

### `Image`

 Row data in the final table. Only the cells of this row's bank are
consulted when following either endpoint directory. 

### `graph_run`

 Given the single snapshot produced by the native thick/CD and AB scans,
materialize every bundle's frame lengths, offsets and both endpoint directories
in a separate bank, leaving the complete input area intact. 

### `image_bits`

 Follow the exact frame of the old wire and motif at either packed
endpoint. Its offsets characterize the demand bit bijection used by both
`localAWord` and `localBWord`. 
