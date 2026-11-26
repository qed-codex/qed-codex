---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramMachine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed native control for applying computed idempotent coefficients.
The input and output ABI is documented below. The semantic execution theorem
is a separate obligation; this module supplies concrete instructions only. 

### `prepareMultiplier`

 H(H-1)(H-2)=H(1-H)(2-H). The latter form reuses the checked native
complement service, whose cached constants are ordinary ring data. 

### `tripleStep`

 Two products and two sums evaluate one quadratic coefficient digit. 

### `hornerStep`

 Exactly three scalar loads, three polynomial products and three sums.
The coefficient order is c,b,a because the whole coefficient tape is reversed. 

### `command`

 Input68 is raw H;78 holds the forward computed coefficient tape;88 is
an ambient shape word. Cached one69 and minus-one76 and the low56 product
environment are preserved. Output67 is the raw indicator dictionary. Scratch
61,70,79..87,89..95 must be empty initially and is reclaimed before return. 
