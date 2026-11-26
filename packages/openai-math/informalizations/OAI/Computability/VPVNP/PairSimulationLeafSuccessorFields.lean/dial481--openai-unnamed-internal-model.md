---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafSuccessorFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSuccessorFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSuccessorFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing both successor fields in the native leaf loader

The machine copies the outgoing bits first, then the incoming bits, using a
descending destination cursor. Nonwrapping edges select their own low-bit
mask class. A missing edge contributes a whole zero field.


### `selectionTicks`

 Instruction count for selecting one incoming or outgoing successor field, including
endpoint tests and any class calculation. 

### `Result`

 The field copy reaches its exit with the private cursor at the lower address and the
selected bits placed there, preserving persistent state and registers outside the writable
slots. 

### `field_run`

 Select and move one entire successor field, restoring every architectural
input needed for the following direction. 

### `ticks`

 Total instructions for selecting and copying the outgoing and incoming successor fields,
each of length eight times the word width. 

### `pair_run`

 The complete pair of physical fields is placed at the destination in
the send-then-receive logical order, including both nonwrapping endpoints. 
