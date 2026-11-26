---
{
  "module": "OAI/Computability/VPVNP/RAMTapeChargesValue.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeChargesValue.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeChargesValue.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Single-unit arithmetic for binary charge counters

A charge subtracts one from the remaining global budget and adds one to
the cumulative cost. The carry or borrow beyond the high bit detects every
overflow or underflow, including in a zero-width counter.


### `nextCarry`

 Propagate a carry through a set bit when incrementing, or a borrow through a zero bit when
decrementing. 

### `adjust`

 Ripple one incoming unit up or down across the little-endian bits. 

### `prevWord`

 The predecessor cost word. At zero the borrow flag rejects the charge. 
