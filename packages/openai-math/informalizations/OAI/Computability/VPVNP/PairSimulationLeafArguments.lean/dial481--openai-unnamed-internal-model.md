---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafArguments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafArguments.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafArguments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The four actual argument vectors at a cursor leaf

Outgoing slot zero is the stay arc and slot one is the flip arc. The
incoming slots retain these same numbers at their destinations. Each
genuine arc concatenates the successor fields and then the sorting
fields in the order used by the validator. The dummy arcs have width
zero, so the four vectors occupy four consecutive private intervals.


### `column_width`

 Width of the numerical system column in the padded cursor arc. 

### `ordered_ram_offset`

 Compression and the site validator number every bit of the actual
message systems identically. 

### `state`

 The padded compression state for the cursor graph, with base and lane coordinates and the
widths of the successor and sorting messages. 

### `iso`

 Identify the padded cursor graph with its compression state, numbering payload bits in RAM
system order. 

### `realSlot`

 The padded slot index of the genuine stay or flip arc designated by the side bit. 

### `buffers`

 The state's independent halves, interpreted in the padded cursor's
original coordinates. 

### `field_width`

 Every slot at either end is genuine precisely at ordinal zero or one. 

### `portNumber`

 Ordinals of the two outgoing and the two incoming private vectors. 

### `port`

 Select the incoming half-wire when the direction bit is true and the outgoing half-wire
otherwise, at the given side. 

### `read_port`

 The word actually read at the port offset of the private node arena
is the validator's requested bit of the independently supplied half-wires. 
