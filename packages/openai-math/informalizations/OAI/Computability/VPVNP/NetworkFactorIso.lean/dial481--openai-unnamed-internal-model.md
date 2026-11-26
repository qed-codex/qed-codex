---
{
  "module": "OAI/Computability/VPVNP/NetworkFactorIso.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NetworkFactorIso.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NetworkFactorIso.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local factors after relabelling a network

Reindex each whole local factor by the new site and pull its incoming and
outgoing arguments back along the alphabet bijections. This preserves the
contraction, even for a network with parallel edges.


### `pushFactors`

 Move an arbitrary local factor to its corresponding relabelled site. 

### `contract_pushFactors`

 One shared payload per relabelled edge corresponds to one per original
edge. Every local factor then sees exactly its original incident arguments. 

### `pushChoiceFintype`

 Transport the finite family of individual choices counted by a local
factor. At the image site, its elements are the choices on the pulled-back
half-wire data. 

### `contract_pushChoiceCount`

 The multiplicities of the transported local choice types have the same
contraction as the original local choice counts. 
