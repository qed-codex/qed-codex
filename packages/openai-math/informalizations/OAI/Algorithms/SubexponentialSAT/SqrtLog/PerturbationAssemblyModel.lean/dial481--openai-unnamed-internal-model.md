---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyModel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual fixed-length polynomial services instantiate the shifted-row
machine. Its semantic result follows from the executed Horner fold. 

### `native_shift_run`

 Native multiply/add contracts are discharged here. The only remaining
premises describe the runtime scalar row, constants, caches, and scratch. 
