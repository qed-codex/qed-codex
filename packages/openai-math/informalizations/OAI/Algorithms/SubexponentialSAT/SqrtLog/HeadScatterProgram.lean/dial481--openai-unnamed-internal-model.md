---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HeadScatterProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HeadScatterProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HeadScatterProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Runtime scatter of head bits into the original ambient coordinate order.
Coordinate identifiers are framed unary words; array replacement is a genuine
runtime scan. No coordinate permutation is compiled into the instruction table. 

### `state`

 The three persistent input stacks are 10, 11, 12. Working stacks are the
ambient mask 0, remaining bits 1, remaining identifiers 2, unary identifier 3,
replacement bit 4, constant width 5, and four array-scan workspaces 6--9. 
