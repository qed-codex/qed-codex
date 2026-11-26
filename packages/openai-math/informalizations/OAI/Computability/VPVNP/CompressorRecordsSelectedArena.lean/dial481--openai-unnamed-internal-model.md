---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsSelectedArena.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsSelectedArena.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsSelectedArena.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Consecutive score, placement and role arrays for a selected shrinking term

The two scores and the chosen layout follow the actual motif term rows.
Four old-position columns then contain the selected placement, and four
words per absolute old arc contain its demand-role record.


### `positions`

 Number of old packed positions in this shrinking state, one for each base vertex and
packing-lane address. 

### `motifs`

 Number of selected motif term rows, counted in the physical motif order used by the score
pass. 

### `origin`

 Address immediately after the fixed-stride motif term rows, where the first layout score is
stored. 

### `placementBase`

 Start of the placement columns, three words past the score origin to allow for two scores
and the chosen-layout bit. 

### `roleBase`

 Start of the demand-role records after the four placement columns of one word per old
position. 

### `endAddr`

 Exclusive end of the selected arena, after four role words for each absolute old arc. 

### `scoreTables`

 Score-pass operands for the motif rows, selector bits, two consecutive score counters and
the layout-choice cell at offset two from the score origin. 

### `placementWord`

 Machine-word address of the start of placement column `t`, spaced by the number of old
positions. 

### `shrinkWords`

 Build the fourteen shrink-worker operands from the existing geometry and input pointers,
the selected layout word and the four placement-column addresses. 

### `selectedWords`

 The dynamic operand is read from the cell written by the strict score comparison. 

### `demandWords`

 Assemble the eleven demand-worker operands from shrink geometry, the old outgoing incidence
array, the selected placement columns and the role-record destination. 

### `Fits`

 The exclusive end of the score, placement and role arena lies strictly below the
machine-word modulus. 

### `decoded_offsets`

 The old color/offset entries are indexed by base vertices, while the
mate/displacement entries are indexed by directed base slots. 

### `OldInputs`

 The old color, offset, mate, displacement and outgoing incidence arrays all end at or
before the score origin, separating them from the new output columns. 
