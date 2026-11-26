---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenTypedDecode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenTypedDecode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenTypedDecode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Typed assignments for arbitrary hidden-field streams

Splitting a complete raw stream at the recorded widths gives exactly one
assignment to the absorbed edges resident at the site. The native decoder
produces those fields with the original IDs and the exact remaining suffix.


### `decode_fields`

 Split a stream into an ordered vector of full-width words. 

### `decode_rows`

 The native decoder can start with any placeholders of the right widths.
Its output is precisely the rows of a typed local assignment. 

### `rows_prefix_unique`

 Equality of two complete prefixes, allowing arbitrary suffixes, forces
both the typed assignment and the suffix to agree. 

### `native_complete`

 Execute the entire hidden-field loop on an arbitrary complete input.
Its continuation sees precisely the suffix after the decoded typed assignment. 
