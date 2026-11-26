---
{
  "module": "OAI/Computability/VPVNP/CompressorSliceAdjacency.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSliceAdjacency.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSliceAdjacency.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native construction of both endpoint directories for copy slices

Scan the rectangular output frames of Appendix E in row-major order. A nonempty
frame appends its identifier to the row for its source and the row for its
target. The stored counts delimit the meaningful portions of both directories.


### `oldBank`

 Source-field adjacency directory, with one row per old field and one slot per new field. 

### `newBank`

 Target-field adjacency directory, with one row per new field and one slot per old field. 

### `AdjRegions`

 Counters precede the raw frames, which precede both reference arrays.
The inequalities allow gaps between arrays. 

### `AdjAt`

 Both directories represent the same prefix of the scan. 

### `AdjAt.frame_eq`

 Every frame word retains its offsets or length throughout the adjacency pass. 

### `adjNonempty`

 Number of nonempty frames in a contiguous part of the scan. 

### `adjSegment_run`

 A segment of the native program visits all consecutive identifiers starting at `k`.
The total cost counts calls and probes, and the instruction total counts each return. 

### `adjCost_eq_length_add_probes`

 Splitting the reported segment cost into its call and probe totals. 

### `adjPass_run`

 Starting with zero counts, the scan constructs every row at both endpoints.
Empty frames and zero-dimensional tables produce no incidences. 
