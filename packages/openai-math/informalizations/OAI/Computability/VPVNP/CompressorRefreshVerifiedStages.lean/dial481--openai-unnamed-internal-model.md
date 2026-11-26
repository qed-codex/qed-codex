---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshVerifiedStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshVerifiedStages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshVerifiedStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cursor and address checks for the complete native refresh schedule

The certified walk follows the actual selected term tape through the external
scans, demands, term row, supplies, fixed expander, slot scans and final base rows.
Old columns supply the first two scans. Every remaining access stays inside the
packed level. The resulting checks can be attached to the global online calendar.


### `StageBounds`

 The reports span the selected stage's cursor interval, read only at or above the lower
address bound and write only within the refresh allocation. 

### `verified_sources`

 All raw stages of the selected physical execution, together with their
scheduler guards and concrete data read/write bounds. 
