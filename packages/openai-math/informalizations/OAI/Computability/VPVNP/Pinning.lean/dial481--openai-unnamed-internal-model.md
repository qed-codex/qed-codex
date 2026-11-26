---
{
  "module": "OAI/Computability/VPVNP/Pinning.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Pinning.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Pinning.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Pinning the program bits

In §1.1 of *VP and VNP differ over every field*, a fixed prefix selects a
program, and the remaining bits encode a directed graph. Pinning a prefix
removes every monomial belonging to a different program. The Hamiltonian
cycle projection follows whenever the selected program counts each spanning
cycle once and rejects all other adjacency matrices within the clock.


### `pinVariables`

 The projection pins the prefix. Each suffix bit selects either one or its edge variable. 

### `pairedPolynomial_pin`

 The coefficient hypothesis concerns only words beginning with the chosen prefix. 

### `pairedPolynomial_pin_hamiltonian`

 Pinning a prefix whose coefficients recognize Hamiltonian adjacency matrices
projects the family member at length `p + m * m` to the directed cycle polynomial. 

### `P_pin_hamiltonian`

 The selected integer counts may be recognized before base change to the field. 
