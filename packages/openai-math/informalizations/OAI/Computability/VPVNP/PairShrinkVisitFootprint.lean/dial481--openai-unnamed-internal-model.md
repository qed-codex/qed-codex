---
{
  "module": "OAI/Computability/VPVNP/PairShrinkVisitFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkVisitFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkVisitFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Read-only support of a complete shrinking vertex visit

A successful visit follows the child, absorbed-field and map readers on the
scratch and tape returned by their predecessors. The union of their actual
read domains bounds the chronological trace even if a later DFS visit fails.


### `TraceSupport`

 Every external memory access in the trace is a read at an address satisfying `allow`. 

### `visit_footprint`

 Only readers that the native visit reaches contribute to the footprint. 
