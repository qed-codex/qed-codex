---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite stack controls for binary word scans

The first pass pops matching bits of the operands, applies the one-bit
transition, and pushes each result onto a temporary stack. The second pass
reverses that stack onto the output. The same fixed table works at every word
width. Its final control remembers the carry, borrow, or other Boolean flag.


### `ScanPort`

 The two operand stacks, reversed temporary result and final output stack for a binary word
scan. 

### `ScanState`

 Control for reading paired operand bits, carrying the Boolean flag, emitting a temporary
result and reversing it onto the output. 

### `scanCode`

 Run the one-bit operation on corresponding bits and return the result in word order with
the final flag in control. 

### `scanStacks`

 Install the supplied bit lists on the left, right, temporary and output ports of the scan. 

### `scanRuns`

 Both inputs are consumed. The output stack receives the little-endian
result. The scratch stack is empty and the final flag is retained. 
