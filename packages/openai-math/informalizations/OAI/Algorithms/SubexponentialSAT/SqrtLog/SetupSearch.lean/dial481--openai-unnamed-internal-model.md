---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SetupSearch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SetupSearch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SetupSearch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `guard_eval`

 The guard is an actual finite subroutine call; all caller stacks are framed. 

### `save_eval`

 Saving the current candidate overwrites only the answer port. 

### `body_eval`

 One real callback performs one candidate test. 

### `command_eval`

 Exact bounded-search schedule. The input data include the coefficient w^4,
L, and a second copy of L as loop fuel. Each callback is a genuine arithmetic
trace and every failed candidate is charged. 
