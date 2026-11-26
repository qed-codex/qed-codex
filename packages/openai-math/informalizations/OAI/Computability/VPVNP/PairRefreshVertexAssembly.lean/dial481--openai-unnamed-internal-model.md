---
{
  "module": "OAI/Computability/VPVNP/PairRefreshVertexAssembly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshVertexAssembly.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshVertexAssembly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The refresh role's complete vertex image

The level locator runs first, using the fourteen registers retained by the
refresh body. The handoff and child scan then fill the private child argument
buffer. The remainder of the body reuses the saved locator values and returns
to the DFS continuation.


### `childBody`

 The refresh child-argument preparation and its continuation into the resident kernel body. 

### `locatorBank`

 The locator register bank as embedded in the complete refresh vertex segment. 

### `segment`

 One role entry for the locator, argument scan and the kernel body. 

### `levelPC`

 Program counters of the level-location phase preceding child preparation. 

### `childPC`

 Program counters in the combined child-preparation and resident-body segment following the
level scan. 

### `bodyPC`

 Program counters of the resident refresh body after the child argument has been installed. 

### `bodyRegs`

 Embedding of the resident refresh body's private registers inside the child-preparation
segment. 

### `levelRegs`

 The level locator's registers transported through the resident body's embedding. 

### `Installed`

 Agreement of the installed refresh vertex instructions with the width-resized assembly at
each placed address. 

### `locate`

 Locate the actual noninitial node before reading its children. The locator
writes only its assigned registers and reaches the first handoff instruction. 
