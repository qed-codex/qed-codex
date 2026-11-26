---
{
  "module": "OAI/Computability/VPVNP/PairSimulationStackScratch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationStackScratch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationStackScratch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A stack leaf inside the private DFS workspace

The live pending descriptor addresses lie below the private stack intervals.
A source rejection precludes a successful native call at every instruction
budget. On acceptance the ordered writes define an update of the caller's
scratch, including stale cells above the current stack tops.


### `Footprint.applyScratch`

 Update the scratch cells using the complete ordered sequence of pushes.
The value supplied for addresses below the scratch is immaterial. 

### `Frame.keepsPending`

 Every descriptor below the workspace boundary survives the virtual
stack execution at its exact pending address. 

### `Frame.dfsReg`

 Preserve each dispatcher register under the two disjoint assignments
of physical registers. 

### `rejects_returns`

 Missing source choices and rejecting source halts both rule out any
successful native execution, including one with a smaller budget than
the stack simulation's advertised clock. 
