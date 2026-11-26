---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalSiteRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalSiteRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalSiteRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Exact traces and private stack for the terminal-site guard 

### `Continues`

 A deterministic prefix has the indicated exact trace for every subsequent
fuel and choice suffix. Its external memory is available to the continuation. 

### `active_run`

 An active site supplies its exact root and both endpoint arrays to the geometry initializer. 

### `equal_run`

 Reaching the terminal ordinal accepts on the next test, consuming no choices. 

### `late_run`

 An ordinal past the last site takes the rejecting branch. 

### `late_reject`

 Sufficient fuel cannot turn a malformed ordinal into a returning path. 

### `equal_terminal`

 The terminal ordinal has exactly its empty-choice accepting path. 

### `finish_run`

 After the histogram flush, read the original ordinal afresh and return
its successor. All four rows work with arbitrary registers and private cells. 

### `active_caps`

 The entry trace and continuation trace have fixed local and external costs. 

### `fresh_stack`

 A fresh burst starts with zero private cells. At geometry entry its one
pending descriptor is the root and all other cells still have value zero. 
