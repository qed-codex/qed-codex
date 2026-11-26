---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterBits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterBits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterBits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-width binary choices for a primed node

The root degree on the stack determines how many words to read. Each location,
split or child state has one little-endian encoding. A choice word outside its
required range, or a call with excess or missing bits, is rejected.


### `digits`

 Canonical little-endian representation of an in-range natural. 

### `takeBounded`

 Consume a word and check the upper bound on its value. 

### `encodeToken`

 Exactly the branch bits consumed in one node call. No discriminator is guessed. 

### `Legal`

 The dynamic range check at a node. 

### `readToken`

 Each call must exhaust precisely the choices for its pending node. 

### `legal_of_step`

 A successful stack operation requires a legal node choice. 

### `decodeVisits`

 Binary decoding and stack traversal together, with one branch-bit list per call. 
