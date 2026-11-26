---
{
  "module": "OAI/Computability/VPVNP/RAMValidatorPost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorPost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorPost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Deterministic memory pass of the site validator

After a successful bucket simulation, the site fills its sorting buffer from
its header and the returned reports. It runs the bitonic layers on the incident
bit vector and checks every read and the outgoing last physical slot.


### `checkSiteMemory`

 This computation accesses just the local header, reports, and incident
array. Its result includes the work on malformed sorting fields. 

### `checkSiteMemory_work`

 The memory pass runs only after the bucket simulation succeeded. Its
bound needs no validity hypothesis on the sorting or successor bits. 
