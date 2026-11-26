---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafRegisterBank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafRegisterBank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafRegisterBank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Register wiring between the virtual validator's operand staging and scalar fill loop 

### `Source`

 Input register names for the site dimensions, bucket, fuel, address and words, and the
virtual machine's public operands. 

### `Reg`

 The combined scalar-loader register bank, with fill-loop registers and a separate bank of
source words. 

### `load`

 Physical embedding of the fill-loop registers in the combined scalar-loader bank. 

### `stagingName`

 Wire each staging register to its scalar source, fill destination, or shared stack constant
and temporary. 

### `stage`

 The injective host placement of staging registers induced by their wiring into the
scalar-loader bank. 

### `stack`

 Physical placement of the validator's stack registers in the scalar-loader bank. 

### `staged_represents`

 Staging writes only three scratch registers. The entire logical stack
bank therefore retains its private cells and pointers. 
