---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafWeightProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafWeightProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafWeightProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The Boolean part of a local squarefree head weight, executed by a fixed
parallel scan of the assignment, support mask, and head mask. 

### `good`

 Missing mask cells are unselected; the intended inputs have equal length. 

### `command_eval`

 Exact scan execution. All three work tapes are consumed and register6 is
true precisely when every selected assignment bit is true. 
