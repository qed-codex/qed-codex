---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Runtime-degree readback of a reconstructed scalar count. The original
fixed program already reads a runtime B-bit first word and discards a suffix;
this theorem removes the old four-coordinate type restriction. 

### `extract_eval`

 Physical first-coordinate extraction, with arbitrary remaining dimension. 

### `decisionProgram_run`

 The same dynamic-dimensional reader followed by the audited modular
positivity routine. The Boolean is physically written at output stack zero. 
