---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkTermPacketBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermPacketBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermPacketBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Work and data-arena bounds of the shrinking term packets

Both packets can be replayed under the online calendar. Every cursor
increment occurs before the exclusive motif stop. Their reads and
writes stay within the current shrinking arena, and each report obeys
the source instruction cap.


### `PacketRun.bounds`

 The two source rows already have the cursor progress, private cap and
external charge needed to construct their linked online rows. 

### `PacketRun.arena`

 A data replay needs agreement only inside the allocated shrinking
level. In particular all locations before the level's start are excluded. 
