---
{
  "module": "OAI/Computability/VPVNP/HamiltonianRelabel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HamiltonianRelabel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HamiltonianRelabel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Weighted directed Hamiltonian cycles on a finite vertex type

Relabel the vertices by matrix indices, substitute zero on forbidden arcs, and
put the indicated variable or scalar on each allowed arc. In the resulting
formal polynomial only the permitted spanning permutations contribute.


### `hamiltonian_projection_on_allowed`

 The projected matrix has the given arc label on allowed arcs and zero elsewhere. 
