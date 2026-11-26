---
{
  "module": "OAI/Computability/VPVNP/QueryProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/QueryProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/QueryProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite control for a binary query program

A read addresses one of the fixed payload bits and branches to another
control state. The clock counts payload queries. Halting consumes no query.


### `QueryStep`

 One binary query action, either a Boolean halt or a payload-bit read with low and high
successor states. 

### `QueryProgram`

 A binary query program on `k` payload bits, specified by its initial state and the action
at each state. 

### `QueryProgram.start`

 State from which execution of the query program begins. 

### `QueryProgram.step`

 Action prescribed at each query state, including the addressed bit and the two successors
  for a read. 

### `QueryProgram.eval`

 Evaluate from a given state, spending one unit of fuel per bit read and rejecting a read
attempted at zero fuel. 
