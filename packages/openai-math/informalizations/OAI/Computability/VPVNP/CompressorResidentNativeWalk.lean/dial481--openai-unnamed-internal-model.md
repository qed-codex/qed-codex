---
{
  "module": "OAI/Computability/VPVNP/CompressorResidentNativeWalk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorResidentNativeWalk.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorResidentNativeWalk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Chronological native source walk of the resident directories 

### `Mutable`

 Addresses the resident group may write, comprising its allocated array interval and header
offsets 30 through 35. 

### `Native`

 The chosen resident stage runs from cursor zero, reaches its limit, reads above the lower
bound, and writes only within its mutable region. 

### `values`

 Assemble the resident-stage operands from the state layout, level header, absolute and role
array heads, and selected side. 

### `native_walk`

 Both tables and the six headers execute against the post-memory of the
preceding stage. All modified cells lie in the declared two intervals. 
