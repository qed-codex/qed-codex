---
{
  "module": "OAI/Computability/VPVNP/CompressionPowerHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionPowerHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionPowerHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local records throughout a repeated compressor block

The term chosen in each substep determines the network for the next substep.
Append the actual local records along this branch-dependent execution. The
fixed per-block bound on substeps then gives the exponential bounds on local
field lengths and occurrences in Theorem 7.1.


### `repeatRecords`

 Keep the records supplied by the same procedure on each branch. 

### `repeat_recordBounds`

 Bounds for every elementary record remain uniform. A repeated execution
contains at most `s*T` substeps on any branch. 

### `repeat_history_growth`

 Every local expansion has bounded occurrence count and peak field width
with one uniform constant `C^s` per whole block. 

### `repeatWithLanes_history_bounds`

 Every intermediate field width, individual map degree, and final wire width
obeys the same estimate. Enlarging the coefficient to at least two gives the
constant convention of Theorem 7.1. 
