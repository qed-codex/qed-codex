---
{
  "module": "OAI/Computability/VPVNP/PairTraversalReferenceFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalReferenceFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalReferenceFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Memory preserved by every prefix of the native traversal passes

A tag call writes its own tag. A leaf call writes its two header words.
A fiber call also writes its child row, whose length is the count in the
retained raw directory. The scan leaves those input directories intact.
These bounds apply after each reference call, including inside a layer.


### `PrefixFrame`

 Only addresses in the half-open interval can differ after a prefix. 

### `leaf_prefix`

 Prefixes of the leaf scan are confined to the leaf row interval. 

### `tag_prefix`

 Every tag report writes within the current tag interval. 

### `fiber_prefix`

 A fiber call only updates the two row headers and the bounded live
identifier list. The counts for every subsequent call remain readable. 

### `tag_chain_prefix`

 Every reference prefix of all tag jobs stays in their consecutive arena. 

### `fiber_chain_prefix`

 Native directory workers preserve all addresses outside the selected
fiber layers, even partway through the current layer. 

### `selected_rows_prefix`

 All intermediate descriptor-row memories have the same raw headers and
the same higher words as the row pass's entry memory. 

### `selected_reference_frame`

 Every reference prefix preserves each address outside both arenas,
including the final arc bits in the gap between descriptor rows and tags. 

### `selected_reference_schedule`

 The resident scheduler fields survive every partial scan of the actual
selected tag and row workers. The protected low interval contains the raw
level scalars and the high interval starts at the terminal header. 
