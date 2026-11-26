---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentTableEntryProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentTableEntryProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentTableEntryProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed native table-entry selector. The only input magnitudes are unary
stack data. Output registers 5,6,7 encode the six possible small coefficients. 

### `program_trace`

 A real fixed instruction-table trace, including its final halt. 

### `program_hadicTable`

 Correct small coefficient, with no integer-arithmetic callback. 
