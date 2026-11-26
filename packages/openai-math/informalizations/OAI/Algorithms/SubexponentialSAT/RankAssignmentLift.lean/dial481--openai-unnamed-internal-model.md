---
{
  "module": "OAI/Algorithms/SubexponentialSAT/RankAssignmentLift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/RankAssignmentLift.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/RankAssignmentLift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Direct caller-state interface for the preserving rank-padding program. 

### `programAt_trace`

 Only the caller's designated output stack changes. The other assigned and
unassigned stacks are both framed, without an opaque state-embedding endpoint. 
