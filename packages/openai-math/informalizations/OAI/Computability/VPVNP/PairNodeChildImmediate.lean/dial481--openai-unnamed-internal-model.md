---
{
  "module": "OAI/Computability/VPVNP/PairNodeChildImmediate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildImmediate.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildImmediate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Child-argument scans on the eleven-operand vertex machine

A fixed register bank supplies every slot number. The initializer writes zero
and one as instruction literals and derives each following ordinal by addition.
The body uses a register copy in the slot's existing setup instruction. The
number of setup instructions and the field, packet and probe traces of the
child scan are therefore independent of the source of the slot numbers.


### `instruction`

 Body instruction embedded at the existing parent, child and slot labels. 

### `resize_instruction`

 The body can be emitted at the five-bit literal width of the actual vertex
image even when the slot exponent is greater than five. 

### `native_ready`

 Execute the parent header and argument scan with initialized ordinal
registers. Every supplied public word remains available to other vertex code. 

### `reject_ready`

 A short argument tape cannot return through the register-based body. 

### `native_stage`

 The complete hosted stage starts with arbitrary ordinal-register contents.
It fills the bank, reads the actual descriptor and consumes the placed child
arguments. The only added events are the bank's private initialization ticks. 

### `reject_stage`

 Short-tape rejection holds already at the first bank instruction. 
