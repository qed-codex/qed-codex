---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordShiftBorrow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordShiftBorrow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordShiftBorrow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Subtracting one from the binary shift amount

A leading zero in the little-endian amount creates a pending one on the
scratch stack. At the first set bit, the machine clears it and restores
the pending ones. Reaching the end signals zero and clears the scratch.


### `borrow_run`

 A positive binary shift amount decreases by one with its width preserved.
For a zero amount, the zero branch is reached with both amount and scratch empty. 
