---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorBase.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorBase.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorBase.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Wide native factor arithmetic and paid tape movement. 

### `accumulate`

 The running head-local product is parked on151 while the next factor is
computed on67. Native multiplication consumes61 and returns67. 

### `moved`

 Movement itself is paid; output-state notation is used only in proofs. 
