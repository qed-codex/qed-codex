---
{
  "module": "OAI/Computability/VPVNP/RAMTapeDivision.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeDivision.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeDivision.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Restoring division in quadratic bit-stack time

This fixed finite control computes both outputs of the word RAM's unsigned
division and remainder instructions. It preserves the divisor and leaves all
temporary stacks empty. The separate zero-divisor path also works at zero
width. Every input has exactly one accepting path with the stated clock.


### `digitRun`

 One complete quotient-digit loop, including the shift, subtraction and
the restoration of the divisor and selected remainder. 

### `ticks`

 Exact running time of the restoring word macro. 

### `divideWordRun`

 Both RAM opcode results in little-endian bit-stack format. The same fixed
program table applies to every word width. 

### `dividePaths`

 An extra instruction beyond the transition bound visits the accepting
halt. The deterministic division routine has exactly one accepting path. 
