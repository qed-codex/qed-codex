---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticMagnitude.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticMagnitude.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticMagnitude.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reducing an arbitrary-width count to one residue limb

A positive working-width divisor and a little-endian count may have different
lengths. The bit division routine computes the remainder at the divisor width.
Its unused quotient is erased before the residue returns.


### `machine`

 Divide a little-endian count by the advised modulus and discard the quotient, leaving the
remainder. 

### `frame`

 Division stack state holding the count, divisor, and remainder stream with the other work
stacks empty. 

### `cost`

 Number of steps to reduce an `n`-bit count modulo a positive `w`-bit divisor and erase the
quotient. 
