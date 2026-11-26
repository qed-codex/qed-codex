---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkOutputAllocation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkOutputAllocation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkOutputAllocation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Allocation of a selected shrinking pass

Place the surviving width rectangle beyond the current role table, term
rows and retained directories. Dense interval records follow that rectangle.
The slot constructor then uses fresh consecutive heads for roles, cyclic
successors, subdivision counts and the ordered-slot workspace.


### `motifCount`

 Number of motif descriptors in the shrinking output allocation, one per numbered piece of
each packed-site bundle. 

### `absoluteCount`

 Number of old arcs in absolute role-table order, used to size the four-word role records. 

### `widthBase`

 First address available for surviving width data, taken after the term rows, old-arc role
records and all retained directories. 

### `slotsBase`

 Start of the ordered-slot allocation after reserving the surviving width rectangle and the
per-motif interval records for every subdivision. 

### `heads`

 Place the role, next-site, subdivision and scratch tables for slot construction from the
given start, using the existing old-arc role records. 

### `slotHeads`

 Compute the slot-constructor table bases for this level after allocating its surviving
width and interval records. 

### `stop`

 Exclusive end of the shrinking output allocation, including the slot constructor's
workspace at this level. 

### `splitBank`

 Allocate the selected term's surviving widths and slice records using its actual
subdivision counts and the space after the retained data. 
