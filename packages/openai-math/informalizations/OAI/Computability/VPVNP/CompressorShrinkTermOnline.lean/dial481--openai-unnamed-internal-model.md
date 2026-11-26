---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkTermOnline.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermOnline.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermOnline.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The two shrinking term packets in the repeated online block

The gather occupies ordinal 20 of its shrinking substep, and the fused
term selector occupies ordinal 21. The stage occurrences retain the
original resetting instruction programs, physical operands, bit streams
and reports when placed into the global script.


### `prior`

 The header, greedy and bundle visits that precede term gathering within this shrinking
substep. 

### `remaining`

 The selected placement and later slice and slot visits following term selection in this
shrinking substep. 

### `window`

 The exact two-visit interval occupied by demand gathering and term selection in the
repeated block script. 

### `localIndex`

 Number the gather as the first term visit and the selector as the second. 

### `index`

 Map the gather or selector through its two-visit window to its global script index. 

### `ordinal`

 The chronological phase ordinal of a term visit at a given block repetition, after the
initial sequence and earlier substeps. 

### `globalVisit`

 Install the chosen term worker at its global index with the physical operand bank,
motif-count stop and gather or selection tapes. 
