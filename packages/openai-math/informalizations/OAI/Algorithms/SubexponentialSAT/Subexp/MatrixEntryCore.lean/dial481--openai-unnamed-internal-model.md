---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/MatrixEntryCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixEntryCore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixEntryCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The fixed arithmetic workspace and subroutines of the joint-entry program. 

### `prepare`

 On a compatible joint entry the first pop removes the nonfixed unchanged
anchor. Positivity of that count is an explicit premise proved in refinement. 
