---
{
  "module": "OAI/Computability/VPVNP/FlatRectangle.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FlatRectangle.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FlatRectangle.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Interpolating the sides of a flat rectangle

A four-point configuration with the distances of a Euclidean rectangle
extends across each pair of parallel sides with exactly the Euclidean
cross distances. The proof uses the midpoint inequality on a saturated
diagonal and the first variation of squared distance to exchange the two
sides of a flat triangle. This gives the rectangle-filling step in
Sections 4.2 and 5.4 directly from the squared CAT(0) segment inequality.


### `rectangle_interpolate`

 Euclidean cross distances on the two interpolated parallel sides of a
rectangle, including rectangles of zero width or length. 
