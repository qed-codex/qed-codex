---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkHistoryAccess.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkHistoryAccess.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkHistoryAccess.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # External read and write addresses of the selected shrinking rows 

### `placement_access`

 The placement report group reads only the old color, offset, mate and
displacement addresses, and writes only the four new columns. 

### `role_access`

 Even the indirect role lookups refer to the addresses determined by the
original incidence columns at the start of this phase. 

### `inputFloor`

 Lowest address among the old color, offset, mate and displacement columns supplied to the
shrinking pass. 

### `selected_access`

 Every event of the chronological placement and role scans lies in
its physical source or output interval. These estimates hold after selecting
either layout. 
