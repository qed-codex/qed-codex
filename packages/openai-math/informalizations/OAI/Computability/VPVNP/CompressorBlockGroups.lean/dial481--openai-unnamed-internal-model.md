---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockGroups.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockGroups.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockGroups.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Windows for source runs in the online descriptor script

Each native source trace occupies a contiguous range in the fixed block.
The windows identify the worker for each visit and its ordinal among all
the heterogeneous substeps. They can be applied to the source packets
without numbering the repeated instances of the same instruction table by hand.


### `parts`

 The twelve consecutive visit groups of shrinking step `i`, in their order in the compiled
block. 

### `refreshParts`

 The seven consecutive groups of the degree refresh, from header publication through the
successor pointer. 

### `within`

 Restrict a script window to its indexed subgroup, moving earlier and later groups into the
surrounding prefix and suffix. 

### `shrinkWindow`

 The window occupied by shrinking step `i` in the complete block script. 

### `refreshWindow`

 The terminal window of a block, containing the refresh after all shrinking steps. 

### `shrink`

 Locate one of the twelve visit groups of a shrinking step in the global script. 

### `refresh`

 Locate one of the seven visit groups of the degree refresh in the global script. 
