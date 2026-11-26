---
{
  "module": "OAI/Computability/VPVNP/RAMValidatorBoundaryWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorBoundaryWord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorBoundaryWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word tests for the boundary records of a RAM transcript

A read uses the preceding slot's value exactly when that slot is occupied and has
its address. At a successor edge the sender also compares the entire transmitted
slot with its final slot. Both word programs respect the parser on all input tuples.


### `Slot`

 A transcript slot after decoding, either empty or holding a word-valued RAM record. 

### `RawSlot`

 Five machine words making up a physical slot before occupancy and record fields are
decoded. 

### `readOK`

 Check the value of an occupied read against the preceding physical slot. 

### `equalSlot`

 Compare two physical slots, including the timestamp and ordinal of a probe. 

### `readRaw`

 Execute the predecessor test on two arbitrary five-word tuples. 

### `equalRaw`

 Execute whole-slot equality on two arbitrary five-word tuples. 
