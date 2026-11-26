---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafScopeResourceBoundsReachable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafScopeResourceBoundsReachable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafScopeResourceBoundsReachable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Pointwise bounds on every trial of the concrete selector recurrence.
The score may be arbitrary: resource validity does not assume score correctness. 

### `supplied_trial`

 The actual supplied code-row table plus the actual selector trial and optional
marked clause. All assumptions concern runtime parsing or input width. 
