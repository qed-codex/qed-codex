---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkTermForward.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermForward.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermForward.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The certified term interval of the complete shrinking script

The raw reports of the actual gather and term verifier are retained as
two chronological packets. Both satisfy the online replay and clock
conditions. The selector's recipe reads the same published level header
after the gather writes its dense demand pairs.


### `packet`

 Combine a globally indexed term visit with its actual entry memory and the reports emitted
by its source run. 

### `packetList`

 The gather packet followed by the selector packet, starting the selector in the memory
produced by the gather reports. 
