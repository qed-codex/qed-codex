---
{
  "module": "OAI/Computability/VPVNP/CompressorOnlineRowInverse.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorOnlineRowInverse.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorOnlineRowInverse.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Recovering a physical descriptor row on an accepting run

The calendar, recipe, launcher, data worker and closing call are inverted on
the same choice stream. Only the worker uses private choice bits. Its local
invariant supplies the valid frame, live cursor, and private clock for every
successful call, including calls reached by arbitrary submitted tapes.


### `RowStart`

 All data needed to enter a source row in the current physical memory.
The invariant and its advancement rule concern one data call at a time. 

### `RowStart.phase`

 Calendar phase selected for the current row ordinal at entry to the inverse run. 

### `RowStart.worker`

 Catalog index of the data worker launched for this row. 

### `RowStart.fuel`

 Private fuel bound available to each data-worker call while recovering the row. 

### `RowStart.invariant`

 Predicate on the worker cursor and memory used to validate successive calls within the
  row. 

### `recover_row`

 Separate the complete first row and accepting remainder. The witness is
built from the supplied stream's actual reports, and its data execution is
validated at the row-specific private clock. 
