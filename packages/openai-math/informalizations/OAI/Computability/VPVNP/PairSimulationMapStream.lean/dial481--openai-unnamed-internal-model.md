---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapStream.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapStream.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapStream.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a grouped motif one copy at a time

Each iteration checks the two ends of all incident selectors against the
anchor, decodes the common tag, and reads the local demand and payload row.
The cursor advances on every supply edge, including edges away from the
party. The terminal test compares this entire vector with the descriptor.


### `Cursor`

 Offsets of the next copy and labels of the completed copies, newest first. 

### `Cursor.offset`

 Cumulative payload width already consumed on each supply edge, giving the starting bit
  offset of the next copy. 

### `Cursor.labelsRev`

 Labels obtained from completed copies, stored newest first so the scan can prepend each
  new row result. 

### `scan`

 Read one selector and one row per iteration. A malformed copy stops the scan. 

### `offset_le`

 At a copy boundary the cumulative offset fits a fixed multiple of the copy index,
even for a descriptor whose final width test will fail. 

### `totalWidth_le`

 The full-vector comparison can use the same bound on arbitrary decoded selectors. 

### `scan_none`

 A missing or inconsistent tag rejects the complete stream at any position. 

### `scan_some`

 The cursor before copy `i` is its prefix sum, the final cursor is the total,
and each accepted row appears with its original multiplicity and copy position. 

### `agrees`

 Check both port directions at this copy, including both ends of a loop. 

### `agrees_eq_consistent_one`

 Restrict the input to one selector position to invoke the native whole-array
agreement test on this copy. 

### `selectCopy`

 An unused anchor code and a mismatch between any two incident ports
both suppress the row lookup for this copy. 

### `selectCopy_of_consistent`

 A native precheck of the complete port arrays leaves just one anchor-table
lookup per copy in the subsequent loop. 

### `readRow`

 The local base-matrix row indexed by demand and payload fields, starting
each payload field at the current cursor. 

### `finish`

 Check all final payload offsets and restore the order of the emitted labels. 

### `evaluate`

 The complete streaming evaluator starts at zero and validates the full
vector before returning the labels in copy order. 

### `evaluate_after_consistency`

 Factor out a port-major native agreement pass. The remaining scan only
decodes the anchor and reads payload and demand rows. 

### `evaluate_eq_run`

 Equivalence with the metered entry interpreter for arbitrary input bits and
arbitrary selector tables, with no consistency, completeness or width hypotheses. 

### `searchRow`

 The row search tests the finite word tuple used by the native lookup tree.
Neither the row table nor the field list depends on the number of repetitions. 

### `rowName`

 The name is taken from the matching row of the fixed matrix. 

### `runBlock`

 Execute the scan with the fixed selector and local matrix tables of this
block. The register width only has to contain the base digits used by the row tree. 
