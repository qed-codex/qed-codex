---
{
  "module": "OAI/Computability/VPVNP/CompressorBundleSortedWidths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleSortedWidths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleSortedWidths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sorted width rows from the bounded lists of old ports

Run the global key gather, the increasing-port rank scan, and the width scatter
on their successive post-memories. The resulting thick rows give the
concatenation order used to assemble AB blocks. Motif rows give the old CD
widths in piece-number order.


### `scatterPublic`

 Use the original owner/width columns and the completed rank destination.
The sorted width rectangle has the same stride as the bounded lists. 

### `sorted_widths`

 Three successive native passes produce the exact sorted width rows directly
from the preimage table, the classified keys, and the old width column. 
