---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Pathwise clock for the physical sorting passes 

### `ticks`

 Includes every phase update, row scan, split and array reversal. 

### `ticks_le`

 The sorting part of the physical stack computation fits a fixed power
when the address and word lengths fit in `n` and the block has at most
eight records per input bit. 

### `eventually_ticks_le`

 In the paper's live construction the constant `B` only affects the
length threshold. The bound applies to every raw incident assignment. 
