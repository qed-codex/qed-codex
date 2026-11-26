---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterCall.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite table for a scheduled coefficient-counter call

All scheduled calls use the same structured body and reset their private
registers at entry. On success the body leaves the next cursor and the total
number of calls in two designated registers. A single comparison then either
accepts at the last item or returns the next cursor.


### `pc`

 Embed a label of the scheduled call body into the finite instruction table with its four
terminal opcodes. 

### `stop`

 Continuation that compares the next cursor with the total call count after a successful
body exit. 

### `bad`

 Instruction address for a failed guard or rejected call. 

### `back`

 Instruction that returns the next cursor as persistent state for the next scheduled call. 

### `accept`

 Halting instruction reached when the next cursor equals the total number of calls. 

### `template`

 Compilation introduces four terminal opcodes. Neither the input length
nor the number of calls determines the number of instruction labels. 

### `execute_stop`

 Any surplus branch bits after the last opcode reject, even if the
item itself would have succeeded on a shorter stream. 

### `execute_body`

 Exact native execution of a completed body, including the final cursor
comparison and halt/return and the exact-use check on the branch tape. 
