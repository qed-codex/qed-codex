---
{
  "module": "OAI/Computability/VPVNP/HardnessWitnessMonomial.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessWitnessMonomial.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessWitnessMonomial.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Specializing the selected monomials at a Boolean witness

A selected scalar may be labelled by one output variable or one witness variable.
After specialization, a selected witness label contributes zero if its bit is false
and one if it is true. The output-variable labels survive as formal variables.


### `monomial`

 A scalar, optionally multiplied by one labelled variable. 

### `variableWeight`

 The formal variable retained by a compatible label, or the constant one. 

### `witnessValue_prod_monomial`

 A false selected witness variable annihilates the product. Otherwise the
product factors into the selected scalars and the selected output variables. 
