---
{
  "module": "OAI/Algorithms/SubexponentialSAT/BitProgramCompile.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BitProgramCompile.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BitProgramCompile.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The finite Boolean-stack language compiles instruction for instruction to
an actual finite TM2 machine. The verified stack compiler then supplies measured
primitive tape executions. No source instruction contains an unbounded function.


### `tm`

 All three finite dimensions are determined by the fixed source program. 

### `tm_step`

 A source instruction is exactly one finite TM2 block execution. 

### `primitive`

 The output is a fully specified primitive tape machine, obtained by the
previously verified finite-control and stack-block compilers. 

### `primitive_halted`

 Halting exposes the first output bit, without a cleanup precondition on
the remaining stacks or the finite Boolean registers. 
