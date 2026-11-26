---
{
  "module": "OAI/Computability/VPVNP/SpectralCurvature.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralCurvature.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralCurvature.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The squared midpoint inequality for wire metric spaces

Section 4.1 rescales the three segments from a midpoint to the three
marked vertices. In each tangent sector the distance from the first ray at
time `t` to the second ray at time one obeys a Euclidean quadratic law.
The triangle inequality between the opposite rays at arbitrary `t` forces
the comparison at the original midpoint. Saturation forces each original
sector to have its Euclidean distances at every parameter.


### `squared_midpoint_of_transport`

 Lemma 4.1's inequality when the segment transport inequalities (2.2)
are given in the space and its rescaling at the marked midpoint. 

### `IsEuclideanSector`

 Euclidean (possibly degenerate) distances throughout the filled sector
of two segments. The mixed coefficient is determined by the three boundary
lengths, as in the Euclidean cosine rule. 

### `euclideanSectors_of_midpoint_eq`

 At equality in Lemma 4.1, both sectors based at the midpoint, joining
the third vertex to each endpoint, are Euclidean throughout. 

### `hasCATZeroSegments_of_wire_transport`

 Equation (4.2) from spectral configurations, using the six-point wire
transport law of Lemma 2.2. No completeness assumption on the target is needed. 

### `euclideanSectors_of_wire_transport`

 The equality assertion of Lemma 4.1 under the same six-point wire
transport law. The formula applies to every marked point in both sectors. 
