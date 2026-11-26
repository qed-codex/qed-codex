---
{
  "module": "OAI/Computability/VPVNP/MacaulayReadFinish.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayReadFinish.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayReadFinish.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Selecting a matrix entry and reclaiming its temporary buffers

Divisibility selects either the coefficient routine or the zero scalar. On a
powered row, equality selects an advised encoding of zero or one. The bit
selection preserves its full flag word. Both the exponent buffer and flag
are cleared before the next matrix read.


### `emit`

 Prepend the stored field encoding of zero or one to the reader's result stack according to
the given bit. 

### `erase`

 Clear the packed exponents and flag left by the selected monomial scan. 

### `finish`

 Read the scan flag, emit zero on a failed match or run the supplied coefficient routine on
a match, then clear the scan buffers. 

### `frame_bound`

 Bound every physical stack, including registers and the scalar result.
The supplied word bound also covers the immutable degree/ordinal descriptors. 

### `finish_bounded`

 Run the flag router and reclaim the two buffers. The clock of the long
scalar call is charged once, with its peak cap retained through the tag test. 
