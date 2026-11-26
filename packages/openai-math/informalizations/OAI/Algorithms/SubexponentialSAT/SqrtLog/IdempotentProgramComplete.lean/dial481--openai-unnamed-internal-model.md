---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramComplete.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramComplete.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramComplete.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed finite bit program constructs the ternary H-adic lift from its
binary precision alone. Preparation, array arithmetic, iteration and output
serialization are all covered by actual bit-instruction traces. 

### `completeProgram_runs`

 The input has only the binary precision in stack 31. No arithmetic table,
constants, counter, advice or other prepared data is supplied to the machine. 

### `completeProgram_indicator`

 The actual output words are t polynomials of degree below three whose
H-adic sum is the required local indicator. 
