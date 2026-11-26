---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapHandlerClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapHandlerClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapHandlerClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Instruction and probe bounds for the fixed map handler family

The descriptor writer's instruction count and its external probes are
fixed for each grid point and party. The rest of the call uses only private
instructions. These bounds also cover prefixes ending at rejection.


### `clock`

 A handler initializes its descriptor, selects the entry, then runs the table. 

### `probes`

 Only the compiled external loads in the descriptor writer charge probes. 

### `clockFactor`

 One fixed multiplier covers descriptor writing, initialization and literal lowering. 

### `probeBound`

 The finite bound on external loads is independent of all repetition counts. 

### `trace_le`

 Apply the bounds to the exact instruction and probe conclusions of the native handler.
Every prefix has a smaller resource use on that same path. 

### `costs`

 Instruction bound and external probe count for a map invocation. Shrink and refresh use the
handler selected by the demand grid point and party, with the clock evaluated at the
demand's repetition count. A node without a lookup costs zero in both coordinates. 

### `costs_le`

 The same two fixed constants can be used at every selected shrink and refresh node. 

### `probeTotal_le`

 Charge the actual selected maps in their placement subtree to the same occurrence
count used for the child fields and the vertex history. 
