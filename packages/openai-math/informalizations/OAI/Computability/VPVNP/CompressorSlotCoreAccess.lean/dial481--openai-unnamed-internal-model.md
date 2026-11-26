---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotCoreAccess.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotCoreAccess.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotCoreAccess.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Access bounds of the five sorted-slot workers on the selected branch

Recover the owner records, zero counters and sorted fields at their actual
phase boundaries. This gives the addresses of every emitted probe, including
the indirect row and inverse-field lookups.


### `readRegion`

 The physical inputs used by the branch and all intermediate slot arrays. 

### `writeRegion`

 Slot outputs including the small preparation tables. 

### `Space`

 Bounds used to allocate and instantiate the native shrinking workers. 

### `OrderedTables`

 The two-way rectangular slot order on this actual selected network. 

### `core_access`

 All five sorted-slot phases access the allocated data, and the exact
post-memory supplies the typed base matching for the subsequent mate scans. 
