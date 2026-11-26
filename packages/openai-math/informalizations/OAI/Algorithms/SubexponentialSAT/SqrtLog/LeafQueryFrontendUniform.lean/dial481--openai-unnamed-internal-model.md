---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafQueryFrontendUniform.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafQueryFrontendUniform.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafQueryFrontendUniform.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `frontend_eval_input_bound`

 The actual frontend has a bound depending only on its physical input query
and the fixed formula width. No intermediate state or computed padding witness
occurs in this bound. 

### `frontend_time_le`

 The input bound applies to every occurrence of the frontend in a larger
execution, by uniqueness of its deterministic instruction count. 
