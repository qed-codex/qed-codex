---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalBody.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalBody.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalBody.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact finite-fuel semantics inside a terminal worker

The protected registers hold the restored worker state, its two header
addresses and the marker one. Ordinary instructions simulate one source
instruction each. On a continuing exit the controller records the next
worker and its entire word. Every insufficient fuel or unused choice
stream is accounted for by the same interpreter.


### `target`

 The worker and persistent word selected by a successful exit. 

### `exitEvents`

 Instructions that publish the next stage and its persistent word. 

### `exitReport`

 Extend the worker's report by the control writes at a continuing exit. 

### `boundedExit`

 Check that the worker and its control writes fit in the remaining fuel. 

### `execute_body`

 Exact success and failure of a worker with the real exit protocol.
This equality is valid for all fuel, registers, private memory, external
memory and binary streams. 
