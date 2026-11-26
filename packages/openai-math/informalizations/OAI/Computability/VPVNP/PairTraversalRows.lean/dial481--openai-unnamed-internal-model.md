---
{
  "module": "OAI/Computability/VPVNP/PairTraversalRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Storing placement-fiber rows for the depth-first traversal

In Section 13 and Appendix E of *VP and VNP differ over every field*, each
position has a bounded row listing its immediate old positions. Here the
first two words of a row store its child-list address and count. The remaining
cells hold the actual older descriptor addresses in the reader's order.
Successive layers occupy disjoint intervals, and every row fits in the same
fixed stride, regardless of the wire widths or the chosen branch.


### `ChainOrders`

 The actual numerical order of sites at the output of each selected term. 

### `branchOrders`

 Site numbers at each stage come from that state's base and lane coordinates. 

### `Layer`

 A layer in numerical site order. Child identifiers refer to the preceding
layer's site numbers, before translation to absolute word addresses. 

### `Layer.count`

 Number of site rows in a single DFS layer. 

### `Layer.ids`

 The list of old-site child ordinals for each row of this layer. 

### `address`

 Absolute address of a site's DFS row given the layer base and its capacity-plus-two word
pitch. 

### `endPos`

 Exclusive end of a layer's DFS rows, obtained from its site count and fixed row pitch. 

### `stepLayer`

 Child identifiers have the exact order in which the local history reader
visits the placement fiber. 

### `leafLayer`

 The initial cursor layer with one childless DFS row per site in the chosen initial order. 

### `stepLayers`

 The chronological output DFS layers of the selected term chain, using each pass's placement
fibers and site order. 

### `chainLayers`

 The complete selected row layout formed by prepending the initial cursor leaf layer to the
pass output layers. 

### `stepLayers_capacity`

 The substep record limit bounds the number of stored words in every
child list, including on branches with parallel arcs or empty placement fibers. 

### `childWords`

 The finite list of absolute child descriptor addresses. 

### `Layer.Rows`

 Memory contains each site's row header and its child addresses at the designated
fixed-pitch location, with the header address representable as a word. 

### `cell`

 Populate the header and live children. Unused reserved cells retain
their original contents. 

### `writeLayer`

 The memory image of one layer over arbitrary contents at other addresses. 

### `Layer.Live`

 A word belongs to a live header or payload of this layer. Reserved padding
and cells outside the layer are excluded. 

### `writeLayer_rows`

 A complete row, including the exclusive-end bound required by the
native child-copy loop. 

### `words`

 Total row storage has a fixed number of words per position at each layer. 

### `build`

 Build all layers in increasing stage order, preserving older rows. 

### `AllRows`

 Consecutive layers satisfy the row memory predicate with each new layer starting at the
exclusive end of the preceding layer. 

### `sitePointers`

 Base pointer and child-list pointer of a site in a specified layer. 

### `chainPointers`

 Pointers to every output site of a selected term. The argument `base` is
where the first output layer starts, immediately after the input layer. 

### `chainPointers_rowsAt`

 The table representation agrees with the descriptor row read by the native
traversal, including the ordering of the children. 

### `chain_memory_rows`

 Initial leaf headers and all later descriptors are simultaneously present
in the same memory, built on any initial contents. 

### `build_outside`

 Building the descriptor region leaves the rest of memory available to
other pair-simulation phases. 

### `count_stepLayers_le`

 Every old position is assigned to exactly one successor. Thus the number
of rows, summed over the levels, is at most the total history size across the
final positions. This gives a word bound without inspecting intermediate sites. 

### `selectedLayers`

 Exact row counts and old IDs determined by an admissible branch of the
actual compressor. The site numbers of every intermediate state are used. 

### `selected_words_le`

 The selected descriptor region fits in the product of the fixed stride,
final order and history allowance. This gives a sufficient address-space test
without enumerating the rows. 

### `selected_memory_traversal`

 In the memory constructed for this branch the native DFS reads precisely
the actual placement tree. No hypotheses about the contents of headers or
child lists are required. 
