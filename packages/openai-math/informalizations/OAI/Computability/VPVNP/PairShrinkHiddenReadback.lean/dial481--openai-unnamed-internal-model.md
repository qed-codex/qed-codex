---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading both map columns after the complete hidden-field scan

The final private memory of the native shrinking guess worker is a fold of
field stores. Distinct dense identifiers keep all of these fields resident
through the end of the scan.


### `storeRows_read`

 Read one member of the complete native scan's private-memory update. 

### `rows_fit`

 The allocation of one private slot per dense identifier bounds every
field store in each site's restricted row. 

### `resident_read`

 Every owned coordinate remains available after all rows have been written. 

### `storeRows_mapColumn`

 The same native store scan supplies the bit to either endpoint of the
absorbed edge, evaluated on the local party's independent half-wires. 
