---
{
  "module": "OAI/Computability/VPVNP/RAMTapeBoundaryEnds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeBoundaryEnds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeBoundaryEnds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Restoring a record and checking zero boundary messages

The incoming edge check saves each inspected bit so that the usual restore
loop reconstructs the predecessor. The outgoing edge check consumes its
message. Each check accumulates the zero test in a single control bit.


### `restoreSlot_runs`

 Return the saved slot to the predecessor stack, reversing the order in
which its bits were pushed during the scan. 

### `checkPrev_runs`

 Check an incoming boundary message and save the inspected bits. 

### `checkSent_runs`

 Check an outgoing boundary message and consume its bit stream. 
