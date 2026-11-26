---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortOneStagePorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortOneStagePorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortOneStagePorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Registers shared by the boundary moves and row traversal of a sorting stage

The row traversal and the exchange-stream split share their temporary ports.
The stage also has a preserved unary record count for splitting a whole block.
When installed in the schedule, its phase and stride refer directly to the
schedule's counters.


### `Port`

 The extra port holds the unary number of records in a site block. 

### `bank`

 Initialize one stage's row and boundary stacks, including the site identifier, stage
exponents, live record streams, flags and unary block size. 

### `dispatchPorts`

 Connect the local-versus-cross-site stride test to the row-width and stride counters and
temporary storage. 

### `boundaryPorts`

 Route block splitting and advancement to the same current, next, incident and scratch
stacks used by the row traversal. 

### `prepare`

 The local branch leaves the incident stream in place. The cross-site
branch separates its first block onto the send stack. 

### `advance`

 Discard the old current block and reverse the completed next block into its place on the
stage's physical ports. 

### `schedulePorts`

 Share the stage's phase and stride directly with the schedule counters and route its
remaining stacks to the schedule's data bank. 

### `data`

 Between layers, the schedule itself supplies phase and stride. 
