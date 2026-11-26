---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortStartup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortStartup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortStartup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Preparing the bitonic sorter from the site's public registers

The initialized site already holds its word width and its number of slots,
`4H`, in unary. Copy the latter and halve the copy until only one mark remains.
This writes the row width `h = log₂(4H)`. The phase loop receives `h+d` marks
from the row and site widths. Both original dimensions remain available to the
record reader, and the temporary stacks finish empty.


### `Port`

 Registers for the site address width, slot count, logarithm calculation, row width, and
remaining phase count. 

### `bank`

 Encode the supplied dimensions, working copy, row width, and remaining phase count as unary
stacks. 

### `routine`

 A fixed control, with the slot count and both widths held on actual stacks. 

### `cost`

 Number of startup steps for copying the slot count, computing its ceiling binary logarithm,
and assembling the phase count. 

### `runs`

 Only the two new output registers change, even for a non-power-of-two slot count. 

### `runs_framed`

 A caller can map the output registers directly to the stage counter and the row
enumerator. Every stack outside these two outputs is restored. 

### `Scratch`

 Two temporary sorter startup stacks for the slot-count copy and the logarithm calculation. 

### `Registers`

 Combined register bank for schedule control, site setup, startup scratch, and sorting
offsets. 

### `caller`

 Embed a site setup register into the combined sorter register bank. 

### `ports`

 Wire each startup port to its address-width, slot-count, scratch, row-width, or schedule
register. 

### `ready`

 Install the prepared site stacks in the idle sorter with the given row width and remaining
phase count and zero phase and stride. 

### `startup_runs`

 Preserve all bit fields, including the staged records, word width, and slot count.
Only the outer schedule and the inner row traversal receive new marks. 

### `from_prepared`

 On the initialized physical site, the sorter sees the same word and slot dimensions
as the record emitter, together with its own binary width and schedule length. 
