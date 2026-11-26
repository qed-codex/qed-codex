---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshDeterminism.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshDeterminism.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshDeterminism.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniqueness of a native degree-refresh execution

The initial memory and the selected branch tapes determine all reports. The two
ordered scans run a deterministic table at each tie or slot and thread its memory
into the next table. Thus splitting a full execution into native phases does not
introduce additional computational paths.


### `DemandScan.Runs.deterministic`

 A fixed sequence of demand scans has one report list. 

### `AllSlots.Runs.deterministic`

 A fixed sequence of local-slot scans has one report list. 

### `PrepareRun.deterministic`

 The gather, directory, external segment and demand tables determine both the
reports and the final memory of the preparation phase. 

### `Finish.Run.deterministic`

 The selected-width table, expander ROM, actual-slot scans and lane-zero table
determine the terminal report list of the selected state. 

### `Build.Run.deterministic`

 A fixed branch choice and initial incidence memory admit at most one complete
list of native refresh reports, for any capacity and packed preparation layout. 
