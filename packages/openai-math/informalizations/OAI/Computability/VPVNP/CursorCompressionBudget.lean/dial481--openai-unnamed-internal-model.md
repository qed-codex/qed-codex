---
{
  "module": "OAI/Computability/VPVNP/CursorCompressionBudget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorCompressionBudget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorCompressionBudget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Communication of the routed cursor network after compression

This specialization uses the actual numbers of sites, cursor positions, and
reserved routing bits in Sections 11 and 12. Its remaining inputs concern
an admitted compressor path and the external operations performed on it.


### `cursorPairSimulation_budget`

 Equations (12.1) and the external budget of Proposition 13.1 for the prescribed
cursor network. Its position and width bounds are supplied by the routing construction. 

### `cursorResource_bounds`

 Fixing the address exponent after the number of lanes per block provides
the lanes, the local field bound, and enough counter bits at the same lengths. 
