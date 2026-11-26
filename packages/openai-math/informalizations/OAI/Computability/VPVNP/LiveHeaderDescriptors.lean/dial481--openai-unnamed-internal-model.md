---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderDescriptors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderDescriptors.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderDescriptors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native descriptor writes for Section 14.1

A fixed straight-line block takes an incident side and a field. It reads
the width, tag, and two phase flags, then writes the field's source offset
and length. The block handles clamped endpoints, the incoming midpoint
of the first tail group, and all zero-length intervals.


### `Parameters`

 Public data are small sizes and scratch addresses. Exponent size is the
total `t*Z`. Configuration size excludes the mode and zero padding. 

### `Parameters.widthAddress`

 Public operand index for the address holding the incident cut width. 

### `Parameters.tagAddress`

 Public operand index for the address holding the selected live-mode tag. 

### `Parameters.firstHalfAddress`

 Public operand index for the address of the first-half flag. 

### `Parameters.firstTailAddress`

 Public operand index for the address marking the first evaluator group after the
  midpoint. 

### `Parameters.delta`

 Public operand index supplying the cut's basic width parameter. 

### `Parameters.exponentSize`

 Public operand index supplying the allocated exponent field size. 

### `Parameters.configSize`

 Public operand index supplying the allocated evaluator configuration size. 

### `Parameters.offsetAddress`

 Public operand index for the destination cell of the computed source offset. 

### `Parameters.countAddress`

 Public operand index for the destination cell of the computed field length. 

### `load`

 Load the public sizes and descriptor destinations and read the live width, mode tag, and
phase flags. 

### `masks`

 Registers 15 and 16 indicate respectively a pair-format and a tail-format
payload. Register 11 is the length of the mode (zero or one). 

### `lengths`

 Apply the phase and mode masks to obtain the exterior, exponent, and configuration field
lengths. 

### `starts`

 Compute successive field offsets and the residual padding length from the live width and
the enabled field lengths. 

### `startReg`

 Select the register containing the computed source offset for the requested field. 

### `countReg`

 Select the register containing the computed length for the requested field. 

### `emit`

 Write the field length and its offset, setting the offset to zero when the interval is
empty. 

### `block`

 The descriptor worker that reads metadata, selects the masks for the incident side,
computes its field intervals, and publishes one interval. 

### `offWord`

 Zero-length fields receive offset zero. 

### `events`

 Four scratch reads and two writes. The other twenty-seven operations
are register arithmetic and public parameter loads. 

### `block_exec`

 The block materializes both descriptor words at designated addresses.
Their exact natural values fit because the whole source interval fits in
the incident width. All parameter cells are read before either write. 

### `output_words`

 When the chosen output cells are distinct, the field runner reads back
the offset and count deposited by the descriptor block. 
