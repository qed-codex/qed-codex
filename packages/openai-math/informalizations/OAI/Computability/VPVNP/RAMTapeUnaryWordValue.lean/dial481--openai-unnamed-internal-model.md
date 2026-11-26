---
{
  "module": "OAI/Computability/VPVNP/RAMTapeUnaryWordValue.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeUnaryWordValue.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeUnaryWordValue.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary word increment for the unary input routine

Reading one unary mark adds one to a fixed-width little-endian word. The scan
keeps a single carry bit in finite control, including the carry out of the
highest bit. The input-length and unit words both fit the allocated width.


### `incScan`

 Add the incoming carry to a little-endian bit list and retain the overflow bit. 

### `incScan_value_of_lt`

 If the increment fits in the allocated word, the result retains its full value. 

### `width`

 Allocated word width for a program parameter `p` and unary input length `n`. 

### `inputWord`

 The encoded length fits even for a zero program parameter. 

### `unitWord`

 The word one is available for every input, including the empty input. 
