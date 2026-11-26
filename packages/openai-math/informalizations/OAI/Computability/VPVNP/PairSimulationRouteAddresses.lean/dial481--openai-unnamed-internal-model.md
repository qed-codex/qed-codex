---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRouteAddresses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteAddresses.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteAddresses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selecting the three resident field addresses at a cursor vertex

The two mask bits select the outgoing and incoming sides independently.
The same running offset locates the system's field in all four local buffers.


### `Reg`

 Input flags, buffer bases and field offset, together with the three output addresses. 

### `instruction`

 Each outgoing branch adds the offset to both starts. The incoming
branch adds it to the selected incoming start. 

### `Linked`

 The machine contains the eight address-selection rows at their assigned labels. 

### `Ready`

 The outgoing and incoming side bits and the four local buffer bases at entry. 

### `Result`

 The selected field starts, return label and state preserved for the field scan. 

### `native`

 Exactly five native local steps select the three absolute addresses. 
