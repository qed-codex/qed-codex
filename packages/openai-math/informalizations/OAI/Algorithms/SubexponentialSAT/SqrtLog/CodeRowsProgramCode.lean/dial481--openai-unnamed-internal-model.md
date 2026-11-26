---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeRowsProgramCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeRowsProgramCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeRowsProgramCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The finite table for sparse code rows. Runtime loops visit vertices,
local checks, and local ports only. The original clause count is used for a
binary comparison, never as the bound of a per-row scan. 

### `coefficientOffset`

 Coefficients are 0, 1, or 2, with one-hot bits saved on registers8/9. 

### `zeroVertexStacks`

 The supplied unary r shape creates the initial zero vertex word. 
