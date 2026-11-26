---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A cursor-controlled burst RAM for the two primed input passes

Each public cursor dispatches one skip, choice-and-write, literal write, or read-and-write.
Private control is re-created at the beginning of each call. The external memory is read
only by a `read` instruction. Cursor `M` is an explicit halt, so the `M` data calls can
also be used as a prefix returning the terminal cursor for the subsequent grammar parse.


### `Item`

 One input-pass action. It skips a position, stores a chosen bit at an address, or copies a
literal or fetched word to its destination. 

### `Item.owns`

 Test whether this schedule item consumes a nondeterministic bit choice. 

### `Item.bits`

 The exact choice stream for one item, a singleton for a choice and empty for a skip or
copy. 

### `Item.report`

 Events and successor cursor for the scheduled action on the supplied memory and choice bit. 

### `Item.memory`

 External memory after a skip, a write of an encoded choice bit, or a copy from the
indicated source. 

### `cursor`

 Represent a schedule position up to and including the terminal position as a word, using
the bound on the entire schedule. 

### `successor`

 Cursor returned after executing the item at index `i`, representing position `i + 1`. 

### `Dispatch`

 Control states of the scheduled input machine for visiting an item, writing its word,
returning the next cursor, halting or rejecting an invalid cursor. 

### `scheduledProgram`

 Execute one schedule item per burst call, branch at each bit choice, and halt when the
persistent cursor reaches the item count. 

### `haltReport`

 Terminal schedule report with an empty trace and no successor cursor. 

### `scheduledReports`

 Reports of a schedule on the designated branch bits, evaluating each fetch against
memory after the preceding call. The final halt is separate. 

### `execute_item_only`

 A successful data call consumes one bit precisely at a choice instruction. 
