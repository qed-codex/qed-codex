---
{
  "module": "OAI/Computability/VPVNP/RankQueryExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Full rectangular rank query on the determinant stack

A single finite control traverses the rectangle of bidegrees. At each
request it stages the six fields of the weighted Gram determinant, executes
the Schur engine, tests the returned scalar, and advances or terminates.
The result register contains the rank of the original rectangular matrix
over the advised field.


### `fullRank`

 Run the rectangular rank scan with the Schur engine's root query at each bidegree and leave
the resulting rank in the cursor registers. 

### `rankTime`

 Step bound for scanning an `n` by `m` matrix. It allows a Schur root query and cursor check
at each of the `(n+1)*((n+m)*n+1)` bidegrees. 

### `fullRank_runs`

 The rectangular query's only engine hypotheses specify the concrete
dispatch, entry, and arithmetic routines. No rank-oracle hypothesis enters
the scan or the decision to stop. 
