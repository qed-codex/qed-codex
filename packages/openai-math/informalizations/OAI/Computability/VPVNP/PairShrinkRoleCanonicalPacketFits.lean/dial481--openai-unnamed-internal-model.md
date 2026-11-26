---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleCanonicalPacketFits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleCanonicalPacketFits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleCanonicalPacketFits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Private argument bounds for the children of a canonical shrinking row 

### `CanonicalSiteData.childPacketFits`

 The tree reader enumerates the descriptor's children in their physical order. Each of
their half-wire packets fits the reserved argument slot above the geometry pointer. The
histogram starts strictly beyond that pointer even for an empty child list. 
