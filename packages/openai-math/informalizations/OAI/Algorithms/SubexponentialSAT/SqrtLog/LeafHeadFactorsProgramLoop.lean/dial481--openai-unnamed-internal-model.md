---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafHeadFactorsProgramLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafHeadFactorsProgramLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafHeadFactorsProgramLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `loop_visits`

 Descending physical visits prepend records, so the resulting list is in
ascending original-factor order. Every visit is discharged by visit_row. 
