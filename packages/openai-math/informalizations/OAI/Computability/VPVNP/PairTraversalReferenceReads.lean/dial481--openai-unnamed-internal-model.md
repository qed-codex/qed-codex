---
{
  "module": "OAI/Computability/VPVNP/PairTraversalReferenceReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalReferenceReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalReferenceReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Raw input addresses of the selected traversal passes

The tag and leaf workers only write. Each fiber worker reads a count and the
corresponding identifiers from the retained placement directory. Every prefix
of the descriptor scan preserves these raw inputs, including between two
sites of the same layer.


### `tag_reads`

 Every tag worker has an empty external read set. 

### `leaf_reads`

 Every leaf worker has an empty external read set, including its header writes. 

### `fiber_reads`

 Every site in a fiber layer reads its retained count and source identifiers
strictly below the original raw-directory limit. 

### `tag_chain_reads`

 Tagging any number of layers uses no external reads. 

### `fiber_chain_reads`

 The same raw-directory limit applies to every later fiber layer, even as
the base of the new descriptors advances. 

### `selected_reference_reads`

 Complete reference read footprint of the selected tag and descriptor
passes, starting from the retained branch directories. 
