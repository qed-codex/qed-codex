---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsABGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsABGraph.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsABGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# AB rows in the mathematical motif numbering

The bundle-total column is indexed by the assigned outgoing port. The native
piece scan constructs widths and starts in the same order as the AB demands
at their two packed endpoints, for every absolute lane and every parallel port.


### `ABColumns`

 Memory representation of all two-ended AB fields, with natural addresses and
the stride used by the term-row and kernel-slice readers. 

### `graph_run`

 All AB widths and offsets are computed in one native segment. 
