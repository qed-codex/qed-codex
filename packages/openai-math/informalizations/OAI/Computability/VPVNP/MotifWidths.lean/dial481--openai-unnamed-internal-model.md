---
{
  "module": "OAI/Computability/VPVNP/MotifWidths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifWidths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifWidths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selector and payload widths in a fixed motif

Theorem 6.1 of *VP and VNP differ over every field* first fixes a denominator
multiple and then a power of the base identity. This order matters because the
number of direct-sum copies can depend on the chosen multiple. Every subsequent
input uses repetitions of that single base block. Its selector overhead can
be made arbitrarily small, and its padding costs a constant in squared width.


### `selectorBits`

 The least number of bits for a base selector, indexing a direct-sum
copy and the `h` independent choices of supply grid point. 

### `exists_selector_block`

 Arbitrarily small selector fraction, with an arbitrary dependence of the
number `K t` of direct-sum copies on the denominator multiple `t`. 

### `exists_selector_tolerance`

 A single strictly positive tolerance leaves room for the selector bits
inside the prescribed squared energy coefficient. 

### `widthNorm_sum_le`

 Triangle inequality for the aggregate payload over any finite selector list. 

### `copies`

 Number of repetitions of a block of width scale `L`. 

### `copies_dominate`

 The surplus demand bits can be fixed at both endpoints. 

### `padded_energy_le`

 Given any admitted total payload vector, add the selector bits on every
supply edge. The linear term from rounding the number of blocks is absorbed
by the strict margin in the quadratic coefficient. 

### `exists_padded_grid`

 Choosing the upper demand grid point makes the repeated integer base
widths large enough at every edge, including when all demand widths vanish. 

### `base_payload_bound`

 Adding the `h` supply grid points for a base selector costs at most `hBR`. 

### `outer_indices_linear`

 The number of base copies and every coordinate of every admitted outer
payload are bounded linearly in the largest input width. 
