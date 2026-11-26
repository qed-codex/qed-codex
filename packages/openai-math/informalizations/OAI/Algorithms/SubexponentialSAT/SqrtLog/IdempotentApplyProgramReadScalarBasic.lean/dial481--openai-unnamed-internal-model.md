---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramReadScalarBasic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramReadScalarBasic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramReadScalarBasic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Scalar loading uses only checked stack primitives and constant formatting.
This definition boundary keeps its correctness independent of polynomial arithmetic. 

### `readScalar`

 Taking a word from the reversed coefficient tape reverses just that word,
so stack80 receives the original forward scalar representation. 
