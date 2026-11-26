---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramGenerateFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramGenerateFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramGenerateFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `generate_lifted`

 Generic fixed-port call of the closed generator. The result and all frame
claims refer to the actual final state of the bit program. 

### `generate_lifted_update`

 Under the empty-work contract, the generator changes only its designated
output stack. Register scratch remains explicit in the frame assertion. 
