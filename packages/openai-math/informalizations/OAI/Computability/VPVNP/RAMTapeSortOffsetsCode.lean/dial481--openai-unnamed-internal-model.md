---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortOffsetsCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortOffsetsCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortOffsetsCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed stack controls for a physical sorting row counter

The width arrives on a unary stack. Initialization builds a zero word of
that width and restores the width tally. Each advance adds one to the binary
and unary counters. The outgoing carry records when the traversal has reached
the last row, including the one-row case at width zero.


### `Port`

 Stacks for the unary row width, binary row index, unary row index, temporary bits and
continuation flag. 

### `Phase`

 Control for initializing the binary index from the width, advancing binary and unary row
counts, and recording overflow at the final row. 

### `code`

 Build a width-sized zero index and execute a carry-propagating row increment while
maintaining its unary copy. 

### `store`

 Install the width, binary index, unary index, scratch and continuation bit lists on the
row-counter ports. 

### `ones`

 Unary encoding of a natural number as that many true bits. 

### `initialize_run`

 Initialize from the supplied width. 

### `advance_run`

 Advance both counters and set the continuation flag from the binary carry out. 

### `clear_run`

 Clear both counters after the final row. 
