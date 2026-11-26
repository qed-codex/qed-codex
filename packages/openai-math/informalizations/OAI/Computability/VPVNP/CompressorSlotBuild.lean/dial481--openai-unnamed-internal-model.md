---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotBuild.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotBuild.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotBuild.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Complete shrinking slot and incidence construction from the selected rows

The demand-role scan supplies the CD indicator and three packed role sites
on each old arc. The term/slice scan supplies each genuine subdivision width.
Beginning with those rows, native preparation, ordering, inversion and width
scans construct all six incidence columns for the very next compressor state.
The scratch and output counters may initially contain arbitrary words.


### `Construction`

 Reports for a complete shrinking slot construction, from preparing the selected input
tables to writing the next state's incidence columns. 

### `Construction.prepare`

 Reports for publishing subdivisions, building the role and successor tables, and clearing
  the append counters. 

### `Construction.passes`

 Reports for constructing the slot and mate directories and gathering their widths from
  the prepared inputs. 

### `Construction.all`

 All preparation and construction reports in execution order. 

### `Construction.final`

 Memory after replaying the preparation reports and then the slot, mate, and width passes. 

### `Construction.final_eq`

 The memory consumed by the next level is the replay of this construction's chronological log. 

### `Construction.Native`

 The preparation and construction reports are produced by their respective native workers,
with construction starting from the prepared memory. 

### `Construction.Cursors`

 All preparation and construction passes return their prescribed ending cursors for this
level. 

### `splitRows_of_values`

 Convert the simultaneous natural-number width readback of the selected
slice sweep to the word representation used by the ordered incidence passes. 

### `build`

 Construct the complete shared incidence directory in arbitrary initial
scratch memory. Source word bounds are the live radices of the level.
The frame covers every earlier input and every later reserved address. 
