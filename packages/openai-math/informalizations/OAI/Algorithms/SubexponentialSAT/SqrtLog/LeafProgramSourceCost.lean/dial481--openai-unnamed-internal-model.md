---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramSourceCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramSourceCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramSourceCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Every source-wrapper copy and cleanup is charged against actual word
lengths. The fixed finite allocation makes this overhead linear even without
assuming that intermediate destinations were empty. 

### `saved_bound`

 Coarse bound for a copy list of statically known size, including any
appending to its destinations. 

### `cost_bound`

 Full wrapper overhead, including source-private and arithmetic cleanup.
The core invocation is accounted for separately by its actual step count. 
