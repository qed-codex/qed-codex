---
{
  "module": "OAI/Computability/VPVNP/HamiltonianGadget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HamiltonianGadget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HamiltonianGadget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Directed Hamiltonian-cycle graph for exact-one clauses

Each variable has a track with endpoints, one pair of ports per occurrence slot, and a
buffer between successive pairs. At the slot belonging to a literal, the directed
crossing for the literal's true value passes through its clause vertex. The opposite
crossing uses the edge between the ports.


### `Vertex`

 The Hamiltonian reduction has a track for each variable, ports for literal occurrences,
separators between tracks, and one vertex per clause. 

### `prevPort`

 Left neighbor of a buffer in the linear order on its track. 

### `nextPort`

 Right neighbor of a buffer in the linear order on its track. 

### `portBuffer`

 Each port has exactly one adjacent buffer along its track. 

### `Allowed`

 Allowed directed edges. The occurrence data give the variable, clause and
satisfying variable value of each slot. 

### `card_vertex`

 The graph uses polynomially many vertices, including for empty occurrence lists. 
