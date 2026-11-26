---
{
  "module": "OAI/Computability/VPVNP/LiveStageOperands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveStageOperands.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveStageOperands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relocating the operands of a native component template

The live stage linker uses one shared register and public-word format. This
embedding allows arbitrary finite component tables, including their private
loads, stores and jumps, to participate in that format. No extra instruction,
probe or choice is introduced by operand relocation.


### `relocate`

 Relabel each native operand while keeping jump targets and literal words fixed. 

### `widen`

 Relocate a template's registers and public operand references, preserving its entry and
instruction positions. 

### `restrictConfig`

 Project a relocated configuration onto its component registers while retaining the program
counter, persistent word, and private memory. 

### `execute_widen`

 The enclosing register file executes the component on its own embedded
operands, with identical event logs, returned words, and rejection behavior. 

### `execute_widen_start`

 At each fresh call boundary operand relocation has zero overhead. 
