---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Clocked stack computation of rectangular matrix rank

The evaluator halts when it reaches a returned scalar at empty stack. The rank
scan uses this evaluator for every bidegree, with no access to polynomial
matrices or their determinants.


### `drive`

 Tail-recursive execution with a timeout. An empty-stack return is a
successful result, including exactly at the clock boundary. 

### `clock`

 Bound on abstract stack transitions for a Schur query with matrix order `n` and degree
limits `U` and `Z`. 

### `compute`

 Run the determinant coefficient query at bidegree `(u,z)` with its proved transition bound,
defaulting to zero on timeout. 

### `computeRank`

 Rectangular matrix rank from the stack program and scalar input accesses. 

### `clock_le_exp`

 The clock bound is singly exponential in the common bit bound. 

### `rankClock_le_exp`

 Total scalar-stack clock over the rectangular scan, including queries
for zero rows or zero columns. 
