---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotWidth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotWidth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotWidth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Width lookup on the sorted shrinking output

The split array is indexed by original old arc (including its lane), role-edge
type, and local subdivision. The canonical outgoing array is indexed by the new
site and its local slot. The two lookups refer to the same selected motif.


### `SplitRows`

 The chosen widths in the contiguous old-arc/type/subdivision rows. 

### `splitNumber_genuine`

 Reading the digits of a genuine absolute ID produces its exact split-row offset. 

### `portIndex`

 Ordinary new outgoing slot number: site first, local slot second. 

### `readback`

 One actual outgoing slot: both read addresses are inside their allocated
input regions and the written word is the width used in the semantic shrinking step. 

### `write_all`

 Every canonical outgoing width is written once, including all zero-width
slots and the dummy tail. 
