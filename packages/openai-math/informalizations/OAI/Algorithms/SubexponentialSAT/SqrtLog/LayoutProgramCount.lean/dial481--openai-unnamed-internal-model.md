---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The scalar loop length R−d is computed by deleting actual unary tokens.
The scan's distinguished unchanged anchor is removed first. Neither natural
subtraction nor a loop-count constructor is a machine primitive. 

### `command_eval`

 Removes the anchor token, then computes the required saturating length. 
