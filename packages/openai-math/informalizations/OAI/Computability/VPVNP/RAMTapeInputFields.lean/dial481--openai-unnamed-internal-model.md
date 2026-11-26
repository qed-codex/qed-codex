---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInputFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading fixed-width fields with a finite stack control

The reader consumes one unary count mark and one input bit at a time. It
collects the bits in reverse order and restores them to their destination in
a second pass. Both passes use the same finite control at every input length.


### `Field`

 Fixed-width fields following the prefix on a site tape, namely the address, four-bit
header, and incident vector. 

### `Field.counter`

 Select the unary width counter for the address, header, or incident vector. 

### `Field.output`

 Select the stack on which the reader deposits the requested field. 

### `collect`

 Consume one input bit per true width mark, pushing the bits onto a temporary stack in
reverse order. 

### `restore`

 Move the collected field bits from the temporary stack to their output stack in original
order. 

### `readField`

 Read one fixed-width field by collecting its bits and then restoring their order. 

### `frame`

 The unrelated registers are carried through all field instructions. 

### `fieldResult`

 Deterministic stack update after a field has been read. 

### `readField_runs`

 One counter mark and one input bit are consumed in three stack steps,
then two steps restore each bit to its original order. 

### `padding`

 A zero padding bit consumes a pop and a return. A one in this region
executes a rejecting halt. 
