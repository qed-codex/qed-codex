---
{
  "module": "OAI/Computability/VPVNP/PairTraversalRoleNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalRoleNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalRoleNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native writes of the role tags used by the descriptor dispatcher

A fixed burst reads the offset, layer base, row stride, and tag from its
public parameters. Its persistent state is the current site number. Each
burst writes one tag and increments the site number. A full layer scan
changes exactly the words indexed by its descriptor headers.


### `params`

 Public directory words for one layer. 

### `visit`

 Use the site's persistent index to compute its absolute role-table address. 

### `events`

 Chronological role-worker events, including the external write of the selected role code at
the site's displaced row address. 

### `image`

 The image of the first `count` sites of the role table. 

### `run_layer`

 Run the fixed role-writing worker on every site in one actual descriptor
layer. The report cost includes one burst invocation and one external write. 
