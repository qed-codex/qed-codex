---
{
  "module": "OAI/Computability/VPVNP/BitSlotXor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BitSlotXor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BitSlotXor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary tag arithmetic on the private RAM

Appendix C's greedy tag assignment uses the additive group of binary vectors.
With the slot numbering of `BitSlotIndex`, vector addition is one native XOR
instruction, including when the tag occupies only the low bits of a RAM word.


### `bitWordFinEquiv_add_val`

 The binary numbering takes coordinatewise addition to XOR of the numbers. 

### `tagWord`

 Store a binary tag in the low bits of a RAM word, zero-extending its number. 

### `tagWord_xor`

 Evaluating the native bitwise instruction computes tag addition exactly. 
