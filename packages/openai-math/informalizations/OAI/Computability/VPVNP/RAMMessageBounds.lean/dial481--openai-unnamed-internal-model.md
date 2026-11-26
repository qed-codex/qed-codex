---
{
  "module": "OAI/Computability/VPVNP/RAMMessageBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMMessageBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMMessageBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word bounds throughout the distributed RAM sort

Every comparator copies one of its two input records. Thus a pointwise
predicate of the input is preserved both by the pre-comparison blocks sent
between sites and by the last records sent on successor links. Applying this
to the canonical record wires proves representability of all these messages.


### `actual_sortSends_preserves`

 Every physical sort send is a pre-comparison block whose records retain
any pointwise property shared by all input records. 

### `MemoryMessages.FitsWord`

 Every present record in a sorting message or last-record message has address and timestamp
fields representable at the word width. 

### `actualMemoryMessages_fitsWord`

 For an execution within the cost cap, every occupied record sent by a
sort stage or a predecessor fits in the three address and timestamp words. 
