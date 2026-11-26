---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Diagram/Replacement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagram/Replacement.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagram/Replacement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Comparing size and volume conventions 

### `sum_arity`

 Each internal edge contributes two argument positions and each
exterior bit contributes one. 

### `volume_trivalent`

 Wire-inclusive volume is at most three times vertices plus exterior bits. 


# A bipartite presentation

Insert one binary equality table on each internal and external wire.
Each of the original argument positions now has its own edge. All
these edges join an original vertex and a junction. Exterior positions
have distinct equality leaves and even an old loop is subdivided.


 # The degree of an original station in the subdivided network 


# Networks with unoriented local functions

Use one owner per port rather than specifying a local port order. Evaluating
a station only needs the values on its own ports. Choosing an enumeration
converts such a description into a diagram with the same edges and weights.


### `weight`

 Allow the two ends of an edge to carry different values until contraction. 

### `weight_ofLocal`

 Local weights are independent of the chosen enumeration of ports. 


# Contracting clusters

Split the old edges into the visible edges and a disjoint family of
edges internal to the clusters. Sum the latter inside each new table.
This identity allows loops, empty clusters and scalar vertices.


### `weight_collapse`

 The local kernel at one cluster uses only its own hidden bits.
It can be read in any port order. 

### `Between`

 Keep only wires that cross the partition. 


# Expanding a network by a simultaneous wire identity

Cut each edge into two half-edges. Insert the two copies of its bit
into the demand ports of the packet. The new sites and the old stations
are disjoint, even when several demands have a common endpoint.



# Contracting a summand of the simultaneous wire identity

The partition may depend on the selector. When each cut end meets its
assigned packet site, the surviving graph has just the crossing supplies.


### `arity_replaced`

 Including all local supplies only increases the bound on a cluster's arity. 
