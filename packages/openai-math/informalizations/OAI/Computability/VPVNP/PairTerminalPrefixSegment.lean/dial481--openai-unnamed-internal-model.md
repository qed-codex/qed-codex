---
{
  "module": "OAI/Computability/VPVNP/PairTerminalPrefixSegment.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalPrefixSegment.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalPrefixSegment.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Execution of the live terminal-prefix pass

The width and start pointers and the arc count are reloaded from the terminal
header on each reset-entry call. The scan leaves them intact. When the cursor
reaches the stored count, the closing call writes the descriptor displacement
plus the accumulated bit width to the role-offset cell.


### `HeaderLayout`

 The header words used by the prefix stage fit in memory. The two arc arrays
are disjoint from these header words. 

### `probeRegion`

 The active width and start intervals and the live header words used by this
stage. This set bounds all external probes before any disjointness condition
on the controller's own cells is imposed. 

### `footprint`

 Read and write addresses of a report are both in the stage's data region. 

### `active_from`

 Run any remaining portion of the active scan. Its memory invariant is the
one for the three-operand width scan, although the eleven-operand table obtains
the pointer values through external probes on every call. 

### `run_active`

 The native scan returns the arc count as its persistent state. Its last
accumulator and its stored starts have their exact natural-number values. 

### `roleValue`

 The role-tag displacement published by the closing call. 

### `Run`

 Complete native execution, including the accepting call. The frame of the
stored prefix is relative to the initial memory with the role cell updated. 

### `run`

 All active arc visits and the accepting role-offset publication form a
single reset-entry run, including for a final network with no arcs. 

### `Run.unique`

 The terminating stage admits precisely its canonical sequence of empty
choice streams, with the same reports on every accepting execution. 

### `Run.charge`

 Total charged work counts one unit for starting each call in addition to
its external probes. 

### `Run.controller_frame`

 Every read and write in the entire completed segment avoids the linked
controller's phase cell and saved-state cell. 

### `Run.role_val`

 With room for the descriptor words and final bits together, the published
word is their ordinary natural-number sum. 
