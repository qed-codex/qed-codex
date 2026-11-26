---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CRTLocalProgramInverse.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CRTLocalProgramInverse.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CRTLocalProgramInverse.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Native residue-power preparation with dynamic extension degree and ring
precision. Stack 209 contains a unary residue-size-minus-two exponent;
stack 212 independently contains the unary ring precision. 

### `defectCommand`

 The remaining scalar inverse stages: form the residue defect, then run
the precision-many geometric recurrence. Every operator is a fixed command. 
