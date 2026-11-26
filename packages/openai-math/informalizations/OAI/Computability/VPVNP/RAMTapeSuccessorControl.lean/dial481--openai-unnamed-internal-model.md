---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The fixed stack control for checking a parsed successor field

The control reads each of the eight little-endian words, retaining its
small tag. It compares the cost and the cap bit by bit. All input words
are restored. The two output stacks receive the running-state flag and
the format validity flag, respectively.


### `CheckPort`

 Stacks for the eight parsed words, cap comparison, running-state bit, and field verdict. 

### `CheckState`

 Phases for scanning successor tags, comparing the cost with the cap, and emitting the
running and validity bits. 

### `capPorts`

 Wire the cap comparator to successor word one, the public cap, and their two scratch
stacks. 

### `checkCode`

 Scan the eight word tags, compare cost against the cap, and push the running bit and field
validity bit. 

### `checkResult`

 Push the supplied running bit and verdict onto their respective stacks, preserving the rest
of the bank. 

### `checkRoutine`

 Install the successor checker on the caller's ports for a present field or an absent-edge
clamp. 
