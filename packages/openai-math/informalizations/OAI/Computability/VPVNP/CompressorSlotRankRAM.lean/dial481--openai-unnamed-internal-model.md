---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotRankRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotRankRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotRankRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native RAM ranks for ordered incidence slots

The input row lists the incident slot keys in the order in which the descriptor
builder found them. The burst call counts keys strictly below its persistent
input and writes the count to the endpoint's slot field. It reads each key once.


### `visit`

 Register 0 is the moving read address, 1 the pivot, 2 the unit,
3 the running count and 4 a temporary word. 

### `rankCode`

 Public words 0 and 1 are the row address and destination address.
The rank accumulator starts at zero on entry to the burst call. 

### `quotient_indicator`

 Unsigned division by the key's successor, followed by a nonzero test,
implements strict order on word values. 

### `rank_native`

 The call starts with a fresh private workspace, reads the entire row in
descriptor order, writes the strict rank to the requested field, and returns it.
The destination may coincide with a source cell since the write follows all reads. 

### `rank_opcode_work`

 The table uses only registers and external probes. In the metered opcode
interpreter each dispatch costs at most six elementary word operations, including
when a supplied read stream stops early. 
