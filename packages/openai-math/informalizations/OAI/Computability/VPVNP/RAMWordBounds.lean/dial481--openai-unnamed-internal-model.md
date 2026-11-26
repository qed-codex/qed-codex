---
{
  "module": "OAI/Computability/VPVNP/RAMWordBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMWordBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMWordBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word bounds for burst RAM records

The address of a probe is already a word. Its starting cost and ordinal are
bounded by the total cost of the calls, including the one unit charged per
call. Initialization at site `a` uses `a` for both address and timestamp.
These bounds hold throughout every permutation of the padded input blocks.


### `RecordFitsWord`

 All three natural-valued fields of an occupied record fit in words. 

### `probeRecords_bounds`

 The start and ordinal of a chronological probe are jointly bounded by the
ending cost. This estimate holds even for the final call at the budget cap. 

### `perm_canonicalRecordBlocks_fitsWord`

 Every occupied slot still fits in words after any sorting-network permutation. 
