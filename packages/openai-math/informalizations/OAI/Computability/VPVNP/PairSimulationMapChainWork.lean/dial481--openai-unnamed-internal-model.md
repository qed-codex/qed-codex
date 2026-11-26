---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapChainWork.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapChainWork.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapChainWork.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Summing local map checks and leaf runs in a placement history

Each selected term places old vertices intact at one output vertex. The
work of its map interpreters and of the original leaves therefore obeys
the same placement-fiber recurrence as the recorded occurrence count.


### `MapInputs`

 Interpreter inputs at the individual map slots of an entire branch.
The index on each invocation is the degree recorded at that slot. 

### `mapAndLeafCost`

 Sum the instruction charges of individual recorded map slots and original leaves
inside the actual preimage subtree of each final site. 

### `mapAndLeafWork`

 Metered interpreter charges in the same placement fibers. 

### `mapAndLeafCost_le`

 This bound holds for every input to every recorded interpreter, without
an acceptance requirement or equality of independently supplied half-wires. 

### `mapAndLeafWork_le`

 This bound holds for every input to every recorded interpreter, without
an acceptance requirement or equality of independently supplied half-wires. 
