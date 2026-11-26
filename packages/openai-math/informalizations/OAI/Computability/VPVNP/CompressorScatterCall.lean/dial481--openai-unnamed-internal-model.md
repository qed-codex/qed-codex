---
{
  "module": "OAI/Computability/VPVNP/CompressorScatterCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorScatterCall.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorScatterCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A native call with a bank of scattered stores

A finite list of assignments snapshots every operand from the entry memory.
The call then stores selected registers to computed addresses and returns
one designated register. The exact external effect is a fold of these stores.


### `op`

 Translate a row-recipe register assignment to its corresponding burst operation. 

### `ops`

 Run all register assignments, then emit the ordered external writes from the selected
register pairs. 

### `stores`

 Resolve address and value register pairs to a list of word-addressed stores. 

### `storeLog`

 Encode the ordered address-value pairs as external write events. 

### `applyStores`

 Apply the ordered stores to memory, with later writes taking precedence at a repeated
address. 

### `report`

 Evaluate the assignments from zero registers, append the selected stores to the event log,
and return the designated register's value. 
