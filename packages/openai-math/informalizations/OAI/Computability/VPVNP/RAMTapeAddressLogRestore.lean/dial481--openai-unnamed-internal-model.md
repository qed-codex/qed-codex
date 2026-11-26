---
{
  "module": "OAI/Computability/VPVNP/RAMTapeAddressLogRestore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeAddressLogRestore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeAddressLogRestore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rewinding the private write log

A load returns the visited key bits, value bits, and occupancy markers to
three independent streams. The final pass transfers the saved result onto
the output stack. Each stream requires one empty test and two steps per bit.


### `restoreRuns`

 The four final rewind passes restore the log and deliver the read result. 
