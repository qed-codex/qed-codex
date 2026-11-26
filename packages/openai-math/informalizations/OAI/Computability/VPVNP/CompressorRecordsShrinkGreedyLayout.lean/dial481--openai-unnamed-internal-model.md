---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkGreedyLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkGreedyLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkGreedyLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fresh storage for the shrinking step's color and tag assignments

Both directed mate arrays and the original lane displacement stay in the
input incidence directory. New storage contains the two complete assignment
directories, one projected tag per outgoing base port, and a shared zero.


### `colorBase`

 The origin of the greedy color assignment's fresh storage. 

### `offsetBase`

 The first address after the color walk's labels and work rows, where the tag-offset walk
begins. 

### `shiftBase`

 The first address after both greedy walk regions, reserved for the projected displacements
of old base ports. 

### `zeroCell`

 The shared zero operand stored immediately after the projected displacement column. 

### `greedyStop`

 The exclusive upper bound of the greedy assignment workspace, one word past its zero
operand. 

### `colorLayout`

 The bounded layout of the greedy color walk, with room for the two directed incidences at
each slot. 

### `tagLayout`

 The bounded layout of the greedy offset walk, using its four tag-count groups per work row. 

### `OldBelow`

 The six old columns are below the beginning of the new scratch range. 

### `tables`

 Assemble the walker's port tables from the old incidence directory and the specified label,
zero, and displacement columns. 
