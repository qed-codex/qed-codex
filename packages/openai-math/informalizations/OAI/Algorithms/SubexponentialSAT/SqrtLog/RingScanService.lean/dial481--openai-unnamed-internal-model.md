---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanService.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanService.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanService.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 One fixed native service for arbitrary-degree coefficient-ring products. 

### `serviceMul_eval`

 Complete native multiplication, including table copying, paid triple
expansion, both unary counters, scalar contraction, and all cleanup. The
cached table is preserved; its one-time construction is a separate service. 

### `serviceMul_primitive`

 The fixed service compiles to a primitive bit machine; the constant
simulation overhead depends only on the instruction table. 
