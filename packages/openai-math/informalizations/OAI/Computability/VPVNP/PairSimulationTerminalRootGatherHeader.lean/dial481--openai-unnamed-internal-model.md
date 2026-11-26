---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalRootGatherHeader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalRootGatherHeader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalRootGatherHeader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native endpoint headers for outgoing and incoming terminal slots 

### `header_run_reads`

 The header selects the edge, fetches its width and exclusive prefix, and
leaves the source interval ready for the bit loop. Only the incoming pass
needs an inverse incidence read. 
