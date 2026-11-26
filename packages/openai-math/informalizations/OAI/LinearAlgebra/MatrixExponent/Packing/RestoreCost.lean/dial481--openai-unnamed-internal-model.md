---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Packing/RestoreCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/RestoreCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/RestoreCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Routing exceptional units through their two contact trees

Descend to the tip assigned to the destination, cross its unique link,
then climb to the receiving terminal. The group label stays fixed.


### `side`

 The endpoint owning an intermediate station. 

### `route_degree`

 Each station on an arm is visited at most once. Count both wire
incidences at a visit, even when both ends have the same owner. 


# Routing tethers between frozen members and the core

A short splitting tree may carry the whole frozen charge. The long
addressing trees carry only the load of a single outlet or core endpoint.


### `Plan`

 Each tether bit has its own index, even when many bits take one route. 

 # Squared arity on the short splitting trees 

### `hot_at`

 All paths visiting a vertex of a splitting tree come from one
frozen tensor. Each contributes at most two incidences there. 

### `hot_squares`

 Only the short splitting-tree depth multiplies the frozen square
budget. It is independent of the full host degree. 

### `cold_max`

 A single outlet serves a single core destination. Thus both sides
of any cold route satisfy the same core load bound. 


# Indexing frozen members and tether outlets

A positive load floor and a bound on the total load at a site give a
bound on the required slots. One outlet per distinct core destination
suffices. Thus a group of parallel bits is never split.


### `number`

 Number the occupants of each location without conflicts. 

### `outlets`

 Bits of a frozen member have the same outlet exactly when they
have the same core destination. 

 # Restoring individual frozen members on the common host 

### `parallelBits`

 Parallel tether bits from one frozen tensor to a core occurrence. 


# Restoring the frozen border and the degree-four support

Keep the core wires and realize the tethers by one exact packet.
The orientation of each old incidence is retained. Exterior bits
are never identified, even when frozen members share a parking site.


 # Total load and squared load after restoring bounded degree 

### `charge`

 Charge every parked member and all incident supply bits, also when
coarsening makes some of those bits internal to a site. 

### `squares`

 Full-degree routing contributes only a light-arity term. The large
frozen square budget is multiplied only by the short outlet depth. 

### `floor`

 Unoccupied sites have zero charge. Every other site carries at
least one whole original bundle or one surviving frozen member. 

 # Original tether multiplicities are lower bounds after cutting 
