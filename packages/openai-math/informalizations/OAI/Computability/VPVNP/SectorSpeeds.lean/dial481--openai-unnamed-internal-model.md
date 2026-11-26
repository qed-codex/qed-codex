---
{
  "module": "OAI/Computability/VPVNP/SectorSpeeds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SectorSpeeds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SectorSpeeds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Directional speeds on an affine sector

In Section 4.1 of *VP and VNP differ over every field*, the sector map takes
affine segments to constant-speed geodesics. The distance per unit step in
a direction is independent of the step length. Fraction transport toward a
point beyond a second interior base point shows that the speed is independent
of the base point as well.


### `exists_positive_step_mem`

 A sufficiently short positive step from an interior point stays in the domain. 

### `exists_sector_speed`

 A single directional speed applies to all positive steps from all interior
base points, including steps that end on the boundary of the domain. 
