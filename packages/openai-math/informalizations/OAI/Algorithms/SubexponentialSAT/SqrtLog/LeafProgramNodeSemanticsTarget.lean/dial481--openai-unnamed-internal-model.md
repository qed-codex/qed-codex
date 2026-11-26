---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeSemanticsTarget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeSemanticsTarget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeSemanticsTarget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The reconstruction target retains one shared total U-order. Its source
rows retain original variable identifiers, and its outer sum is over free
Boolean assignments in one fixed-high branch. 

### `hashPath`

 A row is evaluated as the supplied sparse clause circuit. 

### `digitAt`

 The digit family may be the actual computed coefficient array; there is
no assumption that its untruncated product has the required small degree. 
