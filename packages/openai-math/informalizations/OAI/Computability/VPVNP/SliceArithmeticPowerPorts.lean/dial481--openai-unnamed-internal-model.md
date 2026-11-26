---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticPowerPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticPowerPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticPowerPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Ports of the binary powering and inversion control 

### `Extra`

 Extra inversion ports for the saved base and exponent, the live bit stream, the zero-test
flag, and temporary stacks. 

### `Port`

 The multiplier's full port bank extended with the ports for binary powering and inversion. 

### `frame`

 Caller-visible scalar advice and operands, together with the exponent
scan's remaining bits and the temporary zero-test flag. 
