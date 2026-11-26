---
{
  "module": "OAI/Computability/VPVNP/HardnessAlternatives.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessAlternatives.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessAlternatives.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choosing among weighted CNFs

Each alternative has a selector bit and a private block of data bits. The selector
bits are one-hot. The chosen formula is enforced, while every unchosen block is
filled with zeros. Consequently an accepted local assignment extends uniquely
to an accepted global assignment, even for zero-variable formulas.


### `Slot`

 Boolean variables of the disjoint-alternatives formula. Each alternative gets a selector
and its own block of local variables. 

### `width`

 The total number of selectors and local variables in the alternatives formula. 

### `index`

 A bijection from the tagged selector and local-variable slots onto the finite set of CNF
variable indices. 

### `formula`

 Select exactly one formula, enforcing its clauses and zeroing all inactive variables. 

### `weight`

 Label each selector and each data slot. The labels can be weights or any
parameters from which the weights will be built. 

### `weighted_formula`

 The polynomial of the selector formula is the sum of the individual polynomials,
each multiplied by the weight of its selected branch. 

### `literalCount_formula_le`

 A uniform bound in the number of alternatives, the largest block width,
and the largest literal count. Empty clauses are detected before guarding. 
