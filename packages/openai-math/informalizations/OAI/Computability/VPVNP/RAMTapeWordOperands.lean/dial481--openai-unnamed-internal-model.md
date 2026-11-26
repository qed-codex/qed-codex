---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordOperands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordOperands.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordOperands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading register, public-word and fixed-literal operands

A finite-state scan copies one bit per source cell, restoring the original
word and overwriting the destination. Its finite output transition may copy
the input bits unchanged, or ignore them and emit the low bits of a fixed
literal. In the latter case the source supplies only the word width.


### `State`

 Control for clearing the destination, scanning a source word with a finite bit
transformation, and restoring the source. 

### `code`

 Load an operand word using the given bit transition, overwrite the destination and restore
the source in its original order. 

### `emitted`

 Output bit list and final finite state obtained by applying the operand transformation once
per input bit. 

### `run`

 The source is preserved, the destination is overwritten, and both
scratch stacks are empty on return. 

### `copyBit`

 Load any saved word from a register, the persistent input, or public data. 

### `literalBit`

 A fixed literal is compiled into a finite family of control states for
its successively halved values. Word width affects only the input stack. 

### `literal_run`

 Load a width-dependent residue of a fixed constant. 
