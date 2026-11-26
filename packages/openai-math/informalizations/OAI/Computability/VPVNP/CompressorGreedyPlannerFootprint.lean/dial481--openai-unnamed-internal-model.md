---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyPlannerFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyPlannerFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyPlannerFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Reads of the six greedy launch recipes

The recipes use the pitch word, three scalar fields, three old incidence
heads, and the selected table head. The locations are computed relative to
the first level of the block at the actual visit.


### `scalar_support`

 When the launch state addresses the correct block, each loaded scalar
is in the data region, and the sole address load below it is the pitch. 
