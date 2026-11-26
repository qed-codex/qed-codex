---
{
  "module": "OAI/Computability/VPVNP/AffinePinTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffinePinTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffinePinTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native indexed selection from an immutable packed pin table 

### `Port`

 Stack addresses for a fixed-stride table lookup, including its unary counters, packed
source, saved prefix, reversed entry and output. 

### `bank`

 Encode the index, stride, offset and width in unary and install the source table and output
stack with empty lookup scratch. 

### `machine`

 Prepend the `stride` bits starting at bit `i * stride` of the source table to the output
stack, restoring the source table after the read. 

### `cost`

 Exact step count to compute the offset `i * stride`, copy the width marker and retrieve the
full fixed-width table entry at index `i`. 
