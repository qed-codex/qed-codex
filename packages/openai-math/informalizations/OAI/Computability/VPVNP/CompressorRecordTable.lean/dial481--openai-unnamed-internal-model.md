---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounded incidence lists in the descriptor scans

The third scan of Appendix E appends old-position and role identifiers to bounded lists at
their new owners. In the first scan the same operation records members of each wire bundle.
The arrays store the count and the contiguous identifier slots separately. The code below
executes one insertion in the burst RAM. Its three external probes and seven instructions
are independent of the payload width described by the identifier.


### `appendRecord`

 The caller supplies the count-cell address, the first row address, the slot capacity and
the identifier in registers 0–3. Registers 4–6 hold the count, slot address and unit. 

### `rowRepresents`

 Array state at one owner. Only the prefix below its stored length is meaningful. 

### `appendRecord_represents`

 Under the row address bounds, the post-state represents the old list followed by the
new identifier, in the order in which the outer scan visits its incidences. 

### `appendRecord_native`

 Executing the fixed instruction table returns the new length in the persistent state. 
