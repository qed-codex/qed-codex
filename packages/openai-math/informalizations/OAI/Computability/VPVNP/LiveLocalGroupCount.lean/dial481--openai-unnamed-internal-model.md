---
{
  "module": "OAI/Computability/VPVNP/LiveLocalGroupCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLocalGroupCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLocalGroupCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Assembling the native local count on every physical cut assignment

Only the two active continuations enter the assembly. They start in the real
post-header memory at the corresponding native stage. The unit branch, mixed
modes, malformed padding and the incoming-cut condition are discharged here.
The cap on each continuation includes the actual preceding header and router
reports.


### `profile`

 The evaluated live-header sizes governing this group's cuts and advice. 

### `Conditions`

 Physical address, clock and bucket bounds needed by the checked header. 

### `Prepared`

 State of the checked physical prefix from which a pair or tail routine
actually starts. The same object gives the accumulated report cap and tag. 

### `memory`

 The actual continuation memory obtained by replaying the prepared header reports on the
distributed input. 

### `remaining`

 Accepted continuations from the prepared memory whose reports fit the caps together with
the preceding header reports. 

### `PairContinuation`

 The first-half proof obligation after mode and padding validation. 

### `TailContinuation`

 The second-half proof obligation, including a possible malformed
incoming configuration and the final group's accepting endpoint. 

### `group`

 The exact `group` conclusion used in `FixedModelDiagonal.LocalCertificate`
for the real instruction table, start word zero, physical memory, and native
report caps. The supplied components are confined to their valid active routes. 
