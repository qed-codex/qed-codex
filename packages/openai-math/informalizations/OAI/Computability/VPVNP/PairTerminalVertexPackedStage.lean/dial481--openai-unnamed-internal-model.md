---
{
  "module": "OAI/Computability/VPVNP/PairTerminalVertexPackedStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalVertexPackedStage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalVertexPackedStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From the native shared scan to each packed vertex

Every subsequent site sees the exact rows, role tags and shared choices
of the accepted bit worker. It also sees the earlier level arrays and the
noncontrol header cells from that worker's input. The two control words
may be rewritten at each site handoff.


### `VertexPacked.shared`

 A single true shared-bit stage supplies the reference memory for all
subsequent ordinals. Its data include the exact branch bit at every wire. 
