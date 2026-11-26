---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotBaseScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotBaseScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotBaseScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native scan of packed base arcs

Each call starts at one packed base and outgoing slot. Two reads follow the
lane-zero source row to its adjacent incoming field in the inverse table.
The worker strips the incoming side and lane digits, writes the base target
and lane displacement to separate arrays, and advances its persistent cursor.


### `code`

 The public words, in order, are the degree, number of lanes, row-table base,
inverse-table base, base-target output address, and displacement output address. 

### `srcRect`

 Row of the outgoing slot over lane zero. 

### `rowAddr`

 Address of the outgoing endpoint field in the row table at lane zero for the given base
port. 

### `invAddr`

 Address in the inverse table of the incoming field paired with the source field read at
lane zero. 

### `dstRect`

 Incoming rectangular slot of the same arc. 

### `dstSite`

 Recover the target site index from the incoming rectangular slot by removing the slot and
side digits. 

### `target`

 Base index and incoming slot, encoded in the same radix as the source cursor. 

### `displacement`

 Residual lane of the target reached from source lane zero, giving the base arc's lane
displacement. 

### `events`

 Trace of one base-port visit, reading the row and inverse tables before writing the target
base port and lane displacement. 

### `native`

 The two lookups precede both writes, so the words in the trace are computed
from the memory at the start of the call, even if some addresses coincide. 

### `opcode_work`

 Worst-case word operations, including arbitrary shortened read streams. 

### `ReadsOutside`

 Each table lookup falls outside the two output regions. The inverse address
is specified using the field returned by the original row-table read. 

### `run`

 Fill both base-graph tables using two reads and two writes per arc.
The two output arrays may be placed in either order. 

### `srcRect_val`

 The native mixed-radix address equals the lane-zero row when it fits. 

### `read_addresses`

 Both word addresses denote the ordinary natural-number table lookups. 

### `outputs_eq`

 With fitting input addresses the words computed by the worker agree with
the numerical lane-zero lookup and incoming-slot decoder. 
