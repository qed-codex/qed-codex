---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkResidentsPlan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkResidentsPlan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkResidentsPlan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native planner rows for the six-party resident directories

Build hidden and map owner columns, clear their counters, append the dense
ordinals, and publish the six absolute heads in level header cells 30–35.
The chosen layout is read from the score comparison's actual output cell.


### `size`

 Number of dense resident IDs for the chosen kind, four per motif for hidden residents and
six per motif for maps. 

### `owner`

 Planner expression for the start of the owner column. Hidden owners start at `first`, and
map owners start just after the hidden ID rows. 

### `counts`

 Planner address of the per-site counters, immediately after the owner column for this
resident kind. 

### `rows`

 Planner address of the resident ID rows, immediately after the count word for the last
packed site. 

### `endAddr`

 First address after the map ID rows, which end the workspace for the two resident
directories. 

### `bank`

 The six operand expressions for resident collection, giving the resident count, owner base,
site count, counter base, IDs per row, and ID row base. 

### `phases`

 The three visits for one resident kind write each ID’s packed owner using the chosen
layout, clear one counter per site, then append the IDs to their owners’ rows. 

### `heads`

 The six directory bases in publication order, with owner, count, and ID row bases for
hidden residents followed by the same three bases for maps. 

### `publications`

 Six visits that write the resident directory bases to offsets 30 through 35 of the old
level header. 

### `visits`

 The complete resident schedule builds the hidden directory, builds the map directory, then
publishes their six bases in the old level header. 

### `Ready`

 Only the site count, motif count and start of the allocated arena vary
across the linked levels. 
