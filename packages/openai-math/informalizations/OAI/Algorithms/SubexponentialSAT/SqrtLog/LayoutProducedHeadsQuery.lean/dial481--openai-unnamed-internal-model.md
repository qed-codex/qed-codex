---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProducedHeadsQuery.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProducedHeadsQuery.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProducedHeadsQuery.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The maximum size of an actually emitted head list is bounded directly
from a query's integer guards. Ambient owner IDs remain unchanged, while
all layout parameters use the measured free-variable count. 

### `query_max_bound_rat`

 This is the actual finite maximum over all node/head addresses, not an
assumed head-size parameter. No validity premise beyond the checked integer
guards is needed for these structurally deduplicated query scopes. 

### `query_max_bound_real`

 Form consumed by the produced-query resource envelope: ambient head
sizes with the free-variable layout schedule. 
