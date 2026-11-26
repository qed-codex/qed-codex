---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterStackBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterStackBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterStackBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scratch capacity during the preorder traversal

The pending frames partition the still unread leaves. Their total leaf count
cannot increase, even if the path is later rejected for repeated positions.
Replacing a pending internal frame by its children decreases the number of
nodes still to visit by exactly one. These bounds apply after every prefix.


### `leafMass`

 Unvisited leaves represented by the pending subtree roots. 

### `pendingNodes`

 Nodes remaining in those subtrees, including their pending roots. 

### `advance`

 Executing a prefix may leave pending subtrees for the next visit. 

### `advance_bounds`

 Prefix accounting includes malformed paths until their first failed step. 

### `root_bounds`

 A stack plane of one word per possible leaf suffices at every prefix.
In particular no rejected path accesses an additional frame. 

### `testMarks`

 Test and set the mark of each selected leaf. A fresh parse begins with
all marks cleared. 

### `freshMarks_iff`

 The linear test-and-set loop implements the decoder's position check. 
