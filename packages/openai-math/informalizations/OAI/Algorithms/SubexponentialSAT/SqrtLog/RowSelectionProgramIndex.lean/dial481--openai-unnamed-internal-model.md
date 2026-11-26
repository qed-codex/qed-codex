---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelectionProgramIndex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelectionProgramIndex.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelectionProgramIndex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Runtime, self-delimiting natural-index alphabet. The range control is the
existing unary loop, with one delimiter inserted in each emitted payload. 

### `encodeTuple`

 A length-m function into Fin a, serialized as m self-delimiting natural fields. 

### `tupleRows`

 The actual row order emitted by the fixed tuple generator. 
