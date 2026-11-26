---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Input-only contract for the closed native low-variable worker. 

### `LowInput`

 This record describes only the actual incoming words, arithmetic caches,
and empty work tapes. It contains no evaluation or execution oracle. 
