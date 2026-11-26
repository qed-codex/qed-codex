---
{
  "module": "OAI/Computability/VPVNP/CompressorPublishedHeadsRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPublishedHeadsRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPublishedHeadsRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native publication of consecutive DFS header words

Each published head executes one fixed six-instruction write and returns its
cursor at one. The following source packet evaluates its operands on the
memory left by that write. The frame and readback proofs ensure that each
value is the one computed from the original graph and its arena pointers.


### `report`

 Native six-event report for publishing one word at a specified address and returning cursor
one. 

### `image`

 Memory after the fixed ordered publication, expressed solely using the
original graph operands and the destination block. 

### `Outside`

 All addresses outside a contiguous field block retain their old words. 

### `Published`

 A complete contiguous publication supplies a chronological native source
walk, the fourteen/four/one-word readback and the frame of every other cell. 

### `run_fields`

 Specialize the consecutive destinations to fields of the old level
header. Its physical pitch survives every publication. 

### `Published.packets`

 The chronological packets have the exact execution, progress and source
footprints required by the online scheduler. 
