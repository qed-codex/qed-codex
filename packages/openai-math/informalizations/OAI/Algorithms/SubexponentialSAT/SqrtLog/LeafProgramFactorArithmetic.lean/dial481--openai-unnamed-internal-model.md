---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorArithmetic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual native multiplication call in the wide factor loop. This
adapter derives its execution from the concrete sparse product program and
retains an exact frame, including every outer factor/source tape. 

### `accumulate_eval`

 One factor is computed on67 and multiplied into the persistent running
product151. All three moves and the native product execution are charged. 
