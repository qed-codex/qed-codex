---
{
  "module": "OAI/Computability/VPVNP/PairSimulationSharedBitControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationSharedBitControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationSharedBitControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Shared-bit frames along partial native runs

The shared-bit worker can write only one wire per data call. Its ordinary
header words survive both that write and the controller's two handoff writes.
This invariant covers any successful prefix of the terminal program.


### `control`

 Every successful shared-bit burst preserves an address outside both the
wire bank and the terminal controller cells. The invariant starts at the
actual physical memory left by the row phase. 
