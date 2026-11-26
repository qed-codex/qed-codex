---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorLocal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorLocal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorLocal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fuel-checked private instruction execution between external probes

The controller consumes an instruction credit before fetching the opcode.
Ordinary continuations jump to the next credit test. A private choice consumes
one already nominated bit, with a short stream reaching rejection. Read and
write callbacks return to the site controller for charging and recording.


### `Port`

 Ports of the private instruction interpreter together with its unary fuel stack and binary
guess stream. 

### `fuelPort`

 Stack holding one token per remaining private instruction. 

### `choicePort`

 Stack containing the remaining nominated binary choices for private branches. 

### `State`

 Control states for checking fuel at a program counter, executing an ISA instruction and
yielding its callback. 

### `code`

 Consume one fuel token before dispatch, follow private branches using the choice stack, and
yield external actions or termination to the site controller. 

### `store`

 Build the local interpreter's stack bank from the public words, logged private
configuration, fuel tally and remaining guess bits. 

### `instructionExit`

 Callback selected by the current template instruction and its conditional jump test on the
logged configuration. 

### `instructionPost`

 Logged private configuration after the current instruction's register and private-memory
updates. 
