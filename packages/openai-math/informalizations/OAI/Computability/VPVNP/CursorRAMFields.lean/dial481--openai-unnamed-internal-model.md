---
{
  "module": "OAI/Computability/VPVNP/CursorRAMFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorRAMFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorRAMFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reindexing cursor fields by physical RAM sends

Each internal successor boundary has exactly one active mask. After clamping
all other successor fields to zero, the independent source settings in the
cursor contraction are in bijection with the original RAM send arrays.


### `ActiveSends`

 A site can send a nonzero successor field only in the class of its own
nonwrapping successor. Every sorting-system send is active. 

### `physicalSends`

 Restrict a site's expanded payload to the physical successor and sorting sends. 

### `activeSendsEquiv`

 Exactly the expanded source assignments satisfying the local clamps
survive, once for each setting of the physical send arrays. 

### `contract_ram`

 For any local validator the cursor contraction with inactive sends clamped
is exactly the RAM contraction indexed by the original send arrays. 
