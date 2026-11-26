---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterRename.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterRename.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterRename.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Register and public-word placement for the pair counter

The input passes and the preorder parser use their own local operand numbers.
Relabeling the operands embeds each finite block into the common auxiliary
machine. A native write to a register still has exactly the specified effect
on the embedded register file.


### `renameOp`

 Relocate both operand spaces of a native instruction. 

### `effect_rename`

 Restricting the updated large register file gives the same operation as
executing directly on the small register file. Reads, writes, guard failures
and the emitted RAM event agree exactly. 

### `renameFlow`

 Relabel the operands of an entire structured graph, preserving its branch
order and all of its loop back edges. 

### `renameLabels`

 Instruction labels are transported according to their enclosing blocks. 
