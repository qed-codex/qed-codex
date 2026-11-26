---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PolynomialExecutorProgramModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PolynomialExecutorProgramModel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PolynomialExecutorProgramModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual arbitrary-degree RingModel semantics, with no supplied arithmetic
oracle and no supplied value of the input source expression. 

### `model_run`

 The fixed interpreter reads source instructions, performs native arithmetic,
and leaves a framed coefficient array with the exact truncated meaning. 

### `model_primitive`

 Primitive execution inherits the fixed-table simulation constant. The
output array and its polynomial meaning are the same as for native execution. 
