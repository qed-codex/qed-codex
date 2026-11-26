---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ProducedQueryResourcesOrigin.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ProducedQueryResourcesOrigin.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ProducedQueryResourcesOrigin.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual selector provenance for a query.  This package includes every
trial (successful or not), the final selected rows, and an optional mark.
It carries no resource inequality about the resulting query. 

### `Origin`

 Inputs and exact row identity of an actual generated selector query. 

### `ScanBounds`

 Numerical output from the actual neutral-completed scan and high mask. 

### `eventually_scan_bounds`

 One cutoff for all generated queries and marks. No cardinality, rank,
head-size, or runtime premise is hidden in selector provenance. 
