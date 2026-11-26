---
{
  "module": "OAI/Computability/VPVNP/RAMValidatorLocality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorLocality.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorLocality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Locality of the distributed RAM validator

A processor can check its candidate path using its own header, the two
adjacent successor fields when present, and the sort fields incident to it.
The comparison layers may carry arbitrary records. Agreement of the received
blocks suffices to reproduce the local replay and agreement of the sent
blocks suffices to reproduce the local send checks.


### `physical_sort_locality`

 Fixing the two incident blocks of each physical layer fixes both the
processor's comparison checks and its final block. 

### `Messages.AgreeAt`

 Two message assignments give the same fields at a site. Each existing
successor edge is named by its sender. The first and last missing edges
therefore require no equality. 

### `validator_congr`

 The local path predicate for any candidate reports, including rejecting
candidates, depends only on the site's header word and incident fields. 
