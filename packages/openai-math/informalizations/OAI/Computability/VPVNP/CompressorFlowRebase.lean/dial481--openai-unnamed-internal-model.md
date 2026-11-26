---
{
  "module": "OAI/Computability/VPVNP/CompressorFlowRebase.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorFlowRebase.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorFlowRebase.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Calling a native flow with a register as its persistent argument

The enclosing call keeps its own persistent word. Each persistent-word load in
a component becomes a copy from a register outside its ordinary operand bank.
The component therefore observes one fixed input throughout loops and branches.


### `opAt`

 Relabel an instruction's operands, replacing a persistent-state load by a copy from the
designated argument register. 

### `code`

 Rebase a whole flow on an argument register while relabeling registers, public operands,
and branch conditions. 

### `line_outside`

 One relocated opcode can only write an embedded register. 

### `liftExec`

 Lift a finite small-register computation to the enclosing register space.
All unrelated enclosing registers retain their prior values. 

### `restrictExec`

 Conversely, every successful enclosing execution restricts to a genuine
execution of the original program. Both directions include the exact event log. 
