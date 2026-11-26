---
{
  "module": "OAI/Computability/VPVNP/FractionalGeodesic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FractionalGeodesic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FractionalGeodesic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Geodesics from unique fractional points

In Corollary 2.5 of *VP and VNP differ over every field*, fractional points are
characterized by their distances to the two endpoints. Uniqueness for every pair of
endpoints makes these fractional points a constant-speed geodesic.


### `exists_constantSpeedSegment`

 Unique fractional points determine a constant-speed segment between each pair. 

### `existsUnique_constantSpeedSegment`

 Any two constant-speed segments with these endpoints agree at every parameter. 

### `continuous_of_constantSpeed`

 A constant-speed segment is Lipschitz, hence continuous. 
