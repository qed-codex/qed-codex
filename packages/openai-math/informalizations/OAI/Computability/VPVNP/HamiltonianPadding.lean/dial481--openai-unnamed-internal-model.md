---
{
  "module": "OAI/Computability/VPVNP/HamiltonianPadding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HamiltonianPadding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HamiltonianPadding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Subdividing a forced arc of a directed Hamiltonian cycle

Section 15.1 of *VP and VNP differ over every field* pads the directed
Hamiltonian-cycle polynomial by one vertex. Number the new vertex by zero
and embed the old vertices by `Fin.succ`.


### `subdivideCycle`

 Insert vertex zero immediately after the old vertex `a` in its cycle. 

### `map_sameCycle`

 A map that sends each step in a finite permutation orbit to two vertices
of the same target orbit sends the whole orbit into that target orbit. 

### `cyclePaddingProjection`

 The forced arc from the old root to the new vertex has weight one.
The new outgoing arcs carry the old root's variables except for the
arc back to the root, which is forbidden. 

### `hamiltonianCyclePolynomial_pad`

 Contracting the forced arc projects the polynomial of order `m + 1`
to the polynomial of order `m` over any coefficient semiring. 

### `Circuit.contract_hamiltonian`

 Contraction gives an exact circuit at the smaller order with the same number
of binary gates. 

### `hamiltonianCyclePolynomial_two`

 The directed cycle on two vertices consists of its two opposite arcs. 

### `cycleEdgeProjection`

 Keep the first arc and set the other factors to one, as in Section 1.1. 
