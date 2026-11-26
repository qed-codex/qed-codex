---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramSourceFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramSourceFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramSourceFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact store restoration for the executed source callback. The source
kernel may change its four initialized caches and source output; the wrapper
restores all four caches and removes every staged source control. 

### `coreFrame_of_local`

 Native source-row correctness gives the local frame below; relocation
transports it without imposing any condition on unrelated global masters. 
