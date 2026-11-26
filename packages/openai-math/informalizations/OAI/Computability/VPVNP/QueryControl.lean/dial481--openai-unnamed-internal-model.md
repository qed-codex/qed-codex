---
{
  "module": "OAI/Computability/VPVNP/QueryControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/QueryControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/QueryControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Read a query bit on the literal machine's tape

A control records the remaining number of queries, the query-program state, and a phase.
Phase zero scans right until the blank immediately after the input. A query for suffix bit
`i` then moves left by `k - i` cells. Phase one reads the selected symbol and starts the next
query. The input and work tapes are preserved throughout the simulation.


### `Control`

 Control state recording the remaining query budget, the query-program state, and the
tape-scan phase. 

### `predFin`

 Decrease a bounded counter by one, saturating at zero. 

### `offset`

 Distance from the blank after the payload to bit `i` of its `k`-bit suffix. 

### `start`

 Start at the query program's initial state with all `t` queries available and scan phase
zero. 

### `command`

 Take one tape-control step toward the requested bit, branch on its value when reached, or
halt with the query result. 

### `machine`

 Compile the bounded binary query controller into the universal machine's instruction table. 

### `countAt`

 Count accepting paths with the specified tick budget, control state, input-head position,
and initially blank work tape. 
