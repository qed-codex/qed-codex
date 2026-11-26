---
{
  "module": "OAI/Computability/VPVNP/ExteriorLevels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExteriorLevels.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExteriorLevels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite exterior levels for wire relocation

The two summands in Appendix A.2 factor through the neighboring exterior
levels. The restricted creation and contraction matrices retain the integral
anticommutation identity in their ordered subset bases.


### `Level`

 The coordinate indices for the degree-`b` exterior power on `Q` generators. 

### `indexSet`

 Realize bounded generator indices as natural-number indices. 

### `entry`

 Rectangular matrix of an exterior operator between two finite levels. 

### `matrix_car`

 Equation (A.1) in the bounded subset basis. The two intermediate sums
have `Q.choose (b+1)` and `Q.choose (b-1)` terms, respectively. 

### `int_matrix_car`

 A single pair of integer matrix families gives (A.1) after base change
to any commutative ring, including fields of characteristic two. 

### `matrix_car_apply`

 Contracting the old marked index against the two orders in (A.1) gives
the original coefficient at the new index times the identity wire. 
