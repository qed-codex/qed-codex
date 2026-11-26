---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Control/BucketNet.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Control/BucketNet.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Control/BucketNet.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Occurrence ranks in a finite sequence 

### `histogram`

 Count occurrences at earlier positions, or in the whole sequence for `none`. 


# Binary prefix counts

At each bit, keep the old count and send the updated one to the next
position. Only that counter is connected between two blocks.



# Selecting positions by occurrence rank

Dividing a little-endian count by a power of two discards leading wires.
A comparison with a constant selects the required bucket.

