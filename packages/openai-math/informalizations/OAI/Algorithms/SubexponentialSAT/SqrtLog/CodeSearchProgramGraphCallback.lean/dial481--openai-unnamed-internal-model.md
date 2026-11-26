---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramGraphCallback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramGraphCallback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramGraphCallback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 An actual reusable local-code callback: preparation, the complete word
predicate, then physical cleanup. All surrounding record-parser tapes and
flags are outside the invoked routine's ports. 

### `graphWordCallback_eval`

 Every character uses the same closed bit predicate, whether or not this
candidate graph is good. The cleanup charge includes all arithmetic scratch. 
