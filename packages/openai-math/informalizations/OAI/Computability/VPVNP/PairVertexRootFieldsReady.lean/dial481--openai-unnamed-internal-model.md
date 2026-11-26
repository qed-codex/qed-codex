---
{
  "module": "OAI/Computability/VPVNP/PairVertexRootFieldsReady.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexRootFieldsReady.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexRootFieldsReady.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Root packet and DFS state at the end of the terminal gather

The bootstrap pushes the root address onto an initially zero private memory.
The gather installs the actual terminal vertex's two half-wire lists in its
node interval. At DFS row zero the pending root, vertex-wide geometry, all
38 cached leaf inputs and the zero histogram are resident together.


### `singleton`

 The concrete boot store gives exactly the singleton stack below the
geometry pointer, even when the payload word is zero. 
