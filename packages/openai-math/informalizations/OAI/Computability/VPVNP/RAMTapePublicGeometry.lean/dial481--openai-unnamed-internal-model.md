---
{
  "module": "OAI/Computability/VPVNP/RAMTapePublicGeometry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicGeometry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicGeometry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Converting the physical geometry tallies into public RAM words

The processor supplies four unary stacks and a persistent width-sized zero
template. For each field, copy the zero template into the destination, save
the field's unary marks, and increment the destination word once per mark.
All four source tallies and the template remain available to the processor.


### `Port`

 Stack labels for four unary geometry tallies, their corresponding word outputs, a zero
template, and conversion scratch. 

### `initial`

 Geometry-conversion bank before any of the four unary fields has been converted to a word. 

### `result`

 Bank containing all four packed geometry words and the original tallies and zero template. 

### `prepare`

 The four source fields are prepared in the public operand order. 

### `steps`

 Total conversion steps for input length, address width, bucket capacity, and word width. 
