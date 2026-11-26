---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyLevelPlan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyLevelPlan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyLevelPlan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Planning the ordered greedy scans for a shrinking level

The initializer receives the current level's base mate pointers in its public
frame. The color and tag labels occupy separate arenas, each immediately
followed by its fixed-stride records. A read starts at the first record and
stops at the address just past the last record.


### `offsetBase`

 Starting address of the tag-label arena, immediately following the color labels and
records. 

### `shiftBase`

 Starting address of the extracted shifts, immediately following the tag labels and records. 

### `zeroAddress`

 Address of the shared zero word following all per-port shifts. 

### `greedyStop`

 Exclusive end of the greedy scratch region, one word past the shared zero cell. 

### `colorPrepare`

 Calendar visit that prepares the color-test operand records for every base vertex. 

### `colorRead`

 Calendar visit that scans the prepared color records to assign the greedy color labels. 

### `tagPrepare`

 Calendar visit that prepares the four-operand tag tests from the extracted shifts and label
tables. 

### `tagRead`

 Calendar visit that scans the prepared tag records to assign the greedy tag labels. 

### `walkVisits`

 The four greedy walk visits in order, preparing and scanning colors before preparing and
scanning tags. 

### `extractShifts`

 Calendar visit that projects the old incidence shifts into the scratch shift column, one
row per base port. 

### `publishZero`

 Single-row visit that initializes the shared zero cell used by the greedy walks. 

### `visits`

 Project the displacement and install the zero operand before preparing either directory. 

### `Reads`

 Values supplied by the physical level header and the chosen scratch origin. 
