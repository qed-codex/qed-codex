---
{
  "module": "OAI/Computability/VPVNP/HamiltonianHardness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HamiltonianHardness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HamiltonianHardness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hamiltonian-cycle completeness and the transfer in Corollary 1.2

The exact-one presentation of an arbitrary VNP family projects from a directed
Hamiltonian-cycle polynomial of polynomially bounded order. For the paper's
integer family this is the projection in the direction used in §15.1.


### `pProjects_hamiltonian_of_isVNP`

 The directed Hamiltonian-cycle polynomial is hard under literal p-projections in all
characteristics. The graph construction uses the Boolean variables, clauses and occurrences
of the weighted exact-one presentation. 

### `P_pProjects_hamiltonian`

 The explicit integer family projects from directed Hamiltonian cycles, over every field. 

### `hamiltonian_uniform_of_P`

 The directed Hamiltonian-cycle assertion of Corollary 1.2 follows from the eventual
lower bound for `P` over one algebraically closed field of the specified characteristic. 
