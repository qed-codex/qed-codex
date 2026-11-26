---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotMateFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotMateFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotMateFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External addresses of the three mate-table passes

The first pass inverts the base permutation. The other two expand that
matching to all lanes, once in each direction. On the reverse pass the
inverse table determines the index of the displacement read. Its entries
remain bounded by the base-port count after the forward expansion.


### `actual_scan_footprint`

 The lifted incidence pass reads the selected base-mate and displacement
columns. It writes one cell in its output column per actual port. 

### `mate_footprint`

 The three chronological native scans read within the five mate columns
and write only the inverse-base and two actual columns. The bounds include
the data-dependent displacement reads of the reverse scan. 
