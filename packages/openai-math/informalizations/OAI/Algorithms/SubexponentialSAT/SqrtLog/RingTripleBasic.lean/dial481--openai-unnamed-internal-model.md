---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingTripleBasic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingTripleBasic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingTripleBasic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed-port primitives for dynamic Cartesian triple expansion. All loop
bounds and coefficient widths are words on stacks, not generated code. 

### `loadPorts`

 0 loads the next y, 1 the next table coefficient, 2 the next x. 
