---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PackingUnaryMin.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingUnaryMin.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingUnaryMin.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed destructive minimum routine for unary packing counts. 

### `program_trace`

 Count words are compared by actual simultaneous pops. Both inputs are
cleared, and the result is a canonical true-unary minimum. 
