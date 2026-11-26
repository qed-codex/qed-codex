---
{
  "module": "OAI/Computability/VPVNP/CATZeroEquality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CATZeroEquality.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CATZeroEquality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Equality in CAT(0) comparison along a segment

The difference between the Euclidean comparison quadratic and the squared
distance to a fixed test point is a nonnegative concave function of the
segment parameter. Vanishing at an interior parameter forces it to vanish
along the entire segment.


### `catPoint_bound_eq_of_interior`

 If squared CAT(0) comparison with a fixed vertex is an equality at an
interior point of the opposite side, it is an equality at every point of that side. 
