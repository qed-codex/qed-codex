---
{
  "module": "OAI/Computability/VPVNP/PlacedTensor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PlacedTensor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PlacedTensor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Moving local tensor factors to a common party set

Under the placement of roles at parties used in Lemma 2.3 of *VP and VNP differ
over every field*, independent linear maps on the original roles still act
locally. At a party that carries several roles their matrix entries multiply.
Regrouping tensor products, the unit tensor and zero arrays also commute with
placement.


### `placeTensor`

 Place the tensor's original factors on the specified parties. 

### `placedAssignmentEquiv`

 A global assignment of the placed indices is the same as an assignment of
the original indices, including when several roles share a party. 

### `Restricts.placeTensor`

 Local restrictions on the original roles act on their placed factors by
taking the product of the matrix entries assigned to each party. 

### `placeTensor_tensorProduct`

 Placement respects parallel tensor products up to local basis bijections. 

### `placeTensor_unit`

 Placing a unit tensor gives a unit tensor, up to local basis bijections. 

### `placeTensor_coeff_eq_zero_iff`

 The placed array vanishes exactly when its original array vanishes. 

### `placeTensor_wire`

 Placing the endpoint factors of a wire gives the wire on their image parties,
including the case where the two endpoints coincide. 

### `value_placed_tensorProduct`

 The spectral value of a placed tensor product is multiplicative. 

### `value_placed_tensorPowerFin`

 Placing all factors of a tensor power gives the corresponding power of
the placed tensor's spectral value. 
