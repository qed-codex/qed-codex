---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordTermScores.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordTermScores.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordTermScores.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The two layout counters on the stored motif terms

The dense term row has its repetition count at offset one and its vector of payload
coordinates starting at offset two. One pass visits all motif rows for a fixed role
and layout. Its native worker computes the supply width, including the selector bits.
Eight such passes are preceded by a two-cell clear and followed by one comparison
that writes the common layout into its level's cell.


### `word`

 Encode a natural term-score parameter as a machine word. 

### `Tables`

 The dense term layout, score-counter base, selector width, and destination for the common
layout choice. 

### `Tables.termBase`

 First address of the fixed-stride term rows. 

### `Tables.termStride`

 Distance in words between successive motif term rows. 

### `Tables.scoreBase`

 Address of the first of two adjacent layout score counters. 

### `Tables.selectorBits`

 Selector width charged once for each repetition in the term record. 

### `Tables.levelCell`

 Address where the final comparison publishes the chosen layout. 

### `Axis`

 Parameters for one scoring pass over a fixed payload coordinate and layout side. 

### `Axis.coordinate`

 Payload coordinate whose width contributes to this scoring pass. 

### `Axis.side`

 Layout side whose counter the pass updates. 

### `Axis.weight`

 Weight multiplying the squared supply width in this pass. 

### `params`

 Assemble the seven public operands for the term-score worker from the term layout and
selected scoring axis. 

### `rowBase`

 First word of motif term row `i` at the configured stride. 

### `repetitions`

 Address of the repetition-count word in motif term row `i`. 

### `payload`

 Address of the axis's payload-width coordinate in the specified motif term row. 

### `counter`

 Select the score-counter address for the Boolean layout side. 

### `supplyWidth`

 Natural supply width of one axis and motif, including the selector width for each stored
repetition. 

### `axisTotal`

 Sum the axis's weighted squared supply widths over the first `n` motif rows. 

### `total`

 Add the axis totals assigned to the requested layout side. 

### `total_fin_axes`

 Enumerating the eight axes by layout and role is the same as summing the four
role scores of the selected layout over the dense motif rows. 

### `worker`

 Four probes: read the repetition count and payload, then read and write the counter. 

### `workerMachine`

 Instantiate the native single-row score accumulator with the term layout and axis operands. 

### `nextScore`

 The updated machine-word score after adding the current row's weighted squared supply width
to its side's counter. 

### `workerReport`

 The report of one score update, with reads of the repetition count, payload width, and
counter, followed by the counter write and next row cursor. 

### `Layout`

 Only the two accumulator addresses and the output cell need separation. Repetition
and coordinate reads may be shared between axes or between rows. 

### `Layout.ofIntervals`

 Consecutive dense term rows and a disjoint two-word scratch region implement all
the read/write separation required by the eight passes. 

### `total_le`

 A single integer bound, using the number of rows, the fixed weights in the given
layout and the largest supply width, suffices for every counter in the phase. 

### `Snapshot`

 The words in the counters are residues of the integer totals. All other words still
have their values from the entry to the score phase. 

### `pass`

 All rows of one role pass, from a fresh private register file at each call. 

### `runAxes`

 Execute the successive axis-specific public tables, with the previous pass's memory
and a fresh row cursor at each pass boundary. 

### `clearCode`

 A fixed call clears both scores, even when reusing a scratch area. 

### `clearMachine`

 Instantiate the native call that clears the two adjacent layout score counters. 

### `clearReport`

 The six-event report that writes zero to both score counters and returns zero. 

### `compareTemplate`

 The comparison reads both accumulators and writes the chosen bit directly to the
designated level cell. The strict branch returns one. 

### `compareMachine`

 Instantiate the comparison call with the two-counter base and the destination level cell. 

### `bit`

 Choose layout one exactly when its score is strictly smaller than layout zero's score,
resolving ties in favor of zero. 

### `compareReport`

 The comparison report reads both scores, writes the chosen bit to the level cell, and
returns that bit. 

### `run_prefix`

 Actual memory at an arbitrary prefix, after clearing, visiting whole earlier axes,
and then processing the first `k` rows of the current axis. A bound on the final scores
suffices for all such prefix scores. 

### `run`

 The scheduled clear, eight row passes, and level-cell write all execute the native
instruction tables. Only the row cursors are reset at the pass boundaries. 
