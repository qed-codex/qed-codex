---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramFinal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramFinal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramFinal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Full native application of a computed idempotent coefficient array.
The multiplier is built from H and ordinary cached constants; the indicator
is then computed by the measured Horner loop. 

### `command_eval`

 No desired polynomial is supplied to the command: only H, scalar constants,
and the computed base-coefficient tape occur in the initial memory contract. 

### `applied_coefficients_denote`

 Exact semantics of the bytes produced by the native application command. 

### `program_coefficients`

 The fixed native program consumes the concrete array computed by the lift
and returns the stored indicator polynomial with the stated exact meaning. 
