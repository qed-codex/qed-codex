---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafFill.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafFill.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafFill.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Installing a scalar field in the validator's represented stack bank

Only the selected top pointer and its occupied cells change. The proof also
covers empty fields and allows later leaves to reuse a previously occupied
region. All reads and writes in the initialization are private.


### `Reg`

 Registers for a scalar stack fill, combining the stack allocation registers with the
field's length and source word. 

### `pointers`

 Embed the stack allocation registers into the physical register placement of the scalar
fill loop. 

### `stack`

 The host placement of stack registers reached through the fill loop's allocation registers. 

### `fieldRegisters`

 The six physical registers of a port's scalar write loop, in order from its top pointer
through length, value, zero, one and scratch. 

### `install_scalar`

 Deterministic execution of a scalar-port load, starting from a represented
bank and the two runtime operands. The destination port is empty at entry. 
