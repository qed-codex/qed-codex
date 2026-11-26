---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortRowProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The fixed finite stack control for one sorting row

The public address routine delivers the local-stride and orientation bits.
A local row fetches both operands from the current array. A cross-site row
verifies the sent copy and then combines a freshly fetched local record
with the receive. The two physical incident streams are consumed only by
the corresponding cross-site operations.


### `select`

 Run the row comparator on the chosen right operand and retain the minimum or maximum as
directed. 

### `verify`

 Compare the staged local record with the outgoing record and emit the verification flag. 

### `oriented`

 Pop the public comparator orientation and consume the two staged
records. A missing address decision rejects. 

### `localPass`

 Fetch the current row and its local partner, then apply the comparison in the requested
orientation. 

### `crossPass`

 Verify the outgoing copy against the current row, fetch that row again, and compare it with
the incoming partner. 

### `program`

 Dispatch on the local-stride flag, execute the corresponding row pass, and clear the
partner offset. 
