---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortRowAddressUnary.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowAddressUnary.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowAddressUnary.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Converting the sorter’s high-bit-first row offset to a unary count 

### `Port`

 Stacks for high-bit-first binary input, the unary output and the scratch tally used while
doubling it. 

### `State`

 Control for reading the next bit, doubling the unary accumulator, restoring its marks and
adding the bit. 

### `code`

 Consume high-order bits first and update the unary offset by doubling and adding the
incoming bit. 

### `bank`

 Install the remaining binary input and unary encodings of the output and scratch counts. 

### `routine`

 Convert the possibly toggled row address to the unary count used to fetch its partner
record. 

### `runs`

 The accumulator doubles once per bit. Charging each old unary mark to a newly
created mark bounds the total number of stack steps linearly in the final offset. 
