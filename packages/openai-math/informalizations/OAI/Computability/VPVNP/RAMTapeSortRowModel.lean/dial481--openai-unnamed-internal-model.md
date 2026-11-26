---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortRowModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowModel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Register layout and outcomes for a physical compare-exchange row

A local partner is fetched from the current block. At a cross-site layer
the outgoing block is compared with the site’s current records and the
incoming partner record supplies the other comparator operand. The flags
are retained in reverse chronological order, just as the output records are.


### `RightSource`

 Source of the right comparison operand, either the fetched local partner, the outgoing
record, or the incoming record. 

### `RightSource.port`

 Select the row stack holding the right operand for this source. 

### `comparePorts`

 Wire a record comparator into the row stacks, sending its output to the next block and its
validity bit to the flags stack. 

### `chosen`

 Choose the smaller or larger raw record according to the comparator orientation, choosing
the first on a minimum tie and the second on a maximum tie. 

### `selectOK`

 Test that both raw slots have canonical record tags. 

### `verifyOK`

 Test canonicality of both slots and equality according to the record comparator. 

### `Ready`

 All sources of a prepared row except the two cross-site streams. 

### `result`

 Terminal register values of one row. A cross-site row pushes its verify
flag first and its select flag second. 
