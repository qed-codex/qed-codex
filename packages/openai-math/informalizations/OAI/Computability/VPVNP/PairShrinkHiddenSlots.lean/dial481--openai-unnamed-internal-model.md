---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenSlots.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenSlots.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenSlots.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private fields for absorbed edges in a shrinking pass

Each absorbed edge receives one slot indexed by its dense motif and role
ordinal. The local history scans the restricted list of owners. The source
and target maps at that owner use the same private field.


### `id`

 The identifier carried by a row of the hidden owner directory. 

### `address`

 The base of a private bit field, shared between its two map incidences. 

### `directory_id`

 Each entry in the native local row contains its full dense identifier. 

### `store_other`

 Writing a resident field preserves every bit of any other slot. 

### `party`

 The party reading an absorbed edge at the indicated end. 

### `mapColumn`

 Select the absorbed column from the actual local supply argument.
Both ends use the hidden assignment at their common packed site. 

### `mapColumn_read`

 A shared private slot gives the coordinate of either incident map column.
The half-wire argument is arbitrary, including unrelated assignments to the
source and target party's surviving fields. 
