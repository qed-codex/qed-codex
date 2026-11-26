---
{
  "module": "OAI/Computability/VPVNP/PairTerminalLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical terminal layout of the compressed pair

The final 32 words of the live pair workspace hold the terminal controller
header. The selected traversal rows, final bit interval and role words lie
below it. A private burst uses a node's absolute descriptor address for its
argument buffer. The first unused node buffer begins the private histogram.
A twelve-word geometry directory follows that histogram, and a 38-word
operand cache precedes the local verifier stacks.


### `headerBase`

 Beginning of the terminal controller header inside the live pair workspace. 

### `privateRegions`

 The program-wide argument, histogram, cache and stack intervals. 

### `geometry`

 Immutable words reloaded by cursor leaves and the map dispatch after
the DFS has popped their node address. Cell `n` points at this array. 

### `geometryPointer_before_node`

 Every real node buffer starts above the private cell that points to
the immutable geometry. This includes the initial cursor layer. 

### `eventually_fitWithReserve`

 All simultaneous external and private regions fit on every selected
cursor branch. The untouched high header and the private pointer cell are
separated from their adjacent live arrays. 

### `eventually_fit`

 The selected private region through the last virtual verifier stack. 
