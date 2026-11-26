---
{
  "module": "OAI/Computability/VPVNP/PairShrinkMapReload.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkMapReload.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkMapReload.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reloading the geometry and histogram heads before the shrinking maps

The DFS end register points to a private word containing the geometry head. The
histogram head is its eleventh field. This fixed prefix reads those two words from
the actual configuration before entering the grid and party map loop.


### `instruction`

 Four native instructions follow the private geometry pointer at the stack end and load
geometry word 11, the histogram base, into locator register 10. 

### `run`

 The private reload leaves the packed owner and the cached hidden-field head intact. 

### `setup`

 Install the four histogram-reload instructions ahead of a located resident map body, using
its locator registers and DFS stack-end register. 

### `body`

 Geometry preparation and the installed map share their full register bank. 
