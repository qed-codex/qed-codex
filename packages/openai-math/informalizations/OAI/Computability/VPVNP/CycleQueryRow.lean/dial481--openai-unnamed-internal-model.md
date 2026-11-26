---
{
  "module": "OAI/Computability/VPVNP/CycleQueryRow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CycleQueryRow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CycleQueryRow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a directed Hamiltonian cycle row by row

A running control stores the number of completed rows, the current vertex, the column
to inspect, and the unique edge found so far in the row. Each transition reads one
payload bit. A second edge in a row or an empty row immediately gives a rejection.


### `CycleState`

 A halted result or a row count, vertex, column, and previously found successor. 

### `afterRow`

 Continue the traversal at the unique edge's target. The first return must occur
after exactly `m` rows. 

### `cycleQuery`

 A fixed finite control for an `m × m` binary adjacency matrix in row-major order. 

### `cycleQuery_eval_row`

 With the remaining clock increased by one row, the scan either rejects the row or
continues with its unique successor and exactly the original remaining clock. 
