---
{
  "module": "OAI/Computability/VPVNP/Hamiltonian.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Hamiltonian.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Hamiltonian.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Directed Hamiltonian cycles as binary matrices

Section 1.1 of *VP and VNP differ over every field* projects the pair of
variables encoding an edge bit to `(1, X e)`. This gives one monomial for
each accepted adjacency matrix. The identity below identifies their sum,
as a formal polynomial, with the sum indexed by single-cycle permutations.


### `booleanPolynomial`

 The edge polynomial obtained by retaining exactly the variables at true bits. 

### `permutationEdges`

 The adjacency matrix of the directed edges from each vertex to its image. 

### `spanningCycles`

 Single directed cycles on all vertices. A loop is a cycle of order one. 

### `rowSuccessor`

 Scan a row for its first edge. The diagonal default is used for an empty row. 

### `acceptsCycleMatrix`

 Each row is the graph of its scanned successor,
every column is hit, and all vertices occur in the first `m` steps starting from `root`.
Every quantifier in this Boolean test ranges over the vertices. 

### `cycleIndicator`

 The zero-one coefficient for a deterministic Hamiltonian-cycle predicate. 

### `hamiltonianCyclePolynomial`

 The directed Hamiltonian-cycle polynomial in matrix indeterminates. 
