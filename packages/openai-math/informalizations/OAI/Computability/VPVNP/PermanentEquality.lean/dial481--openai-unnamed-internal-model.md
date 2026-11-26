---
{
  "module": "OAI/Computability/VPVNP/PermanentEquality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentEquality.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentEquality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# An equality gadget for the permanent

The three internal rows have column weights `(-b,-b,b)`, `(-1,-1,1)`,
and `(1,1,1)`. The first two rows can also exit with weights `A` and `B`.
Taking the coefficient that fills every internal column exactly once
cancels the choices that use only one incoming port.


### `equalityRows`

 Product of the three internal row forms, including the two possible exits. 

### `equalityMatrix`

 Weights of the internal directed edges, in port order. 

### `equalityRows_eq_prod`

 Each row chooses an internal column or exits the gadget. 

### `coeff_equalityRows`

 When neither port enters, the internal cycle covers have total weight
one. When both enter, the two exits contribute `A * B`. 

### `map_neg_half_normalized`

 In a field of characteristic different from two, the required weight
`b = −1/2` remains normalized after applying any coefficient homomorphism. 
