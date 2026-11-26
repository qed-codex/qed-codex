---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorProductSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorProductSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorProductSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The original concrete factor accumulator, with empty correction support.
All three tape moves and the original sparse product call are charged. 

### `budget_polynomial`

 The degree and constant are fixed independently of all input dimensions. 

### `accumulate_run_space`

 The same executed accumulator returns a valid bounded dictionary and an
exact frame for every other stack. Its polynomial local time controls every
prefix, including all caller storage and all native arithmetic temporaries. 
