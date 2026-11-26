---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSpecializationProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSpecializationProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSpecializationProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Immediate Boolean specialization using the actual dictionary scanner. 

 The dictionary framing, key rewrite and record traversal follow the actual
MomentsProjectionProgramNative implementation. The replacement comparator tests
support inclusion, so this scan implements evaluation at a Boolean correction
assignment. Numeric-key collisions are intentionally left for normalization. 

### `serializedEval`

 Primitive instruction trace with explicit serialized input and output. 

### `raw_dictionary_runsIn`

 The fixed native scanner performs immediate Boolean specialization before
any dictionary multiplication. Duplicate numeric keys await normalization. 

### `raw_dictionary_run_space`

 Every stack, including retained mask, parser buffers, original records and
new records, is included throughout this polynomial local routine. 
