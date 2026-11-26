---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/NativePackingBoundsGenerated.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/NativePackingBoundsGenerated.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/NativePackingBoundsGenerated.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Native address-plan frontend bounds. The source size includes the actual
input plans and the number of represented types, not a scope-generated plan. 

### `label_stream_le`

 The label tape starts empty, so its length is bounded by its actual
executed instruction count. No output-length certificate is assumed. 
