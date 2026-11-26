---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramDynamicFold.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramDynamicFold.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramDynamicFold.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A measured physical record fold with accumulator-dependent cost. This
retains the actual fixed callback and parser; the cost recurrence can account
for changing sparse dictionary lengths without postulating a uniform bound. 

### `Contract`

 A refinement relation may track the sparse accumulator and arbitrary
persistent machine context. The callback must consume its parsed payload. 
