---
{
  "module": "OAI/Computability/VPVNP/MetricMidpoints.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MetricMidpoints.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MetricMidpoints.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # From exact midpoints to fractional points

In the geodesic-completion argument of Corollary 2.5, bisect a segment
repeatedly, keeping the half that contains the prescribed distance from its
left endpoint. The left endpoints are Cauchy and their limit has both
prescribed endpoint distances.


### `exists_fractionalPoint_of_midpoints`

 In a complete metric space with exact midpoints, every segment admits
a point at each fraction of its length. 
