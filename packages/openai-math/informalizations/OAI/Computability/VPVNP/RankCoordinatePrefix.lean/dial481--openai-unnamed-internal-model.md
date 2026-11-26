---
{
  "module": "OAI/Computability/VPVNP/RankCoordinatePrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinatePrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinatePrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Physical prefix scan for the greedy row and column indices of Appendix D.2

Each test queries the rank of the original matrix up to the current inclusive
row. The same controller works on the transposed selected-row matrix for the
column scan. Only a failed test increments the cursor. The returned cursor is
the zero-based original index.


### `greedyPrefix`

 Finite controller for a rank test and a cursor increment. Both subroutine
returns redirect directly to the caller. 

### `testIteration`

 One iteration consumes the returned decision bit. When it is true, the
successful candidate stays in the cursor register. 

### `first_test_runs`

 With a first successful index `last`, bounded subcalls give a bounded
physical scan. The cap is independent of the number of preceding failed tests. 

### `greedyPrefix_runs`

 The test contract refers to prefix ranks of the supplied matrix, not a basis
computed recursively. It also applies verbatim to column selection on a transpose. 
