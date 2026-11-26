---
{
  "module": "OAI/Computability/VPVNP/LiveActiveGroupCounts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveActiveGroupCounts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveActiveGroupCounts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Incoming checks on the active branches

On a first-half or midpoint input the native header tests the incoming
padding directly. At a later incoming cut a nonzero transition count forces
a decodable configuration. Consequently, after both header scans succeed,
the native active branch may use the raw pair or transition count directly.


### `incoming_of_active_nonzero`

 The potentially stronger incoming check contributes no further factor
once the physical padding passes and the active group's count is nonzero. 
