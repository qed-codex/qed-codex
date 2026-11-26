---
{
  "module": "OAI/Computability/VPVNP/PairTerminalVertexPackedGather.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalVertexPackedGather.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalVertexPackedGather.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Root-gather operands at every physical site

The terminal worker reloads the current vertex ordinal and six header words,
including the live width, inverse, and prefix pointers. Its root layout
agrees with the layout read from the physical shared-bit post-memory.


### `VertexPacked.gather`

 Inputs consumed by the concrete gather's DFS handoff. Its private end
fit is supplied by the site's argument arena. All external fits and the
typed shared-bit and row equalities are recovered from the packed layout. 
