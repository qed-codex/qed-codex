---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortReplayInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortReplayInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortReplayInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Initial physical records of the sorting replay

A completed local transcript contributes its initialization and probe records
in their original order. The emitter then fills every remaining slot with
the canonical empty record. Its output bytes are exactly the input block for
the finite layer traversal.


### `emittedBlock`

 Initial five-word records at all row indices of a site, including empty slots. 

### `close_emittedBlock`

 The exact physical output of the record-emission routine supplies the
initial block of the finite sort without any data conversion. 

### `decoded_emittedBlock`

 When the records came from this site's report stream, their checked
parse is the typed validator's local input array. 
