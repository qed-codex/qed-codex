---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsProgramProduct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsProgramProduct.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsProgramProduct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed sparse-product instruction table. Its three subservices perform
coefficient scaling, key join/clipping, and additive normalization, respectively.
All outer source lengths and ring dimensions live on tape. 

### `idle`

 Common product idle store: caches and runtime controls only. 

### `environment`

 Runtime persistent context. Every non-context low stack is initially empty. 

### `program_run`

 Public product ABI, with all scratch stacks empty at return. 
