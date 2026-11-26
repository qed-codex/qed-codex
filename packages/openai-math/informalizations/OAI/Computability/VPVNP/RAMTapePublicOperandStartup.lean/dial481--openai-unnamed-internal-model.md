---
{
  "module": "OAI/Computability/VPVNP/RAMTapePublicOperandStartup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicOperandStartup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicOperandStartup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Computing the live table's public operands from the original site input

The geometry parser, word initialization and expression interpreter form one
fixed finite control. It retains the processor's record fields and leaves the
operand vector at the front of its arithmetic register bank.


### `Source`

 Port bank of the physical geometry parser and the register file sized for the expression
vector. 

### `sourceProgram`

 Initialize the geometry words from the raw tape, then evaluate the expression vector on the
arithmetic bank. 

### `arithmetic`

 Arithmetic output bank with the geometry inputs, evaluated operand vector, zero persistent
word, and empty private log. 

### `clockCoefficient`

 Fixed clock coefficient for physical geometry startup, register allocation, and vector
evaluation. 
