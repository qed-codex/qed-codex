---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockLevelFit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockLevelFit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockLevelFit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical endpoints of selected shrink and refresh substeps

The static table dimensions of the block program fit the actual graph
at any level having at most the initially reserved number of positions.
Each exclusive endpoint stays within its named table, before the next
level and strictly below the machine word modulus.


### `tableStart`

 Natural address of the first word of table `j` in the given level's fixed-stride array
bank. 

### `Endpoint`

 Bounds placing an exclusive suballocation end inside its table, before the next level and
below the word modulus. 

### `shrink`

 All seven packed arenas and both resident placements use the native
indices of the actual shrink calendar. Table zero also admits the contiguous
output and resident variants. 

### `refresh`

 Table zero holds the complete refresh scratch, term, supply and output
incidence plan. Table four holds the three physical placement columns. 
