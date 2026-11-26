---
{
  "module": "OAI/Computability/VPVNP/PairOutputRowDirectory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairOutputRowDirectory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairOutputRowDirectory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Decoding the output rows of a traversal

The leaf layer precedes the selected output layers. A popped word identifies
an output row precisely when it is the header of a site of one of these
layers. Empty layers contribute no candidates to the finite directory.


### `Row`

 An output row identified by a tagged output layer and a site ordinal bounded by that
layer’s count. The traversal uses the pair to recover the absolute descriptor address. 

### `rowAddress`

 The site number is relative to its output layer. Layer zero of the
physical layout holds the leaves. 

### `decode`

 Search the fixed row headers in level and site order using machine-word equality. 

### `decode_eq_some_iff`

 Each valid output header selects its unique level and site. 

### `decode_eq_none_iff`

 Words in the leaf region, row interiors, or beyond the directory have no output row. 
