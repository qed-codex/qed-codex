---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshOperandInputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshOperandInputs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshOperandInputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Operand addresses for a selected refresh site

The child and parent carry independent private argument buffers. Their argument banks read
the old and new incidence widths, respectively. Both banks name the same physical site
ordinal. The four external segment heads describe independently oriented half-wires.


### `Input`

 Address expressions for a refresh site's old child and promoted parent argument buffers,
external segment tables, demand row and selected term record. 

### `Input.child`

 Address plan for the child's private arguments at the old site, using the input state's
  incidence directory. 

### `Input.parent`

 Address plan for the promoted parent's private arguments, using the output state's
  incidence directory. 

### `Input.lanes`

 Expression for the number of residual lane positions, equal to two to the residual lane
  exponent. 

### `Input.offOut`

 Head of the outgoing segment-offset array, supplied by word five of the segment bank. 

### `Input.offIn`

 Head of the incoming segment-offset array, supplied by word six of the segment bank. 

### `Input.widthOut`

 Head of the outgoing segment-width array, supplied by word one of the segment bank. 

### `Input.widthIn`

 Head of the incoming segment-width array, supplied by word seven of the segment bank. 

### `Input.demandBase`

 Expression evaluating to the base address of the gathered demand records. 

### `Input.termBase`

 Expression evaluating to the base address of the selected refresh term records. 

### `Describes`

 The child and promoted parent expressions represent their actual arguments and incidence
directories. The parent site ordinal, lane count and segment, demand and term heads
evaluate to the specified live words. 
