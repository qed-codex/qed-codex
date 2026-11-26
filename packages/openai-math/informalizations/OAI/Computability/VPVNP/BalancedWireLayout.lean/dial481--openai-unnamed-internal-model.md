---
{
  "module": "OAI/Computability/VPVNP/BalancedWireLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BalancedWireLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BalancedWireLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Spectral cost of the balanced circuit cuts

Place the coefficient tensor of an arithmetic circuit at its terminal parties. Each
balanced cut can choose its own two centers. Local contraction of the explicit
factors at those centers realizes the corresponding term, giving the product of wire
values used in the upper bound (4.5).


### `cutSide`

 Terminals in `S` use the first center, and the rest use the second. 

### `CutFactors.placed`

 Place each party `i` at `place i` and give each joint assignment the cut matrix entry
indexed by its restrictions to `S` and its complement. 

### `CutFactors.wire_restricts`

 The term on this cut is a local restriction of the terminal and bridge wires. 

### `Circuit.spectralValue_le_balanced_wires`

 Spectral value of the full coefficient tensor, bounded by the wire networks of
the balanced terms only, each with independently chosen centers. 

### `Circuit.spectralValue_le_balanced_cost`

 Express the finite spectral estimate using the power law for each wire. Here
`r` is any numerical upper bound on the bridge dimension, and `q` is the terminal
dimension. The outer wire lengths add in the exponent of `q`. 
