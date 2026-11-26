---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAMLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scratch addresses for preorder parsing

One row of the input rectangle belongs to each site in each of the two
groups. After these rows are two planes for pending stack frames, one mark
per position, one word per production, and one word for the stack depth.


### `Cell`

 Separate logical locations in the physical scratch interval. 

### `size`

 Number of words in the parser scratch interval, comprising two groups of input rows, two
stack planes, position marks, production counters, and the stack depth. 

### `cellOffset`

 Row-major address of every typed cell, contiguous across the six regions. 

### `address`

 External word address of a typed parser cell, obtained by adding its offset in the scratch
layout to `base`. 

### `splitIndex`

 All legal pairs (degree minus one, split minus one) in triangular order. 

### `labelCount`

 Number of occupied production counter cells. 

### `labelIndex`

 Dense production indexing, using the triangular prefix for the split and
then row-major coordinates for the parent, left child and right child. 
