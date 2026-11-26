---
{
  "module": "OAI/Computability/VPVNP/RAMTapeISASemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeISASemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeISASemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Instruction dispatch and its typed exits

A local instruction updates the register or private-log bank before reporting
the next program counter. Binary choices and external reads and writes are
returned to the call controller. This separates their charging and bit choices
from the deterministic work of fetching and interpreting the instruction.


### `Callback`

 Typed instruction exit carrying the next counter, a choice, an external access, a returned
state, or a halt decision. 

### `Callback.action`

 Native continuation represented by the exit label and the resulting
architectural bank. The outer call controller handles the read answer and the
binary choice. 

### `post`

 The fields written by deterministic instruction preparation. The program
counter belongs to the finite control and is set by `Callback.action`. 

### `exitFor`

 Determine an instruction’s typed exit, using the supplied test bit to select the target of
a conditional jump. 

### `jumpTest`

 Only conditional jumps leave a single-bit test result for the dispatcher. 
