---
{
  "module": "OAI/Computability/VPVNP/RAMTapeBoundaryRecord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeBoundaryRecord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeBoundaryRecord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scanning the five fields of a boundary record

The same field subroutine serves both the adjacent-row check and the outgoing
edge check. After the fifth return the saved stack contains the whole current
record in reverse order, ready for restoration as the next predecessor.


### `recordView`

 In row mode the right stream is the remaining block. In edge mode it is
the outgoing message. The other stream is left untouched by the field pass. 

### `record_run`

 A whole record takes five field scans, including one continuation jump
per field. The last continuation chooses the check for the active mode. 
