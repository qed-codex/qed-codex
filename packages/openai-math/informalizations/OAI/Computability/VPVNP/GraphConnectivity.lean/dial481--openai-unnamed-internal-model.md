---
{
  "module": "OAI/Computability/VPVNP/GraphConnectivity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GraphConnectivity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GraphConnectivity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Connected support of the regular arc multigraph

In the last paragraph of Section 5.3 of *VP and VNP differ over every field*,
the Poincaré inequality for the real line forces connectivity. The multigraph
is specified by its arc multiplicities. Removing loops and identifying
parallel edges leaves the following simple graph, with the same reachability.


### `arcSupportGraph`

 The underlying simple graph of an arc multiplicity matrix. 

### `arcSupportGraph_adj`

 For symmetric multiplicities an edge is present precisely when its
distinct endpoints are joined by an arc. 

### `arcSupportGraph_reachable_iff`

 Reachability is unchanged when loops are removed and parallel arcs are
identified. 

### `arcSupportGraph_reachable`

 Every two vertices of a symmetric arc multigraph with a real Poincaré
bound are joined by a walk in its underlying simple graph. 

### `arcSupportGraph_connected`

 On a nonempty vertex set the real-valued inequality certifies
connectivity in the graph-theoretic sense. 

### `RegularArcGraph.poincare_on_arcs`

 The matrix Poincaré inequality, expressed with the paper's averages over
ordered vertex pairs and directed arcs. Parallel edges occur once per port. 

### `exists_connected_regularArcGraph`

 Lift a symmetric loop-free regular arc matrix to a connected undirected
multigraph without changing any transition multiplicity. 
