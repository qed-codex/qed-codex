---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramGraphPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramGraphPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramGraphPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed physical input preparation for the Walsh character checker. The
matrix, row count, and two binary scalar words are copied from persistent tapes. A parsed
reversed payload is transferred once, restoring the word's forward order. 
