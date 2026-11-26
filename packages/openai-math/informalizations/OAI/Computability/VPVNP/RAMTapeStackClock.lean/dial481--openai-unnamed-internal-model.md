---
{
  "module": "OAI/Computability/VPVNP/RAMTapeStackClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeStackClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeStackClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Path counts and clock of the physical stack interpreter

At most one packed cell is added by each stack instruction. Seeking and
restoring any stack costs at most six transitions per preceding cell, plus
four for dispatch and the operation itself. Every virtual choice is a
single literal two-record row.


### `physical`

 Accepting path count on the packed primary tape and initially empty scratch tape. 

### `physical_eq`

 All virtual leaves have been reached by the indicated physical clock.
This compares the actual integer path counts, with repeated targets counted
once per incoming branch slot. 
