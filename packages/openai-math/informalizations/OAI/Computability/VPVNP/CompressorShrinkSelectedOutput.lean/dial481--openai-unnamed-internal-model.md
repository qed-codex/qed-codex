---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkSelectedOutput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSelectedOutput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSelectedOutput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The fixed output workers after a selected shrinking pass

The four role programs read the layout bit, dense-to-absolute motif table,
and selected term fields from one post-selection memory. The slot passes
consume their absolute width rectangle. Their complete trace preserves
the preimage directory and gives the next state's six incidence columns.


### `layoutWord`

 Word address of the chosen layout bit, two cells after the start of the score arena. 

### `Passes`

 The width-scan traces for the four surviving roles, their output memory, and the subsequent
construction of the successor’s slot tables. 

### `Passes.widthRows`

 Lists of native width reports grouped by surviving role, in the order of the four role
  sweeps. 

### `Passes.postWidths`

 The memory handed from the four role width sweeps to the slot-table construction. 

### `Passes.slots`

 Construction traces that consume the role widths and build the successor’s slot and
  incidence tables. 

### `Passes.reports`

 The full output trace, with the role width reports flattened in sweep order and followed by
all slot-construction reports. 

### `Passes.final`

 Memory obtained by replaying the slot construction from the memory produced by the width
sweeps. 

### `Complete`

 The actual fixed controls and final readback on one selected branch. 

### `build_at`

 Execute the same fixed controls at the width-table and slot-table heads
chosen by the block calendar. A gap between the two tables is permitted. 

### `build_selected`

 The width and ordered-slot arrays are produced from the earlier selected
stage and the physical absolute-ID table. The layout bit remains at its
score-comparison address through the preimage and output passes. 
