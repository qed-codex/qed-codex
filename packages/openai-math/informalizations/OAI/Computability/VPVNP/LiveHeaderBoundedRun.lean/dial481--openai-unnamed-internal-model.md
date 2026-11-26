---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderBoundedRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderBoundedRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderBoundedRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Completing a bounded native stage

The active calls preserve all source choices and memory effects. A single
extra empty choice list acknowledges the end cursor and produces the
accepting report seen by the linker.


### `activeReport`

 An active worker's report with the three local cursor-bound instructions prepended. 

### `closedReport`

 The terminal report of the bound check, accepting after its three local instructions. 

### `Active`

 Every source call begins with an active cursor. The result of the last
call may be the bound itself. 

### `runSegment_active_iff`

 Exact trace equivalence for all the calls below the bound. 

### `runSegment_complete`

 Append the closing call to a successful active segment. 

### `active_of_cursor_run`

 For a table advancing its cursor by one on every successful call, every
prefix of an in-bounds source scan satisfies the guard. 

### `runSegment_cursor_complete`

 Finish a complete cursor scan without requiring a separate prefix proof
for its concrete report list. 
