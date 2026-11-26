---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshStageFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshStageFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshStageFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Guarded deterministic compressor scans

The source call at ordinal `j` emits a concrete list of events and returns
`j+1`. Bounds on the read and write addresses of those events preserve the
scheduler's frame and control words throughout the scan. The resulting
trace can be replayed after the scheduler changes its own cells.


### `Scanned`

 The exact returned cursor in each source report, including the terminal ordinal. 

### `scan`

 Establish ordinal order, terminal invariant and all accessed addresses before the
scheduler installs any worker frame. 

### `Scanned.guarded`

 Ordinal order and write separation validate a guard in any prepared replay memory. 

### `validScan`

 Prove guard validity and the footprint of the same genuine deterministic
source run. The source-specific invariant may track partial descriptor data. 
