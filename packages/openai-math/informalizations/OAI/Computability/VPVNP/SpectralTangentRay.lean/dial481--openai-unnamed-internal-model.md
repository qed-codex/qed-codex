---
{
  "module": "OAI/Computability/VPVNP/SpectralTangentRay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralTangentRay.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralTangentRay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rays in the rescaled tangent space

The rescaling of three geodesic segments in Lemma 4.1 produces rays. For
each pair with common origin their equal-parameter distance is exactly
linear, with slope the infimum of the original positive-parameter ratios.


### `RadialSegment`

 A constant-speed geodesic on the unit interval, represented by a total
function on the real line for the coordinate sector constructions. 

### `RadialSegment.path`

 Parametrized path that runs at constant speed from the basepoint at zero to its endpoint
  at one. 

### `radialSlope`

 The speed of separation in the tangent cone. 

### `tangentRay`

 Rescaling a segment produces a ray defined at every nonnegative time. 

### `tangentRay_speed`

 The ray inherits the speed of its original segment. 

### `tangentRay_cross`

 The distance between two rays at time `r` is exactly `r` times their
common infinitesimal separation. 
