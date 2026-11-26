---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkReadbackTransfer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkReadbackTransfer.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkReadbackTransfer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Shrinking slice readbacks after later memory writes

The AB endpoint lists, surviving interval descriptors and sparse subdivision
widths lie below the ordered-slot workspace. A subsequent pass that preserves those addresses can read them in its own
terminal memory.


### `SliceReadbacks`

 The AB and surviving CD tables of a single selected block, as read from
one physical memory. 

### `abFields_transfer_interval`

 Transfer every AB frame and its two endpoint lists through a memory
frame covering the full bundle rectangle. 

### `abFields_transfer`

 The prefix-frame form used immediately after the slot construction. 

### `CompleteTables.slice_transfer`

 Transfer both kinds of interval tables and the sparse widths from an actual
three-table run through a later copy preserving the addresses before the
ordered-slot workspace. 
