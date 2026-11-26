---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshDemandScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshDemandScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshDemandScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dense demand vectors for the degree-refresh term reader

For each ordered tie, one native pass visits the old base vertex and residual
lane of every block. The selected segment column supplies the outgoing or
incoming width at that tie's local half-slot. The resulting contiguous array
is the input used by the motif term verifier.


### `Params`

 Eight public words that specify a tie's ports, the block dimensions, the selected width
column, and the dense demand destination. 

### `visit`

 Public words are the residual lane count, port count, target port, source
port, tie count, tie index, selected width-column base and dense output base. 

### `inputAddr`

 Address of the selected segment width for the block and ordered tie being scanned. 

### `outputAddr`

 Address of one demand entry, indexed first by block ordinal and then by tie ordinal. 

### `events`

 The 25 events that read a selected width and write it into the block's dense demand vector. 

### `Runs`

 The actual lists of native calls, in tie order and then block order. 

### `src`

 Source width address for one tie pass and one finite block index. 

### `dst`

 Destination demand address for the same tie pass and block index. 

### `Layout`

 Source widths avoid every demand write, and the destination address determines the tie and
block uniquely. 

### `Saved`

 Completed cells for the passes preceding the current tie and the visited
block prefix of the current tie. Outside this set the initial memory is intact. 

### `scan_run`

 One tie's scan, retaining all earlier writes and every unvisited cell. 

### `scans`

 All tie scans share the same memory and source tables. 

### `words`

 One public table for each fixed role of the motif. 

### `blocks`

 Enumerate blocks by old base vertex and residual lane, with the residual lane varying
fastest. 

### `Apart`

 The source columns are disjoint from the dense output interval. 

### `read_demand`

 Recover the exact tie width from the completed external segment pass. At an
incoming half-slot, its own destination identifier is the incoming-width key. 

### `rowBase`

 Base address handed to the term verifier for this block. 

### `demand_table`

 Execute all fixed tie scans from the terminal segment directory. The
motif verifier reads exactly the graph's demand function at each row base.
The cost is three calls-plus-probes per pair of a block and a tie. 
