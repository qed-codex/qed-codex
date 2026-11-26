---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalFive.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalFive.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalFive.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The five terminal segments in every accepting pair traversal

An accepting path splits at the unique first accepting exit of each worker.
Conversely, the five completed physical segments join with the original
choice strings in their original order. No normalization or padding of
branch strings occurs at the stage boundaries.


### `Block`

 The private choices, worker reports and physical exit memory of one stage. 

### `Block.choices`

 Ordered private choice stream for each call of this stage. 

### `Block.logs`

 Entry and original worker report for each call. 

### `Block.memory`

 Physical memory after the final call of the stage. 

### `FiveTrace`

 The five completed native worker phases and their consecutive physical memories. 

### `FiveTrace.bootstrap`

 Trace of the terminal-header setup. 

### `FiveTrace.prefixRows`

 Trace of the final width-prefix scan. 

### `FiveTrace.traversalRows`

 Trace of the traversal-row and role-tag construction. 

### `FiveTrace.sharedBits`

 Trace of the shared wire-bit scan. 

### `FiveTrace.vertices`

 Trace of the ascending vertex calls and final ordinal check. 

### `FiveTrace.choices`

 All call choice strings in physical order. 

### `FiveTrace.logs`

 All tagged worker reports in physical order. 

### `accepts_five`

 A physical accepted branch string has all five completed stage runs.
Its cap applies to the physical reports after dispatch and handoff. 
