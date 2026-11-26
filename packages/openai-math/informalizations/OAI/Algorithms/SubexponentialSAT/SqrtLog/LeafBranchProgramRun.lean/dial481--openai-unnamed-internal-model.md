---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafBranchProgramRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafBranchProgramRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafBranchProgramRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual overflow-controlled aggregation. The looser quadratic-in-branches
bound accommodates arbitrary leading zeroes in native binary answers. 

### `loop_sum`

 Loop induction follows actual callback and odometer executions. `limit`
bounds the total allocated binary length, not a supplied list of answers. 

### `enumerate_sum`

 Full branch aggregation executes a fixed loop and returns the exact sum
of the counts computed by its actual residual callback. 

### `visits_counter_length`

 The native odometer keeps the framing width constant through every visit. 
