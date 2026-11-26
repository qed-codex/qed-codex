---
{
  "module": "OAI/Computability/VPVNP/RAMTapeISAOperand.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeISAOperand.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeISAOperand.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Architectural operand staging and scratch cleanup

Copies may read architectural, public, or temporary stacks. Two reserved
work stacks hold the reversed source and output during a copy. A same-register
copy is a separate no-op in the instruction dispatcher. Other instructions
stage their inputs before writing a destination that aliases an input.


### `copySafe`

 The port avoids work stacks 14 and 15, both reserved by operand copying. 

### `copyPorts`

 Route a copying scan to the source, destination, and the two reserved work stacks. 

### `loadOperand`

 Copy a word from the source port to the destination with the finite operand scan. 

### `clearPort`

 Clear a stack by popping until the first empty test. 

### `loadLiteral`

 Load a fixed natural literal into the destination register using the persistent word to
determine the bit width. 

### `loadLiteral_at`

 A fresh call may initially have empty registers. The width template in
the persistent port determines the literal independently of the old register. 
