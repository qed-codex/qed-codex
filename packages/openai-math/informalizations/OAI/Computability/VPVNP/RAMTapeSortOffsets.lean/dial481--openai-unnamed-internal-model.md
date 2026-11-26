---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortOffsets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortOffsets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortOffsets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Visiting the physical rows of a sorting layer

A single finite routine visits the offsets in increasing order. The caller
can use the fixed-width binary row for the direction and partner tests and
the unary row to gather its record. The callback's other tape streams pass
from one visit to the next.


### `idle`

 Only the row width is occupied between successive traversals. 

### `visit`

 The callback's ports at a physical row. The temporary and loop-flag stacks are empty. 

### `routine`

 Fixed control independent of the input width, row count, and record size. 

### `runs`

 A traversal makes one callback for each physical row, in increasing order.
The additive charge per row is linear in its binary width and includes the
cleanup of the unary offsets after the last callback. 
