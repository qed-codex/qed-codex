---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMOnce.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOnce.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOnce.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Running acyclic opcode fragments of the input assembler

These fragments have no internal loop. A supplied Boolean controls any
explicit choice, and the returned event sequence records its occurrence.
The implementation below provides executable witnesses for structured
execution and a static instruction bound on every successful path.


### `Effect`

 The event trace, final registers and final memory produced by executing an acyclic code
fragment. 

### `once`

 Execute the branch selected by the register comparison. A loop requires
its own finite derivation and is excluded from this acyclic evaluator. 

### `once_sound`

 The computed trace is a real finite execution and is bounded by the
static instruction count. 
