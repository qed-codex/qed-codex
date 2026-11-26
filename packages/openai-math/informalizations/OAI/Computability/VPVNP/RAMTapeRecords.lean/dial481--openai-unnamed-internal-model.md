---
{
  "module": "OAI/Computability/VPVNP/RAMTapeRecords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeRecords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeRecords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed control for emitting a whole five-word RAM probe record

The call interpreter stages the tag, address, value, call start and probe
ordinal in five word stacks. Each emission takes one free slot, copies all
five words in order, and restores the caller's registers. The empty and
malformed remaining-slot counters reject without continuing.


### `appendRecord`

 The one-record callback. The tag selects initialization, read or write
and all fields already occupy the paper's fixed word width. 

### `emitted`

 Bank after record emission, with the new free-slot tally and the reversed record encoding
prepended to the buffer. 

### `appendRecord_run`

 Staging canonical record words in the five registers produces precisely
the bits of the paper's physical slot, with no fresh choices. 
