---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramProducedRankMatrix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramProducedRankMatrix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramProducedRankMatrix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The exact row-major matrix emitted by the entry scanner, in the actual
selected identifier order. These proofs introduce no runtime permutation. 

### `matrixRel_typed`

 Every physical pair retains its original row number and selected ID. 

### `selectedMatrix`

 The coefficient matrix uses exactly the scanner's selected-ID order. 

### `actualBuckets_length_le_rank`

 Exact cardinality of the actual output buckets, derived from the original
entry relation and the physical preprocessing relation. 
