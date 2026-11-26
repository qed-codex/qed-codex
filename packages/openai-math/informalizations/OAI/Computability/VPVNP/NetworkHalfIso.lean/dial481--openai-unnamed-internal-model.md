---
{
  "module": "OAI/Computability/VPVNP/NetworkHalfIso.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NetworkHalfIso.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NetworkHalfIso.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Half-wire coordinates under network relabelling

In a placed expansion, changing the coordinates of the input network gives
a bijection on the independent half-wire assignments at each old site. The
same expansion can then use the original output network for each choice.


### `refl`

 Relabel each site, edge and payload by its identity map. 

### `pullHalfEquiv`

 Pulling the half-wire indices back to an original site is a bijection. 

### `Step.reindexInput`

 Reindex the input of an exact step, retaining its chosen output for every term. 

### `Step.reindexInput_term_output`

 An input reindexing retains the output network at each choice. 
