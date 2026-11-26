---
{
  "module": "OAI/Computability/VPVNP/RegularArcGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RegularArcGraph.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RegularArcGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loop-free regular multigraphs represented by paired arcs

Theorem 5.1 counts the oriented arcs of a multigraph, with equal
multiplicities in both directions. Each vertex has one arc per port.
Reversal pairs the arcs at opposite ends of each undirected edge.


### `RegularArcGraph`

 A loop-free undirected multigraph with exactly `b` outgoing arcs at each vertex. 

### `RegularArcGraph.reverse`

 Involutive permutation pairing each outgoing port with the oppositely oriented port of
  the same undirected edge. 

### `multiplicity`

 Number of arcs going from `u` to `v`. 

### `multiplicity_pos_iff`

 Positive multiplicity is equivalent to the existence of a port leading to the vertex. 

### `multiplicity_self`

 Loop-freeness gives zero diagonal in the multiplicity matrix. 

### `multiplicity_symmetric`

 Reversal gives a bijection between the arcs of the two orientations. 

### `degree`

 Counting the outgoing ports gives the degree at every vertex. 

### `reverse_ne`

 Reversal exchanges the two different arcs of each edge. 

### `sum_cost`

 Group the sum of any arc cost by its ordered pair of endpoints. 

### `exists_regularArcGraph`

 Realize a symmetric zero-diagonal matrix with constant row sum by a regular graph. 
