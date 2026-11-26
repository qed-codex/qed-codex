---
{
  "module": "OAI/Computability/VPVNP/LiveAuxiliaryHeaders.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveAuxiliaryHeaders.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveAuxiliaryHeaders.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sparse initialization of the auxiliary pair counter

The live group stores the prescribed §11 header in a separate area of its
external memory. Only the cut lengths, index bits, advice bits, actual exterior
bits and nominated histogram words are written. The two exterior fields use
fixed capacities for addressing even when an endpoint has an empty cut.


### `exteriorBase`

 Offset of the first exterior field after the three lengths, indices and advice. 

### `span`

 Reserved header prefix, including padding in both exterior fields. 

### `cells`

 Physical offsets visited by the writer in ascending order. The first range
also contains the populated part of the left exterior field. 

### `cells_length`

 The write count uses the actual cut lengths, including at an empty endpoint. 

### `install`

 Sparse writes into the live machine's separate area for the pair's headers. 

### `install_outside`

 All writes fall within the reserved prefix. In particular, separate live
scratch addresses may already hold data. 

### `install_read`

 Reading a translated virtual address in a zero-initialized header area
recovers the prescribed word. This includes all padding and unused sites. 

### `copyWord`

 Copy a full computed word at offset `state - pub 0` between the arrays
at `pub 1` and `pub 2`. Used for cut lengths and histogram components. 

### `copyWord_native`

 Each native word-copy call performs one read and one write and advances the
persistent cursor without branching. 
