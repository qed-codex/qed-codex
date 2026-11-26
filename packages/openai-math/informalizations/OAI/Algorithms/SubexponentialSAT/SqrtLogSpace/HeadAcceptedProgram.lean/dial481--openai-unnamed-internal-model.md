---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadAcceptedProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadAcceptedProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadAcceptedProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The fixed accepted-head path first constructs the actual ambient assignment,
then evaluates its selected factor records, adds the resulting dense array to
the head accumulator, and reclaims the arithmetic environment. Zero-valued and
empty factor products follow the same addition/reset path. 

### `accepted`

 This concrete command has no callback or evaluator parameter. 

### `program`

 One fixed head rescan includes entry cleanup, every candidate, and final
counter cleanup. Its dimensions and parameters are read from physical words. 
