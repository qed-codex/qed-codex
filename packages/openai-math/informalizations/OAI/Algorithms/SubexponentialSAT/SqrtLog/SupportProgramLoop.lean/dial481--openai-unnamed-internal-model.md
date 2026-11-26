---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A single finite loop visits all runtime mask lengths. Its body is the
actual expansion and pruning program, not a semantic recursion instruction. 

### `Invariant`

 The counter and registers are deliberately absent from the data invariant. 

### `program_trace`

 The same instruction table works for every n and J. The output masks are
complete and duplicate-free; the bound uses exactly the binomial support count. 
