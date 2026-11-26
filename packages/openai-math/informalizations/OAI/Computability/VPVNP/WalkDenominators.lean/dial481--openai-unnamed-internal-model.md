---
{
  "module": "OAI/Computability/VPVNP/WalkDenominators.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WalkDenominators.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WalkDenominators.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choosing the port count for the averaged lazy walk

In Section 5.3 of *VP and VNP differ over every field*, the mean of the first
`t` positive powers of a lazy walk on a `b`-regular graph has common
denominator `t * (2 * b) ^ t`. The port set has size `Q = D ^ (4 * t)`.
Here `t`, `D` and `b` are powers of two. A sufficiently large choice of `D`
makes the port count divisible by this denominator for *every* rounded
degree satisfying the support bound `2 * b ≤ 16 * C * D`.


### `walk_denominator_dvd_port_count`

 Sufficient size conditions for the divisibility in the first paragraph
of the port construction. 

### `exists_walk_port_order`

 The sparse recursion may request arbitrarily large starting order `D`.
Choose it before the rounded degree `b` is known. 

### `exists_walk_smoothing_scale`

 When the sparse Poincaré bound grows like `α ^ j` with `α < m = 2^r`,
choose `j` so that the even smoothing length `t = m^j / 4` dominates the
rounded port bound `β = max 1 (2*C' * α^j)` by the factor `1776` used in
the cloud iteration. 
