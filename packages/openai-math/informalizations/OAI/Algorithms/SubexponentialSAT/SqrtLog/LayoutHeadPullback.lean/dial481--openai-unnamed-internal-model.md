---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutHeadPullback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutHeadPullback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutHeadPullback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Pullback of a head-coherent incidence layout to the original variables. 

### `headOwner`

 The owner map restricted to one original-variable head. 

### `row_restrict`

 Pulling a row back and then restricting its columns to a head is the
same operation as pulling back along the restricted owner map. 

### `pullback`

 An actual copy layout whose head labels are induced by `owner` gives an
original-variable layout. All constraints remain integer fiber sums. 
