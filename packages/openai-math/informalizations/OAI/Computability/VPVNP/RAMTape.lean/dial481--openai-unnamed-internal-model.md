---
{
  "module": "OAI/Computability/VPVNP/RAMTape.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTape.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTape.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Writable nondeterministic controls for the coefficient machine

A named finite control can inspect both head symbols, write and move both tapes,
and make a binary choice. The compiler emits the nine literal rows for each state.
Each occupied branch slot contributes its own path count.


### `Command`

 Halting or two-head transition with a named successor state. 

### `Choices`

 The occupied nondeterministic branch slots of one table row. 

### `Control`

 The commands available at each state and pair of scanned symbols. 

### `instruction`

 Encode one named command as a universal-machine instruction. 

### `records`

 Encode the occupied branch slots, preserving their multiplicities. 

### `compile`

 The physical table for a fixed finite control. 

### `running`

 Physical configuration of a named nonhalting state and its two tapes. 

### `running_state_ge_two`

 The two halting states precede every encoded control state. 

### `count`

 Accepting paths from the given named configuration within the tape clock. 

### `after`

 The contribution of one executed command to the remaining accepting path count. 

### `paths_step`

 A literal binary row adds two counts, including when its targets agree. 
