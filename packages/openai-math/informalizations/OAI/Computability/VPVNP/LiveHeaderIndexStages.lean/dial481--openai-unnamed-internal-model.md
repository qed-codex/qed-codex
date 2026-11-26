---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderIndexStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderIndexStages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderIndexStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The initial index stage of the physical live-header program

The public row supplies the index array, its two summary cells and the scan
length. The actual distributed headers supply the one-based group number.
The closing call accepts and hands its memory to the advice stage.


### `indexTable`

 The burst table for copying one distributed group-index bit and updating its summary. 

### `indexWords`

 The index worker's three public addresses for the unpacked digits, highest set position,
and population count. 

### `index_step`

 Every successful index-cell call increments the cursor and leaves the
tag unchanged in its real external memory. 

### `index_stage_native`

 The concrete widened index component reads all occupied processor words,
accepts at its capacity, and installs the high bit, population and copied
digits with the prescribed call and probe bounds. 
