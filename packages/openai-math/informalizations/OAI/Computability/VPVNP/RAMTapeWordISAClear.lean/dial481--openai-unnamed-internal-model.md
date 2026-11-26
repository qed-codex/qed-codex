---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordISAClear.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordISAClear.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordISAClear.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Clearing a finite set of work stacks

An opcode may retain intermediate words at its return boundary. The caller
clears those stacks before the next instruction, using one pop per bit and
one empty-stack test per selected stack.


### `clearList`

 Clear each listed port by popping its bits until the stack is empty, then return. 

### `cleared`

 Clearing a stack twice has the same result as clearing it once. 
