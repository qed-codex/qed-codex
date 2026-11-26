---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortReplaySlot.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortReplaySlot.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortReplaySlot.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The decoded value and validity of an addressed sorting record

The physical comparator works on five arbitrary words, while the word-work
replay uses the checked bit decoder. Re-encoding the parsed slot characterizes
precisely when that decoder returns a record, including the all-zero empty slot.


### `Canonical`

 Parsing a raw five-word slot and re-encoding it reproduces every word, including the
all-zero encoding of an empty slot. 

### `fieldWords`

 The raw five words at the exact bit address used by the checked RAM scan. 

### `orientation`

 The integer address comparison and phase-direction test in the checked
replay give the same bit as the finite row-address routine. 
