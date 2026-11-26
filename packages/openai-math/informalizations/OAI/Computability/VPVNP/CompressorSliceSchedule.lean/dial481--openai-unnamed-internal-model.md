---
{
  "module": "OAI/Computability/VPVNP/CompressorSliceSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSliceSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSliceSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scheduling the compressor's interval records

The source-major Cartesian scan uses one persistent pair number. Its quotient
and remainder select source and target fields in their two external arrays.
The output frame for that pair consists of three words, two offsets and a
length. Empty intersections have length zero.


### `fieldAt`

 Descriptor at a numerical array index. The default width occurs only
outside the array and is never read by a scheduled visit. 

### `pairAt`

 Read the pair whose row-major index is `k`. 

### `sliceAt`

 Copy interval for the `k`th old/new field pair in source-major order. 

### `numbered_pairs`

 The word-arithmetic index order is the order of the record builder's
Cartesian product, including fields of width zero. 

### `emitted`

 Number of records emitted among the first `t` candidate visits,
starting with persistent index `k`. 

### `Inputs`

 The four arrays read by the pair visitor contain natural width and start
coordinates. Array heads are in words 1–4 of the visitor's public data. 

### `FrameSpace`

 All five physical arrays fit their word addresses. Only the frame array
is written during the pair pass. Input arrays may share other data. 

### `FramesAt`

 Contents of all completed frames. The length word is overwritten even
on the empty branch so arbitrary stale output cannot be read as a record. 

### `writeFrame`

 Physical writes of a frame, using the ordinary natural offsets of a
validated array. The two empty offsets can have arbitrary prior contents. 

### `frameSegment_run`

 A contiguous segment of actual pair calls carries the linear pair cursor
and writes every completed frame. The scan starts from arbitrary prior contents
of its unused output slots. 

### `frameHead`

 First frame after the two totals, the incidence counts and the prefix arrays. 

### `stop`

 Last exclusive workspace address. Each pair reserves three frame cells
and one reference slot in each of the two endpoint directories. 

### `Workspace`

 Address bounds and separation of the slice workspace from both input width arrays. 

### `pairData`

 Pair worker public data. 

### `adjacencyData`

 Endpoint-directory worker public data. 

### `Passes`

 Reports from the five rows of the local descriptor schedule. 

### `Passes.clear`

 Reports for zeroing the two totals and both endpoint count arrays. 

### `Passes.oldPrefix`

 Reports for computing the starts of the old fields from their widths. 

### `Passes.newPrefix`

 Reports for computing the starts of the new fields from their widths. 

### `Passes.frames`

 Reports from testing the field pairs and storing their interval offsets and lengths. 

### `Passes.directories`

 Reports from indexing nonempty pair frames in both endpoint directories. 

### `Passes.prepared`

 Memory after clearing and computing both arrays of field starts. 

### `Passes.tested`

 Memory after the pair scan writes its frames into the prepared workspace. 

### `Passes.result`

 Memory after both endpoint directories have been populated from the tested frames. 

### `Passes.all`

 Reports of all five sweeps in execution order. 

### `NativePasses`

 The five reset-cursor segments of the fixed worker schedule, in chronological order. 

### `Stored`

 The final table stores the three words for each nonempty pair and its
identifier in both compact incidence lists. Each list occupies the live prefix
of its bounded row, in the order of the candidate scan. 

### `References`

 Following a reference in the live portion of an endpoint row. 

### `Stored.references`

 A source or target's physical row contains exactly the positive-length
frames incident to that field. Dividing the returned ID by the target count
recovers the source, and its remainder recovers the target. 

### `build`

 Build the interval records and both of their endpoint directories
directly from the two width arrays. All scratch words may initially be stale.
The exact totals include address preparation, the intersection tests, and the
writes that compact both endpoint lists. 
