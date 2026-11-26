---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A complete fixed primitive support-mask generator. Only two unary input
stacks are preloaded; the constant alphabet and seed record are written by the
program. Each stage prunes overweight masks before the next expansion. 

### `inputState`

 Both runtime integers use unary stacks here; their bits are immaterial.
Every other stack starts empty, including the output. 

### `primitive_runsIn`

 Executed output enumerates each squarefree support exactly once, with a
bound polynomial in n,J times the exact binomial count M_J. 
