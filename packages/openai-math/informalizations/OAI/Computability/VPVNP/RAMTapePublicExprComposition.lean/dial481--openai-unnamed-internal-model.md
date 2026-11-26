---
{
  "module": "OAI/Computability/VPVNP/RAMTapePublicExprComposition.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicExprComposition.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicExprComposition.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Register allocation for nested public expressions

An expression writes its result at its base register and uses only registers
above that base for intermediate words. Computing a right operand one position
higher therefore retains the already computed left operand.


### `addr`

 Interpret a natural base address in the finite bank of one more than the supplied register
bound. 

### `BankPort`

 Arithmetic bank with the bounded register file and four public geometry words. 

### `Computes`

 The routine writes the packed natural result at its base within the step budget, preserving
all lower registers, public words, persistent state, and log. 

### `combine`

 Sequence the two operand routines, then apply the binary word operation to the base
register and its successor. 

### `constant`

 Evaluate the operand, then run the constant operation with the next register as scratch. 
