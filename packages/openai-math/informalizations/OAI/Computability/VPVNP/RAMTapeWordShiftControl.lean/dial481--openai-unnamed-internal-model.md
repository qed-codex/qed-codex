---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordShiftControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordShiftControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordShiftControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite control for a bounded variable shift

The loop removes a bit from the data and tries to subtract one from the shift
amount. Each successful subtraction fills a vacated slot with zero. If the
amount is zero, the machine puts the current bit back and copies the remaining
data to the output. If the data runs out, it discards the unused amount.


### `Reg`

 Stacks for the remaining shift amount, data word, reversed temporary data, output and
scratch bits. 

### `State`

 Control for the bounded shift loop, decrementing the amount, inserting zeros, and reversing
data when implementing a left shift. 

### `code`

 Fixed control that discards at most one data bit per successful decrement and preserves the
word width by filling vacated positions with zeros. 

### `store`

 Place the five supplied lists on the shift amount, data, temporary, output and scratch
ports. 
