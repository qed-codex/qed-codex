---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramTableStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramTableStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramTableStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `coefficientStep`

 Assemble a triple from saved tail, next polynomial coefficient, and -1;
perform the native multiply-add; retain the last output and advance a's shift. 
