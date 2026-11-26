---
{
  "module": "OAI/Computability/VPVNP/PairSimulationResidentMapLoopExact.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationResidentMapLoopExact.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationResidentMapLoopExact.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact parsing of a resident map loop

Each map acts on the scratch left by its predecessors. A failed entry
rejects the burst at that occurrence. The native guard and advance rows
consume no choices and execute at their actual cursor addresses.


### `Action`

 Deterministic evaluation of one selected occurrence on the actual scratch. 

### `NoChoices`

 Every successful evaluation of this occurrence, on any node and saved scratch, yields a
trace with an empty sequence of choice bits. 

### `scan`

 Trace and scratch of the linked test, occurrence, advance and remaining entries. 

### `mapReader`

 Run the resident occurrences on successive scratch states as a shrink-role reader. Success
returns their scan trace and final scratch with the entire choice tape as the remainder. 

### `Item`

 Exact deterministic semantics needed from the descriptor reader and the
selected matrix routine at this one occurrence. 

### `Items`

 Exact machine realization of each occurrence in list order at successive cursor positions
starting at `src`, with both successful execution and rejection specified at each position. 

### `Entry`

 Configuration at the scan guard with cursor `src`, exclusive end `src + count`, unit
increment and the node's operand invariant. This is the entry condition for realizing the
map reader. 

### `maps_realizes`

 The linked map loop preserves every remaining tape bit. A rejected occurrence
rules out returning from the original guard even when previous maps succeeded. 
