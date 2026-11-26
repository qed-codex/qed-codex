---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortGather.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortGather.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortGather.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Fetching one record from an arbitrary physical sort block

The two reverse buffers restore the selected record and then the skipped
prefix. The selected record also goes to the operand stack in forward order.
The finite control depends only on the five-field record format. Neither the
word width nor the requested offset occurs in its states.


### `fetch`

 Consume a unary record offset, preserve its source block, and prepend the selected
record to the destination. All temporary stacks are cleared on return. 

### `cost`

 Tick allowance to skip i five-word records, fetch the next one and restore both it and the
skipped prefix to the block. 

### `fetch_slice_runs`

 In the physical block encoding the fetched bits are exactly the record slice,
including when the supplied bits encode a malformed record. 
