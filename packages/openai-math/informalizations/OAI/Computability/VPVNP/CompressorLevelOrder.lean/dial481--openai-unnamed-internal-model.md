---
{
  "module": "OAI/Computability/VPVNP/CompressorLevelOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorLevelOrder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorLevelOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Order of the selected compressor levels

The native calendar repeats a fixed list of pass types. Choices alter the
data of the next level but preserve the scheduled order. The first indices
in a block enumerate shrinking transitions in increasing order, and the
last index is its refresh.


### `PassOrigin.ordinal`

 Slot of the elementary kernel in one block of the online calendar. 

### `executeLevels_order`

 On every branch, the exact chronological kernel sequence is the fixed
calendar block repeated the prescribed number of times. 
