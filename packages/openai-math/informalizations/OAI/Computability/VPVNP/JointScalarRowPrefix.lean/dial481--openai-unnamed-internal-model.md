---
{
  "module": "OAI/Computability/VPVNP/JointScalarRowPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarRowPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarRowPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Prepending the equation address to a packed scalar query

The index register and the row field of the scalar query can have different
widths. The length of an immutable unary template selects the low bits to
prepend. A missing high bit is copied as zero. The two scratch stacks allow
the source to be restored and the bits to be emitted in little-endian order.


### `Port`

 Stacks for the source equation address, unary output width, destination and two temporary
bit sequences. 

### `Phase`

 Control states for staging the low address bits, restoring the source and emitting the
resized row prefix. 

### `body`

 Prepend the equation address at the width specified by the unary template, restoring the
source and template on return. 

### `bank`

 Assign the equation address, width template, destination and both temporary sequences to
their respective stacks. 

### `resize`

 Take the requested number of low bits from a little-endian word, filling any missing high
bits with zero. 

### `digits_ofFn`

 Canonical physical little-endian digits of an integer at any width. 

### `resize_digits`

 Resize the low-bit array of a natural number. The source must represent
the number. The result is the canonical low target-width word even on truncation. 

### `runs`

 All input stacks are restored. Only the destination gains bits. 
