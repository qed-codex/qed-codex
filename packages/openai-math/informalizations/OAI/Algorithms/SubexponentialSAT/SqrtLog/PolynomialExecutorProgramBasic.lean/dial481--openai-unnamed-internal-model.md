---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PolynomialExecutorProgramBasic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PolynomialExecutorProgramBasic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PolynomialExecutorProgramBasic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Executable coefficient-array meaning of the row postfix interpreter.
Literal padding and all arithmetic operate on stored coefficient words. 

### `evaluate_full`

 No degree restriction on intermediate expressions is required. The final
row degree bound alone restores the complete polynomial. 
