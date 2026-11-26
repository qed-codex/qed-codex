---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshBaseOutput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshBaseOutput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshBaseOutput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the base slots at lane zero

In a lifted slot graph the target of an outgoing slot at lane zero contains the destination
base vertex, its incoming slot, and the displacement. Appendix E uses one scan of these
slots to emit both base incidence tables and the displacement table of the next level.


### `params`

 Persistent state is the next base slot. The fixed public parameters give the two
radices and the addresses of the one input and three output columns. 

### `visit`

 Native visit that reads an actual mate at lane zero and emits its base mate, inverse mate,
and displacement. 

### `source`

 Convert a packed base slot index into the actual slot index of that vertex and port at lane
zero. 

### `mate`

 Read the actual outgoing mate of a lane-zero source slot. 

### `destination`

 Discard the lane from an actual mate index to recover its destination base slot. 

### `displacement`

 Extract the destination lane of a lane-zero arc, which equals its displacement. 

### `update`

 Install the base mate, reverse mate, and displacement recovered from a single lane-zero
lookup. 

### `events`

 The 28-event trace of one base-output visit, with one actual-mate read and three
base-column writes. 

### `baseCount`

 Number of base slots, counting every local port of each base vertex. 

### `actualCount`

 Number of actual slots, including all binary lanes at each base vertex and port. 

### `read_row`

 The one actual read at lane zero decodes the base mate and its residual displacement. 

### `Prefix`

 Slots already visited in the lane-zero pass, indexed by the source.
The inverse column is indexed by the matched destination. 

### `Outside`

 A memory address disjoint from all three written base columns. 

### `scan_run`

 All lane-zero calls through the given cursor, with unchanged memory outside the output
columns. Neither the inverse actual column nor the width column is read by these calls. 

### `base_pass`

 One call for each base slot recovers the entire base matching, its inverse, and its
displacement. Together with the actual columns these give the complete level directory. 
