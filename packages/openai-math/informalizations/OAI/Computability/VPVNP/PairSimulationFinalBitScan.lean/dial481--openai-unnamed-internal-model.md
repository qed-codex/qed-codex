---
{
  "module": "OAI/Computability/VPVNP/PairSimulationFinalBitScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationFinalBitScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationFinalBitScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native histories of the terminal shared-bit worker

The terminal header gives the total number of bits and their base address.
The worker consumes singleton choices in descending physical order and then
consumes one empty closing call. Replaying its reports builds the same memory
image as the shared-wire reports used by the contraction formula.


### `Layout`

 The two header cells stay outside the address range written by the worker. 

### `Layout.ofBelow`

 The physical wire interval ends below the terminal header. 

### `reports`

 The reports contain the actual header reads, choices, writes, returned
ordinals and the accepting report of the last call. 

### `run_scan`

 Full native execution from the zero ordinal, including the closing call. 

### `image`

 Native reports replay to the original reverse-order wire image. 

### `accepted_iff`

 Acceptance itself forces every data choice, the number of calls and the
single empty closing call. The reports retain the full native probe history. 

### `acceptedEquiv`

 Shared-bit assignments enumerate exactly the accepted paths. The cap
predicate may include clock and external-probe bounds on the actual reports. 

### `controller_frame`

 All probes avoid the controller cells which hold the phase and the worker's
persistent state between calls. 

### `stage_cost`

 Each linked call costs four additional probes, including the handoff from
the accepting worker call to the vertex stage. 

### `stageRun`

 The shared-bit stage of the linked terminal program. Its physical reports
include the control reads and writes for each returned ordinal and the
handoff to the vertex worker after the closing call. 
