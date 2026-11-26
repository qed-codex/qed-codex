---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingProgramAssemblyBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingProgramAssemblyBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingProgramAssemblyBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Numerical closure for the fixed packing scorer.  Every argument of the
bound is an input size or a numeric weight; no running-time oracle occurs. 

### `runBudget_weights_le`

 Direct interface to the two exact weights and four input bit strings
returned by `run_from_memory`. 
