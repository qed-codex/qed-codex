---
{
  "module": "OAI/Computability/VPVNP/PermanentPadding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentPadding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentPadding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Diagonal padding for the permanent

Section 15.1 of *VP and VNP differ over every field* pads a matrix of
indeterminates by adjoining one diagonal entry equal to one and setting all
other entries in its new row and column to zero.


### `permanentPolynomial`

 The permanent of the generic `m` by `m` matrix. 

### `permanentPolynomial_eq_sum`

 The row-first formula used in the paper. 

### `permanentPadding`

 Vertex zero is the new vertex, and `Fin.succ` embeds the old indices. 

### `permanentPadding_polynomial`

 Exactly the permutations fixing the new index survive diagonal padding. 
