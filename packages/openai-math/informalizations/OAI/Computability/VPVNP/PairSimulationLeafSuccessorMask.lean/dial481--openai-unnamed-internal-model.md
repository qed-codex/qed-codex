---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafSuccessorMask.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSuccessorMask.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSuccessorMask.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Low-bit masks in the native successor selector

The XOR of a nonwrapping sender and its successor is a nonempty prefix of
one bits. A one-bit right shift shortens that prefix by one. These identities
justify both the selector's initial register and its subsequent countdown.


### `mask`

 The bits from zero through `t`, inclusive. 

### `sender_xor`

 The arithmetic instructions produce the mask for the sender's unique
nonwrapping successor class. 
