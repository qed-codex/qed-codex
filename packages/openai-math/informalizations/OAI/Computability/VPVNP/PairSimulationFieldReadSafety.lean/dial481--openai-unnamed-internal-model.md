---
{
  "module": "OAI/Computability/VPVNP/PairSimulationFieldReadSafety.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationFieldReadSafety.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationFieldReadSafety.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Field traces below the terminal header

External reads confined below the allocated terminal header exclude its stage and
saved-state cells. The two slice formats locate their length and offsets at different
addresses.


### `TerminalLink.workerCell_of_lt`

 All addresses below a fitting terminal header avoid the stage cell and saved word. 

### `TerminalLink.expr_worker_reads`

 Register formulas whose loads all precede the terminal header read worker cells. 

### `PrivateSlices.frameEvents_worker_reads`

 A natural frame head and its two successors all lie below the terminal header. 

### `PrivateSlices.ab_frame_before`

 Source-major indexing puts the three cells of any AB frame strictly inside
the allocated interval bank for its bundle. 

### `PrivateSlices.surviving_frame_before`

 The surviving row holds one frame per subdivision, preceding its directory
references in the same allocated bank. 

### `RefreshSliceClock.segmentEvents_reads_iff`

 The two reads of a refresh segment use the selected width and offset column heads
at its physical ordinal. 

### `RefreshSliceClock.segmentEvents_worker_reads`

 All segments in two allocated refresh columns precede the terminal controls.
The bound uses the ordinal within the columns, including at their last cell. 
