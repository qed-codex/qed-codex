---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramIncidence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramIncidence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramIncidence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The native lookup theorem specialized to actual hash-indexed incidence
payloads. Every occurrence of a variable uses the payload from the selected
hash slice; lookup correctness is discharged rather than an extra premise. 

### `canonicalLiteral_incidence`

 This is the direct original-literal input theorem, with the selected hash
index retained explicitly in the payload function and physical table. 
