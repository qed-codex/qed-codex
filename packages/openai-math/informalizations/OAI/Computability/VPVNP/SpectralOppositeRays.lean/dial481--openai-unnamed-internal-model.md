---
{
  "module": "OAI/Computability/VPVNP/SpectralOppositeRays.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralOppositeRays.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralOppositeRays.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Opposite rays in the spectral tangent space

At a midpoint the rays toward the two original endpoints separate at twice
the speed of either ray. Applying the triangle inequality to points arbitrarily
far along those rays gives the quadratic comparison of Lemma 4.1.


### `opposite_segment_distance`

 Equal-parameter points on the two halves of a segment have exactly the
sum of their distances from the midpoint. 

### `radialSlope_opposite`

 Opposite directions at a midpoint attain the full separation speed. 

### `tangentRay_opposite`

 Opposite rays in the tangent space have linear separation at every
nonnegative parameter, including parameters beyond the original endpoints. 

### `opposite_ray_quadratic_bound`

 If the two distances to the opposite rays obey the Euclidean quadratic
formula, the triangle inequality at arbitrarily large parameters bounds the
sum of the two squared distances at unit parameter. 
