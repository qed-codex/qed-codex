---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramSignedSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramSignedSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramSignedSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A typed view of the physically produced signed-matrix preprocessing output.
The view does not compute or reorder entries: it identifies the exact list
already emitted by the primitive scanner. All supplied rows are retained. 

### `shiftedMatrix_typed`

 The existential coefficients are just the already produced words at their
original row and column positions. No basis or permutation is inserted. 

### `generated_signed_bucket_exact`

 Exact bucket membership for the matrix actually emitted from signed
integer entries. The number d is the full serialized row count. 
