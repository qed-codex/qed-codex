---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkPreimages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkPreimages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkPreimages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Building the preimage directory of the chosen shrinking layout

Appendix E's third scan uses the owner column of the selected placement. The count
array starts with a native clear. The subsequent calls append each old position once,
leaving every packed site's immediate children in increasing old-site order. An
ordinal read uses the count address and the rectangular row address in the resulting
memory.


### `oldCount`

 Number of old positions scanned for children, counting every packing lane at every base
vertex. 

### `newCount`

 Number of packed sites receiving child rows, one for each base vertex, tag, and residual
lane. 

### `capacity`

 Number of old children per packed site in either layout, equal to the number of color masks
times the degree. 

### `oldOrder`

 Enumerate old positions by base vertex, color mask, slot label, tag, and residual lane, in
the order used by the preimage scan. 

### `newOrder`

 Enumerate packed sites by base vertex, tag, and residual lane to index the count and child
rows. 

### `place`

 Map an old-position word to its packed owner in the chosen layout. A cursor beyond the old
positions maps to zero. 

### `params`

 The collector's old-site owner array is the first output column of the actual
shrinking scan. The remaining two arrays may occupy any later disjoint regions. 

### `Areas`

 Bounds placing the count column after the old-site owner column and the rectangular child
table after the counts, all within the word address space. 

### `Areas.packed`

 With contiguous fresh arrays the directory occupies one word per old child and one
count per new position. The first free address is `start + newCount X + oldCount X`. 

### `owner_at`

 The stored owner read at a numeric cursor agrees with the typed packing placement. 

### `owner_formula`

 At the same cursor the numerical owner formula on the four input columns gives
the word read by the preimage collector. 

### `children`

 Enumerate the old positions assigned to a given packed site in the chosen layout, retaining
their original scan order. 

### `Directory`

 Physical row counts and ordinal data words, in the restricted old-site order used
by the local history parser. 

### `build`

 The count clear and the append pass execute from arbitrary initial scratch contents.
One clear costs two calls-plus-probes per packed position. Appending costs five per
old position. Every address outside the count and row arrays retains its initial word. 

### `selectedTerm`

 The term chosen by the shrink selection in the state's compression step. Its placement
determines the children used by the traversal directory. 

### `selected_placement`

 The physical owner map agrees on every word with the placement of the selected
shrinking term in the actual input and output state orders. 

### `selectedDirectory`

 The concrete raw directory can be passed directly to the DFS layer compiler for
this selected term. Both site orders are those used by the branch's kernel readers. 
