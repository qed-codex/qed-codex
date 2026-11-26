---
{
  "module": "OAI/Computability/VPVNP/PairRefreshTraversalFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshTraversalFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshTraversalFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private geometry and cache through the refresh map

At the terminal layout's actual geometry address, the pointer cell and both dispatch
words survive the canonical upper scratch update. The scalar cache lies after the
complete map workspace and all its cells are preserved as well.


### `cache_preserved`

 Every scalar cache word lies above every address written by this visit. 

### `geometry_preserved`

 The actual geometry pointer, role offset and histogram base are unchanged. 
