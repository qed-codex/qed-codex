---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshExpanderROM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshExpanderROM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshExpanderROM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initializing the fixed expander incidence table

The fixed expander supplies one finite schedule row per outgoing port and
local slot. Each row carries the port and local slot of its reverse edge as
public words. A native call writes the two columns read by the degree-refresh
slot writer. These public values depend only on the expander.


### `put`

 Public words are row ID, reverse port, reverse slot, port column base, and
slot column base. The call returns the successor row ID. 

### `events`

 The 11 events that publish an expander edge's destination port and reverse slot at its
fixed ordinal. 

### `words`

 Public schedule data for the edge with row-major ID `i`. 

### `report`

 The report of one fixed expander row, including its two writes and the next edge ordinal. 

### `runRows`

 Execute each hardwired row from the state and memory returned by the
previous call, collecting the actual reports. 

### `Regions`

 Both output regions fit, and their intervals are disjoint. 

### `Ready`

 The values in the two cells are the actual port and slot of the reverse
edge, at exactly the addresses used by the slot writer. 

### `initialize_expander`

 Initialize the fixed expander from arbitrary incoming memory. The finite
schedule makes one call with two writes per edge, preserving all addresses
outside the two reserved intervals. 
