---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeScaleProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeScaleProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeScaleProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Base stage. 

 Fixed physical ABI for scaling all coefficients in a sparse dictionary.
The low 32 stacks are the common coefficient-ring service. The eight high
stacks hold source, reversed output, scalar, key, coefficient staging, frame
staging, final output, and a preserved copy of the unary degree. 

 Moves stage. 

 Emit stage. 

### `emit`

 Emit one result into a reversed stream. Reversing the complete stream once
at the end restores the original record order. 

 Native stage. 

 Loop stage. 

 Cost stage. 

 Semantics stage. 
