---
{
  "module": "OAI/Computability/VPVNP/RAMTapePublicOperandPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicOperandPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicOperandPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Installing the evaluated public operands in the actual processor bank

The first arithmetic registers are the instruction interpreter's public-word
ports. The arithmetic program reads and writes those ports directly. Its
temporary registers and the retained input fields have separate labels.


### `Port`

 Port space combining the site interpreter and the arithmetic source of its public operands. 

### `ports`

 Identify the first arithmetic result registers with the interpreter’s public operand ports
and keep the other source ports separate. 

### `siteWords`

 Exactly the public registers of the site interpreter are populated. 

### `result`

 Original processor fields and all arithmetic workspace after initialization. 

### `program`

 Run the physical operand initializer on the port bank that installs its results directly in
the site interpreter. 
