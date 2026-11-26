---
{
  "module": "OAI/Computability/VPVNP/LinearNormalization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LinearNormalization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LinearNormalization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Noether normalization by linear combinations of specified generators

Over an infinite field, a dependent tuple admits a linear shear after
which one generator can be removed while preserving integrality. Repeating
this reduction gives an independent tuple in the linear span of the
original one. In a polynomial algebra the length of the tuple is its
number of variables.


### `exists_of_integral_adjoin`

 Linear normalization for a tuple whose generated subalgebra has an integral
extension to the whole ambient algebra. 

### `exists_linear_normalization`

 An explicitly generated polynomial algebra in `m` variables has an integral
normalization by exactly `m` linear combinations of the given generators. 
