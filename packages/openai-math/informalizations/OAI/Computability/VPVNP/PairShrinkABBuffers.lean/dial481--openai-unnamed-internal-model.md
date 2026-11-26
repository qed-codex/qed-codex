---
{
  "module": "OAI/Computability/VPVNP/PairShrinkABBuffers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkABBuffers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkABBuffers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# AB demand buffers of a resident shrinking map

The packed descriptor stores a three-word interval for each pair consisting
of a thick old arc and an assigned motif. Its source and target offsets are
relative to the old half-word and the selected AB operand. Each frame copies
a slice from one old half. Taken in old-field order these writes reconstruct
the precise row argument of the matrix at either A or B, even when the two
old halves were guessed independently.


### `frame`

 Physical start of the three words in the completed indexed-starts bank. 

### `frame_words`

 The physical word loads from the final AB bank yield the exact typed slice. 

### `copyBits`

 Bits copied by a single actual AB frame at either packed endpoint. 

### `operand`

 Read the AB operand of the typed demand-bit bijection from a collection of
old half-wires. The field data can be different at the two packed endpoints. 

### `copyBits_operand`

 Each copied bit already has its eventual value in the assembled AB word. 

### `fill`

 Private-memory effect of the source-major copies into one AB destination. 

### `store_at_target`

 A positive slice writes its own target coordinates and leaves every other
coordinate of the AB word unchanged. Zero-length frames have no memory effect. 

### `fill_operand`

 Visiting every thick arc in the bundle reconstructs the exact AB buffer.
The physical readout works for arbitrary prior destination memory. 
