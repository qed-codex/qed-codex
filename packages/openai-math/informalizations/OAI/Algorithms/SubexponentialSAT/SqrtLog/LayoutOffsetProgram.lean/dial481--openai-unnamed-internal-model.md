---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutOffsetProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutOffsetProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutOffsetProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed native producer of the signed-bucket offset 2*B*(8*Q)^(2*R).
All arithmetic acts on runtime binary words. This offset is unrelated to
the unary scalar-row width 1+2*A*R+Q. 

### `power_cost_le`

 This bound uses the actual base and exponent word lengths, including
any zero padding. The numerical exponent is an explicit parameter. 
