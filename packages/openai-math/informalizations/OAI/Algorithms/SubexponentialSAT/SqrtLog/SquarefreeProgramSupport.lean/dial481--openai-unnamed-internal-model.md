---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramSupport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramSupport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramSupport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed primitive bit-mask union. Both runtime input words have the same
length. The output is prepended in reverse order; no list operation is atomic
and the instruction table does not depend on the word length. 

### `supportUnion_trace`

 Semantic bridge: the exact bit program computes finite-set support union. 
