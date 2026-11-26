---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramQueryReadbackStore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramQueryReadbackStore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramQueryReadbackStore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact wide-store restoration for count readback.  Parser and odometer
registers are preserved even though the reusable narrow ABI includes them. 

### `completed_stacks`

 All reader temporaries were blank before the call. Thus only its source
coefficient and output count differ at return. 
