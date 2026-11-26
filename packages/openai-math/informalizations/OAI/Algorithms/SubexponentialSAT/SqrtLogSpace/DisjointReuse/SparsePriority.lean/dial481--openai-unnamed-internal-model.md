---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparsePriority.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparsePriority.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparsePriority.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Appendix A: smallest-width, largest-core selection and marked degrees. 

### `degree`

 Number of width-`c` clauses containing a literal core. 

### `candidates`

 Enumerate clause/core pairs, never tuples of parameter-dependent size. 

### `clause_card_le`

 A coarse polynomial clause bound, sufficient for the search cost. 

### `violatingCandidates`

 The threshold is tested by exact natural arithmetic. 

### `select`

 The lexicographic key orders smaller widths first and larger cores first. 

### `Priority`

 The local consequences of the source priority, independent of deterministic tie order. 

### `Priority.marked_degree_childA`

 A marked `A` child may discard clauses; adding its single core preserves the bound. 

### `Priority.marked_degree_childB`

 Petals and false-core units preserve the bound at every marked `B` child. 
