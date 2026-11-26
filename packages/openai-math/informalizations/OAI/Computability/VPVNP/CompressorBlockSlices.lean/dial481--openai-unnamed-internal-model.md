---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockSlices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockSlices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockSlices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical AB intersections and selected-role subdivisions of a block

The AB stage pairs the thick sorted fields with the new AB widths in the
same bundle. The four selected-role stages recover the absolute motif ID,
read its chosen supply coordinate and write both the split width and the
singleton intersection record. The subsequent slot pass reads those
physical split widths.


### `abInputs`

 Address operands for intersecting the sorted old thick-wire intervals with the new AB
intervals in each bundle. 

### `intersections`

 The AB interval-intersection scans for the given shrinking step and its fixed thick-wire
and bundle capacities. 

### `subdivisionSum`

 Total subdivision count across the shrinking slot template. 

### `intervals`

 Address of the surviving-interval array following the four width columns for each slot
subdivision. 

### `survivingHeads`

 The physical motif, term, layout, width and interval operands used to compute the surviving
subdivisions. 

### `surviving`

 The native phases that read the selected terms and write the surviving subdivision widths
and intervals. 

### `visits`

 The shrinking slice visits in order, first AB intersections and then surviving-role
subdivisions. 
