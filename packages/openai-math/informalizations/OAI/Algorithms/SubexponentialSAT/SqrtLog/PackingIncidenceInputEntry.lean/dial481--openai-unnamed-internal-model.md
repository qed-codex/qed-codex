---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingIncidenceInputEntry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingIncidenceInputEntry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingIncidenceInputEntry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Entry from the actual descending high mask produced by the high-variable pass. 

 Raw scopes and the computed mask feed the actual incidence-pair producer. 

### `primitive_pairs`

 The primitive output is the table whose order is accepted by the exact
conditional incidence scorer. No linear read-plan table is an input. 

### `score_refines`

 The very same generated plan order refines the exact Cinc score. 

### `entry_budget_le`

 Explicit polynomial bound for the whole descending-mask-to-pair-table path. 
