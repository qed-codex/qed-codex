---
{
  "module": "OAI/Computability/VPVNP/RAMSortBlockSlices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortBlockSlices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortBlockSlices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Consecutive record intervals in a sorting exchange

Each site sends a block of `4H` five-word records. A validator can parse and
check its incident sorting field one record at a time, by reading the bit
interval beginning at offset `i * 5 * w`. This gives the same records and
canonicality check as the serialized block format.


### `recordSlice`

 The physical interval occupied by the five words of the `i`th record. 

### `blockParse_slice`

 Parsing the physical slice reads the corresponding entry of the full
block parser on every input, including malformed encodings. 

### `blockEncode_slice`

 Slicing an encoded block gives the encoding of its corresponding slot. 

### `blockCanonical_iff`

 A block passes its re-encoding test precisely when every physical slice
is the canonical encoding of a record or an empty slot. 
