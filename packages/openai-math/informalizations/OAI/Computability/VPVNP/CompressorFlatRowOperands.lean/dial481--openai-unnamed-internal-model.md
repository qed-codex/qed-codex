---
{
  "module": "OAI/Computability/VPVNP/CompressorFlatRowOperands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorFlatRowOperands.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorFlatRowOperands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading local worker operands in a whole-level scan

For each parameter and for the local cursor, the prologue computes
`base + globalRow * stride`, optionally reads the word there, and adds a
fixed offset. The source-worker registers remain zero until its body starts.


### `Registers`

 Register count for a flattened row worker, including the original registers, operand cache,
and three temporaries. 

### `Params`

 Number of public words needed for three address fields per local operand, including the
local cursor. 

### `Public`

 Public operand bank indexed by the address-field positions of a flattened row worker. 

### `field`

 Flatten an operand number and its base, stride, or offset field into one public-word index. 

### `ordinary`

 Embed an original worker register into the leading register bank of the flattened worker. 

### `slot`

 Register holding one cached local operand or the local cursor after the prologue. 

### `scratch`

 Select one of the three temporary registers following the operand cache. 

### `addr`

 Row-dependent address computed from an operand's public base and stride. 

### `value`

 Operand supplied to the body after optionally loading from its row address and adding the
public offset. 

### `operand`

 One affine parameter takes seven lines, with the fifth line a single
read for indirect operands and a register copy for direct operands. 

### `operandEvents`

 Seven prologue events for one operand, including an external read precisely when its load
flag is set. 

### `registers`

 Combine the body registers, cached operands, and three temporaries into a single register
bank. 

### `prologue`

 Instructions that cache all operands for the current global row and calculate the successor
row cursor. 

### `events`

 Complete prologue event list for a global row, including the operand reads and cursor
arithmetic. 
