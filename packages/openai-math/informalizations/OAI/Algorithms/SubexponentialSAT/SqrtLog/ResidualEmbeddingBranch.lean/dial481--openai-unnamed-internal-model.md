---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ResidualEmbeddingBranch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ResidualEmbeddingBranch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ResidualEmbeddingBranch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed high-coordinate branches and original ambient coordinate labels.
Only free assignments are summed inside one branch. 

### `Branch`

 Compatibility with the fixed values of the high variables. 

### `neutral_scope_avoids_high`

 The neutral factors are formed in the free universe; hence even an unused
high coordinate cannot create a neutral factor or an additional assignment. 
