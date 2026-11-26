---
{
  "module": "OAI/Computability/VPVNP/CompressorTermWorker.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTermWorker.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTermWorker.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed native worker for a strided motif scan

One call starts at the current motif ordinal. Its address prelude multiplies
the ordinal by each of the two strides. The grid search, repetition routine
and payload writer have disjoint reset register banks. Between them two native
stores save the grid and repetition results in the row just computed.


### `Registers`

 Total private register count for the address prelude, grid search, repetition routine, and
payload writer. 

### `Ports`

 Total public operand count for the address, grid, repetition, and payload banks. 

### `headReg`

 Embed the address prelude's seven registers at the start of the fused worker's register
bank. 

### `gridReg`

 Embed the grid search's eight registers immediately after the address prelude's registers. 

### `repReg`

 Embed the repetition routine's eight registers after the grid search's register bank. 

### `payloadReg`

 Embed the payload writer's registers in the final block of the fused worker's register
bank. 

### `addrPort`

 Index the two base addresses and two strides in the worker's public operand bank. 

### `gridPort`

 Index the grid-search operands immediately after the four address operands. 

### `repPort`

 Index the repetition routine's operands after the address and grid operands. 

### `payloadPort`

 Index the payload writer's operands in the final block of public words. 

### `words`

 Assemble the four public operand banks in the order used by the fused term worker. 

### `source`

 Address of motif `j`'s input demand row computed from the input base and stride. 

### `base`

 Address of motif `j`'s output term record computed from the output base and stride. 

### `prelude`

 Compute the demand and term addresses, output field addresses, and next motif ordinal from
the persistent cursor. 

### `headerCode`

 Assemble the fixed stages and choose their private register locations. 

### `code`

 Combine the strided address prelude, grid and repetition stores, and payload writer in one
worker. 

### `pass`

 Schedule the fused worker with the successor motif ordinal as its return word. 

### `headerLog`

 The only external writes beyond the payload are the row index and the
repetition header. The thirteen address operations consume private ticks. 

### `execute_iff`

 After the empty-choice prefix, the payload is executed on reset ordinary
registers with its computed base. Conversely every execution restricts to
one payload derivation with exactly its tape and memory effect. 
