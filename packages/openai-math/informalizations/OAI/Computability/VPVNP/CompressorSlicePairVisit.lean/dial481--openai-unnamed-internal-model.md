---
{
  "module": "OAI/Computability/VPVNP/CompressorSlicePairVisit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlicePairVisit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlicePairVisit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Indexed RAM visits for the interval scan

The persistent word enumerates the Cartesian product in source-major order.
One call reads both fields from the external start and width arrays. It stores
the two offsets and length of a nonempty copy in the pair's three-word slot.
For an empty copy it writes zero in the length cell, even when the slot
initially contains arbitrary words.


### `table`

 Public words contain the new field count, four array bases in source/target
and start/width order, and the base of the three-word output slots. 

### `oldIndex`

 Source field of a pair ordinal, obtained by division by the number of target fields. 

### `newIndex`

 Target field of a pair ordinal, obtained by reduction modulo the number of target fields. 

### `base`

 First word of the slot assigned to this ordered pair. 

### `slice`

 Compute the interval copy for the selected pair using both start and width arrays in
memory. 

### `report`

 Full trace of an indexed visit, including the four array reads. 

### `visit_native`

 A reset call computes the interval intersection and returns the next
pair identifier. The two endpoint bounds suffice for correct word arithmetic. 
