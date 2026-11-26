---
{
  "module": "OAI/Computability/VPVNP/PrimedScheduleRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedScheduleRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedScheduleRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Composing successive calls of the primed coefficient counter

Each item of the two input scans, the site parses, and the final comparisons
has a fixed absolute call number. The machine passes that number in its
persistent word. The only possible successful execution on prescribed header
memory therefore has exactly one list of choices per item, and carries the
actual external memory through all phases.


### `cursor`

 Encode the absolute call index as the persistent width-`w` word. 

### `control`

 A running call at item `i`, and the unique accepted state at the end. 

### `Item`

 Semantics of a scheduled counter call. Given its absolute index, incoming memory and choice
stream, it returns a report on success. 

### `runItems`

 Independent per-item semantics, with reports recording the actual reads
and writes. A supplied choice list after the last item is rejected. 

### `ScheduleSpec`

 What the opcode proof for each phase must establish. Invariants may depend
on the cursor and the memory, so this applies to the parse stack, leaf marks,
and cumulative histogram throughout the counter. 

### `native_eq_runItems`

 The actual reset-private-memory run computes the same reports as the
composition of the item semantics. 

### `runItems_progress`

 At a successful partial run the next cursor and the number of consumed
choice lists agree, so splitting a sequence into individual items is unique. 

### `runSegment_append`

 Reports of adjacent phases compose with exact transfer of persistent
state, external memory, and branch lists. 

### `Choices`

 One exact branch list per scheduled item, including a possibly empty
list for deterministic input scans or final comparisons. 

### `nativeScheduleEquiv`

 Native accepting paths of the assembled machine and the fixed-index
per-item choices count the same executions. 
