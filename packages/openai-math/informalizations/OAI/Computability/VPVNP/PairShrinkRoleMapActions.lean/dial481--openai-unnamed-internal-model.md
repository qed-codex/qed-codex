---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleMapActions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleMapActions.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleMapActions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native map actions of the selected shrinking site

The packed row enumerates all resident motif-party occurrences. The gathers
and matrix routines use the current scratch in order, and their success
bits are determined by the typed inputs at those occurrences.


### `jobInput`

 Matrix-entry input of a resident party job, with the site's hidden assignment transported
along the party's placement equality. 

### `actions`

 The native actions in the actual selected row order. Every later action
receives the scratch returned by its predecessor. 
