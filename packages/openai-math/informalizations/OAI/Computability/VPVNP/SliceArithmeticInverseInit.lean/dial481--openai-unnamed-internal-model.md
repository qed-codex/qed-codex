---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticInverseInit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticInverseInit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticInverseInit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initializing inversion on packed field-element stacks

The controller copies the exponent advice to a consumable stack, scans the
input for zero and installs the appropriate packed constant in the multiplier's
accumulator. Starting at zero for zero input handles the field of order two,
whose Fermat exponent is zero.


### `initializeInput`

 Fixed stack instructions for installing the exponent scan and initial accumulator. 

### `initialize_runs`

 The saved exponent and base are preserved, the working bits are installed,
and the flag and temporary stacks are empty upon return. 
