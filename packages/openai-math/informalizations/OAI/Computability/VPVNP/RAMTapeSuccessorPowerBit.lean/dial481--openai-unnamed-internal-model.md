---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorPowerBit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorPowerBit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorPowerBit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Writing a power of two into a fixed-width little-endian word 

### `Port`

 Stacks for the unary exponent, destination word, and saved zero bits. 

### `State`

 Control states for skipping low bits, setting the power-of-two bit, and restoring the lower
zeros. 

### `code`

 Consume the unary exponent, write a one at that bit position, and fill the lower positions
with zeros, rejecting if the word is too short. 

### `bank`

 Initialize the exponent as unary marks and the scratch stack as zeros alongside the
supplied word bits. 

### `routine`

 Install the bit-setting instruction table on the caller's stacks, entering at the exponent
scan. 
