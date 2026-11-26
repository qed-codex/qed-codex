---
{
  "module": "OAI/Computability/VPVNP/ComplexityLib/Family.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ComplexityLib/Family.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ComplexityLib/Family.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite variable families in the two models

Numbering the variables preserves the polynomial, its degree, and its minimum
project circuit size. For a VNP verifier, number the visible variables first,
then the witness variables, as required by complexitylib's Boolean sum.


### `numberedFamily`

 The upstream polynomial family obtained by numbering the variables at each length. 

### `numbered_mem_VP_iff`

 A family has polynomial-size circuits in one model precisely when its
numbered family has polynomial-size circuits in the other. 

### `numbered_mem_VNP`

 A project VNP verifier gives an upstream VNP verifier with the same Boolean
witness length and the same formal polynomial at each index. 
