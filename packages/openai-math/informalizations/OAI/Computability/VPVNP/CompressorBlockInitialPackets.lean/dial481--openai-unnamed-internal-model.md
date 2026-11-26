---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockInitialPackets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockInitialPackets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockInitialPackets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The four chronological source visits at level zero

The scalar publisher, array-head publisher, cursor scan and role store run
in order. The source trace certifies each visit's stop test and memory
footprint, and leaves the initial cursor incidence and persistent metadata
available even when the block count is zero.


### `order`

 The four level-zero visits in execution order, ending with the store of the cursor role. 

### `headLogs`

 The initial scalar report and the following pointer report evaluated in its post-memory. 

### `cursorLogs`

 The cursor scan reports that populate the six incidence columns beginning at level zero's
incidence base. 

### `logs`

 The full level-zero report sequence for header publication, the cursor scan and the final
role store. 

### `post`

 External memory after all four level-zero source visits. 

### `clock`

 A fixed native clock bound for every source call in this prefix. 

### `Source`

 A source visit runs on the supplied operands and branch tapes within the initial packet
clock, producing the given reports. 

### `quiet`

 Every data call in the initial segment consumes the empty choice string. 
