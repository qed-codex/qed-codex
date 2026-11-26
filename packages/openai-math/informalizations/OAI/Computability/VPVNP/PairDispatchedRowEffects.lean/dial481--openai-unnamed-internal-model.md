---
{
  "module": "OAI/Computability/VPVNP/PairDispatchedRowEffects.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairDispatchedRowEffects.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairDispatchedRowEffects.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local row effects under the physical vertex dispatcher

Each term pass and each cursor leaf selects its role by a tag lookup.
The router adds this lookup to the role trace and preserves the returned
suffix, the role's scratch update and its histogram increment. This lifts
the role-specific decoder and emission proofs to the common DFS entry.


### `dispatcher_read_iff`

 Inverting a successful dispatch recovers the selected role's job and
the very same suffix. Conversely, each role success gives this wrapped job. 

### `dispatchEvents_footprint`

 All role tags use one probe at the tag address. The branches differ
only in their number of ticks. 

### `RoleJobGuard`

 The role body starts at its own entry and returns to the common DFS
header. Its cost may use a different allowance from the full job's cost. 

### `dispatcher_nodeStep_of_suffix`

 At a known role row, only the body must be matched against the term
reader, and only its writes have to be checked against the child packets. 

### `dispatcher_leaf_subtrees`

 The singleton cursor subtree returns exactly the body's scratch and
suffix, for successful and rejected input streams alike. 

### `dispatcher_leaf_emits`

 A leaf emits one occurrence. Adding the tag lookup preserves that
occurrence's bit code and increments, and links its path at the DFS entry. 
