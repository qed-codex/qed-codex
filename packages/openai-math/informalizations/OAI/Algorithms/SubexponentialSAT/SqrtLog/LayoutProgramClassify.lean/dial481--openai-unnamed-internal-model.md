---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramClassify.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramClassify.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramClassify.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The original fixed-control four-word scan classifies the new integer
numerator too. Only its final scalar arithmetic changes: the read result is
fed to the exact integer formula, not to the old finite-field formula. 

### `integerFromScan_correct`

 The compatibility bit is exactly the guard of the literal integer formula;
the two unary counters are its distance and transposition parameters. 

### `classifyInteger_runsIn`

 Concrete finite bit execution of the classification stage. `integerFromScan`
is the next stage's specification; it is not executed as a machine primitive. 
