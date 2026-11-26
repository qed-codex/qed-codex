---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshEmitCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshEmitCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshEmitCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Communication cost of the entire refresh pass

The three header publications, the selected native core, six incidence copies,
and the traversal publications account for all source reports. Their combined
charge is linear in the number of positions of the old graph. Calendar costs
use the number of actual visits in the fixed block.


### `rawRate`

 One fixed source charge per old position. The two additive publication
costs are absorbed because every incoming state has at least one position. 

### `raw_le`

 Bound the actual combined source charge by the uniform per-position rate. 

### `groupCost_bound`

 The online recipe and frame probes of the shared prefix, selected worker
and remaining packets are included in the same linear bound. 

### `aggregate`

 The deterministic prefix and the selected prefix may have distinct packet
records. Their reports agree at the actual selector, so the original core
bound pays for the shared prefix exactly once. 
