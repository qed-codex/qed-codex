---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterRenameRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterRenameRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterRenameRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing embedded parser and assembly programs

Relocating operands preserves the complete event sequence and external memory
of every successful structured execution. This allows the uniform assembly
and traversal codes to share one private register file.


### `line_outside`

 One relocated opcode can only write an embedded register. 

### `liftExec`

 Lift a finite small-register computation to the enclosing register space.
All unrelated enclosing registers retain their prior values. 

### `restrictExec`

 Conversely, every successful enclosing execution restricts to a genuine
execution of the original program. Both directions include the exact event log. 
