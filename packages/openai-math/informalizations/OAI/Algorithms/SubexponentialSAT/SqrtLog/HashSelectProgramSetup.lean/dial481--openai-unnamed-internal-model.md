---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramSetup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramSetup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramSetup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A concrete 10-register, 14-stack layout joins runtime tuple generation to
the selector. It can be relocated into a larger evaluator with liftProgram. 

### `setup_eval`

 Initial input convention: stacks 0..8 empty, rows in 9, family destination
10 empty, alphabet in 11, runtime tuple depth in 12, runtime K in 13. 
