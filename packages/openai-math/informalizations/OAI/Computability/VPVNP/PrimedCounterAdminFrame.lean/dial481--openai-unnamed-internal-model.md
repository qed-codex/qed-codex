---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterAdminFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterAdminFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterAdminFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Memory updates at the boundaries of the primed parser

Before each site, the parser clears every location mark and installs a
singleton root stack. The histogram survives these operations. After the
last site, the comparison at a dense index reads the count of its unique
production label.


### `store_below`

 Typed scratch stores preserve every word in the reserved prefix. 

### `clear_holds`

 One clear call erases exactly the selected location from the logical mark set. 

### `rootStore`

 Install a frame in slot zero and overwrite the old stack depth with one. 

### `root_data`

 The three root stores leave every input bit, mark and production count intact. 

### `root_rep`

 The root stores install a singleton stack regardless of the old depth or frame words. 

### `root_holds`

 Root initialization installs a singleton pending stack for the new site. 

### `compare_iff`

 The final word comparison tests the exact logical production count. 
