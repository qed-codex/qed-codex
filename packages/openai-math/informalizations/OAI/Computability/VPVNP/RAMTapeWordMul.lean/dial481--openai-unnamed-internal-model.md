---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordMul.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordMul.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordMul.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed bit-stack control for word multiplication

The multiplier is read from least to most significant bit. Each round
simultaneously shifts the multiplicand and conditionally adds it into the
accumulator, discarding overflow at the width of the input stacks. Two
scratch stacks restore both words to least-significant-bit-first order.
The number of control states and stacks is independent of the word width.


### `Reg`

 Bit stacks for the multiplier, multiplicand, running accumulator and temporary shifted and
summed words. 

### `State`

 Control states for initialization and for the shift-and-add rounds that consume successive
multiplier bits. 

### `code`

 The only data in finite control are the handful of bits between pop and
push instructions. Inputs are copied into these stacks by the caller. 

### `store`

 Install the five bit lists as the current multiplication operands, accumulator and
temporary words. 

### `loop_run`

 Consume the multiplier and compute a multiply-add, with wraparound. 

### `multiply_run`

 Start with two words and empty work stacks. The accumulator is initialized
to a zero word of the multiplicand's width. All four other stacks are empty at
exit. For equal widths `w` the time is `8*w² + 9*w + 4`. 

### `multiply_word_run`

 The multiplication opcode, at every word width, is implemented by this
single finite control. Each input and output uses the RAM word bit encoding. 
