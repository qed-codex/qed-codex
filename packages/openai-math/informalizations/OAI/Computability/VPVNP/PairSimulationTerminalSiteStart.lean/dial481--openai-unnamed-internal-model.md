---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalSiteStart.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalSiteStart.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalSiteStart.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The final-site ordinal guard and DFS entry

The persistent word selects a final vertex. Its row address and the endpoint
array heads are read from the header in the pair workspace. The private
stack is initialized with just that vertex's descriptor before entering the
geometry initializer. The flush continuation returns the next ordinal.


### `pre`

 Form the pair-workspace header, then fetch the final vertex count. 

### `boot`

 Fetch the endpoint array heads, form the root row, and store its address
as the only pending DFS visit. 

### `Stage`

 Instruction labels for the site ordinal guard, initialization of its DFS root and the flush
continuation that returns the next ordinal. 

### `entry`

 First instruction of the site guard, where the bootstrap begins preparing the header and
ordinal comparison. 

### `target`

 Resolves the next position in a straight-line block to its instruction label, using the
supplied continuation at the position just past the block. 

### `instruction`

 Relocate the site entry and the flush continuation into the finite vertex table. 

### `Linked`

 Requires all bootstrap and flush instructions to be installed at their stage labels with
the specified registers, public ports and geometry entry. 

### `Stage.bootstrap`

 Classifies guard and initialization labels as bootstrap rows and the four ordinal-return
instructions as flush rows, allowing each part to be linked separately. 

### `StartLinked`

 Only entry and guard rows are required before transferring to the geometry code. 

### `FinishLinked`

 The flush continuation uses exactly its four designated labels. 

### `headerWord`

 The numerical header address before interpreting its words. 

### `headerWord_eq`

 On well-sized words the computed header is the address allocated by the terminal calendar. 

### `fieldTrace`

 Header-relative physical read and the preceding address instructions. 

### `guardTrace`

 Trace before the site ordinal comparison, with ten setup ticks followed by address
calculation and the external read of the final site count at header offset seven. 

### `bootTrace`

 Trace for an active site's DFS initialization. Eight header field reads supply the root and
layout data, followed by five ticks that compute the root address and push it onto the
private stack. 

### `GuardReady`

 Bank before branching on the ordinal. 

### `BootReady`

 The local bank passed to the private geometry initializer. 
