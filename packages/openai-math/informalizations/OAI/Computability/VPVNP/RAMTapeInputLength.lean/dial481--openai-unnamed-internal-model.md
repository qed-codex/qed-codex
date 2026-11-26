---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInputLength.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputLength.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputLength.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the complete input length before parsing the site fields

The size stack acquires one unary mark per input bit, including program-prefix
bits and padding. The control saves each popped bit on a temporary stack and
then transfers the bits back, restoring the original input in head-first order.


### `LengthPhase`

 States of the length pass that saves every input bit, counts it with a unary mark, and
restores the input. 

### `lengthCode`

 A fixed control, independent of the length and contents of the physical input. 

### `length_runs`

 Exactly five stack instructions per input bit and two end tests. With an
empty size stack the output is the unary input length. Every other stack,
including the complete input, agrees with its value on entry. 
