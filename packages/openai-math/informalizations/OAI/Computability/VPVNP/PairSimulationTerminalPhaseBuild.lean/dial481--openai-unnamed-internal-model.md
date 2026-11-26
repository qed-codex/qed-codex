---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalPhaseBuild.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalPhaseBuild.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalPhaseBuild.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Constructing the five terminal phases from native worker runs

Pair each original report with its genuine entry state and use the read
footprint to execute the worker on the physical memory. At an ordinary
return the next entry uses the returned word, including when that word is
zero. At acceptance the phase ends at the actual memory after the handoff.


### `stageLogs`

 The worker's report list annotated with the state at each call. 

### `single_phase`

 A closed one-call phase executes on exactly the given physical memory,
including any reads or writes of the controller cells inside the worker. 

### `closed_phase`

 Build an actual completed phase from the ordinary worker's finite
execution. The caller may place arbitrary values in both control cells. 

### `Phase.of_source_segment`

 Implicit-parameter form for constructing a phase in a larger traversal. 
