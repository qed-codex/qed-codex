---
{
  "module": "OAI/Computability/VPVNP/AdviceCircuitProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AdviceCircuitProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AdviceCircuitProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Boolean circuit instructions for the coefficient-query interpreter

Each instruction reads unary addresses counted from the top of the valuation stack.
The newly computed gate value is prepended. A variable or a constant can be read
from the initial valuation stack, and all earlier gate values remain accessible.


### `Instruction`

 An advice instruction that computes NOT or AND from addresses counted from the top of the
current valuation stack. 

### `unary`

 Encode an address as one true bit per valuation entry to skip followed by a false
terminator. 

### `Instruction.encode`

 Encode a gate with a false tag for NOT or a true tag for AND, followed by one unary address
per operand. 

### `encode`

 Concatenate the encodings of all instructions in execution order to form the circuit advice
stream. 

### `Instruction.value`

 Evaluate one gate against a valuation list, returning none if any operand address falls
outside the list. 

### `run`

 Execute the instruction list, prepending each new gate value to the valuation used by the
remaining instructions. 
