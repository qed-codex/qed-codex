---
{
  "module": "OAI/Computability/VPVNP/NullstellensatzGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NullstellensatzGraph.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NullstellensatzGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The graph used for effective Nullstellensatz certificates

When the equations `F i` have no common zero, the functions `x_j` and
`t * F i` generate the polynomial algebra in `x,t`. A linear Noether
normalization of this generating system keeps each normalized coordinate
linear in `t` and of bounded total degree. This is the graph construction
of Jelonek's proof of the effective Nullstellensatz, specialized to affine
space.


### `graphGenerator`

 The original coordinates and the equation values multiplied by an extra variable. 

### `exists_certificate_of_inconsistent`

 Qualitative Nullstellensatz gives a certificate before any degree bound is imposed. 

### `graphGenerator_adjoin`

 The graph functions generate the full polynomial algebra if the system is inconsistent. 

### `graphGenerator_span_decompose`

 Every linear combination of the graph functions has the displayed affine-in-`t` form. 

### `graphGenerator_span_degree`

 Normalization by linear combinations increases the equation degree by at most one. 
