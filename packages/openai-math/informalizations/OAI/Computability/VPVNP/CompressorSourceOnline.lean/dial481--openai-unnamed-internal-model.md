---
{
  "module": "OAI/Computability/VPVNP/CompressorSourceOnline.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceOnline.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceOnline.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Lifting a physical source scan into the online block program

A visit identifies an occurrence of an actual finite worker, its operand
bank, initial and final cursors, and the complete branch tape. The launch
certificate reads those operands from the online recipe. The source trace
then replays on the prepared RAM. The scheduler's ordinal advances once
and the shared data for the next worker agrees with the raw source memory.


### `Visit`

 Values supplied to one occurrence of the script's actual worker. 

### `Visit.phase`

 Catalog occurrence identifying the worker used by this visit. 

### `Visit.fuel`

 Private instruction cap for each worker call in this visit. 

### `Visit.start`

 Initial persistent cursor passed to the worker. 

### `Visit.stop`

 Cursor value marking the end of the scheduled visit. 

### `Visit.params`

 Public operand words for the selected catalog worker. 

### `Visit.choices`

 Sequence of branch tapes, one per call of this worker. 

### `Runs`

 Running the selected worker with the visit's operands, cursor, fuel, and tapes yields
exactly the supplied reports. 

### `row`

 Directory row for replaying this visit, using the recipe input computed from the given
ports and memory. 

### `Launch`

 The live memory values after the calendar, recipe and launcher calls. 

### `Progress`

 Cursor guard facts, independent of the control memory inserted by the
dispatcher. Some scanners advance by a record stride or start at a nonzero
cursor. 

### `packet`

 Replay one genuine source packet into the live script, producing the
actual online step and the data and ordinal needed by the next packet. 
