---
{
  "module": "OAI/Computability/VPVNP/RAMTapeRecordBuffer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeRecordBuffer.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeRecordBuffer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relating the emitted tape records to the site's initial sorting array

One invocation of the record callback extends the accumulated prefix by the
canonical bits of the staged record. Closing an admitted prefix adds just the
vacant physical slots. Its decoded wire array is the `localRecords` input to
the distributed validator, including the initialization record at sites with
no calls.


### `Holds`

 Between emissions all output bits are on the reverse buffer, and every
free slot is represented by one true mark. 

### `Holds.emit`

 Constructing a single probe or initialization record does not change
the caller's five word registers. It extends the physical array once. 

### `slots`

 The remaining indices return the unique empty slot. 

### `slots_eq_localRecords`

 Widening the emitted slots, in order, recovers the complete typed input
to the actual Batcher sorting replay. 
