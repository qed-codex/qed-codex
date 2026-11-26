---
{
  "module": "OAI/Computability/VPVNP/MotifSupplyEnergy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifSupplyEnergy.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifSupplyEnergy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Positive spectral energy of a connected supply motif

In Theorem 6.1 the binary supply network restricts to the two-entry diagonal:
at each party the local map selects the same output color on every incident
wire. The selected coefficient is one precisely when the coloring is
constant along every edge. Connectivity therefore forces the sum of the
supply wire distances to be at least one at each spectral point.


### `color_eq_of_connected`

 Edgewise agreement of colors propagates along paths of the supply graph. 

### `connectedNetwork_restricts_diagonal`

 A connected network of equality wires realizes the diagonal by selecting
the output color on every incident half-wire. 

### `one_le_sum_connected_wireDistance`

 The binary supply network has value at least two, giving a logarithmic
lower bound on the sum of the edge distances. 

### `exists_pos_connected_wireDistance`

 Some supply edge has positive spectral distance. 

### `connected_distanceEnergy_pos`

 The weighted supply energy in Theorem 6.1 is positive for every
spectral point when all edge masses are positive. 
