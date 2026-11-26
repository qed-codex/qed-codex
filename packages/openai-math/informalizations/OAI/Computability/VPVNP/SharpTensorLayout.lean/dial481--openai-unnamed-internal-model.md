---
{
  "module": "OAI/Computability/VPVNP/SharpTensorLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SharpTensorLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SharpTensorLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cube-witness comparison at the original circuit exponent

For a tensor form admitting an encoding linear in its local dimension up to a
polynomial in the tensor power, the central wire in (4.5) costs the original
circuit exponent `C` times the centroid distance.


### `not_small_universal_of_sharp_tensor_layout`

 A literal projection with length `M * (h + 1)^D * (2^b)^h` supplies the exact
layout comparison from the paper, without multiplying the exponent `C`. 
