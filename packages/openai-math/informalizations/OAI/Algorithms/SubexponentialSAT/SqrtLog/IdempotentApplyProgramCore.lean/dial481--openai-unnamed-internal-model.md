---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramCore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Algebraic invariant for the native descending Horner application. Each
coefficient digit has three entries, and no power is recomputed by expansion. 

### `apply_coefficients`

 Horner application equals the exact H-adic indicator polynomial, with U
combined into the Horner multiplier rather than expanded into stored powers. 
