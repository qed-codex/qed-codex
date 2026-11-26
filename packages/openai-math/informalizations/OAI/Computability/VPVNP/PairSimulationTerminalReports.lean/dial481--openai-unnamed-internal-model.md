---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalReports.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalReports.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalReports.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Observable terminal calls and their resource charges

A terminal worker is entered either at bootstrap or with a restored state.
The report keeps each source choice in order, charges at most four additional
probes and thirty additional events, and determines both header cells used by
the next call. The final successful exit leaves the source memory result.


### `Entry`

 A fresh terminal invocation or a resumed stage with its saved state. 

### `Entry.stage`

 Worker selected by this entry. 

### `Entry.state`

 Persistent word passed to the selected worker. 

### `Entry.marker`

 Persistent word received by the enclosing terminal program. 

### `Entry.prefixEvents`

 Physical events that enter the selected worker. 

### `Entry.Valid`

 The external stage and state cells encode a resumed entry. 

### `Entry.reads`

 Number of external reads used to enter this worker. 

### `Entry.follow`

 Next terminal entry after the worker's report. 

### `report`

 Complete physical report, including entry and exit events. 
