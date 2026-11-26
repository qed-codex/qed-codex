---
{
  "module": "OAI/Computability/VPVNP/PairNativeGeometryFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeGeometryFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeGeometryFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native word width and rounded bucket for a live pair

The width is the fourth power of the address width plus ten. The rounded
bucket exponent is computed by integer ceiling division after the power
and ceiling-logarithm instructions have completed.


### `widthCode`

 Compute the machine word width by adding ten to the address width in register 5 and raising
the sum to the fourth power in register 6. 

### `bucketCode`

 Round the logarithm in register 3 up by ceiling division by positive `b`, then shift one
left by that quotient to obtain the bucket size in register 7. 
