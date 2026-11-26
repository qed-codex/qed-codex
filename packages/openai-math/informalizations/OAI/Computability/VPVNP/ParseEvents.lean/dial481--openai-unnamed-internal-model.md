---
{
  "module": "OAI/Computability/VPVNP/ParseEvents.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseEvents.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseEvents.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Canonical interval tables of ordered parses 

### `rootEvent`

 The occurrence at the root interval, including its production choice. 

### `events`

 Include the root and concatenate the two children in their leaf intervals. 

### `event_bounds`

 Every occupied interval is contained in the leaf interval of its ancestor. 

### `disjoint_childEvents`

 The left and right subtrees have disjoint occurrences. 
