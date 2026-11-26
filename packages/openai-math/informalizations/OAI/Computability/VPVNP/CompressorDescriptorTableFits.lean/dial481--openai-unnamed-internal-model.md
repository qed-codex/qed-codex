---
{
  "module": "OAI/Computability/VPVNP/CompressorDescriptorTableFits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDescriptorTableFits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDescriptorTableFits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packed suballocations of the descriptor tables

Fixed fields per initial position suffice for all the subarrays of one degree refresh.
The bound includes all segment scratch columns, demands, strided terms, supplies,
expander ROM columns and the six output incidence columns.


### `tableFits`

 Any packed suballocation with a fixed linear bound on its length fits this table. 

### `tableStop_lt`

 The exclusive end of a packed suballocation is representable as a word. 

### `refresh_plan_bound`

 Exact allocation bound per current site of an elementary degree refresh. 

### `refresh_table_room`

 At a chosen refresh table base, the entire realized pass remains in that level,
and its exclusive end is a word. 

### `prefix_bounds`

 The terminal prefix table starts after the final width column, and its final
prefix entry precedes the high header containing the cumulative total word. 
