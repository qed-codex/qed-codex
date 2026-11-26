---
{
  "module": "OAI/Computability/VPVNP/BitSlotIndex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BitSlotIndex.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BitSlotIndex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary numbering of wire slots and tags

The shrinking step in Appendix C of *VP and VNP differ over every field*
uses a fixed coordinate block to label a power-of-two set of slots. The
first coordinate is the most significant bit. Encoding and decoding recurse
on the tail, so the same numbering works for both slot and tag blocks.


### `bitWordFinEquiv`

 Read a binary coordinate block in decreasing order of place value. 

### `bitWordFinEquiv_val`

 Encoding the head and tail as a single ordinary binary integer. 

### `bitWordFinEquiv_symm_head`

 Decoding the most significant coordinate divides by the tail's range. 

### `bitWordFinEquiv_symm_tail`

 The remaining coordinates decode the residue modulo the size of the tail. 
