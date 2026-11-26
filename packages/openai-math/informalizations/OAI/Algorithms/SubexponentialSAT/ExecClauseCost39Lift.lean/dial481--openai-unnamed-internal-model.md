---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecClauseCost39Lift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecClauseCost39Lift.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecClauseCost39Lift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `membershipEqReg`

 Fixed register ports for the membership routine's equality subroutine. 

### `membershipEqStack`

 Compare caller stack 1 with caller stack 3. 

### `membershipEq_eval`

 The actual comparator call framed in the membership routine's fixed ports.
Unassigned data is preserved, and the inspected stacks retain bounded tails. 
