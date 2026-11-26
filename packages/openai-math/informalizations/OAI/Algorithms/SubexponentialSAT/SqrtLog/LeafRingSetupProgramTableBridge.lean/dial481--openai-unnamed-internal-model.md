---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafRingSetupProgramTableBridge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafRingSetupProgramTableBridge.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafRingSetupProgramTableBridge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Physical table-input projection and the exact native table-call bridge. 

### `TableInput`

 Physical inputs to the table producer. The polynomial bytes are supplied
by `searchAndPad_eval`, and the scalar bytes by `scalarCall_eval`. 

### `tableCall_produces`

 No table is supplied to this call. It runs native power recurrence and
layout on the actual runtime coefficient array. 
