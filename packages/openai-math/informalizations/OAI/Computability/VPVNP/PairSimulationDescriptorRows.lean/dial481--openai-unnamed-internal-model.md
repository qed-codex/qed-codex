---
{
  "module": "OAI/Computability/VPVNP/PairSimulationDescriptorRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationDescriptorRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationDescriptorRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Converting preimage identifiers to child descriptor addresses

A native pass reads a site's stored count and child identifiers. It writes
a header and a separate row of addresses in the older level's descriptor
table. The input order, including the empty preimage list, is preserved.
The child scan reads and writes one word per old position independently
of the widths of all tensor fields.


### `body`

 Register 0 scans identifiers up to register 1. Register 2 is the
destination cursor. Registers 3–5 contain the older table base, its
descriptor stride and the unit. Register 6 holds the current address. 

### `scan`

 While the input cursor is below its end, read each child identifier, convert it to an
address in the older descriptor table, and write that address at the advancing destination
cursor. 

### `address`

 Compute a child descriptor's address in word arithmetic by adding its identifier times the
older table's row stride to the table base. 

### `rowMemory`

 Exact state of the output row, with all other memory cells retained. 

### `scan_exec`

 The finite loop scans exactly the indicated interval, returning its
external probe count and instruction count even for an empty child row. 

### `linked_scan`

 Link the identifier scan to arbitrary native successor code. 

### `header`

 A separate fixed three-probe block loads the preimage count from
register 0 and writes the row pointer and count at the node's first two
descriptor cells. Register 1 holds the row pointer, register 2 the node
address, and register 3 the unit. 

### `represents_DFS_row`

 A scanned preimage row and the written header have precisely the
representation read by the native stack traversal. 
