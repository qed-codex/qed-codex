---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramCallback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramCallback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramCallback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 An actual reusable local-code callback: preparation, the complete word
predicate, then physical cleanup. All surrounding record-parser tapes and
flags are outside the invoked routine's ports. 

### `wordCallback_eval`

 Callback correctness is unconditional on the supplied matrix; a rejected
candidate is processed by the same bit program. The quantitative theorem is
separate so that cleanup, too, must be charged. 
