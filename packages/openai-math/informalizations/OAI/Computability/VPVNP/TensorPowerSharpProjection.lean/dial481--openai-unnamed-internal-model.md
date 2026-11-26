---
{
  "module": "OAI/Computability/VPVNP/TensorPowerSharpProjection.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorPowerSharpProjection.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorPowerSharpProjection.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Tensor powers as projections with a near-linear input length

The exact-one table has one row per party, position and digit comparison.
Its row count is linear in the power index. The columns are the one-hot
flags, whose count grows at the rate of the local dimension to that power.


### `sharpCoefficient`

 Uniform constant in the source-length estimate for the exact-one table. 

### `projection_at_sharp_length`

 At every length above this explicit bound, the universal polynomial projects
to the tensor power. The bound depends only on the bit width and party count. 

### `sharp_projection`

 The exponential growth rate of the projection length is at most the local
dimension, with polynomial overhead in the power index. 
