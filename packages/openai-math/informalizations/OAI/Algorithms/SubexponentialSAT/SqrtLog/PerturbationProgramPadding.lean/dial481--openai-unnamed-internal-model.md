---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramPadding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramPadding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramPadding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Explicit finite scalar-to-polynomial padding. The runtime degree and
coefficient width are tapes, so this command is independent of all dimensions. 

### `iteration`

 Read a scalar, build its padded constant polynomial, prepend that cell to
an accumulating output stream, and restore every temporary stack. 

### `fold_output`

 Starting with highest degree first makes the final stream coefficient-zero first. 
