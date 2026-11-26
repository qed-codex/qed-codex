---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalRootGatherReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalRootGatherReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalRootGatherReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # External read addresses of the terminal endpoint gather 

### `Layout.Readable`

 Allowed external addresses for this vertex's incoming-edge lookup, outgoing
edge metadata and shared bit intervals. The incoming lookup precedes the width
and prefix reads, so those two bounds depend on the actual entry memory. 

### `arc_reads`

 The bit-copy loop reads exactly within the chosen source interval. 
