---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockCursorPacket.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockCursorPacket.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockCursorPacket.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cursor incidence as the third source packet of the block program

The worker reads its eleven operands from the published first-level frame.
It starts at zero, returns each following row index, and writes all six
incidence columns for the actual cursor state. Every address before the
columns retains its incoming value.


### `run`

 The scan follows the two raw header publishers. Its report list certifies
the exact typed outgoing, incoming, displacement and width records, including
the incoming entries written at computed destination indices. 
