---
{
  "module": "OAI/Computability/VPVNP/RAMTapeAddressLogValues.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeAddressLogValues.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeAddressLogValues.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scanning a value during an addressed load

Each saved query bit controls one iteration of the value scan. The loop
restores the query while saving the value for the later log rewind. On a
match, it also saves the result for delivery in its original bit order.


### `valueRuns`

 The matched branch uses five instructions per bit. A miss omits the
push to the result stack and uses four. The final empty test selects the
next record on a miss and starts the log rewind on a match. 
