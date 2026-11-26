---
{
  "module": "OAI/Computability/VPVNP/RankCursorPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Stack layout of a complete rank scan

The arithmetic cursor and the Schur engine use separate banks. The row
count and balanced product depth supply two constant fields of every root
request. The scalar output is read from the engine's result port.


### `ScanPort`

 Ports of the rectangular rank scan. The cursor and Schur engine have separate stack banks
alongside the row count, product depth, and copy scratch. 

### `scanBank`

 A bank with independently specified engine and arithmetic registers. 

### `idle`

 All frame and query stacks are empty between requests; the auxiliary
engine bank retains the matrix and field description. 

### `yielded`

 At the scalar check boundary the Schur result occupies its result port. 
