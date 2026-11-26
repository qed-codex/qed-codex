---
{
  "module": "OAI/Computability/VPVNP/CompressorSliceAdjacencyNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSliceAdjacencyNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSliceAdjacencyNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Indexing the copy records incident to each field

In the Appendix E interval scan, each candidate has a three-word output frame.
A second scan reads the length from this frame. For a positive length it appends
the candidate number to the adjacency lists of both fields. Rows are allocated
with one possible reference per opposite field.


### `adjFrameLength`

 The seven public words are the new field count, the old field count, the output
frame base, and the count and reference bases for the old and new fields in order. 

### `adjOldCount`

 Address of the number of retained slice frames for source field `i`. 

### `adjOldRow`

 First reference cell in the adjacency row for source field `i`. 

### `adjNewCount`

 Address of the number of retained slice frames for target field `j`. 

### `adjNewRow`

 First reference cell in the adjacency row for target field `j`. 

### `adjAppend`

 Write one candidate number at the current end of a row and increment its count. 

### `adjUpdate`

 Append the frame ordinal to both endpoint rows exactly when its recorded length is
positive. 

### `adjTemplate`

 One fresh call reads the frame length, handles both nonempty adjacency writes
and returns the next candidate number. Register eight is zero at call entry. 

### `adjEvents`

 The target row's size is read from memory after the source row's two writes. 
