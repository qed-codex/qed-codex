---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyPrepareVisitAccess.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyPrepareVisitAccess.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyPrepareVisitAccess.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Memory accesses of one relocated greedy record writer

The public control-word loader and the final cursor increment have no
external probes. The header and operand writers stay inside the current
walk layout, and the only external reads are the two mate tables.


### `one`

 Native single vertex visit and the complete bounds on its external addresses. 
