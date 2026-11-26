---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramRegisters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramRegisters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramRegisters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Source-preserving storage for the fixed Newton register machine. Every
copy, replacement, and clearing operation is an actual finite bit program. 

### `storeResult`

 Store the computed result, preserving bit order and emptying the result port. 

### `prepareOperands`

 The cached unary degree is copied; the raw service may consume its copy. 

### `registerBinary`

 The complete register operation has fixed syntax. `raw` is the shared
native service, lifted to the low 32 stacks. 

### `registerBinary_eval`

 All argument copies and the replacement are paid. The only hypothesis
about the arithmetic itself is an actual evaluation of its fixed command. 
