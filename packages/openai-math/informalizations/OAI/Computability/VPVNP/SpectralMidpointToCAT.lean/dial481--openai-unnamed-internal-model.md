---
{
  "module": "OAI/Computability/VPVNP/SpectralMidpointToCAT.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralMidpointToCAT.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralMidpointToCAT.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From midpoint comparison to CAT(0) comparison

Section 4.1 passes from (4.1) to the full geodesic inequality (4.2). Along a
constant-speed segment, subtracting the comparison quadratic from the squared
distance gives a continuous midpoint-convex function that vanishes at both
ends. At a maximum, express its parameter as the midpoint of an interval with
one end at a boundary point. The maximum is then at most half itself.


### `nonpos_of_midpoint_convex`

 A continuous midpoint-convex function vanishing at both ends of the unit interval is
nonpositive on the whole interval. 

### `hasCATZeroSegments_of_midpoint`

 The squared midpoint comparison (4.1) implies the full CAT(0) inequality (4.2). 
