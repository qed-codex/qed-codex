---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ProgramProjection.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ProgramProjection.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ProgramProjection.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Inverse projection and exact frame recovery for actual lifted programs.
The program labels are unchanged by port lifting. No execution is added or
postulated: every projected step comes from the concrete lifted instruction. 

### `liftProgram_trace_frame`

 Lifting preserves every unassigned cell throughout an actual execution. 
