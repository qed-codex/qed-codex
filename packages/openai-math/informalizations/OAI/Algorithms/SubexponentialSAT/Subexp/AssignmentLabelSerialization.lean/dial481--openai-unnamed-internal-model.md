---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentLabelSerialization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentLabelSerialization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentLabelSerialization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The vertex-label producer emits exactly the semantic bucket records,
in ascending vertex order before its explicit accumulator reversal. 

### `labelRecords_eq_vertexRecords`

 Gathering every actual seed array at the supplied typed read plans
produces exactly the type-key and unary-vertex records used by the bucket. 

### `labelBytes_eq_vertexRecords`

 The physical accumulator stores the same records in reverse list order. 

### `natural_labelRecords_eq_vertexRecords`

 The producer can consume the rows already emitted by the natural
assignment loop, without reserializing or reordering that assignment. 
