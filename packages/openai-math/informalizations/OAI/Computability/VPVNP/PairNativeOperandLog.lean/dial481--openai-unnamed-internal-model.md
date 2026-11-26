---
{
  "module": "OAI/Computability/VPVNP/PairNativeOperandLog.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeOperandLog.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeOperandLog.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Logarithmic operands inside the native pair burst

Repeated floor division by two needs no increment of the operand. For a
ceiling logarithm at `x > 1`, the same loop starts at `x-1` with counter
one. This covers the largest word as well as zero and powers of two.


### `Code`

 The twelve-register instruction flows used to evaluate binary logarithms inside a native
operand computation. 

### `program`

 Compute the floor or ceiling binary logarithm of register 2 in register 3 by repeated
halving. For a ceiling logarithm above one the loop starts from one less than the operand
and counts from one. 

### `run`

 The result occupies register three. Registers four and above, including
the word-width register, keep their original contents. 
