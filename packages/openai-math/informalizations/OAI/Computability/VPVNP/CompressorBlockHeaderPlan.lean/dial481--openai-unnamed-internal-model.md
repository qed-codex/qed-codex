---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockHeaderPlan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockHeaderPlan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockHeaderPlan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initial and per-substep header visits

The initial cursor frame occupies scalar offsets six through thirteen.
Every level starts with a scalar visit and an array-head visit. At block
boundaries the next level is published with terminal metadata. Starting
another block relabels the same header in place, so a last block can end
with no residual lanes.


### `firstHeader`

 The address gap from the active frame to the directory is two plus the
catalog arity. Reading the runtime row count therefore locates level zero
without a literal for the arity of the program currently being constructed. 

### `persistentFrame`

 Address expression for the persistent cursor frame, beginning six words into the first
level header. 

### `formula`

 A single visit evaluating the supplied formula row at its source cursor and writing to the
destination operand. 

### `initialScalars`

 A single deterministic visit sets the six input scalars of the first level. 

### `heads`

 A single visit publishing the current level's array pointers from the current and initial
level headers. 

### `initial`

 The startup sequence that publishes initial scalar dimensions, publishes array heads and
scans the persistent cursor frame. 

### `update`

 The source and destination may agree on the first visit of a block. The
formula row reads all six scalars before it begins the contiguous writes. 

### `substep`

 Start a fixed substep by installing its input metadata, then publish
terminal metadata and the incidence/record heads of the next level. 
