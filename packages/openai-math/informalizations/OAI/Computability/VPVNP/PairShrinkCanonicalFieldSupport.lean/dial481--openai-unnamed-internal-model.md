---
{
  "module": "OAI/Computability/VPVNP/PairShrinkCanonicalFieldSupport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCanonicalFieldSupport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCanonicalFieldSupport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External memory of a canonical shrinking visit

The locator and child reader enter the packed row. All remaining reads come
from that row's old level, stored term directory, hidden fields, and selected
matrix operands. The parent decoder and the scratch and histogram updates
take place in private memory. A returned visit therefore preserves external
memory on its entire choice stream, independently of later visits.


### `hiddenRead_noWrites`

 A successful hidden-field parse emits only reads and private events. 

### `canonicalFamily_support_of_maps`

 Read and write footprints of a returned raw visit with its parent fixed. 
