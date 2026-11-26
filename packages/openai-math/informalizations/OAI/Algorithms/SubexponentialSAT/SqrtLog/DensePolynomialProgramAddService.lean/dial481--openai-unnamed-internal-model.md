---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramAddService.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramAddService.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramAddService.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The arbitrary-degree native adder relocated into a caller, with all
untouched stacks preserved. 

### `callAt`

 Relocate the fixed addition program into a caller's physical workspace. 

### `callAt_eval`

 The relocated call changes only its two input/output ports. The complete
bit-level addition trace, including its return instruction, is retained. 
