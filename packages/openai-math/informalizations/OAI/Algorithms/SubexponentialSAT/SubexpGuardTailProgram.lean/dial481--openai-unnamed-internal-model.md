---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpGuardTailProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpGuardTailProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpGuardTailProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual arithmetic operands for the tail guard

Inputs R,Q,delta,s occupy local stacks 0,1,2,3. Outputs R² and
16*Q*delta*s occupy stacks 4 and 5. Stacks 6,7,8 are temporary words and
9 through 13 are arithmetic work. The sources are preserved and every
temporary word is cleared. The constant sixteen is loaded by bit instructions.


### `command_eval`

 Four actual multiplications produce both guard operands. The post-state
changes only the two output stacks, and the runtime is polynomial in input width. 
