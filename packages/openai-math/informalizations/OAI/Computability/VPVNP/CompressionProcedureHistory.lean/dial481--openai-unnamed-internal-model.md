---
{
  "module": "OAI/Computability/VPVNP/CompressionProcedureHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionProcedureHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionProcedureHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local history bounds of exact compressor procedures

The bounds refer to the records attached to each term in the actual execution
tree. Sequential procedures retain both sets of records, including the records
of the continuation selected by each branch.


### `RecordBounds`

 Uniform local record and branch length bounds for every execution of a procedure. 

### `RecordBounds.records`

 The local records for the whole execution tree of each input, used to bound each pass and
  the length of every selected branch. 

### `mono`

 Enlarge both bounds while keeping the same records. 

### `id`

 The empty schedule has an empty history and depth zero. 

### `seq`

 Concatenate the two actual execution records. The largest elementary
bound applies throughout, and the two uniform branch lengths add. 

### `ofPass_length`

 Every branch of a procedure created from one pass has depth exactly one. 

### `ofPass`

 Lift the supplied records and elementary bound of a single pass to the
whole procedure. Each selected history contains exactly that pass. 
