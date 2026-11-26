---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRolePackedRow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRolePackedRow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRolePackedRow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The ordered child addresses stored at a selected shrinking site 

### `oldSites`

 The old sites at a packed site, in the order consumed by the kernel's child reader. 

### `shrinkSiteOrdinal_eq`

 The successor's argument ordinal is the packed-site index used by the resident map rows. 

### `selectedChildRow`

 The physical DFS row contains precisely the ordered old-site fiber of this occurrence.
Each child word points into the preceding selected layer at that site's ordinal. 
