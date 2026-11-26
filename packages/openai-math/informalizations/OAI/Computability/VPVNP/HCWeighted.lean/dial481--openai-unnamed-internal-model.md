---
{
  "module": "OAI/Computability/VPVNP/HCWeighted.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HCWeighted.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HCWeighted.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact-one generating polynomials as Hamiltonian-cycle projections

Each satisfying assignment yields one allowed spanning cycle. Its entry arcs
record the selected variable weights. Summing the weights of these cycles
therefore gives the weighted exact-one polynomial over any commutative ring.


### `arcWeight`

 The entering arc records a true bit by its variable or scalar weight. All
other allowed arcs carry one. 

### `Admissible`

 Spanning cycles in the exact-one gadget that follow an allowed directed edge at every
vertex. 

### `toCycle`

 Turn an exact satisfying assignment into its directed spanning cycle through the variable
tracks and clause vertices. 

### `assignmentsEquiv`

 The weight-preserving encoding of exact-one assignments as allowed Hamiltonian tours. 

### `weighted_projection`

 Projection from a Hamiltonian polynomial of explicit order for any positive-width
exact-one formula, allowing repeated literals and empty clauses. 
