---
{
  "module": "OAI/Computability/VPVNP/RAMUniform.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMUniform.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMUniform.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A single burst instruction table at different word widths

The public parameters and the machine word width depend on the input length.
The instruction destinations, operand registers, and literal constants of a
fixed program do not. A table in the finite literal format can be instantiated
at every width. Increasing the width past the literal width preserves each
constant's natural value.


### `Instr.resize`

 Resize just the immediate constants of an instruction. No opcode, register,
public-data location, jump target, or branch order is changed. 

### `Template`

 The finite, length-independent part of a call program. 

### `Template.literalWidth`

 Bit width in which the fixed instruction table stores its literal constants. 

### `Template.entry`

 First instruction address of this table, shared by all word-width instantiations. 

### `Template.code`

 Instruction stored at each bounded program counter, with constants encoded at the
  template's literal width. 

### `Template.instantiate`

 Resize the table's literal constants to the runtime word width and install the supplied
public operands. 
