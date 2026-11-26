---
{
  "module": "OAI/Computability/VPVNP/PortDenominator.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PortDenominator.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PortDenominator.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integral multiplicities of a lazy Cesàro walk

In Section 5.3 of *VP and VNP differ over every field*, the normalized
adjacency matrix of a symmetric `b`-regular multigraph is made lazy and its
first `t` positive powers are averaged. To realize this matrix on `Q` ports
per vertex, multiply each entry by `Q`. The resulting natural counts are
obtained from walks in the original multigraph with `b` extra loops at each
vertex. The proof works over both the rationals and the reals.


### `exists_cesaroPortCounts`

 The Section 5.3 lazy transition matrix and its Cesàro average give
symmetric natural port multiplicities with row sums `Q` whenever the common
denominator `t * (2*b)^t` divides `Q`. The rational and real specializations
use the same integer witness. 
