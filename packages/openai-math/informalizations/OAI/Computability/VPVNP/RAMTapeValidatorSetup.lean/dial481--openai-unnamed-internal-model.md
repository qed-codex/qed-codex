---
{
  "module": "OAI/Computability/VPVNP/RAMTapeValidatorSetup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeValidatorSetup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeValidatorSetup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Starting the local validator on its physical tape

The fixed input reader and width routines share the public address and bucket
registers. At their return the fields are in their original bit order. The record
emitter receives a writable slot counter and a zero-word template, while a
second slot count remains available for sorting and boundary checks.


### `Work`

 Working registers for computing the validator dimensions, remaining slot tally, zero
template, and temporary storage. 

### `Port`

 Combined register bank for the physical input reader and validator setup. 

### `rawPort`

 Port for the input reader's raw bit stream. 

### `wordPort`

 Port for the unary RAM word width computed from the input dimensions. 

### `slotsPort`

 Port for the retained unary count of record slots. 

### `remainingPort`

 Writable slot counter used by the record emitter. 

### `zerosPort`

 Port for the fixed-width all-zero word template. 

### `prepared`

 Extend the shaped bank with four times the bucket capacity in remaining slots and a zero
word of the computed width. 

### `routine`

 Run the physical input reader, compute the dimensions, and prepare the slot counter and
zero-word template. 

### `runs`

 The initialized local bank and polynomial clock depend only on the data read from
the original physical input, for every incident bit pattern. 
