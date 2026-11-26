---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanAdd.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanAdd.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanAdd.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Native scalar addition inside a flat, runtime-sized coefficient scan. 

### `addTapes`

 The lower eight stacks are precisely the audited scalar ABI. The remaining
seven contain the flat input vectors, output accumulator, and unary controls. 

### `addStep_eval`

 One real coefficient step, including both dynamic-width loads and output
movement. All input suffixes and unary controls are preserved exactly. 
