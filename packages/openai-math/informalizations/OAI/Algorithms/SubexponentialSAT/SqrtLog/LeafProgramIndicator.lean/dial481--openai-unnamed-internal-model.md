---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramIndicator.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramIndicator.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramIndicator.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A closed native sparse-hash indicator service. It first interprets the
actual inline weighted-clause row and then applies the computed idempotent
coefficient tape. The resulting indicator is never supplied as input. 

### `command_eval`

 Both constituent executions are derived from their concrete native
programs. All dimensions, clauses, and coefficients remain runtime data. 

### `callerRegisters`

 The node's theta remains on global78. The coefficient tape expected on
local78 is relocated to143, which is reserved by the assignment producer. 
