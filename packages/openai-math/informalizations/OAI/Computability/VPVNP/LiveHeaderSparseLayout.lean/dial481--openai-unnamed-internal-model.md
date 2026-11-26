---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderSparseLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderSparseLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderSparseLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dense iteration over the sparse auxiliary header

A cursor visits the three cut lengths, the two primed group indices, the
advice, both exterior cuts and the nominations. The destination skips the
unused capacity after each exterior field.


### `rangeStart`

 Cumulative starts, ending with the exact count of populated words. 

### `populated`

 The number of words actually visited by the auxiliary copy sweep over all seven input
fields. 

### `destinationStart`

 Offsets in the virtual machine's actual header, including capacity holes. 

### `rangeAt`

 The descriptor containing a packed cursor; the RAM dispatcher performs the
corresponding seven comparisons directly. 

### `sparseOffset`

 Map a dense copy cursor to its shadow offset, skipping unused exterior capacity before the
next field. 
