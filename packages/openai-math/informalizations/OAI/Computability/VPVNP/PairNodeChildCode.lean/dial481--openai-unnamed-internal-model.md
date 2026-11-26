---
{
  "module": "OAI/Computability/VPVNP/PairNodeChildCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A finite instruction table for a parent's child scan

For a fixed old degree, the table contains the parent header, the shared
child loop, and the setup, width lookup, and guess code of every outgoing
and incoming slot. All destinations refer to its finite label set except
the supplied return address. The same region can be embedded in a larger
vertex handler.


### `Slot`

 One incidence slot of an old site. The Boolean selects outgoing (false) or incoming (true),
and the ordinal selects one of the 2^a ports in that direction. 

### `SlotLabel`

 Instruction labels within a single slot, divided into two for port setup, six for the width
lookup and seven for guessing and storing field bits. 

### `Label`

 Labels for the entire child scan. The alternatives distinguish the parent header, loop
guard, child address calculation and instructions specific to each incidence slot. 

### `size`

 Number of child-scan instructions before the return destination. The shared blocks use 27
instructions, and each of the 2 · 2^a slots contributes 15. 

### `number`

 Arithmetic numbering of all parent and slot instructions. 

### `headerPC`

 Program counter of the j-th parent-header instruction in the supplied placement of
child-scan labels. 

### `sites`

 Restricts the label placement to the loop guard, address calculation and three blocks for
each slot, giving the destinations needed to link the child loop. 

### `instructionWith`

 Emit the relative instruction at a body label. The slot loader may read
a public operand or a private ordinal register. 

### `linkedWith`

 A machine containing this code satisfies every linkage condition, including
the return from the last slot to the original parent guard. 

### `instruction`

 The original table obtains its slot names from public operands. 

### `localPC`

 A standalone parent handler has one terminal instruction in addition to
its child scan. Slot ordinals use the corresponding public parameter number. 

### `table`

 Standalone 16-register machine template for a parent scan. It starts at the first header
instruction, loads slot ordinals from public operands and returns to a final accept
instruction. 
