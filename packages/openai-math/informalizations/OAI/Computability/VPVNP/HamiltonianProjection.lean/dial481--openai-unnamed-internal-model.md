---
{
  "module": "OAI/Computability/VPVNP/HamiltonianProjection.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HamiltonianProjection.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HamiltonianProjection.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Projecting the universal integer family onto directed Hamiltonian cycles

For each matrix order, a deterministic finite query program traverses the
directed cycle, checking one full row at a time. Compiling this program with
a budget of `m * m` queries gives a literal machine table. Pinning its prefix
in equation (1.1) leaves exactly the cycle monomials. This construction uses
an order-dependent prefix whose bit length is polynomially bounded.


### `hamiltonian_projection_orders`

 A single polynomially bounded choice of source orders works over all commutative rings. 

### `hamiltonian_PProjects`

 Directed Hamiltonian cycles are p-projections of the integer family over each field. 
