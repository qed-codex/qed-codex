---
{
  "module": "OAI/Computability/VPVNP/DegreeRefreshExpansion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshExpansion.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshExpansion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Expanding all degree-refresh motifs

Each block independently chooses a term of its internal motif identity. For
that choice, the product of block contractions is a sum over one shared
payload per internal supply edge. The outer external wire assignment remains
common to both of its incident blocks. This gives the portwise product and
the branch-dependent sums in equation (7.1) for the degree refresh.


### `blockSupply`

 The local supply network in the selected term of one block. 

### `refreshFactor`

 The matrix entry at one port multiplies its two local diagonal tests by
the entry of the block motif map. Only the incident half-wires are read. 

### `refresh_edge_expansion`

 The external-bundle identity and the ordinary local identities in all
blocks give the edge-indexed expansion with independent choices in each block. 
