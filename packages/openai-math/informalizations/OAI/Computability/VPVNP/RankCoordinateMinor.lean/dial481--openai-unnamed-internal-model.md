---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateMinor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateMinor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateMinor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Physical scalar reads from the two Cramer minors

A query recomputes the two selected indices in the original matrix and its
transpose. For the replaced-row minor, a register equality selects either an
ordinary matrix entry or the target entry at the selected column. All large
matrices are accessed through scalar calls.


### `equalBranch`

 Compare two caller registers and use the returned bit to enter a subroutine. 

### `equalBranch_runs`

 Branching preserves the call's space cap even if one of its subcalls takes
exponentially many steps. The comparison itself scans only two binary words. 

### `column`

 The original column selected at this ordinal by the greedy row algorithm on the transpose. 

### `square`

 The original row and column bases, presented by two independent index queries. 

### `replaced`

 Replace the selected row of the greedy square minor by the target restricted to the same
selected columns. 

### `read`

 The two index calls precede a single scalar read. 

### `read_square_runs`

 Entry query for the unchanged square minor. The raw scalar reader sees an original
row and an original column in the caller's registers. 

### `read_replaced_runs`

 Entry query for the row-replaced square minor. The last comparison uses the
original query ordinal, and the target is evaluated at the same selected column. 
