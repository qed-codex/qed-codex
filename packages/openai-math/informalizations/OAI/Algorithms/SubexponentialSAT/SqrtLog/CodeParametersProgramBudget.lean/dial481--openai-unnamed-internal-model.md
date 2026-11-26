---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeParametersProgramBudget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeParametersProgramBudget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeParametersProgramBudget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Ordinary-polynomial cost of the actual sparse-code metadata producer.
The two exhaustive code searches have separate costs; this file accounts
for the fixed arithmetic table and all seven unary materializations. 

### `fullBudget_envelope`

 This bound includes the halt after the actual native metadata command. 

### `runtime_ordinary`

 A fixed ordinary polynomial bounds every arithmetic operation, copy,
comparison and unary output in the metadata producer. Input padding is
charged through ml and Bl. Numeric B does not enter this input measure. 
