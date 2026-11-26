---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordISAStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordISAStage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordISAStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Register-level execution of the binary word instructions

The dispatcher stages both operands in separate stacks before executing the
arithmetic kernel. This supports every alias among the two input registers and
the destination. The result is written back, and the finite bank of temporary
stacks is cleared before the instruction returns.


### `kernelPort`

 Map a local arithmetic stack to its reserved work port in the simulated instruction
machine. 

### `arithmeticKernel`

 Execute the binary opcode's fixed stack program on the designated arithmetic work ports. 

### `workPorts`

 All sixteen scratch ports cleared before control returns from the simulated instruction. 

### `binary`

 A finite routine whose entry and control depend only on the opcode and
three register indices. Word width affects only the stack contents. 

### `binary_runs`

 Every binary opcode restores the architectural bank with exactly its
destination register updated. The bound covers staging, arithmetic, writeback
and cleanup of all sixteen work stacks, even for division by zero. 
