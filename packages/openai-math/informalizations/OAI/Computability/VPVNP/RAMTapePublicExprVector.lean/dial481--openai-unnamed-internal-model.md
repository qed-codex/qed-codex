---
{
  "module": "OAI/Computability/VPVNP/RAMTapePublicExprVector.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicExprVector.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicExprVector.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Preparing the finite vector of public operands for the live instruction table

Registers are filled in increasing order. Each expression's private registers
lie above its result, so later evaluations preserve the preceding outputs.
After the last expression, the same finite loop writes zero to every remaining
register.


### `capacity`

 Largest register index used by the vector program. 

### `registerCount`

 Size of the register file allocated for evaluating the entire public expression vector. 

### `vector`

 Evaluate public expressions in increasing slot order and zero the remaining registers. 

### `output`

 Expected register contents after vector evaluation, with packed expression values in the
operand slots and zero elsewhere. 

### `coefficient`

 The coefficient of the quadratic word-width bound depends only on the fixed expression vector. 

### `output_at`

 The instruction table can address its public operands in their original order. 
