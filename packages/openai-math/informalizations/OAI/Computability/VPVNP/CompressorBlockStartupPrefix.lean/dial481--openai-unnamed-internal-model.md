---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockStartupPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockStartupPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockStartupPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The level-zero source prefix from physical startup data

At each sufficiently large length the saved cursor operands come from the
eight linked startup stages. The four initial descriptor workers produce
the typed cursor graph, preserve all eight operands, and publish the
terminal six scalars used by the first selected substep.


### `Resident`

 The level-zero startup reports execute and leave the packed cursor graph and its persistent
metadata in memory. 

### `Resident.live`

 All fields consumed by the following pass are recovered on a live
memory agreeing with the raw output above the first level header. This
includes the incoming and outgoing columns at their computed indices. 

### `eventually_resident`

 One length threshold covers both the true pair startup and all four
initial descriptor visits, uniformly in the incoming contents of RAM. 
