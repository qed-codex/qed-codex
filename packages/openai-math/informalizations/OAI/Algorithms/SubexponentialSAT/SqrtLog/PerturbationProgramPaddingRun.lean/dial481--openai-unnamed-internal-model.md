---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramPaddingRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramPaddingRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramPaddingRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `command_run`

 Full native construction of the homogeneous stream required by polynomial
Horner, from the actual serialized scalar coefficient array. No padded-input
oracle is assumed: both all zero bits and every copied coefficient are paid. 
