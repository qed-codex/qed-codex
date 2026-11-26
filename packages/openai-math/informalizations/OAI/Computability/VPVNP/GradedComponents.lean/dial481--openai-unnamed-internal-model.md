---
{
  "module": "OAI/Computability/VPVNP/GradedComponents.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GradedComponents.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GradedComponents.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Homogeneous components of the circuit grammar

In the grammar of Section 8.1 the degree-one states are arbitrary linear forms, and a
multiplication gate of degree `d` convolves the component lists of its input gates.


### `homogeneousComponent_mul`

 The degree-`d` component of a product uses precisely the degree splits `i + j = d`. 

### `homogeneousComponent_one_eq_sum`

 The linear component is the linear combination of the individual variables with
coefficients given by their degree-one monomials. 
