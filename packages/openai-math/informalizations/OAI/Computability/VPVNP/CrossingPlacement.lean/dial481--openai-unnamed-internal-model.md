---
{
  "module": "OAI/Computability/VPVNP/CrossingPlacement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CrossingPlacement.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CrossingPlacement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Placing the two crossing wires at tensor parties

The four roles in Lemma 3.2 are the positive and negative endpoints of the two
wires. An arbitrary map from roles to parties may put several endpoints at one
party. Its local basis retains a coordinate for each role at that party.


### `Terminal`

 The two copies of `Bool` label the two wires. On either wire, `false` is
the positive endpoint and `true` is the negative endpoint. 

### `terminalBasis`

 Basis label carried by each terminal. 

### `plusArray`

 The first ordinary summand uses the cut pairing equal endpoint signs. 

### `minusArray`

 The second ordinary summand pairs opposite endpoint signs. 

### `plusArray_add_minusArray`

 The chosen integral crossing factors sum to the product of the two
Kronecker deltas in any coefficient ring. 

### `terminalWires`

 Product of the two identity wires at the designated parties. 

### `placed_crossing_restricts`

 The direct sum of the two placed ordinary summands locally restricts to
the two-wire tensor. This covers arbitrary coincidences among all terminals. 

### `cutSide`

 Side of the two-center cut. The second cut reverses the ends of the Y wire. 

### `crossingNetwork`

 The four terminal wires to their respective centers and the wire carrying
the factorization index between the two centers. 

### `crossingNetworks_restricts`

 Realize the two shifted factors at independently placed pairs of centers.
A local restriction of the direct sum of the two wire networks gives the two
original identity wires at the four terminals. 
