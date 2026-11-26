---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramSourceBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramSourceBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramSourceBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Uniform byte and running-time bounds for each actually emitted finite
source row. The bound uses the full table width, not the rational rank. 

### `source_bounds`

 The scalar table and inverse tables have been materialized. The audited
emitter bound now applies to the actual finite row, including all reads. 

### `indices_length_le`

 The native mismatch-index stream is itself polynomial-sized. 
