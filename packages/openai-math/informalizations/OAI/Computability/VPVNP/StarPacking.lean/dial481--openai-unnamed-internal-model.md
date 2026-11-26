---
{
  "module": "OAI/Computability/VPVNP/StarPacking.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StarPacking.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StarPacking.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packing tensors into a dyadic star

In the star case of Theorem 2.4, a tensor of local dimensions `2^(h*w j)`
fits into the contraction of a star of local dimensions `2^(r*w j)` after
taking `r / h` copies. Coordinate inclusion pads the entries by zero, and
coordinate selection recovers the original tensor power.


### `exists_star_contraction_of_embeddings`

 Pad a tensor by zero along local basis embeddings and realize the padded
array by a single covector at the center. Both local restrictions are exact. 

### `exists_dyadic_star_packing`

 At each party, the floor number of copies has enough local coordinates
in the dyadic star. This includes zero star multiplicity and zero widths. 

### `exists_starPowerFin_packing`

 Contract the power of the width-profile star itself to a zero padding
of the packed tensor power, using a joint covector on all center indices. 
