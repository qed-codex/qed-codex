---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Little-endian bit scans for the word RAM

A word occupies one stack cell per bit. The elementary binary transducers
scan two equal-length stacks from low to high, remembering one carry or
borrow bit in their finite control. The final carry or borrow certifies the
arithmetic even when the result wraps around.


### `value`

 Unsigned value of a little-endian list of bits, with the empty list representing zero. 

### `scan`

 A synchronous transducer. When the inputs are equally long it reads one
bit from each stack per emitted bit and leaves its final control state. 

### `addBit`

 Compute the sum bit and outgoing carry for two operand bits and an incoming carry. 

### `subBit`

 Compute the difference bit and outgoing borrow for two operand bits and an incoming borrow. 

### `addScan`

 Scan paired little-endian bits with a carry and return the sum bits and final carry when
either input ends. 

### `subScan`

 Scan paired little-endian bits with a borrow and return the difference bits and final
borrow when either input ends. 

### `logicScan`

 Parallel Boolean operations use the same scan with a single dummy state. 
