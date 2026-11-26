---
{
  "module": "OAI/Computability/VPVNP/AffinePinIndex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffinePinIndex.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffinePinIndex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Computing packed pin-table offsets from the live binary row index

The little-endian index is consumed once. Its unary value is multiplied by
the stride of the table on scratch stacks. The multiplication preserves the
unary index and stride for the next table.


### `Port`

 The binary input, reversed bit stream, unary output, and scratch stacks for decoding a
coordinate index. 

### `bank`

 Initialize the index decoder with the supplied bit streams, a unary index tally, and empty
scratch. 

### `decode`

 Reverse the little-endian index bits and decode them into a tally with one true marker per
unit of the index. 

### `OffsetPort`

 Tally stacks for an index, stride, and accumulated offset together with the two work stacks
for multiplication. 

### `tallies`

 Set the index, stride, and offset tallies to the supplied natural numbers and initialize
the two work tallies to zero. 

### `scale`

 Add the product of the unary index and stride to the offset tally while preserving the
index and stride. 
