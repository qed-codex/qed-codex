---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsLevelFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsLevelFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsLevelFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical header operands for online compressor recipes

Each recipe enters at the first level of its block. A fixed substep offset
and the runtime level stride select the input or output header. Scalar,
incidence, and scratch-array operands use the published pointer cells. The
directory holds exactly the rows visited by the calendar, which may occupy
less space than the polynomial bound reserved in the capacity calculation.


### `stride`

 Recipe expression that loads the level-header stride from the cell immediately preceding
the directory. 

### `atLevel`

 Address expression for the header a fixed number of level strides after the block's entry
state. 

### `address`

 Address of a field at the specified offset in a header selected relative to the block's
first level. 

### `scalar`

 Recipe expression that loads one word from the selected level header. 

### `incidence`

 Load the published pointer to one of the six incidence columns following the level's scalar
fields. 

### `table`

 Load a table's published base pointer from the level header after the six incidence
pointers. 

### `vertices`

 Read the number of input base vertices from scalar zero of the selected level. 

### `degree`

 Read the input slot degree from scalar one of the selected level. 

### `lanes`

 Read the number of input lanes per base vertex from scalar two of the selected level. 

### `residualLanes`

 Read the number of residual lanes from scalar three of the selected level. 

### `nextDegree`

 Read the next level's slot degree from scalar four of the current level. 

### `expanderDegree`

 Read the refresh expander's degree from scalar five of the selected level. 

### `sites`

 Compute the level's input site count by multiplying the base-vertex count by the lanes per
vertex. 

### `slots`

 Compute the number of input ports visited in a level by multiplying its site count by its
slot degree. 

### `Entry`

 Runtime metadata identifying the first level in this block. 

### `Published`

 The first five persistent scalars describe the actual selected step, including
its residual lanes and next degree. The sixth scalar is the fixed expander degree
for a refresh. 

### `tightDirectory`

 Pack the actual chronological directory before the headers. Capacities of
all persistent per-level arrays and the relative field offsets are preserved. 
