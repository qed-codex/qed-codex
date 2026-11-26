---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordGreedyWalk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordGreedyWalk.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordGreedyWalk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Indexed memory and complete greedy scans

The mutable assignments occupy one word per base vertex. Each fixed-stride
record following those cells contains the assignment's address, the address
of the next record, and the operand pointers read by the native visit. This
layout permits the same fixed instruction table to visit the entire base.


### `WalkLayout`

 `width` counts pointer words after each two-word header. 

### `WalkLayout.origin`

 First address of the contiguous vertex assignments, followed by their fixed-stride greedy
  records. 

### `label`

 The mutable word for an indexed vertex. 

### `base`

 The descriptor for cursor `k`. After the last visit this is the return cursor. 

### `limit`

 Natural start of the following region, reserved for fixed graph data. 

### `record`

 The full descriptor, with the next pointer present also at the last vertex. 

### `initialMemory`

 Assemble the fixed-stride descriptor directory over the supplied memory.
The mutable assignment region starts at zero. Addresses beyond the table
retain their initial values, including fixed displacement operands. 

### `Represents`

 Contents of the table relative to an arbitrary partially filled label vector. 

### `Represents.record`

 Writes to the assignment cells preserve all descriptor headers and pointers. 

### `Pass`

 The machine's complete native execution, final cursor, labels, and exact per-call cost. 

### `Pass.cost`

 Total calls plus probes in the native scan, linear in the base size at fixed degree. 

### `initialMemory_after`

 Fields beyond the fixed-stride records retain their supplied values. 

### `colorOperands`

 Actual operand addresses of the color visit, in incidence order. 

### `color_pass`

 Starting from zero assignments, the full native scan writes precisely the
ordered coloring. No condition on the memory surrounding its directory is needed. 

### `tagCount`

 Number of four-operand tests for one tag. 

### `tagAddresses`

 Place the zero word and the vertex-major array of outgoing tag displacements
immediately after the pointer directory. 

### `tagOperands`

 The four addresses of every test, laid out consecutively in tag test order. 

### `tagData`

 Initialize the immutable operands from the indexed graph's displacements. 

### `tag_pass`

 Starting from zero offsets and the graph's displacement array, the complete
native tag scan writes the same offsets as `orderedTagOffsets` in Appendix C. 
