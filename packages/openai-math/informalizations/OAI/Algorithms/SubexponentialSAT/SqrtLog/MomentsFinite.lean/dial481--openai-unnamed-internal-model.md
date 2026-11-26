---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsFinite.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsFinite.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsFinite.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Bridge from explicit head-assignment/support lists to finite-sum semantics.
The only enumeration requirements are no duplicates and exact membership.
The lists may be supplied by the primitive mask and bucket enumerators. 

### `run_finite_bucket`

 The executable finite-list run equals the actual Boolean bucket product.
This is the squarefree head-moment computation used at a node. 
