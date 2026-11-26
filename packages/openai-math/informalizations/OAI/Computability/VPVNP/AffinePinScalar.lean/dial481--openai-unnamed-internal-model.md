---
{
  "module": "OAI/Computability/VPVNP/AffinePinScalar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffinePinScalar.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffinePinScalar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native scalar output for a coordinate pin 

### `Flag`

 Ports for the active-pin, constant, and unit-monomial bits and the two work stacks used to
write a field literal. 

### `Port`

 The field-addition ports and flag ports used to turn a pin value and a monomial
classification into a scalar coefficient. 

### `frame`

 Initialize field arithmetic from the modulus and accumulator and install the supplied
active, constant, and unit flag stacks. 

### `operation`

 Negate the pin value for the constant term of an active pin. In the remaining cases write
one for its selected variable and zero otherwise. 

### `branch`

 Pop one Boolean flag and run the continuation for that bit, rejecting an empty flag stack. 

### `machine`

 Read the active, constant, and unit flags in order and execute the corresponding scalar
operation. 

### `result`

 The pin-row coefficient selected by the flags, equal to minus the pin value for the active
constant term, one for the active selected variable, and zero otherwise. 

### `cost`

 Step bound for reading the three classification flags and producing the packed scalar by
negation or literal output. 
