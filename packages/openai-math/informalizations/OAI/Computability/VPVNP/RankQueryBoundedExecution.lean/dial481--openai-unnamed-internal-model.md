---
{
  "module": "OAI/Computability/VPVNP/RankQueryBoundedExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryBoundedExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryBoundedExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Separate time and space in the complete rectangular rank query

All determinant root requests share a single storage allowance. In particular
an expensive scalar descriptor read is charged to the running time of the
Schur traversal while retaining its independent peak-storage certificate.


### `boundedRankTime`

 Step bound for scanning Schur coefficients of an n-by-m matrix, including each coefficient
read, zero test, and cursor update. 

### `boundedRankSpace`

 Stack-height bound for the full rectangular rank scan, combining the peak space of a single
coefficient read with the cursor workspace. 

### `fullRank_boundedRun`

 The rank is returned by the literal finite stack control. Every bit
stack respects the displayed cap throughout the entire rectangular scan. 
