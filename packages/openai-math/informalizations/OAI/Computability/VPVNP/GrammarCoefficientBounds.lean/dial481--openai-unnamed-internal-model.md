---
{
  "module": "OAI/Computability/VPVNP/GrammarCoefficientBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrammarCoefficientBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrammarCoefficientBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounds for the coefficients of the label equations

The coefficient of a label monomial in the integer query `Bₓ` counts ordered
parses with that exact histogram whose terminals match the input word. The number
of such trees bounds every coefficient uniformly over subsequent choices of scalars.


### `coeff_labelQuery_eq_card`

 The integer label coefficient counts matching trees, once per ordered parse. 

### `coeff_labelQuery_bounds`

 Every queried coefficient is nonnegative and at most the total count of ordered
parses. In particular its bit length is bounded independently of field constants. 
