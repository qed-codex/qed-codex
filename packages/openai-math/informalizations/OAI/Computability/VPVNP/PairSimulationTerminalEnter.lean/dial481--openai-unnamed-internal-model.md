---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalEnter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalEnter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalEnter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact entry paths of the compressed-pair terminal controller

A zero marker initializes the bootstrap worker from an empty private workspace.
A one marker reloads the selected worker and its private cursor from the two
header cells. The scan and both header reads are included in the native trace.


### `initialEvents`

 Administrative steps before the first bootstrap call. 

### `dispatchEvents`

 Header reads and stage comparisons before a resumed worker call. 

### `enter_initial`

 A fresh call consumes thirteen local instructions and enters the bootstrap
worker with local state zero. 

### `enter_resume`

 A continuation fetches its full cursor and scans to the chosen worker,
preserving the remaining instruction fuel and the complete choice stream. 

### `enter_bad_marker`

 Every marker other than zero and one is rejected before a header probe. 

### `enter_bad_tag`

 If the header does not name a worker, its scan reaches the reject opcode.
This rules out a successful call at every cap and for every choice stream. 
